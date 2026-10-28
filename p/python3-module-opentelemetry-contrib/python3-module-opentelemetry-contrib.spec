%define pypi_name opentelemetry-contrib
%define mod_name opentelemetry
%define prerel_version 1.26.0

%def_without check

Name:    python3-module-%pypi_name
Version: 0.65b0
Release: alt5

Summary: OpenTelemetry instrumentation for Python modules
License: Apache-2.0 and BSD-3-Clause
Group:   Development/Python3
URL:     https://github.com/open-telemetry/opentelemetry-python-contrib

Packager: Alexander Burmatov <thatman@altlinux.org>

Source: %pypi_name-%version.tar

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-setuptools python3-module-wheel
BuildRequires: python3-module-hatchling


%if_with check
BuildRequires: python3-module-pytest
BuildRequires: python3-module-asgiref
BuildRequires: python3-module-opentelemetry-api
BuildRequires: python3-module-opentelemetry-test-utils
BuildRequires: python3-module-importlib-metadata
BuildRequires: python3-module-requests
BuildRequires: python3-module-pytest-benchmark
BuildRequires: python3-module-wrapt
%endif

BuildArch: noarch

%description
%summary.

%package -n python3-module-%mod_name-instrumentation
Summary: OpenTelemetry Instrumentation
Group: Development/Python3
Provides: python3(opentelemetry.instrumentation)

%description -n python3-module-%mod_name-instrumentation
This package provides commands that help automatically instrument a program.

%package -n python3-module-%mod_name-instrumentation-asgi
Summary: OpenTelemetry ASGI Instrumentation
Group: Development/Python3

%description -n python3-module-%mod_name-instrumentation-asgi
This library provides a ASGI middleware that can be used on any ASGI framework
(such as Django, Starlette, FastAPI or Quart) to track requests timing through
OpenTelemetry.

%package -n python3-module-%mod_name-instrumentation-django
Summary: OpenTelemetry Instrumentation for Django
Group: Development/Python3

%description -n python3-module-%mod_name-instrumentation-django
This library allows tracing requests for Django applications.

%package -n python3-module-%mod_name-instrumentation-requests
Summary: OpenTelemetry requests instrumentation
Group: Development/Python3

%description -n python3-module-%mod_name-instrumentation-requests
This library allows tracing HTTP requests made by the requests library.

%package -n python3-module-%mod_name-instrumentation-wsgi
Summary: WSGI Middleware for OpenTelemetry
Group: Development/Python3

%description -n python3-module-%mod_name-instrumentation-wsgi
This library provides a WSGI middleware that can be used on any WSGI framework
(such as Django / Flask) to track requests timing through OpenTelemetry.

%package -n python3-module-%mod_name-instrumentation-celery
Summary: OpenTelemetry Celery Instrumentation
Group: Development/Python3

%description -n python3-module-%mod_name-instrumentation-celery
This library allows tracing Celery tasks.

%package -n python3-module-%mod_name-instrumentation-dbapi
Summary: OpenTelemetry DBAPI Instrumentation
Group: Development/Python3

%description -n python3-module-%mod_name-instrumentation-dbapi
This library provides common instrumentation functionality for Python
Database API Specification compatible libraries.

%package -n python3-module-%mod_name-instrumentation-psycopg2
Summary: OpenTelemetry Psycopg2 Instrumentation
Group: Development/Python3
Requires: python3-module-%mod_name-instrumentation-dbapi = %EVR

%description -n python3-module-%mod_name-instrumentation-psycopg2
This library allows tracing PostgreSQL queries made by the psycopg2 library.

%package -n python3-module-%mod_name-instrumentation-httpx
Summary: OpenTelemetry HTTPX Instrumentation
Group: Development/Python3

%description -n python3-module-%mod_name-instrumentation-httpx
This library allows tracing HTTP requests made by the httpx library.

%package -n python3-module-%mod_name-instrumentation-botocore
Summary: OpenTelemetry Botocore Instrumentation
Group: Development/Python3

%description -n python3-module-%mod_name-instrumentation-botocore
This library allows tracing AWS API calls made by the botocore library.

%package -n python3-module-%mod_name-instrumentation-logging
Summary: OpenTelemetry Logging Instrumentation
Group: Development/Python3

%description -n python3-module-%mod_name-instrumentation-logging
OpenTelemetry logging integration.

