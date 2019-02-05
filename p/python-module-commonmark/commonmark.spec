%define version 0.8.1
%define release alt0.1
%setup_python_module commonmark

Name: %{packagename}
Version: %version
Release: %release
Summary: Python parser for the CommonMark Markdown spec

Group: Development/Python
License: MIT
Url: https://pypi.org/project/CommonMark
Source0: %modulename-%{version}.tar

BuildArch: noarch

Packager: L.A. Kostis <lakostis@altlinux.ru>

%description
Python parser for the CommonMark Markdown spec

%prep
%setup -q -n %modulename-%{version}

%build
%python_build

%install
%python_install --optimize=2 --record=INSTALLED_FILES

%files -f INSTALLED_FILES
%doc README.rst

%changelog
* Mon Feb 04 2019 L.A. Kostis <lakostis@altlinux.ru> 0.8.1-alt0.1
- Initial build for ALTLinux.

