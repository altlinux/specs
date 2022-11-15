%define _unpackaged_files_terminate_build 1

%define oname aws-xray-sdk
%define modname aws_xray_sdk

Name: python3-module-%oname
Version: 2.8.0
Release: alt1.1
Summary: AWS X-Ray SDK for the Python programming language
Group: Development/Python3
License: Apache-2.0
URL: https://github.com/aws/aws-xray-sdk-python

BuildArch: noarch

# https://github.com/aws/aws-xray-sdk-python.git
Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel
BuildRequires: python3(setuptools)
BuildRequires: python3(botocore)
BuildRequires: python3(future)
BuildRequires: python3(jsonpickle)
BuildRequires: python3(wrapt)
BuildRequires: /usr/bin/pytest-3
BuildRequires: python3(sqlite3) python3(sqlalchemy) python3(mock) python3(flask)
BuildRequires: python3(pg8000) python3(flask_sqlalchemy) python3(bottle) python3(webtest) python3(django)

%add_python3_req_skip aiobotocore.client flask_sqlalchemy.model
%add_python3_self_prov_path  %buildroot%python3_sitelibdir/%modname/ext

%description
The AWS X-Ray SDK for Python (the SDK) enables Python developers
to record and emit information from within their applications
to the AWS X-Ray service.

%prep
%setup

%build
%python3_build

%install
%python3_install

%check
pytest-3 -vv \
	--ignore=tests/ext/aiobotocore/test_aiobotocore.py \
	--ignore=tests/ext/pg8000/test_pg8000.py \
	--ignore=tests/ext/psycopg2/test_psycopg2.py \
	--ignore=tests/ext/pymysql/test_pymysql.py \
	--ignore=tests/ext/pynamodb/test_pynamodb.py \
	--ignore=tests/ext/sqlalchemy_core/test_postgres.py \
	--deselect=tests/ext/httplib/test_httplib.py \
	--deselect=tests/ext/requests/test_requests.py::test_ok \
	--deselect=tests/ext/requests/test_requests.py::test_error \
	--deselect=tests/ext/requests/test_requests.py::test_throttle \
	--deselect=tests/ext/requests/test_requests.py::test_fault \
	--deselect=tests/ext/requests/test_requests.py::test_name_uses_hostname \
	--deselect=tests/ext/requests/test_requests.py::test_strip_http_url \
	--deselect=tests/test_async_local_storage.py::test_localstorage_isolation \
	--deselect=tests/test_async_recorder.py \
	--deselect=tests/ext/aiohttp/test_client.py \
	--deselect=tests/ext/aiohttp/test_middleware.py \
	--deselect=tests/ext/django/test_db.py \
	--deselect=tests/ext/django/test_middleware.py \
	--deselect=tests/ext/django/test_settings.py \
	%nil

%files
%doc LICENSE
%doc *.md *.rst
%python3_sitelibdir/%modname
%python3_sitelibdir/%modname-%version-py*.egg-info

%changelog
* Sat Nov 12 2022 Daniel Zagaynov <kotopesutility@altlinux.org> 2.8.0-alt1.1
- NMU: used %%add_python3_self_prov_path macro to skip self-provides from dependencies.

* Wed Aug 25 2021 Aleksei Nikiforov <darktemplar@altlinux.org> 2.8.0-alt1
- Updated to upstream version 2.8.0.
- Enabled tests.

* Wed Sep 09 2020 Aleksei Nikiforov <darktemplar@altlinux.org> 2.6.0-alt1
- Initial build for ALT.
