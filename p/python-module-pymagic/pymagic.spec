%define oname pymagic
%define sover 1

%def_without python3

Name: python-module-%oname
Version: 1.0
Release: alt2.1
Summary: libmagic bindings
License: GPLv3
Group: Development/Python
Url: https://pypi.python.org/pypi/libmagic/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

BuildPreReq: libmagic-devel
BuildPreReq: python-devel python-module-setuptools
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools
BuildPreReq: python-tools-2to3
%endif

%py_provides %oname
%ifarch x86_64
Requires: libmagic.so.%sover()(64bit)
%else
Requires: libmagic.so.%sover
%endif

%description
libmagic bindings using FFL (ctypes).

%if_with python3
%package -n python3-module-%oname
Summary: libmagic bindings
Group: Development/Python3
%py3_provides %oname
%ifarch x86_64
Requires: libmagic.so.%sover()(64bit)
%else
Requires: libmagic.so.%sover
%endif

%description -n python3-module-%oname
libmagic bindings using FFL (ctypes).
%endif

%prep
%setup

sed -i 's|@SOVER@|%sover|' pymagic.py

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
%python_install

%if_with python3
pushd ../python3
%python3_install
popd
%endif

%ifarch x86_64
mv %buildroot%_libexecdir %buildroot%_libdir
%endif

%check
python pymagic.py pymagic.py
%if_with python3
pushd ../python3
python3 pymagic.py pymagic.py
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
* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 1.0-alt2.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Thu Mar 05 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0-alt2
- Fixed build

* Tue Jan 20 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0-alt1
- Initial build for Sisyphus

