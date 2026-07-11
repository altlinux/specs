%define srcname sarge

Name: python3-module-%srcname
Summary: Command pipelines for python 3
Version: 0.1.8
Release: alt1
License: BSD-3-Clause
Url: https://sarge.readthedocs.org/
Group: Development/Python3

# Source-url: https://files.pythonhosted.org/packages/source/s/sarge/sarge-%version.tar.gz
Source: %srcname-%version.tar
Patch: sarge-0.1.8-fix-build.patch

BuildRequires(pre): rpm-macros-python3
BuildRequires: rpm-build-python3
BuildRequires: python3-dev
BuildRequires: python3-module-setuptools

BuildArch: noarch

%description
A wrapper for subprocess which provides command pipeline functionality.

%prep
%setup -n %srcname-%version
%autopatch -p2

%build
%pyproject_build

%install
%pyproject_install

%check
%pyproject_run_pytest

%files
%doc README.rst
%python3_sitelibdir/*

%changelog
* Sat Jul 11 2026 Anton Midyukov <antohami@altlinux.org> 0.1.8-alt1
- New version 0.1.8.

* Thu Jul 29 2021 Anton Midyukov <antohami@altlinux.org> 0.1.6-alt1
- Initial build.
