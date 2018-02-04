%define oname rsa

%def_with python3

Name: python-module-%oname
Version: 3.4.2
Release: alt1.1
Summary: Pure-Python RSA implementation
License: ASLv2
Group: Development/Python
Url: https://pypi.python.org/pypi/rsa/

Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-module-setuptools python-module-pyasn1
BuildPreReq: python-module-unittest2 python-module-pytest
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-module-setuptools python3-module-pyasn1
BuildPreReq: python3-module-unittest2 python3-devel
BuildPreReq: python-tools-2to3 python3-module-pytest
%endif

%py_provides %oname

%description
Python-RSA is a pure-Python RSA implementation. It supports encryption
and decryption, signing and verifying signatures, and key generation
according to PKCS#1 version 1.5. It can be used as a Python library as
well as on the commandline. The code was mostly written by Sybren A.
Stuvel.

%package -n python3-module-%oname
Summary: Pure-Python RSA implementation
Group: Development/Python3
%py3_provides %oname

%description -n python3-module-%oname
Python-RSA is a pure-Python RSA implementation. It supports encryption
and decryption, signing and verifying signatures, and key generation
according to PKCS#1 version 1.5. It can be used as a Python library as
well as on the commandline. The code was mostly written by Sybren A.
Stuvel.

%prep
%setup

%if_with python3
cp -fR . ../python3
find ../python3/rsa -type f -name '*.py' -exec 2to3 -w -n '{}' +
%endif

%build
%python_build_debug

%if_with python3
pushd ../python3
%python3_build_debug
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
py.test
%if_with python3
pushd ../python3
python3 setup.py test
py.test3
popd
%endif

%files
%doc LICENSE README.md
%_bindir/*
%if_with python3
%exclude %_bindir/*.py3
%endif
%python_sitelibdir/*

%if_with python3
%files -n python3-module-%oname
%doc LICENSE README.md
%_bindir/*.py3
%python3_sitelibdir/*
%endif

%changelog
* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 3.4.2-alt1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Thu Aug 03 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 3.4.2-alt1
- Updated to upstream releases 3.4.2.

* Mon Nov 14 2016 Lenar Shakirov <snejok@altlinux.ru> 3.3-alt1
- Version 3.3

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 3.2-alt1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Sun Aug 16 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.2-alt1
- Version 3.2

* Tue Oct 28 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.1.4-alt1
- Initial build for Sisyphus

