%define origname python-gammu

Name: python-module-gammu
Version: 2.7
Release: alt1.1

Summary: Python module to communicate with mobile phones
License: GPL
Group: Communications

Url: http://wammu.eu/gammu/
Source0: http://dl.cihar.com/%origname/python-gammu-%version.tar.gz
Source100: python-module-gammu.watch
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
* Mon Dec 12 2016 Michael Shigorin <mike@altlinux.org> 2.7-alt1.1
- rebuilt against current libgammu

* Mon Oct 24 2016 Michael Shigorin <mike@altlinux.org> 2.7-alt1
- new version (watch file uupdate)

* Tue May 24 2016 Michael Shigorin <mike@altlinux.org> 2.6-alt1
- new version (watch file uupdate)

* Tue Jan 19 2016 Michael Shigorin <mike@altlinux.org> 2.5-alt1
- new version (watch file uupdate)

* Wed Sep 02 2015 Michael Shigorin <mike@altlinux.org> 2.4-alt1
- new version (watch file uupdate)

* Sun Aug 16 2015 Michael Shigorin <mike@altlinux.org> 2.3-alt1
- new version (watch file uupdate)

* Wed May 13 2015 Michael Shigorin <mike@altlinux.org> 2.2-alt1
- new version (watch file uupdate)

* Thu May 07 2015 Michael Shigorin <mike@altlinux.org> 2.1-alt1
- built separately
