%define pypi_name mediafile

%def_with check

Name: python3-module-%pypi_name
Version: 0.14.0
Release: alt1
Summary: elegant audio file tagging
License: MIT
Group: Development/Python3
Url: https://pypi.org/project/mediafile/
Vcs: https://github.com/beetbox/mediafile

BuildArch: noarch

Source: %name-%version.tar

BuildRequires(pre): rpm-build-pyproject
BuildRequires: python3-module-poetry
BuildRequires: python3-module-mutagen
BuildRequires: python3-module-filetype

%if_with check
BuildRequires: python3(pytest)
BuildRequires: python3(tox)
BuildRequires: python3-module-standard-imghdr
%endif

%py3_provides %pypi_name

%description
%summary.

%prep
%setup

%build
%pyproject_build

%install
%pyproject_install

%check
%tox_create_default_config
%tox_check_pyproject


%files
%doc *.rst
%python3_sitelibdir/%pypi_name
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}/

%changelog
* Sat Feb 07 2026 Grigory Ustinov <grenka@altlinux.org> 0.14.0-alt1
- Automatically updated to 0.14.0.

* Sun Oct 12 2025 Grigory Ustinov <grenka@altlinux.org> 0.9.0-alt1.1
- NMU: fixed FTBFS.

* Tue Aug 26 2025 Pavel Shilov <zerospirit@altlinux.org> 0.9.0-alt1
- Initial build for Sisyphus.
