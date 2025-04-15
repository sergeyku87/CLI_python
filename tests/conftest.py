import pytest


LOGS ="""2025-03-28 12:44:46,000 INFO django.request: GET /api/v1/reviews/ 204 OK [192.168.1.59]
2025-03-28 12:21:51,000 INFO django.request: GET /admin/dashboard/ 200 OK [192.168.1.68]
2025-03-28 12:40:47,000 CRITICAL django.core.management: DatabaseError: Deadlock detected
2025-03-28 12:44:46,000 INFO django.request: GET /api/v1/reviews/ 204 OK [192.168.1.59]
"""

@pytest.fixture
def log_file(tmp_path):
    file_logs = tmp_path / "tmp.log"
    file_logs.write_text(LOGS)
    return file_logs

@pytest.fixture
def data():
    return [
        ['/admin/dashboard/', 6, 0, 0, 2, 0],
        ['/admin/login/', 5, 0, 0, 1, 0],
        ['/api/v1/auth/login/', 4, 0, 0, 1, 0],
        ['/api/v1/cart/', 3, 0, 0, 0, 0],
        ['/api/v1/checkout/', 6, 0, 0, 1, 0],
        ['/api/v1/orders/', 2, 0, 0, 2, 0],
        ['/api/v1/payments/', 7, 0, 0, 1, 0],
        ['/api/v1/products/', 3, 0, 0, 0, 0],
        ['/api/v1/reviews/', 5, 0, 0, 0, 0],
        ['/api/v1/shipping/', 2, 0, 0, 1, 0],
        ['/api/v1/support/', 1, 0, 0, 3, 0],
        ['/api/v1/users/', 4, 0, 0, 0, 0],
        ['', 48, 0, 0, 12, 0]
    ]

@pytest.fixture
def output():
    return """Total requests: 60
+---------------------+------+-------+---------+-------+----------+
| HANDLER             | INFO | DEBUG | WARNING | ERROR | CRITICAL |
+---------------------+------+-------+---------+-------+----------+
| /admin/dashboard/   | 6    | 0     | 0       | 2     | 0        |
| /admin/login/       | 5    | 0     | 0       | 1     | 0        |
| /api/v1/auth/login/ | 4    | 0     | 0       | 1     | 0        |
| /api/v1/cart/       | 3    | 0     | 0       | 0     | 0        |
| /api/v1/checkout/   | 6    | 0     | 0       | 1     | 0        |
| /api/v1/orders/     | 2    | 0     | 0       | 2     | 0        |
| /api/v1/payments/   | 7    | 0     | 0       | 1     | 0        |
| /api/v1/products/   | 3    | 0     | 0       | 0     | 0        |
| /api/v1/reviews/    | 5    | 0     | 0       | 0     | 0        |
| /api/v1/shipping/   | 2    | 0     | 0       | 1     | 0        |
| /api/v1/support/    | 1    | 0     | 0       | 3     | 0        |
| /api/v1/users/      | 4    | 0     | 0       | 0     | 0        |
|                     | 48   | 0     | 0       | 12    | 0        |
+---------------------+------+-------+---------+-------+----------+
"""

@pytest.fixture
def main_output():
    return """Total requests: 3
+-------------------+------+-------+---------+-------+----------+
| HANDLER           | INFO | DEBUG | WARNING | ERROR | CRITICAL |
+-------------------+------+-------+---------+-------+----------+
| /admin/dashboard/ | 1    | 0     | 0       | 0     | 0        |
| /api/v1/reviews/  | 2    | 0     | 0       | 0     | 0        |
|                   | 3    | 0     | 0       | 0     | 0        |
+-------------------+------+-------+---------+-------+----------+
"""
