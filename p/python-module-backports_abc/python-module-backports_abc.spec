%define oname backports_abc
%def_without python3

Summary: ABC-Backports
Name: python-module-%oname
Version: 0.5
Release: alt1
Url: https://github.com/cython/backports_abc
Source: %name-%version.tar
Packager: Valentin Rosavitskiy <valintinr@altlinux.org>
License: PYTHON SOFTWARE FOUNDATION LICENSE VERSION 2
Group: Development/Python

BuildArch: noarch
BuildRequires: python-devel python-module-setupdocs python-module-setuptools

%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-module-setupdocs python3-module-setuptools
%endif

%description
A backport of recent additions to the 'collections.abc' module.

%package -n python3-module-%oname
Summary: ABC-Backports
Group: Development/Python3

%description -n python3-module-%oname
A backport of recent additions to the 'collections.abc' module.

%prep
%setup

%if_with python3
cp -fR . ../python3
%endif


%build
%add_optflags -fno-strict-aliasing
%python_build

%if_with python3
pushd ../python3
%python3_build
popd
%endif


%install
%python_build_install --prefix=/usr

%if_with python3
pushd ../python3
%python3_install
popd
%endif



%files
%doc CHANGES.rst LICENSE README.rst
%python_sitelibdir/*


%if_with python3
%files -n python3-module-%oname
%doc CHANGES.rst LICENSE README.rst
%python3_sitelibdir/*
%endif


%changelog
* Wed Nov 30 2016 Valentin Rosavitskiy <valintinr@altlinux.org> 0.5-alt1
- New version

* Thu Sep 08 2016 Valentin Rosavitskiy <valintinr@altlinux.org> 0.4-alt1
- Initial build for ALT