%package -n python3-module-%mod_name-instrumentation-redis
Summary: OpenTelemetry Redis Instrumentation
Group: Development/Python3

%description -n python3-module-%mod_name-instrumentation-redis
This library allows tracing requests made by the Redis library.

%package -n python3-module-%mod_name-instrumentation-system-metrics
Summary: OpenTelemetry System Metrics Instrumentation
Group: Development/Python3

%description -n python3-module-%mod_name-instrumentation-system-metrics
Instrumentation to collect system performance metrics.

%package -n python3-module-%mod_name-instrumentation-fastapi
Summary: OpenTelemetry FastAPI Instrumentation
Group: Development/Python3

%description -n python3-module-%mod_name-instrumentation-fastapi
This library provides automatic and manual instrumentation of FastAPI web
frameworks, instrumenting http requests served by applications utilizing the
framework.

auto-instrumentation using the opentelemetry-instrumentation package is also
supported.

%package -n python3-module-%mod_name-instrumentation-aiohttp-client
Summary: OpenTelemetry AIOHTTP Client Instrumentation
Group: Development/Python3

%description -n python3-module-%mod_name-instrumentation-aiohttp-client
This library allows tracing HTTP requests made by the aiohttp client library.

%package -n python3-module-%mod_name-instrumentation-aiohttp-server
Summary: OpenTelemetry AIOHTTP Server Instrumentation
Group: Development/Python3

%description -n python3-module-%mod_name-instrumentation-aiohttp-server
This library allows tracing requests for aiohttp server applications.

%package -n python3-module-%mod_name-instrumentation-asyncpg
Summary: OpenTelemetry Asyncpg Instrumentation
Group: Development/Python3

%description -n python3-module-%mod_name-instrumentation-asyncpg
This library allows tracing PostgreSQL queries made by the asyncpg library.

%package -n python3-module-%mod_name-instrumentation-aws-lambda
Summary: OpenTelemetry AWS Lambda Instrumentation
Group: Development/Python3

%description -n python3-module-%mod_name-instrumentation-aws-lambda
This library provides an AwsLambdaInstrumentor to trace AWS Lambda
invocations.

%package -n python3-module-%mod_name-instrumentation-flask
Summary: OpenTelemetry Flask Instrumentation
Group: Development/Python3

%description -n python3-module-%mod_name-instrumentation-flask
This library allows tracing of requests made to Flask applications.

%package -n python3-module-%mod_name-instrumentation-mysql
Summary: OpenTelemetry MySQL Instrumentation
Group: Development/Python3

%description -n python3-module-%mod_name-instrumentation-mysql
This library allows tracing MySQL queries made by the mysql-connector
library.

%package -n python3-module-%mod_name-instrumentation-psycopg
Summary: OpenTelemetry Psycopg Instrumentation
Group: Development/Python3

%description -n python3-module-%mod_name-instrumentation-psycopg
This library allows tracing PostgreSQL queries made by the psycopg library.

%package -n python3-module-%mod_name-instrumentation-pymongo
Summary: OpenTelemetry Pymongo Instrumentation
Group: Development/Python3

%description -n python3-module-%mod_name-instrumentation-pymongo
This library allows tracing MongoDB queries made by the pymongo library.

%package -n python3-module-%mod_name-instrumentation-sqlalchemy
Summary: OpenTelemetry SQLAlchemy Instrumentation
Group: Development/Python3

%description -n python3-module-%mod_name-instrumentation-sqlalchemy
This library allows tracing queries made by SQLAlchemy.

%package -n python3-module-%mod_name-instrumentation-sqlite3
Summary: OpenTelemetry Sqlite3 Instrumentation
Group: Development/Python3

%description -n python3-module-%mod_name-instrumentation-sqlite3
This library allows tracing SQLite queries made by the sqlite3 library.

%package -n python3-module-%mod_name-instrumentation-starlette
Summary: OpenTelemetry Starlette Instrumentation
Group: Development/Python3

%description -n python3-module-%mod_name-instrumentation-starlette
This library allows tracing requests for Starlette applications.

%package -n python3-module-%mod_name-instrumentation-urllib
Summary: OpenTelemetry Urllib Instrumentation
Group: Development/Python3

%description -n python3-module-%mod_name-instrumentation-urllib
This library allows tracing HTTP requests made by the urllib library.

