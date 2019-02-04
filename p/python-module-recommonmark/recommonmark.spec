%define version 0.5.0
%define release alt0.1
%setup_python_module recommonmark

Name: %{packagename}
Version: %version
Release: %release
Summary: A markdown parser for docutils

Group: Development/Python
License: MIT
Url: https://github.com/rtfd/recommonmark
Source0: %modulename-%{version}.tar

BuildArch: noarch

Packager: L.A. Kostis <lakostis@altlinux.ru>

%description
A docutils-compatibility bridge to CommonMark.
This allows you to write CommonMark inside of Docutils & Sphinx projects.

%prep
%setup -q -n %modulename-%{version}

%build
%python_build

%install
%python_install --optimize=2 --record=INSTALLED_FILES

%files -f INSTALLED_FILES
%doc README.md

%changelog
* Mon Feb 04 2019 L.A. Kostis <lakostis@altlinux.ru> 0.5.0-alt0.1
- Initial build for ALTLinux.


