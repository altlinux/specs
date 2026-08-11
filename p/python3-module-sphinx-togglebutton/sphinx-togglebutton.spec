%global _unpackaged_files_terminate_build 1
%define pypi_name sphinx-togglebutton

%def_with check

Name: python3-module-%pypi_name
Version: 0.4.5
Release: alt1
Summary: Toggle page content and collapse admonitions in Sphinx.
Group: Development/Python3
License: MIT
BuildArch: noarch
Url: https://pypi.org/project/sphinx-togglebutton/
VCS: https://github.com/executablebooks/sphinx-togglebutton

Source0: %name-%version.tar

BuildRequires(pre): rpm-build-pyproject
BuildRequires: python3(setuptools)
BuildRequires: python3(wheel)

%if_with check
BuildRequires: python3(pytest)
BuildRequires: python3(docutils)
BuildRequires: python3(matplotlib)
BuildRequires: python3(numpy)
BuildRequires: python3(sphinx)
BuildRequires: python3(wheel)
%endif
Requires: python3(docutils)
Requires: python3(matplotlib)
Requires: python3(numpy)
Requires: python3(sphinx)
Requires: python3(wheel)

%py3_provides %pypi_name

%description
sphinx-togglebuttonA small sphinx extension to make it possible to add a
"toggle button" to sections of your page. This allows you to:- Collapse Sphinx
admonitions (notes, warnings, etc) so that their content is hidden until users
click a toggle button. 

%prep
%setup
rm -rf %pypi_name.egg-info

%build
%pyproject_build

%install
%pyproject_install

%check
#tox_check_pyproject

%files
%python3_sitelibdir/sphinx_togglebutton/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}

%changelog
* Tue Aug 11 2026 Pavel Shilov <zerospirit@altlinux.org> 0.4.5-alt1
- Initial build for ALT Linux.

