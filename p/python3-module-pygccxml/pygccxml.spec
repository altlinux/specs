%define  modulename pygccxml

Name:    python3-module-%modulename
Version: 2.5.0
Release: alt1

Summary: Python library for loading and using triangular meshes.
License: MIT
Group:   Development/Python3
URL:     https://github.com/gccxml/pygccxml

BuildRequires(pre): rpm-macros-python3
BuildRequires: rpm-build-python3
BuildRequires: python3-dev python3-module-setuptools
BuildRequires: python3-module-wheel

BuildArch: noarch

# Source-url: https://github.com/gccxml/pygccxml/archive/v%version/pygccxml-%version.tar.gz
Source: %modulename-%version.tar

%description
%summary.

%prep
%setup -n %modulename-%version

%build
%pyproject_build

%install
%pyproject_install

%files
%python3_sitelibdir/%modulename/
%python3_sitelibdir/*.dist-info
%doc *.md

%changelog
* Mon Aug 12 2024 Anton Midyukov <antohami@altlinux.org> 2.5.0-alt1
- Initial build
