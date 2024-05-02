%define modulename docx

%def_with check

Name:    python3-module-%modulename
Version: 1.1.2
Release: alt1

Summary: Create and update Microsoft Word .docx files

License: MIT
Group:   Development/Python3
URL:     https://pypi.org/project/python-docx
VCS:     https://github.com/python-openxml/python-docx

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-wheel

%if_with check
BuildRequires: python3-module-pytest
BuildRequires: python3-module-lxml
BuildRequires: python3-module-typing-extensions
BuildRequires: python3-module-pyparsing
%endif

BuildArch: noarch

Source:  %name-%version.tar

%description
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
%doc LICENSE *.rst README.md
%python3_sitelibdir/%modulename
%python3_sitelibdir/python_%modulename-%version.dist-info

%changelog
* Thu May 02 2024 Grigory Ustinov <grenka@altlinux.org> 1.1.2-alt1
- Automatically updated to 1.1.2.
- Built with check.

* Mon Jan 01 2024 Grigory Ustinov <grenka@altlinux.org> 1.1.0-alt1
- Automatically updated to 1.1.0.

* Sat Oct 21 2023 Grigory Ustinov <grenka@altlinux.org> 1.0.1-alt1
- Automatically updated to 1.0.1.

* Sun Jun 06 2021 Grigory Ustinov <grenka@altlinux.org> 0.8.11-alt1
- Automatically updated to 0.8.11.

* Mon Nov 09 2020 Grigory Ustinov <grenka@altlinux.org> 0.8.10-alt1
- Initial build for Sisyphus.
