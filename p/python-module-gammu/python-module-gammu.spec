%define origname python-gammu

Name: python-module-gammu
Version: 2.1
Release: alt1

Summary: Python module to communicate with mobile phones
License: GPL
Group: Communications

Url: http://wammu.eu/gammu/
Source0: http://dl.cihar.com/%origname/%origname-%version.tar.gz
#Source100: python-module-gammu.watch
Packager: Michael Shigorin <mike@altlinux.org>

BuildRequires: python-module-setuptools libgammu-devel
Obsoletes: python-gammu

%setup_python_module %origname

%description
This provides Python gammu module that can work with any phone
that Gammu supports - many Nokias, Siemens, Alcatel, ...

%prep
%setup -n %origname-%version

%build
%python_build

%install
%python_install

%files
%python_sitelibdir/gammu

%changelog
* Thu May 07 2015 Michael Shigorin <mike@altlinux.org> 2.1-alt1
- built separately
