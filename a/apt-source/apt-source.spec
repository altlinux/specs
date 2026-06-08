%define _unpackaged_files_terminate_build 1
%define mod_name apt_source

Name: apt-source
Version: 0.1.1
Release: alt1

Summary: APT sources list manager
License: GPLv2+
Group: System/Configuration/Other
URL: https://altlinux.space/alterator/apt-source

BuildArch: noarch

Source0: %name-%version.tar

Requires: python3-module-%{mod_name}

BuildRequires(pre): rpm-build-pyproject
BuildRequires: python3-devel
BuildRequires: python3-module-setuptools
%{?!_without_check:%{?!_disable_check:
BuildRequires: python3-module-pytest
BuildRequires: python3-module-faker
}}

%description
%summary.

%package -n python3-module-%{mod_name}
Summary: APT sources list manager
Group: Development/Python3
Requires: python3-module-tabulate

%description -n python3-module-%{mod_name}
%summary.

%prep
%setup

%build
%pyproject_build

%install
%pyproject_install

%check
%pyproject_run_pytest

%files
%_bindir/%name

%files -n python3-module-%{mod_name}
%python3_sitelibdir/%mod_name/
%python3_sitelibdir/%{pyproject_distinfo %mod_name}


%changelog
* Mon Jun 08 2026 Maria Alexeeva <alxvmr@altlinux.org> 0.1.1-alt1
- Added transactional file deletion for source tables.
- Fixed Repository.get_table() resolves symlinks and non-canonical
  paths correctly.
- Thx Oleg Chagaev.

* Mon Mar 30 2026 Maria Alexeeva <alxvmr@altlinux.org> 0.1.0-alt1
- First build for Sisyphus.

