%define _unpackaged_files_terminate_build 1
%define oname rabbitfixture

%def_with python3

Name: python-module-%oname
Version: 0.3.8
Release: alt1
Summary: A RabbitMQ fixture
License: AGPLv3
Group: Development/Python
Url: https://pypi.python.org/pypi/rabbitfixture/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source0: https://pypi.python.org/packages/89/bc/ed8889e81c3f76e30c05363fa11746780794f5c8ad4ab0bbd4e21d9bcfde/%{oname}-%{version}.tar.gz
BuildArch: noarch

#BuildPreReq: python-module-setuptools-tests python-module-amqplib
#BuildPreReq: python-module-fixtures python-module-testtools
#BuildPreReq: python-module-mimeparse
#BuildPreReq: rabbitmq-server
%if_with python3
BuildRequires(pre): rpm-build-python3
#BuildPreReq: python3-devel
#BuildPreReq: python3-module-setuptools-tests python3-module-amqplib
#BuildPreReq: python3-module-fixtures python3-module-testtools
#BuildPreReq: python3-module-mimeparse
%endif

%py_provides %oname
Requires: rabbitmq-server

# Automatically added by buildreq on Thu Jan 28 2016 (-bi)
# optimized out: python-base python-devel python-module-cffi python-module-cryptography python-module-enum34 python-module-mimeparse python-module-pbr python-module-pyasn1 python-module-pytest python-module-serial python-module-setuptools python-module-testtools python-module-traceback2 python-module-twisted-core python-module-unittest2 python-module-zope.interface python-modules python-modules-compiler python-modules-ctypes python-modules-email python-modules-encodings python-modules-json python-modules-unittest python3 python3-base python3-module-cffi python3-module-cryptography python3-module-cssselect python3-module-enum34 python3-module-genshi python3-module-mimeparse python3-module-ntlm python3-module-pbr python3-module-pip python3-module-pycparser python3-module-pytest python3-module-setuptools python3-module-testtools python3-module-traceback2 python3-module-unittest2
BuildRequires: python-module-fixtures python-module-setuptools-tests python3-module-fixtures python3-module-html5lib python3-module-setuptools-tests rpm-build-python3

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
* Wed Jan 11 2017 Igor Vlasenko <viy@altlinux.ru> 0.3.8-alt1
- automated PyPI update

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.3.5-alt1.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 0.3.5-alt1.1
- NMU: Use buildreq for BR.

* Fri Dec 12 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.3.5-alt1
- Initial build for Sisyphus

