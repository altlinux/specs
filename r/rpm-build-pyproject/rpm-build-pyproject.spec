%define _unpackaged_files_terminate_build 1

Name: rpm-build-pyproject
Version: 0.0.2
Release: alt1
Summary: Extra RPM macros for packaging Python projects
License: GPLv2+
Group: Development/Other
BuildArch: noarch
Source: %name-%version.tar

# run command
Requires: rpm-build-python3 >= 0.1.21-alt1
Requires: rpm-macros-pyproject = %EVR

%description
%summary.

%package -n rpm-macros-pyproject
Summary: Extra RPM macros for packaging Python projects
Group: Development/Other
BuildArch: noarch
Conflicts: %name < %version
Requires: python3-module-pyproject-installer >= 0.5.0

%description -n rpm-macros-pyproject
%summary.

%prep
%setup

%install
install -pD -m0644 macros/pyproject -t %buildroot%_rpmmacrosdir/

%files -n rpm-macros-pyproject
%_rpmmacrosdir/pyproject

%files
%doc docs/*

%changelog
* Wed Apr 19 2023 Stanislav Levin <slev@altlinux.org> 0.0.2-alt1
- Added %%pyproject_deps_config_name.
- Added more default exclusions of check dependencies.

* Mon Mar 20 2023 Stanislav Levin <slev@altlinux.org> 0.0.1-alt1
- Added support for external source of upstream dependencies.
