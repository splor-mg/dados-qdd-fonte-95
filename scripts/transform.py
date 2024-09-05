from frictionless import Package
import logging
import petl as etl
from dpm.utils import as_identifier
from scripts.pipelines import transform_pipeline

logger = logging.getLogger(__name__)

def transform_resource(resource_name: str, source_descriptor: str = 'datapackage.yaml'):
    logger.info(f'Transforming resource {resource_name}')

    package = Package(source_descriptor)
    resource = package.get_resource(resource_name)
    resource.transform(transform_pipeline)
    table = resource.to_petl()

    table = etl.selecteq(table, 'FONTE', 95)

    etl.toxlsx(table, F'data/{resource.name}.xlsx', sheet='base_qdd_fiscal')


