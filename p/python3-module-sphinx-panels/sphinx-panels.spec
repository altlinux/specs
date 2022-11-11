%define _unpackaged_files_terminate_build 1
%define pypi_name sphinx-panels

Name: python3-module-%pypi_name
Version: 0.6.0
Release: alt2
License: MIT
Source: sphinx-panels-%version.tar
Group: Development/Python3
BuildArch: noarch
Summary: A sphinx extension for creating document components optimised for HTML+CSS

BuildRequires(pre): rpm-build-python3

# build backend and its deps
BuildRequires: python3(setuptools)
BuildRequires: python3(wheel)

%py3_provides %pypi_name

%description
A sphinx extension for creating document components optimised for HTML+CSS.
 *  The panels directive creates panels of content in a grid layout,
    utilising both the Bootstrap 4 grid system, and cards layout.
 *  The link-button directive creates a click-able button, linking to
    a URL or reference, and can also be used to make an entire panel
    click-able.
 *  The dropdown directive creates toggle-able content.
 *  The tabbed directive creates tabbed content.
 *  opticon and fa (fontawesome) roles allow for inline icons to be added.

%prep
%setup -n sphinx-panels-%version

%build
%pyproject_build

%install
%pyproject_install

%files
%python3_sitelibdir/sphinx_panels/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}/

%changelog
* Thu Nov 10 2022 Stanislav Levin <slev@altlinux.org> 0.6.0-alt2
- Fixed FTBFS (flit_core 3.7.1).

* Sun Apr 17 2022 Fr. Br. George <george@altlinux.org> 0.6.0-alt1
- Autobuild version bump to 0.6.0

* Sun Apr 17 2022 Fr. Br. George <george@altlinux.org> 0.5.2-alt2
- Initial release for ALT
