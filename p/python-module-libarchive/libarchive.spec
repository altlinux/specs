%define oname libarchive

%def_without python3

Name: python-module-%oname
Version: 3.1.2.1
Release: alt4.1
Summary: A libarchive wrapper for Python
License: BSD
Group: Development/Python
Url: https://pypi.python.org/pypi/python-libarchive/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

BuildPreReq: swig libarchive-devel zip
BuildPreReq: python-devel python-module-setuptools
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools
BuildPreReq: python-tools-2to3
%endif

%py_provides %oname
Requires: zip

%description
A complete wrapper for the libarchive library generated using SWIG. Also
included in the package are compatibility layers for the Python zipfile
and tarfile modules.

%if_with python3
%package -n python3-module-%oname
Summary: A libarchive wrapper for Python
Group: Development/Python3
%py3_provides %oname
Requires: zip

%description -n python3-module-%oname
A complete wrapper for the libarchive library generated using SWIG. Also
included in the package are compatibility layers for the Python zipfile
and tarfile modules.
%endif

%prep
%setup

rm -f %oname/*.c

%if_with python3
cp -fR . ../python3
sed -i 's|swig|swig -py3|' ../python3/%oname/Makefile
find ../python3 -type f -name '*.py' -exec 2to3 -w -n '{}' +
%endif

%build
%make -C %oname _libarchive_wrap.c
%python_build_debug

%if_with python3
pushd ../python3
%make -C %oname _libarchive_wrap.c
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
rm -fR %oname
export PYTHONPATH=%buildroot%python_sitelibdir
python tests.py
%if_with python3
pushd ../python3
python3 setup.py test
rm -fR %oname
export PYTHONPATH=%buildroot%python3_sitelibdir
python3 tests.py
popd
%endif

%files
%doc *.rst docs/*.rst
%python_sitelibdir/*

%if_with python3
%files -n python3-module-%oname
%doc *.rst docs/*.rst
%python3_sitelibdir/*
%endif

%changelog
* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 3.1.2.1-alt4.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Fri Jul 14 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 3.1.2.1-alt4
- Fixed build with new libarchive

* Mon Feb 08 2016 Sergey Alembekov <rt@altlinux.ru> 3.1.2.1-alt3
- Fixed _libarchive.i

* Tue Mar 03 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.1.2.1-alt2
- Fixed build

* Mon Dec 22 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.1.2.1-alt1
- Initial build for Sisyphus