%package -n python3-module-%mod_name-propagator-aws-xray
Summary: OpenTelemetry Propagator for AWS X-Ray Service
Group: Development/Python3

%description -n python3-module-%mod_name-propagator-aws-xray
This library provides the propagator necessary to inject or extract a tracing
context across AWS services.

%package -n python3-module-%mod_name-propagator-ot-trace
Summary: OpenTelemetry OT Trace Propagator
Group: Development/Python3

%description -n python3-module-%mod_name-propagator-ot-trace
OpenTelemetry OT Trace Propagator.

%package -n python3-module-%mod_name-util-http
Summary: OpenTelemetry Util HTTP
Group: Development/Python3

%description -n python3-module-%mod_name-util-http
This library provides ASGI, WSGI middleware and other HTTP-related
functionality that is common to instrumented web frameworks (such as Django,
Starlette, FastAPI, etc.) to track requests timing through OpenTelemetry.

%package -n python3-module-%mod_name-distro
Summary: OpenTelemetry Python Distro
Group: Development/Python3

%description -n python3-module-%mod_name-distro
This package provides entrypoints to configure OpenTelemetry.

%prep
%setup -n %pypi_name-%version

%build
pushd ./%mod_name-instrumentation
    %pyproject_build
popd

pushd ./util/%mod_name-util-http
    %pyproject_build
popd

pushd ./%mod_name-distro
    %pyproject_build
popd

# Instrumentations pkg sources
for idir in \
    asgi celery dbapi django httpx psycopg2 requests wsgi botocore \
    logging redis system-metrics fastapi aiohttp-client aiohttp-server \
    asyncpg aws-lambda flask mysql psycopg pymongo sqlalchemy sqlite3 \
    starlette urllib; do
    pushd ./instrumentation/%mod_name-instrumentation-$idir
        %pyproject_build
    popd
done

# Propagators pkg sources
for pdir in ./propagator/%mod_name-propagator-{aws-xray,ot-trace}; do
    pushd $pdir
        %pyproject_build
    popd
done

%install
pushd ./%mod_name-instrumentation
    %pyproject_install
popd

pushd ./util/%mod_name-util-http
    %pyproject_install
popd

pushd ./%mod_name-distro
    %pyproject_install
popd

# Instrumentations pkg sources
for idir in \
    asgi celery dbapi django httpx psycopg2 requests wsgi botocore \
    logging redis system-metrics fastapi aiohttp-client aiohttp-server \
    asyncpg aws-lambda flask mysql psycopg pymongo sqlalchemy sqlite3 \
    starlette urllib; do
    pushd ./instrumentation/%mod_name-instrumentation-$idir
        %pyproject_install
    popd
done

# Propagators pkg sources
for pdir in ./propagator/%mod_name-propagator-{aws-xray,ot-trace}; do
    pushd $pdir
        %pyproject_install
    popd
done

%check
export PYTHONPATH=%buildroot%python3_sitelibdir
pushd ./%mod_name-instrumentation
    %pyproject_run_pytest -k "not test_run.py"
popd

pushd ./util/%mod_name-util-http
    %pyproject_run_pytest
popd

pushd ./%mod_name-distro
    %pyproject_run_pytest
popd

# Instrumentations pkg sources
for idir in ./instrumentation/%mod_name-instrumentation-{asgi,celery,dbapi,django,httpx,psycopg2,requests,wsgi,botocore,logging,redis,system-metrics}; do
    pushd $idir
        %pyproject_run_pytest
    popd
done

# Propagators pkg sources
for pdir in ./propagator/%mod_name-propagator-{aws-xray,ot-trace}; do
    pushd $pdir
        %pyproject_run_pytest
    popd
done

