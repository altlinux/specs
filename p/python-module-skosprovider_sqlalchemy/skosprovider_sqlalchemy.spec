%define oname skosprovider_sqlalchemy

%def_with python3
%def_disable check

Name: python-module-%oname
Version: 0.4.1
Release: alt1.git20141218.1.1
Summary: A SQLAlchemy implementation of the skosprovider interface
License: MIT
Group: Development/Python
Url: https://pypi.python.org/pypi/skosprovider_sqlalchemy/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/koenedaele/skosprovider_sqlalchemy.git
Source: %name-%version.tar
BuildArch: noarch

#BuildPreReq: python-devel python-module-setuptools-tests
#BuildPreReq: python-module-skosprovider python-module-SQLAlchemy
#BuildPreReq: python-module-nose python-module-pytest-cov
#BuildPreReq: python-module-coveralls
%if_with python3
BuildRequires(pre): rpm-build-python3
#BuildPreReq: python3-devel python3-module-setuptools-tests
#BuildPreReq: python3-module-skosprovider python3-module-SQLAlchemy
#BuildPreReq: python3-module-nose python3-module-pytest-cov
#BuildPreReq: python3-module-coveralls
%endif

%py_provides %oname
%py_requires skosprovider sqlalchemy

# Automatically added by buildreq on Thu Jan 28 2016 (-bi)
# optimized out: python-base python-devel python-module-cffi python-module-chardet python-module-coverage python-module-cryptography python-module-enum34 python-module-ndg-httpsclient python-module-ntlm python-module-pyasn1 python-module-pytest python-module-setuptools python-module-yaml python-modules python-modules-compiler python-modules-ctypes python-modules-email python-modules-encodings python-modules-unittest python3 python3-base python3-module-chardet python3-module-coverage python3-module-pytest python3-module-setuptools python3-module-sh python3-module-yaml python3-module-yieldfrom.http.client python3-module-yieldfrom.requests python3-module-yieldfrom.urllib3
BuildRequires: python-module-nose python-module-pytest-cov python-module-z4r-coveralls python3-module-nose python3-module-pytest-cov python3-module-z4r-coveralls rpm-build-python3

%description
An implementation of the skosprovider interface against SQLAlchemy.

%package -n python3-module-%oname
Summary: A SQLAlchemy implementation of the skosprovider interface
Group: Development/Python3
%py3_provides %oname
%py3_requires skosprovider sqlalchemy

%description -n python3-module-%oname
An implementation of the skosprovider interface against SQLAlchemy.

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
%if_with python3
pushd ../python3
python3 setup.py test
popd
%endif

%files
%doc *.rst docs/*.rst
%_bindir/*
%if_with python3
%exclude %_bindir/*.py3
%endif
%python_sitelibdir/*

%if_with python3
%files -n python3-module-%oname
%doc *.rst docs/*.rst
%_bindir/*.py3
%python3_sitelibdir/*
%endif

%changelog
* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.4.1-alt1.git20141218.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 0.4.1-alt1.git20141218.1
- NMU: Use buildreq for BR.

* Sat Jan 17 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.4.1-alt1.git20141218
- Initial build for Sisyphus

