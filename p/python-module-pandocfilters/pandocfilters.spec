%define _unpackaged_files_terminate_build 1
%define oname pandocfilters

%def_with python3

Name: python-module-%oname
Version: 1.4.2
Release: alt1
Summary: Utilities for writing pandoc filters in python
License: BSD
Group: Development/Python
BuildArch: noarch
Url: https://github.com/jgm/pandocfilters

# https://github.com/jgm/pandocfilters.git
Source: %name-%version.tar
Patch1: %oname-%version-alt-fixes.patch

BuildRequires: python-devel python-module-setuptools
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel python3-module-setuptools
%endif

%description
A python module for writing pandoc filters.

%if_with python3
%package -n python3-module-%oname
Summary: Utilities for writing pandoc filters in python
Group: Development/Python3

%description -n python3-module-%oname
A python module for writing pandoc filters.
%endif

%prep
%setup
%patch1 -p1

%if_with python3
cp -fR . ../python3
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
%doc README LICENSE
%python_sitelibdir/*

%if_with python3
%files -n python3-module-%oname
%doc README LICENSE
%python3_sitelibdir/*
%endif

%changelog
* Thu Nov 23 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 1.4.2-alt1
- Initial build for ALT.
