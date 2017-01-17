%define _unpackaged_files_terminate_build 1
%define oname AMQP-Storm

%def_with python3

Name: python-module-%oname
Version: 1.4.0
Release: alt1
Summary: Thread-safe Python AMQP Client Library based on pamqp
License: MIT
Group: Development/Python
Url: https://pypi.python.org/pypi/AMQP-Storm/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/eandersson/amqp-storm.git
Source0: https://pypi.python.org/packages/18/9e/5fe49408f729f5d57f783b464a582a24b29f5edec8250e41c50d2317797c/%{oname}-%{version}.tar.gz
BuildArch: noarch

BuildPreReq: python-devel python-module-setuptools-tests
BuildPreReq: python-module-pamqp
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools-tests
BuildPreReq: python3-module-pamqp
%endif

%py_provides amqpstorm
%py_requires pamqp

%description
A fully thread-safe RabbitMQ library for Python based on pamqp.

%package -n python3-module-%oname
Summary: Thread-safe Python AMQP Client Library based on pamqp
Group: Development/Python3
%py3_provides amqpstorm
%py3_requires pamqp

%description -n python3-module-%oname
A fully thread-safe RabbitMQ library for Python based on pamqp.

%prep
%setup -q -n %{oname}-%{version}

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
%doc *.rst PKG-INFO
%python_sitelibdir/*

%if_with python3
%files -n python3-module-%oname
%doc *.rst PKG-INFO
%python3_sitelibdir/*
%endif

%changelog
* Tue Jan 17 2017 Igor Vlasenko <viy@altlinux.ru> 1.4.0-alt1
- automated PyPI update

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 1.1.7-alt1.git20150126.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Mon Jan 26 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.1.7-alt1.git20150126
- Version 1.1.7

* Thu Dec 25 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.1.6-alt1.git20141224
- Initial build for Sisyphus

