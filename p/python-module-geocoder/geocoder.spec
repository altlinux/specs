%define _unpackaged_files_terminate_build 1
%define oname geocoder

%def_with python3
%def_disable check

Name: python-module-%oname
Version: 1.19.0
Release: alt1
Summary: A complete Python Geocoding module made easy
License: MIT
Group: Development/Python
Url: https://pypi.python.org/pypi/geocoder/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/DenisCarriere/geocoder.git
Source0: https://pypi.python.org/packages/12/13/77cce9fc7ffcb7f105ef04bc5c75107b85b5574bb9a50dbb6de9ac126c32/%{oname}-%{version}.tar.gz
BuildArch: noarch

#BuildPreReq: python-devel python-module-setuptools-tests
#BuildPreReq: python-module-requests python-module-ratelim
#BuildPreReq: python-modules-json
%if_with python3
BuildRequires(pre): rpm-build-python3
#BuildPreReq: python3-devel python3-module-setuptools-tests
#BuildPreReq: python3-module-requests python3-module-ratelim
#BuildPreReq: python-tools-2to3
%endif

%py_provides %oname
%py_requires json requests ratelim

# Automatically added by buildreq on Thu Jan 28 2016 (-bi)
# optimized out: python-base python-devel python-module-cffi python-module-cryptography python-module-enum34 python-module-pyasn1 python-module-setuptools python-modules python-modules-compiler python-modules-ctypes python-modules-email python-modules-encodings python-modules-logging python-modules-unittest python-tools-2to3 python3 python3-base python3-module-cffi python3-module-cryptography python3-module-enum34 python3-module-ndg-httpsclient python3-module-ntlm python3-module-pycparser python3-module-setuptools
BuildRequires: python-module-chardet python-module-ndg-httpsclient python-module-ntlm python-module-pytest python3-module-chardet python3-module-pytest python3-module-urllib3 rpm-build-python3 time

%description
A complete Python Geocoding module made easy.

Every task is made easy with tons of ``help`` & ``debug`` commands!

%package -n python3-module-%oname
Summary: A complete Python Geocoding module made easy
Group: Development/Python3
%py3_provides %oname
%py3_requires json requests ratelim

%description -n python3-module-%oname
A complete Python Geocoding module made easy.

Every task is made easy with tons of ``help`` & ``debug`` commands!

%prep
%setup -q -n %{oname}-%{version}

%if_with python3
cp -fR . ../python3
find ../python3 -type f -name '*.py' -exec 2to3 -w -n '{}' +
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
py.test -vv
%if_with python3
pushd ../python3
python3 setup.py test
py.test-%_python3_version -vv
popd
%endif

%files
%doc AUTHORS.rst PKG-INFO README.rst LICENSE
%_bindir/*
%if_with python3
%exclude %_bindir/*.py3
%endif
%python_sitelibdir/*

%if_with python3
%files -n python3-module-%oname
%doc AUTHORS.rst PKG-INFO README.rst LICENSE
%_bindir/*.py3
%python3_sitelibdir/*
%endif

%changelog
* Tue Jan 17 2017 Igor Vlasenko <viy@altlinux.ru> 1.19.0-alt1
- automated PyPI update

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 1.1.2-alt1.git20150203.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 1.1.2-alt1.git20150203.1
- NMU: Use buildreq for BR.

* Wed Feb 04 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.1.2-alt1.git20150203
- Version 1.1.2

* Tue Feb 03 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.1.1-alt1.git20150202
- Version 1.1.1

* Wed Jan 21 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.6-alt1.git20150120
- Initial build for Sisyphus

