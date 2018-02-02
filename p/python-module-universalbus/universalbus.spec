%define _unpackaged_files_terminate_build 1
%define oname universalbus

%def_with python3

Name: python-module-%oname
Version: 0.0.10
Release: alt1.1
Summary: Universal Bus over rabbitmq
License: Free
Group: Development/Python
Url: https://pypi.python.org/pypi/universalbus/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/KokocGroup/universal-bus.git
Source0: https://pypi.python.org/packages/b4/5e/d7f498992f115136331f10f0051cf9bce43a1f4fcd9a5296b51a4400d8f8/%{oname}-%{version}.tar.gz
BuildArch: noarch

#BuildPreReq: python-devel python-module-setuptools
#BuildPreReq: python-module-pika python-modules-json
%if_with python3
BuildRequires(pre): rpm-build-python3
#BuildPreReq: python3-devel python3-module-setuptools
#BuildPreReq: python3-module-pika
%endif

%py_provides %oname

# Automatically added by buildreq on Thu Jan 28 2016 (-bi)
# optimized out: python-base python-devel python-module-cffi python-module-cryptography python-module-enum34 python-module-pyasn1 python-module-pycares python-module-pycurl python-module-pyev python-module-pytest python-module-serial python-module-setuptools python-module-twisted-core python-module-zope.interface python-modules python-modules-compiler python-modules-ctypes python-modules-email python-modules-encodings python-modules-unittest python-modules-wsgiref python3 python3-base python3-module-cffi python3-module-cryptography python3-module-enum34 python3-module-pycares python3-module-pycparser python3-module-pyev python3-module-pygobject3 python3-module-pytest python3-module-serial python3-module-setuptools python3-module-zope python3-module-zope.interface
BuildRequires: python-module-pika python-module-setuptools python3-module-pika python3-module-setuptools rpm-build-python3

%description
Universal Bus over rabbitmq.

%package -n python3-module-%oname
Summary: Universal Bus over rabbitmq
Group: Development/Python3
%py3_provides %oname

%description -n python3-module-%oname
Universal Bus over rabbitmq.

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
%doc PKG-INFO
%python_sitelibdir/*

%if_with python3
%files -n python3-module-%oname
%doc PKG-INFO
%python3_sitelibdir/*
%endif

%changelog
* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 0.0.10-alt1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Tue Jan 17 2017 Igor Vlasenko <viy@altlinux.ru> 0.0.10-alt1
- automated PyPI update

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.0.6-alt1.git20141116.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 0.0.6-alt1.git20141116.1
- NMU: Use buildreq for BR.

* Mon Nov 17 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.0.6-alt1.git20141116
- Version 0.0.6

* Thu Nov 13 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.0.5-alt1.git20141113
- Initial build for Sisyphus

