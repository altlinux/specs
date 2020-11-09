%define modulename docx

Name:    python3-module-%modulename
Version: 0.8.10
Release: alt1

Summary: Create and update Microsoft Word .docx files.

License: MIT
Group:   Development/Python3
URL:     https://github.com/python-openxml/python-docx

BuildRequires(pre): rpm-build-python3

BuildArch: noarch

Source:  %modulename-%version.tar.gz

Patch0: python-docx-0.8.10.alt.copy-templates.patch

%description
%summary

%prep
%setup -n %modulename-%version
%patch0 -p1

%build
%python3_build

%install
%python3_install

%files
%python3_sitelibdir/%modulename/
%python3_sitelibdir/*.egg-info
%doc *.rst

%changelog
* Mon Nov 09 2020 Grigory Ustinov <grenka@altlinux.org> 0.8.10-alt1
- Initial build for Sisyphus.
