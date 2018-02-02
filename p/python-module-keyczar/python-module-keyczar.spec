%define oname keyczar

%def_with python3

Name: python-module-%oname
Version: 0.716
Release: alt1.1
Summary: Toolkit for safe and simple cryptography
License: Apache 2.0
Group: Development/Python
BuildArch: noarch
Url: https://github.com/google/keyczar

Source: python-%oname-%version.tar
Patch1: %oname-%version-alt-build.patch

BuildRequires: python-devel python-module-setuptools
BuildRequires: python-module-pycrypto python-module-pyasn1
BuildRequires: python-modules-json
BuildRequires: python-module-pytest
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel python3-module-setuptools
BuildRequires: python3-module-pycrypto python3-module-pyasn1
BuildRequires: python3-module-pytest
%endif

%setup_python_module %oname
%py_requires Crypto pyasn1 json

%description
Keyczar is an open source cryptographic toolkit designed to make it
easier and safer for developers to use cryptography in their
applications. Keyczar supports authentication and encryption with both
symmetric and asymmetric keys.

%package -n python3-module-%oname
Summary: Toolkit for safe and simple cryptography
Group: Development/Python3
%py3_provides %oname
%py3_requires Crypto pyasn1

%description -n python3-module-%oname
Keyczar is an open source cryptographic toolkit designed to make it
easier and safer for developers to use cryptography in their
applications. Keyczar supports authentication and encryption with both
symmetric and asymmetric keys.

%prep
%setup
%patch1 -p1

%if_with python3
cp -fR . ../python3
find ../python3 -type f -name '*.py' -exec 2to3 -w -n '{}' +
%endif

%build
%python_build

%if_with python3
pushd ../python3
%python3_build
popd
%endif

%install
%if_with python3
pushd ../python3
%python3_install
popd
pushd %buildroot%_bindir
for i in $(ls); do
	mv $i $i.py3
done
popd
%endif

%python_install

%check
python setup.py test
export PYTHONPATH=$PWD/src
pushd tests/keyczar_tests
py.test -vv
popd
%if_with python3
pushd ../python3
python3 setup.py test
popd
%endif

%files
%doc ChangeLog README doc/*
%_bindir/*
%if_with python3
%exclude %_bindir/*.py3
%endif
%python_sitelibdir/keyczar
%python_sitelibdir/python_keyczar*

%if_with python3
%files -n python3-module-%oname
%doc ChangeLog README doc/*
%_bindir/*.py3
%python3_sitelibdir/keyczar
%python3_sitelibdir/python_keyczar*
%endif

%changelog
* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 0.716-alt1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Thu Nov 23 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 0.716-alt1
- Updated to upstream version 0.716.
- Fixed compatibility issues with pyasn1-0.3.7.

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.715-alt1.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 0.715-alt1.1
- NMU: Use buildreq for BR.

* Wed Feb 25 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.715-alt1
- Version 0.715
- Added module for Python 3

* Fri Jan 11 2013 Igor Vlasenko <viy@altlinux.ru> 0.71c-alt2
- Sisyphus release

* Sat Jan 05 2013 Igor Vlasenko <viy@altlinux.ru> 0.71c-alt1_1
- fc import

* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.6b-alt1.1
- Rebuild with Python-2.7

* Fri Apr 16 2010 Denis Klimov <zver@altlinux.org> 0.6b-alt1
- Initial build for ALT Linux

