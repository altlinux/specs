%define skeldir %_sysconfdir/skel.homeros.ru_RU.UTF-8

Name: homeros-core
Version: 20140202
Release: alt1
Summary: The set of scripts and settings for ALT Linux Homeros
Group: System/Configuration/Other
URL: http://homeros.altlinux.org/
License: GPL
BuildArch: noarch
Packager: Michael Pozhidaev <msp@altlinux.ru>
BuildRequires: etcskel emacs-nox emacs-devel

Source: %name-%version.tar.gz

%package -n homeros-install
Summary: The scripts for ALT Linux Homeros installation
Group: System/Configuration/Other
License: GPL

%package -n homeros-xutils
Summary: The scripts for launching mplayer and xpdf from terminal mode (designed for Homeros environment)
Group: System/Configuration/Other
License: GPL
Requires: mplayer mplayer-tools xpdf 

%package -n homeros-emacs
Summary: The set of GNU Emacs scripts for ALT Linux Homeros
Group: Editors
License: GPL
Requires: emacs-base

%package -n homeros-live-data
Summary: Various data files for ALT Linux Homeros LiveCD
Group: System/Configuration/Other
License: GPL

%description
The set of scripts and settings for ALT Linux Homeros

%description -n homeros-install
The scripts from this package implement LiveCD cloning technique for ALT Linux Homeros installation.

%description -n homeros-xutils
This package contains a following scripts:
- show-movie
- show-pdf

These scripts allow launching mplayer and xpdf from terminal mode
(including terminal GNU Emacs).

%description -n homeros-emacs
This package contains GNU Emacs scripts for ALT Linux Homeros.

%description -n homeros-live-data
The package with various data files for ALT Linux Homeros LiveCD environment.

%prep
%setup -q
%build
%byte_compile_file fsroot/usr/share/emacs/site-lisp/homeros-menu.el

%install
./homeros-core-install %buildroot

%files
%_datadir/sounds/homeros

%files -n homeros-xutils
%_bindir/show-movie
%_bindir/show-pdf

%files -n homeros-install
%_sbindir/homeros-install
/usr/libexec/homeros-install
%_datadir/homeros-install

%files -n homeros-emacs
%_datadir/homeros-emacs-menu
%_emacslispdir/*
%_sysconfdir/rc.d/init.d/homeros-emacs-menu

%files -n homeros-live-data
%_datadir/homeros-live-data

%changelog
* Sun Feb 02 2014 Michael Pozhidaev <msp@altlinux.ru> 20140202-alt1
- homeros-xutils subpackage restored with show-movie and show-pdf scripts

* Wed Jan 22 2014 Michael Pozhidaev <msp@altlinux.ru> 20140122-alt1
- homeros-install: rc.local in the new system is either empty or taken from /etc/rc.d/rc.local.homeros-install-initial

* Mon Aug 05 2013 Michael Pozhidaev <msp@altlinux.ru> 20130806-alt1
-homeros-install script goes to /sbin
- no longer useradd-homeros script
-  no longer skel directory for Homeros

* Mon Aug 05 2013 Michael Pozhidaev <msp@altlinux.ru> 20130805-alt1
- Fixed bug with local scripts launch in homeros-install
- useradd-homeros no longer invoked in homeros-install (usual useradd is used instead of it)

* Fri Apr 12 2013 Michael Pozhidaev <msp@altlinux.ru> 20130412-alt1
- homeros-install deep clean up
- New packages layout: homeros-core, homeros-install, homeros-emacs and homeros-live-data

* Wed Jul 18 2012 Michael Pozhidaev <msp@altlinux.ru> 20120718-alt1
- emacs23 req changed to emacs-nox

* Fri Feb 03 2012 Michael Pozhidaev <msp@altlinux.ru> 20120203-alt1
- Fixed emacs default configuration to be suited for updated w3m

* Sat Jan 14 2012 Michael Pozhidaev <msp@altlinux.ru> 20120114-alt1
- Homeros menu improvements

* Fri Jan 13 2012 Michael Pozhidaev <msp@altlinux.ru> 20120113-alt1
- New menu layout

* Sat Dec 10 2011 Michael Pozhidaev <msp@altlinux.ru> 20111209-alt1
- Added subpackage homeros-mobile
- Subpackage homeros-friend-data renamed to homeros-live-data
- /etc/skel.homeros renamed to /etc/skel.homeros.ru_RU.UTF-8

* Sun Nov 27 2011 Michael Pozhidaev <msp@altlinux.ru> 20111127-alt1
- Added emacspeak-35.0 support

* Tue May 17 2011 Michael Pozhidaev <msp@altlinux.ru> 20110517-alt1
- Added examples for address book and text book
- Added battery-status script
- Removed update-emacs-configuration script

* Fri May 06 2011 Michael Pozhidaev <msp@altlinux.ru> 20110506-alt1
- Added antiword support to dired file types associations

* Thu May 05 2011 Michael Pozhidaev <msp@altlinux.ru> 20110505-alt1
- Added some basic musitorius manipulations

* Wed Apr 27 2011 Michael Pozhidaev <msp@altlinux.ru> 20110427-alt1
- Added heading date and time information onto top of homeros-menu

* Thu Apr 14 2011 Michael Pozhidaev <msp@altlinux.ru> 20110414-alt1
- Added show-pdf command to homeros-xutils

* Wed Apr 13 2011 Michael Pozhidaev <msp@altlinux.ru> 20110413-alt1
- Added show-photo script
- Added calendar.el to initial emacs configuration

* Tue Apr 12 2011 Michael Pozhidaev <msp@altlinux.ru> 20110412-alt1
- Improved homeros-emacs-menu

* Thu Apr 07 2011 Michael Pozhidaev <msp@altlinux.ru> 20110407-alt1
- Added homeros-xutils subpackage
- Various improvements of emacs predefined settings

* Wed Apr 06 2011 Michael Pozhidaev <msp@altlinux.ru> 20110406-alt1
- Added homeros-prepare-user-home command
- useradd-homeros creates directories for user private data since ~/Documents was removed from etcskel

* Sun Jan 30 2011 Michael Pozhidaev <msp@altlinux.ru> 20110130-alt1
- Removed GNOME predifined settings from skel
- Minor fixes in emacs configuration

* Wed Jan 26 2011 Michael Pozhidaev <msp@altlinux.ru> 20110126-alt1
- Fixed typos

* Tue Jan 11 2011 Michael Pozhidaev <msp@altlinux.ru> 20110111-alt1
- Added homeros-emacs-menu service in /etc/rc.d/init.d

* Mon Jan 10 2011 Michael Pozhidaev <msp@altlinux.ru> 20110110-alt1
- Added homeros-emacs-menu subpackage
- Added homeros-friend-data subpackage

* Mon Dec 20 2010 Michael Pozhidaev <msp@altlinux.ru> 20101220-alt1
- Added cl requirement to emacspeak autostart script

* Tue Nov 16 2010 Michael Pozhidaev <msp@altlinux.ru> 20101116-alt2
- Fixed tools subpackage name
- Added homeros-media subpackage with startup soudn file

* Tue Nov 16 2010 Michael Pozhidaev <msp@altlinux.ru> 20101116-alt1
- Added homeros-tools subpackage

* Fri Jan 01 2010 Michael Pozhidaev <msp@altlinux.ru> 20100101-alt1
- Initial package

