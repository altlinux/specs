Name: python3-module-gammu
Version: 2.8
Release: alt2

Summary: Python module to communicate with mobile phones
License: GPLv2
Group: Development/Python3

Url: http://wammu.eu/gammu/
Source0: %name-%version.tar.gz
Source100: python-module-gammu.watch
Packager: Michael Shigorin <mike@altlinux.org>

BuildRequires: libgammu-devel
Obsoletes: python-gammu

%description
This provides Python gammu module that can work with any phone
that Gammu supports - many Nokias, Siemens, Alcatel, ...

%prep
%setup

%build
%python3_build

%install
%python3_install

%files
%python3_sitelibdir/gammu
%python3_sitelibdir/*.egg-info

%changelog
* Tue Aug 03 2021 Grigory Ustinov <grenka@altlinux.org> 2.8-alt2
- Transferred on python3.
- Fixed license tag.

* Fri Jun 16 2017 Michael Shigorin <mike@altlinux.org> 2.8-alt1
- new version (watch file uupdate)

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
