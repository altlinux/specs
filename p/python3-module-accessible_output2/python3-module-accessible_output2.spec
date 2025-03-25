%define _unpackaged_files_terminate_build 1
%define pypi_name accessible_output2

Name:    python3-module-%pypi_name
Version: 0.17
Release: alt2

Summary: Output speech and braille using a variety of screen-reading solutions
License: MIT
Group:   Development/Python3
URL:     https://github.com/accessibleapps/accessible_output2

BuildRequires(pre): rpm-macros-python3
BuildRequires: rpm-build-python3
BuildRequires: python3-devel
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-wheel
BuildRequires: python3-module-libloader
BuildRequires: python3-module-platform_utils

BuildArch: noarch

Source: %pypi_name-%version.tar
%add_python3_req_skip pywintypes
%add_python3_req_skip libloader.com

%description
Accessible Output 2 makes it simple to add spoken and brailled notifications 
to your applications on multiple platforms,
facilitating accessibility for the visually impaired
and also providing a nice alternative means of providing notifications
to a sighted user.

%prep
%setup -n %pypi_name-%version
rm -rv accessible_output2/lib

%build
%pyproject_build

%install
%pyproject_install

%files
%python3_sitelibdir/%pypi_name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}

%changelog
* Fri Mar 21 2025 Artem Semenov <savoptik@altlinux.org> 0.17-alt2
- Cleaned-up the spec

* Tue Jan 21 2025 Artem Semenov <savoptik@altlinux.org> 0.17-alt1
- Initial build for Sisyphus (Closes: #52624)
