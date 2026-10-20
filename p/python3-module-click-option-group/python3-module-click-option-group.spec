%define pypi_name click-option-group
%define mod_name click_option_group

%def_with check

Name:    python3-module-%pypi_name
Version: 0.5.9
Release: alt1

Summary: Option groups missing in Click
License: BSD-3-Clause
Group:   Development/Python3
URL:     https://click-option-group.readthedocs.io/
VCS:     https://github.com/click-contrib/click-option-group

BuildRequires(pre): rpm-macros-python3
BuildRequires: rpm-build-python3
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-wheel
BuildRequires: python3-module-hatch-vcs

%if_with check
BuildRequires: python3-module-click
%endif

BuildArch: noarch

Source: %name-%version.tar

%description
click-option-group is a Click-extension package that adds option groups missing
in Click.

%prep
%setup

%build
export SETUPTOOLS_SCM_PRETEND_VERSION=%version
%pyproject_build

%install
%pyproject_install

%check
%pyproject_run_pytest -v

%files
%doc LICENSE *.md
%python3_sitelibdir/%mod_name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}

%changelog
* Thu Oct 08 2026 Evgeniy Serov <scala@altlinux.org> 0.5.9-alt1
- Initial build for Sisyphus.