%files -n python3-module-%mod_name-instrumentation
%doc %mod_name-instrumentation/{LICENSE,README.rst}
%_bindir/opentelemetry-bootstrap
%_bindir/opentelemetry-instrument
%python3_sitelibdir/%mod_name/instrumentation/__pycache__
%python3_sitelibdir/%mod_name/instrumentation/auto_instrumentation
%python3_sitelibdir/%mod_name/instrumentation/_labeler
%python3_sitelibdir/%mod_name/instrumentation/_semconv.py
%python3_sitelibdir/%mod_name/instrumentation/bootstrap.py
%python3_sitelibdir/%mod_name/instrumentation/bootstrap_gen.py
%python3_sitelibdir/%mod_name/instrumentation/cidict.py
%python3_sitelibdir/%mod_name/instrumentation/dependencies.py
%python3_sitelibdir/%mod_name/instrumentation/distro.py
%python3_sitelibdir/%mod_name/instrumentation/environment_variables.py
%python3_sitelibdir/%mod_name/instrumentation/instrumentor.py
%python3_sitelibdir/%mod_name/instrumentation/propagators.py
%python3_sitelibdir/%mod_name/instrumentation/py.typed
%python3_sitelibdir/%mod_name/instrumentation/sqlcommenter_utils.py
%python3_sitelibdir/%mod_name/instrumentation/utils.py
%python3_sitelibdir/%mod_name/instrumentation/log_utils.py
%python3_sitelibdir/%mod_name/instrumentation/version.py
%python3_sitelibdir/%{pyproject_distinfo %mod_name-instrumentation}

%files -n python3-module-%mod_name-instrumentation-asgi
%doc instrumentation/%mod_name-instrumentation-asgi/{LICENSE,README.rst}
%python3_sitelibdir/%mod_name/instrumentation/asgi
%python3_sitelibdir/%{pyproject_distinfo %mod_name-instrumentation-asgi}

%files -n python3-module-%mod_name-instrumentation-django
%doc instrumentation/%mod_name-instrumentation-django/{LICENSE,README.rst}
%python3_sitelibdir/%mod_name/instrumentation/django
%python3_sitelibdir/%{pyproject_distinfo %mod_name-instrumentation-django}

%files -n python3-module-%mod_name-instrumentation-requests
%doc instrumentation/%mod_name-instrumentation-requests/{LICENSE,README.rst}
%python3_sitelibdir/%mod_name/instrumentation/requests
%python3_sitelibdir/%{pyproject_distinfo %mod_name-instrumentation-requests}

%files -n python3-module-%mod_name-instrumentation-wsgi
%doc instrumentation/%mod_name-instrumentation-wsgi/{LICENSE,README.rst}
%python3_sitelibdir/%mod_name/instrumentation/wsgi
%python3_sitelibdir/%{pyproject_distinfo %mod_name-instrumentation-wsgi}

%files -n python3-module-%mod_name-instrumentation-celery
%doc instrumentation/%mod_name-instrumentation-celery/{LICENSE,README.rst}
%python3_sitelibdir/%mod_name/instrumentation/celery
%python3_sitelibdir/%{pyproject_distinfo %mod_name-instrumentation-celery}

%files -n python3-module-%mod_name-instrumentation-dbapi
%doc instrumentation/%mod_name-instrumentation-dbapi/{LICENSE,README.rst}
%python3_sitelibdir/%mod_name/instrumentation/dbapi
%python3_sitelibdir/%{pyproject_distinfo %mod_name-instrumentation-dbapi}

%files -n python3-module-%mod_name-instrumentation-psycopg2
%doc instrumentation/%mod_name-instrumentation-psycopg2/{LICENSE,README.rst}
%python3_sitelibdir/%mod_name/instrumentation/psycopg2
%python3_sitelibdir/%{pyproject_distinfo %mod_name-instrumentation-psycopg2}

%files -n python3-module-%mod_name-instrumentation-httpx
%doc instrumentation/%mod_name-instrumentation-httpx/{LICENSE,README.rst}
%python3_sitelibdir/%mod_name/instrumentation/httpx
%python3_sitelibdir/%{pyproject_distinfo %mod_name-instrumentation-httpx}

%files -n python3-module-%mod_name-instrumentation-botocore
%doc instrumentation/%mod_name-instrumentation-botocore/{LICENSE,README.rst}
%python3_sitelibdir/%mod_name/instrumentation/botocore
%python3_sitelibdir/%{pyproject_distinfo %mod_name-instrumentation-botocore}

%files -n python3-module-%mod_name-instrumentation-logging
%doc instrumentation/%mod_name-instrumentation-logging/{LICENSE,README.rst}
%python3_sitelibdir/%mod_name/instrumentation/logging
%python3_sitelibdir/%{pyproject_distinfo %mod_name-instrumentation-logging}

%files -n python3-module-%mod_name-instrumentation-redis
%doc instrumentation/%mod_name-instrumentation-redis/{LICENSE,README.rst}
%python3_sitelibdir/%mod_name/instrumentation/redis
%python3_sitelibdir/%{pyproject_distinfo %mod_name-instrumentation-redis}

