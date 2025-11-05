%define _unpackaged_files_terminate_build 1
%define pypi_name libloader

Name:    python3-module-%pypi_name
Version: 1.4.2
Release: alt1

Summary: Cross-platform shared library loader which expects a certain path structure
License: MIT
Group:   Development/Python3
URL:     https://github.com/accessibleapps/libloader

%add_python3_req_skip pywintypes
%add_python3_req_skip win32com.client

BuildRequires(pre): rpm-macros-python3
BuildRequires: rpm-build-python3
BuildRequires: python3-devel
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-wheel
BuildRequires: python3-module-hatchling

BuildArch: noarch

Source: %pypi_name-%version.tar

%description
Libloader provides a way to quickly and easily load shared libraries on macOS,
Windows and Linux.

%prep
%setup -n %pypi_name-%version

%build
%pyproject_build

%install
%pyproject_install

%files
%python3_sitelibdir/%pypi_name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}

%changelog
* Wed Nov 05 2025 Artem Semenov <savoptik@altlinux.org> 1.4.2-alt1
- updated to new version 1.4.2

* Tue Oct 28 2025 Artem Semenov <savoptik@altlinux.org> 1.4.1-alt1
- updated to new version 1.4.1

* Tue Oct 21 2025 Artem Semenov <savoptik@altlinux.org> 1.4.0-alt1
- updated to new version 1.4.0

* Tue Aug 05 2025 Artem Semenov <savoptik@altlinux.org> 1.3.3-alt1
- updated to new version 1.3.3

* Tue Apr 22 2025 Artem Semenov <savoptik@altlinux.org> 1.3.1-alt1
- updated to new version 1.3.1

* Fri Mar 21 2025 Artem Semenov <savoptik@altlinux.org> 0.21-alt2
- Added description
- Cleaned-up the spec

* Tue Jan 21 2025 Artem Semenov <savoptik@altlinux.org> 0.21-alt1
- Initial build for Sisyphus
