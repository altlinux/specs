%define _unpackaged_files_terminate_build 1

# %check is disabled because for %check babi requires hecate (dead package)
%def_without check

Name: babi
Version: 1.5.5
Release: alt1

Summary: A simple text editor written in python
License: MIT
Group: Editors
Url: https://pypi.org/project/babi/
Vcs: https://github.com/asottile/babi

BuildArch: noarch
Source0: %name-%version.tar
Source1: %pyproject_deps_config_name
Requires: python3-module-%name
Requires: python3-modules-curses
%pyproject_runtimedeps_metadata
BuildRequires(pre): rpm-build-pyproject
%pyproject_builddeps_build

%if_with check
BuildRequires: python3-modules-curses
%pyproject_builddeps_metadata
%pyproject_builddeps_check
%endif

%description
A simple text editor written in python

%package -n python3-module-%name
Summary: python3 module for babi
Group: Development/Python3
%description -n python3-module-%name
python3 module for babi

%prep
%setup

# Remove the line 'license_file = LICENSE' for setuptools (actual for version 1.5.5)
sed -i '11d' setup.cfg

%pyproject_deps_resync_build
%pyproject_deps_resync_metadata

%if_with check
%pyproject_deps_resync_check_pipreqfile requirements-dev.txt
%endif

%build
%pyproject_build

%install
%pyproject_install

%check
%pyproject_run_pytest

%files
%_bindir/*

%files -n python3-module-%name
%doc README.md LICENSE
%python3_sitelibdir/%name/
%python3_sitelibdir/%{pyproject_distinfo %name}/

%changelog
* Sat Sep 02 2023 Vladislav Glinkin <smasher@altlinux.org> 1.5.5-alt1
- Initial build for ALT