%files -n python3-module-%mod_name-instrumentation-system-metrics
%doc instrumentation/%mod_name-instrumentation-system-metrics/{LICENSE,README.rst}
%python3_sitelibdir/%mod_name/instrumentation/system_metrics
%python3_sitelibdir/%{pyproject_distinfo %mod_name-instrumentation-system-metrics}

%files -n python3-module-%mod_name-instrumentation-fastapi
%doc instrumentation/%mod_name-instrumentation-fastapi/{LICENSE,README.rst}
%python3_sitelibdir/%mod_name/instrumentation/fastapi
%python3_sitelibdir/%{pyproject_distinfo %mod_name-instrumentation-fastapi}

%files -n python3-module-%mod_name-instrumentation-aiohttp-client
%doc instrumentation/%mod_name-instrumentation-aiohttp-client/{LICENSE,README.rst}
%python3_sitelibdir/%mod_name/instrumentation/aiohttp_client
%python3_sitelibdir/%{pyproject_distinfo %mod_name-instrumentation-aiohttp-client}

%files -n python3-module-%mod_name-instrumentation-aiohttp-server
%doc instrumentation/%mod_name-instrumentation-aiohttp-server/README.rst
%python3_sitelibdir/%mod_name/instrumentation/aiohttp_server
%python3_sitelibdir/%{pyproject_distinfo %mod_name-instrumentation-aiohttp-server}

%files -n python3-module-%mod_name-instrumentation-asyncpg
%doc instrumentation/%mod_name-instrumentation-asyncpg/{LICENSE,README.rst}
%python3_sitelibdir/%mod_name/instrumentation/asyncpg
%python3_sitelibdir/%{pyproject_distinfo %mod_name-instrumentation-asyncpg}

%files -n python3-module-%mod_name-instrumentation-aws-lambda
%doc instrumentation/%mod_name-instrumentation-aws-lambda/{LICENSE,README.rst}
%python3_sitelibdir/%mod_name/instrumentation/aws_lambda
%python3_sitelibdir/%{pyproject_distinfo %mod_name-instrumentation-aws-lambda}

%files -n python3-module-%mod_name-instrumentation-flask
%doc instrumentation/%mod_name-instrumentation-flask/{LICENSE,README.rst}
%python3_sitelibdir/%mod_name/instrumentation/flask
%python3_sitelibdir/%{pyproject_distinfo %mod_name-instrumentation-flask}

%files -n python3-module-%mod_name-instrumentation-mysql
%doc instrumentation/%mod_name-instrumentation-mysql/{LICENSE,README.rst}
%python3_sitelibdir/%mod_name/instrumentation/mysql
%python3_sitelibdir/%{pyproject_distinfo %mod_name-instrumentation-mysql}

%files -n python3-module-%mod_name-instrumentation-psycopg
%doc instrumentation/%mod_name-instrumentation-psycopg/{LICENSE,README.rst}
%python3_sitelibdir/%mod_name/instrumentation/psycopg
%python3_sitelibdir/%{pyproject_distinfo %mod_name-instrumentation-psycopg}

%files -n python3-module-%mod_name-instrumentation-pymongo
%doc instrumentation/%mod_name-instrumentation-pymongo/{LICENSE,README.rst}
%python3_sitelibdir/%mod_name/instrumentation/pymongo
%python3_sitelibdir/%{pyproject_distinfo %mod_name-instrumentation-pymongo}

%files -n python3-module-%mod_name-instrumentation-sqlalchemy
%doc instrumentation/%mod_name-instrumentation-sqlalchemy/{LICENSE,README.rst}
%python3_sitelibdir/%mod_name/instrumentation/sqlalchemy
%python3_sitelibdir/%{pyproject_distinfo %mod_name-instrumentation-sqlalchemy}

%files -n python3-module-%mod_name-instrumentation-sqlite3
%doc instrumentation/%mod_name-instrumentation-sqlite3/{LICENSE,README.rst}
%python3_sitelibdir/%mod_name/instrumentation/sqlite3
%python3_sitelibdir/%{pyproject_distinfo %mod_name-instrumentation-sqlite3}

%files -n python3-module-%mod_name-instrumentation-starlette
%doc instrumentation/%mod_name-instrumentation-starlette/{LICENSE,README.rst}
%python3_sitelibdir/%mod_name/instrumentation/starlette
%python3_sitelibdir/%{pyproject_distinfo %mod_name-instrumentation-starlette}

