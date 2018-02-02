%define oname geocodertools

%def_with python3

Name: python-module-%oname
Version: 0.1.4
Release: alt1.git20150322.1.1.1
Summary: Geo coordinates, reverse geo coding and getting city names out of coordinates
License: MIT
Group: Development/Python
Url: https://pypi.python.org/pypi/geocodertools/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/MartinThoma/geocodertools.git
Source: %name-%version.tar
BuildArch: noarch

#BuildPreReq: python-devel python-module-setuptools
#BuildPreReq: python-module-nose python-module-coverage
#BuildPreReq: python-module-msgpack
#BuildPreReq: python-modules-logging
%if_with python3
BuildRequires(pre): rpm-build-python3
#BuildPreReq: python3-devel python3-module-setuptools
#BuildPreReq: python3-module-nose python3-module-coverage
#BuildPreReq: python3-module-msgpack
%endif

%py_provides %oname
%py_requires logging msgpack

# Automatically added by buildreq on Thu Jan 28 2016 (-bi)
# optimized out: python-base python-devel python-module-pytest python-module-setuptools python-modules python-modules-compiler python-modules-ctypes python-modules-email python-modules-encodings python-modules-hotshot python-modules-json python-modules-logging python-modules-multiprocessing python-modules-unittest python-modules-xml python3 python3-base python3-module-pytest python3-module-setuptools xz
BuildRequires: python-module-coverage python-module-nose python-module-setuptools python3-module-coverage python3-module-nose python3-module-setuptools rpm-build-python3 time

%description
Functions to work with Geo coordinates, reverse geo coding and getting
city names out of coordinates without internet.

%if_with python3
%package -n python3-module-%oname
Summary: Geo coordinates, reverse geo coding and getting city names out of coordinates
Group: Development/Python3
%py3_provides %oname
%py3_requires logging msgpack

%description -n python3-module-%oname
Functions to work with Geo coordinates, reverse geo coding and getting
city names out of coordinates without internet.
%endif

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
%make test
%if_with python3
pushd ../python3
python3 setup.py test
sed -i 's|nosetests|nosetests3|' Makefile
%make test
popd
%endif

%files
%doc *.md docs/source/*.rst
%_bindir/*
%if_with python3
%exclude %_bindir/*.py3
%endif
%python_sitelibdir/*

%if_with python3
%files -n python3-module-%oname
%doc *.md docs/source/*.rst
%_bindir/*.py3
%python3_sitelibdir/*
%endif

%changelog
* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 0.1.4-alt1.git20150322.1.1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.1.4-alt1.git20150322.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 0.1.4-alt1.git20150322.1
- NMU: Use buildreq for BR.

* Sun Mar 22 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1.4-alt1.git20150322
- Initial build for Sisyphus

