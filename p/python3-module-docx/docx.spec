%define modulename docx

Name:    python3-module-%modulename
Version: 1.0.1
Release: alt1

Summary: Create and update Microsoft Word .docx files.

License: MIT
Group:   Development/Python3
URL:     https://github.com/python-openxml/python-docx

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-wheel

BuildArch: noarch

Source:  %name-%version.tar.gz

%description
%summary

%prep
%setup

%build
%pyproject_build

%install
%pyproject_install

%files
%doc LICENSE *.rst
%python3_sitelibdir/%modulename
%python3_sitelibdir/python_%modulename-%version.dist-info

%changelog
* Sat Oct 21 2023 Grigory Ustinov <grenka@altlinux.org> 1.0.1-alt1
- Automatically updated to 1.0.1.

* Sun Jun 06 2021 Grigory Ustinov <grenka@altlinux.org> 0.8.11-alt1
- Automatically updated to 0.8.11.

* Mon Nov 09 2020 Grigory Ustinov <grenka@altlinux.org> 0.8.10-alt1
- Initial build for Sisyphus.
