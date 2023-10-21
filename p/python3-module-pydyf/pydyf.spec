%define  oname pydyf
%def_with check

Name:    python3-module-%oname
Version: 0.8.0
Release: alt1

Summary: A low-level PDF creator

License: BSD-3-Clause
Group:   Development/Python3
URL:     https://pypi.org/project/pydyf

# https://github.com/CourtBouillon/pydyf
Source:  %name-%version.tar

Packager: Grigory Ustinov <grenka@altlinux.org>

BuildRequires(pre): rpm-build-python3

BuildRequires: python3-module-flit

%if_with check
BuildRequires: python3-module-Pillow
BuildRequires: ghostscript
%endif

BuildArch: noarch

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
%tox_check_pyproject -- -k'not test_text'

%files
%doc *.rst
%python3_sitelibdir/%oname
%python3_sitelibdir/*.dist-info

%changelog
* Sat Oct 21 2023 Grigory Ustinov <grenka@altlinux.org> 0.8.0-alt1
- Automatically updated to 0.8.0.

* Thu Jul 20 2023 Grigory Ustinov <grenka@altlinux.org> 0.7.0-alt1
- Automatically updated to 0.7.0.

* Fri Mar 31 2023 Grigory Ustinov <grenka@altlinux.org> 0.6.0-alt1
- New version 0.6.0.

* Tue Oct 18 2022 Grigory Ustinov <grenka@altlinux.org> 0.5.0-alt1
- Initial build for Sisyphus.
