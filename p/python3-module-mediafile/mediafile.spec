%define pypi_name mediafile

%def_with check

Name: python3-module-%pypi_name
Version: 0.17.0
Release: alt1
Summary: elegant audio file tagging
License: MIT
Group: Development/Python3
Url: https://pypi.org/project/mediafile/
Vcs: https://github.com/beetbox/mediafile

BuildArch: noarch

Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-poetry-core

%if_with check
BuildRequires: python3-module-pytest
BuildRequires: python3-module-mutagen
BuildRequires: python3-module-filetype
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
%pyproject_run_pytest -v -k 'not test_read_audio_properties'

%files
%doc *.rst
%python3_sitelibdir/%pypi_name
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}/

%changelog
* Sun Jul 12 2026 Anton Vyatkin <toni@altlinux.org> 0.17.0-alt1
- New version 0.17.0.

* Sat Feb 07 2026 Grigory Ustinov <grenka@altlinux.org> 0.14.0-alt1
- Automatically updated to 0.14.0.

* Sun Oct 12 2025 Grigory Ustinov <grenka@altlinux.org> 0.9.0-alt1.1
- NMU: fixed FTBFS.

* Tue Aug 26 2025 Pavel Shilov <zerospirit@altlinux.org> 0.9.0-alt1
- Initial build for Sisyphus.
