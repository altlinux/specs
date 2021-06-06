%define modulename docx

Name:    python3-module-%modulename
Version: 0.8.11
Release: alt1

Summary: Create and update Microsoft Word .docx files.

License: MIT
Group:   Development/Python3
URL:     https://github.com/python-openxml/python-docx

BuildRequires(pre): rpm-build-python3

BuildArch: noarch

Source:  %name-%version.tar.gz

%description
%summary

%prep
%setup

%build
%python3_build

%install
%python3_install

%files
%python3_sitelibdir/%modulename/
%python3_sitelibdir/*.egg-info
%doc *.rst

%changelog
* Sun Jun 06 2021 Grigory Ustinov <grenka@altlinux.org> 0.8.11-alt1
- Automatically updated to 0.8.11.

* Mon Nov 09 2020 Grigory Ustinov <grenka@altlinux.org> 0.8.10-alt1
- Initial build for Sisyphus.
