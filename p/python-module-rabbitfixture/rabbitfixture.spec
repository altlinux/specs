%define oname rabbitfixture

%def_with python3

Name: python-module-%oname
Version: 0.3.5
Release: alt1
Summary: A RabbitMQ fixture
License: AGPLv3
Group: Development/Python
Url: https://pypi.python.org/pypi/rabbitfixture/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-module-setuptools-tests python-module-amqplib
BuildPreReq: python-module-fixtures python-module-testtools
BuildPreReq: python-module-mimeparse
BuildPreReq: rabbitmq-server
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel
BuildPreReq: python3-module-setuptools-tests python3-module-amqplib
BuildPreReq: python3-module-fixtures python3-module-testtools
BuildPreReq: python3-module-mimeparse
%endif

%py_provides %oname
Requires: rabbitmq-server

%description
A RabbitMQ fixture.

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR

%description tests
A RabbitMQ fixture.

This package contains tests for %oname.

%package -n python3-module-%oname
Summary: A RabbitMQ fixture
Group: Development/Python3
%py3_provides %oname
Requires: rabbitmq-server

%description -n python3-module-%oname
A RabbitMQ fixture.

%package -n python3-module-%oname-tests
Summary: Tests for %oname
Group: Development/Python3
Requires: python3-module-%oname = %EVR

%description -n python3-module-%oname-tests
A RabbitMQ fixture.

This package contains tests for %oname.

%prep
%setup

%if_with python3
cp -fR . ../python3
%endif

%build
%python_build_debug

%if_with python3
pushd ../python3
%python3_build_debug
popd
%endif

%install
%python_install

%if_with python3
pushd ../python3
%python3_install
popd
%endif

%check
python setup.py test
%if_with python3
pushd ../python3
python3 setup.py test
popd
%endif

%files
%doc README
%python_sitelibdir/*
%exclude %python_sitelibdir/*/tests

%files tests
%python_sitelibdir/*/tests

%if_with python3
%files -n python3-module-%oname
%doc README
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*/tests

%files -n python3-module-%oname-tests
%python3_sitelibdir/*/tests
%endif

%changelog
* Fri Dec 12 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.3.5-alt1
- Initial build for Sisyphus

