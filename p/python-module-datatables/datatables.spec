%define oname datatables

%def_with python3

Name: python-module-%oname
Version: 0.4.9
Release: alt1.git20150106.1
Summary: Integrates SQLAlchemy with DataTables (framework agnostic)
License: MIT
Group: Development/Python
Url: https://pypi.python.org/pypi/datatables/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/orf/datatables.git
Source: %name-%version.tar
BuildArch: noarch

#BuildPreReq: python-devel python-module-setuptools-tests
#BuildPreReq: python-module-SQLAlchemy python-module-coveralls
#BuildPreReq: python-module-fake-factory python-modules-sqlite3
%if_with python3
BuildRequires(pre): rpm-build-python3
#BuildPreReq: python3-devel python3-module-setuptools-tests
#BuildPreReq: python3-module-SQLAlchemy python3-module-coveralls
#BuildPreReq: python3-module-fake-factory python3-modules-sqlite3
%endif

%py_provides %oname

# Automatically added by buildreq on Wed Jan 27 2016 (-bi)
# optimized out: python-base python-devel python-module-cffi python-module-chardet python-module-coverage python-module-cryptography python-module-enum34 python-module-ndg-httpsclient python-module-ntlm python-module-pyasn1 python-module-pytest python-module-setuptools python-module-yaml python-modules python-modules-compiler python-modules-ctypes python-modules-email python-modules-encodings python-modules-unittest python3 python3-base python3-module-chardet python3-module-coverage python3-module-pytest python3-module-setuptools python3-module-sh python3-module-yaml python3-module-yieldfrom.http.client python3-module-yieldfrom.requests python3-module-yieldfrom.urllib3
BuildRequires: python-module-setuptools-tests python-module-z4r-coveralls python3-module-setuptools-tests python3-module-z4r-coveralls rpm-build-python3

%description
Integrates SQLAlchemy with DataTables (framework agnostic).

%package -n python3-module-%oname
Summary: Integrates SQLAlchemy with DataTables (framework agnostic)
Group: Development/Python3
%py3_provides %oname

%description -n python3-module-%oname
Integrates SQLAlchemy with DataTables (framework agnostic).

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
%doc *.rst
%python_sitelibdir/*

%if_with python3
%files -n python3-module-%oname
%doc *.rst
%python3_sitelibdir/*
%endif

%changelog
* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 0.4.9-alt1.git20150106.1
- NMU: Use buildreq for BR.

* Sun Jan 18 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.4.9-alt1.git20150106
- Version 0.4.9

* Tue Dec 23 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.4.6-alt1.git20141222
- Initial build for Sisyphus

