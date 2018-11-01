import logging
import baidubce.protocol

from baidubce.bce_client_configuration import BceClientConfiguration
from baidubce.auth.bce_credentials import BceCredentials
from baidubce.services.tsdb.tsdb_client import TsdbClient
from baidubce.bce_client_configuration import BceClientConfiguration
from baidubce.auth.bce_credentials import BceCredentials
from baidubce import exception
from baidubce.services import bos
from baidubce.services.bos import canned_acl
from baidubce.services.bos.bos_client import BosClient

# ak,sk
access_key_id = "ak"
secret_access_key = "sk"

# BOS example
bos_host = "bj.bcebos.com"

logger = logging.getLogger("baidubce.http.bce_http_client")
fh = logging.FileHandler("sample.log")
fh.setLevel(logging.DEBUG)

formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
fh.setFormatter(formatter)
logger.setLevel(logging.DEBUG)
logger.addHandler(fh)

bos_config = BceClientConfiguration(credentials=BceCredentials(access_key_id, secret_access_key), endpoint = bos_host)
bos_client = BosClient(bos_config)

response = bos_client.list_buckets()
for bucket in response.buckets:
    print (bucket.name)

# TSDB example
tsdb_host = "xxx.tsdb-xxx.tsdb.iot.gz.baidubce.com"

protocol= baidubce.protocol.HTTP
connection_timeout_in_mills=None  #连接超时时间
send_buf_size=None                #发送缓冲区大小
recv_buf_size=None                #接收缓冲区大小
retry_policy=None                 #重试策略

#生成config对象
tsdb_config = BceClientConfiguration(
        credentials=BceCredentials(access_key_id, secret_access_key),
        endpoint=tsdb_host,
        protocol=protocol,
        connection_timeout_in_mills=connection_timeout_in_mills,
        send_buf_size=send_buf_size,
        recv_buf_size=recv_buf_size,
        retry_policy=retry_policy)

#创建TsdbCient
tsdb_client = TsdbClient(tsdb_config)

# 获取metric列表
result = tsdb_client.get_metrics()
print (result.metrics)