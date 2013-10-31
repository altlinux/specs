%define sname pysnmp-apps

Name: python-module-pysnmp-apps
Version: 0.3.4
Release: alt1
Url: http://sourceforge.net/projects/pysnmp/
Summary: PySNMP-based command-line tools
License: BSD
Group: Networking/Other
Packager: Evgenii Terechkov <evg@altlinux.org>
Source: %sname-%version.tar.gz

BuildRequires: python-module-setuptools
BuildArch: noarch

%description
PySNMP-based command-line tools, can be used for quick testing and network management purposes

%prep
%setup -n %sname-%version

%build
%python_build

%install
%python_install --record=INSTALLED_FILES

%files -f INSTALLED_FILES
%doc README CHANGES PKG-INFO LICENSE

%changelog
* Fri Nov  1 2013 Terechkov Evgenii <evg@altlinux.org> 0.3.4-alt1
- Initial build for ALT Linux Sisyphus