%files -n python3-module-%mod_name-instrumentation-urllib
%doc instrumentation/%mod_name-instrumentation-urllib/{LICENSE,README.rst}
%python3_sitelibdir/%mod_name/instrumentation/urllib
%python3_sitelibdir/%{pyproject_distinfo %mod_name-instrumentation-urllib}

%files -n python3-module-%mod_name-propagator-aws-xray
%doc propagator/%mod_name-propagator-aws-xray/{LICENSE,README.rst}
%python3_sitelibdir/%mod_name/propagators/aws
%python3_sitelibdir/%{mod_name}_propagator_aws_xray-1.1.0.dev0.dist-info/

%files -n python3-module-%mod_name-propagator-ot-trace
%doc propagator/%mod_name-propagator-ot-trace/README.rst LICENSE
%python3_sitelibdir/%mod_name/propagators/ot_trace
%python3_sitelibdir/%{pyproject_distinfo %mod_name-propagator-ot-trace}

%files -n python3-module-%mod_name-util-http
%doc util/%mod_name-util-http/README.rst LICENSE
%python3_sitelibdir/%mod_name/util/http
%python3_sitelibdir/%{pyproject_distinfo %mod_name-util-http}

%files -n python3-module-%mod_name-distro
%doc %mod_name-distro/README.rst LICENSE
%python3_sitelibdir/%mod_name/distro
%python3_sitelibdir/%{pyproject_distinfo %mod_name-distro}

%changelog
* Tue Oct 27 2026 Alexandr Shashkin <dutyrok@altlinux.org> 0.65b0-alt5
- NMU: Package instrumentation for aiohttp-client, aiohttp-server,
  asyncpg, aws-lambda, flask, mysql, psycopg, pymongo, sqlalchemy,
  sqlite3, starlette and urllib.

* Wed Sep 30 2026 Anton Zhukharev <ancieg@altlinux.org> 0.65b0-alt4
- NMU: Package instrumentation for fastapi.

* Thu Aug 20 2026 Anton Zhukharev <ancieg@altlinux.org> 0.65b0-alt3
- NMU: Package distro and instrumentation for logging, redis and system-metrics.

* Wed Aug 12 2026 Evgeniy Martynenko <enimalojd@altlinux.org> 0.65b0-alt2
- NMU: Package instrumentation for dbapi (closes: #60142).

* Thu Jul 30 2026 Sergey Gvozdetskiy <serjigva@altlinux.org> 0.65b0-alt1
- New version.

* Wed Jul 29 2026 Evgeniy Martynenko <enimalojd@altlinux.org> 0.63b1-alt3
- NMU: Package instrumentation for celery, psycopg2, httpx and botocore.

* Tue Jun 09 2026 Anton Zhukharev <ancieg@altlinux.org> 0.63b1-alt2
- NMU: Package instrumentation for django, requests, and wsgi.

* Fri Jun 05 2026 Sergey Gvozdetskiy <serjigva@altlinux.org> 0.63b1-alt1
- New version.

* Mon Apr 13 2026 Sergey Gvozdetskiy <serjigva@altlinux.org> 0.62b0-alt1
- New version.

* Thu Mar 05 2026 Sergey Gvozdetskiy <serjigva@altlinux.org> 0.61b0-alt1
- New version.

* Tue Dec 23 2025 Sergey Gvozdetskiy <serjigva@altlinux.org> 0.60b1-alt1
- New version.

* Thu Dec 04 2025 Sergey Gvozdetskiy <serjigva@altlinux.org> 0.60b0-alt1
- New version.

* Wed Oct 22 2025 Sergey Gvozdetskiy <serjigva@altlinux.org> 0.59b0-alt1
- New version.

* Tue Jun 24 2025 Sergey Gvozdetskiy <serjigva@altlinux.org> 0.55b1-alt1
- New version.

* Fri Mar 07 2025 Sergey Gvozdetskiy <serjigva@altlinux.org> 0.51b0-alt1
- NMU: New version.

* Fri Jan 24 2025 Ivan A. Melnikov <iv@altlinux.org> 0.47b0-alt1.1
- NMU: fix FTBFS.

* Wed Aug 07 2024 Alexander Burmatov <thatman@altlinux.org> 0.47b0-alt1
- Initial build for Sisyphus.
