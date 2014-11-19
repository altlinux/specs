%define module_name pylibrabbitmq

%def_without python3

Name: python-module-%module_name
Version: 1.6.1
Release: alt2.git20141117
Group: Development/Python
License: GPLv2
Summary: Experimental Python bindings to the RabbitMQ C-library librabbitmq
URL: https://github.com/celery/librabbitmq
# https://github.com/celery/librabbitmq.git
Source: %name-%version.tar
# https://github.com/ask/rabbitmq-c.git
Source1: rabbitmq-c.tar
# https://github.com/rabbitmq/rabbitmq-codegen.git
Source2: rabbitmq-codegen.tar

BuildPreReq: rabbitmq-server-devel librabbitmq-c-devel
BuildPreReq: python-devel python-module-setuptools
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools
%endif

%description
Experimental Python bindings to the RabbitMQ C-library librabbitmq

%package tests
Summary: Tests for %module_name
Group: Development/Python
Requires: %name = %EVR

%description tests
Experimental Python bindings to the RabbitMQ C-library librabbitmq

This package contains tests for %module_name.

%package -n python3-module-%module_name
Summary: Experimental Python bindings to the RabbitMQ C-library librabbitmq
Group: Development/Python3

%description -n python3-module-%module_name
Experimental Python bindings to the RabbitMQ C-library librabbitmq

%package -n python3-module-%module_name-tests
Summary: Tests for %module_name
Group: Development/Python3
Requires: python3-module-%module_name = %EVR

%description -n python3-module-%module_name-tests
Experimental Python bindings to the RabbitMQ C-library librabbitmq

This package contains tests for %module_name.

%prep
%setup
tar -xf %SOURCE1
tar -xf %SOURCE2

%if_with python3
cp -fR . ../python3
%endif

%build
pushd rabbitmq-c
%autoreconf
popd
%add_optflags -fno-strict-aliasing
%python_build

%if_with python3
pushd ../python3
%python3_build
popd
%endif

%install
%python_install

%if_with python3
pushd ../python3
%python3_install
popd
%endif

%files
%doc AUTHORS Changelog LICENSE-GPL-2.0 LICENSE-MPL-RabbitMQ README.rst TODO
%python_sitelibdir/librabbitmq*
%python_sitelibdir/_librabbitmq*
%exclude %python_sitelibdir/*/tests

%files tests
%python_sitelibdir/*/tests

%if_with python3
%files -n python3-module-%module_name
%doc AUTHORS Changelog LICENSE-GPL-2.0 LICENSE-MPL-RabbitMQ README.rst TODO
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*/tests

%files -n python3-module-%module_name-tests
%python3_sitelibdir/*/tests
%endif

%changelog
* Wed Nov 19 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.6.1-alt2.git20141117
- Extracted tests into separate package

* Tue Nov 18 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.6.1-alt1.git20141117
- Version 1.6.1

* Tue Sep 02 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.5.2-alt1.git20140528
- Version 1.5.2

* Sat Sep 28 2013 Slava Dubrovskiy <dubrsl@altlinux.org> 0.5.0-alt2
- rebuild for new librabbitmq

* Fri May 04 2012 Slava Dubrovskiy <dubrsl@altlinux.org> 0.5.0-alt1
- build for ALT
