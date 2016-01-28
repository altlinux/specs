%define oname identicon

%def_with python3

Name: python-module-%oname
Version: 20101207
Release: alt1.1
Summary: Python identicon implementation
License: BSD
Group: Development/Python
Url: https://github.com/aerosol/identicon
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/aerosol/identicon.git
Source: %name-%version.tar
BuildArch: noarch

#BuildPreReq: python-module-setuptools
%if_with python3
BuildRequires(pre): rpm-build-python3
#BuildPreReq: python3-devel python3-module-setuptools
#BuildPreReq: python-tools-2to3
%endif

%py_requires PIL

# Automatically added by buildreq on Thu Jan 28 2016 (-bi)
# optimized out: python-base python-modules python-modules-compiler python-modules-email python-modules-encodings python-modules-logging python3 python3-base
BuildRequires: python-devel python-tools-2to3 rpm-build-python3 time

%description
identicon.py: identicon python implementation.

%package -n python3-module-%oname
Summary: Python identicon implementation
Group: Development/Python3
%py3_requires PIL

%description -n python3-module-%oname
identicon.py: identicon python implementation.

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
%python_install

%if_with python3
pushd ../python3
%python3_install
popd
%endif

%files
%doc *.md
%python_sitelibdir/*

%if_with python3
%files -n python3-module-%oname
%doc *.md
%python3_sitelibdir/*
%endif

%changelog
* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 20101207-alt1.1
- NMU: Use buildreq for BR.

* Tue Sep 02 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 20101207-alt1
- Initial build for Sisyphus

