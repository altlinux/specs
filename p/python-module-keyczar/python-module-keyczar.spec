%define module_name keyczar

%def_with python3

Name: python-module-%module_name
Version: 0.715
Release: alt1.1.1

Summary: Toolkit for safe and simple cryptography

License: Apache 2.0
Group: Development/Python
Url: http://www.keyczar.org/

Source: python-%module_name-%version.tar

BuildArch: noarch
#BuildPreReq: python-devel python-module-setuptools-tests
#BuildPreReq: python-module-pycrypto python-module-pyasn1
#BuildPreReq: python-modules-json
%if_with python3
BuildRequires(pre): rpm-build-python3
#BuildPreReq: python3-devel python3-module-setuptools-tests
#BuildPreReq: python3-module-pycrypto python3-module-pyasn1
#BuildPreReq: python-tools-2to3
%endif

%setup_python_module %module_name
%py_requires Crypto pyasn1 json

# Automatically added by buildreq on Thu Jan 28 2016 (-bi)
# optimized out: python-base python-devel python-module-pluggy python-module-py python-module-pytest python-module-setuptools python-modules python-modules-compiler python-modules-ctypes python-modules-email python-modules-encodings python-modules-logging python-modules-unittest python-tools-2to3 python3 python3-base python3-module-pytest python3-module-setuptools
BuildRequires: python-module-pyasn1 python-module-pycrypto python-module-setuptools-tests python-modules-json python3-module-pycrypto python3-module-setuptools-tests rpm-build-python3 time

%description
Keyczar is an open source cryptographic toolkit designed to make it
easier and safer for developers to use cryptography in their
applications. Keyczar supports authentication and encryption with both
symmetric and asymmetric keys.

%package -n python3-module-%module_name
Summary: Toolkit for safe and simple cryptography
Group: Development/Python3
%py3_provides %module_name
%py3_requires Crypto pyasn1

%description -n python3-module-%module_name
Keyczar is an open source cryptographic toolkit designed to make it
easier and safer for developers to use cryptography in their
applications. Keyczar supports authentication and encryption with both
symmetric and asymmetric keys.

%prep
%setup

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
%files -n python3-module-%module_name
%doc ChangeLog README doc/*
%_bindir/*.py3
%python3_sitelibdir/keyczar
%python3_sitelibdir/python_keyczar*
%endif

%changelog
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

