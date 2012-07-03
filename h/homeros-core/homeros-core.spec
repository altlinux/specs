%define skeldir %_sysconfdir/skel.homeros.ru_RU.UTF-8

Name: homeros-core
Version: 20120203
Release: alt1
Summary: The set of scripts and predefined settings for ALT Linux Homeros distribution
Group: System/Configuration/Other
URL: http://homeros.altlinux.org
License: GPL
BuildArch: noarch
Packager: Michael Pozhidaev <msp@altlinux.ru>
BuildRequires: etcskel emacs23 emacs-devel

Source: %name-%version.tar.gz

%package -n etcskel-homeros
Summary: /etc/skel directory for ALT Linux Homeros distribution
Group: System/Configuration/Other
License: GPL
%add_python_req_skip orca re time

%package -n homeros-tools
Summary: The set of script for ALT Linux Homeros distribution
Group: System/Configuration/Other
License: GPL

%package -n homeros-xutils
Summary: The set of scripts to run some applications in X session
Group: System/Configuration/Other
License: GPL
Requires: mplayer xinit gqview xmodmap xpdf-reader

%package -n homeros-mobile
Summary: The set of scripts for power control on mobile devices
Group: System/Configuration/Other
License: GPL

%package -n homeros-media
Summary: Media files for ALT Linux Homeros distributions
Group: System/Configuration/Other
License: GPL

%package -n homeros-emacs-menu
Summary: The menu for quick application launch in Homeros Friend distributions
Group: Editors
License: GPL
Requires: emacs-base

%package -n homeros-live-data
Summary: Various data files for ALT Linux Homeros LiveCD system
Group: System/Configuration/Other
License: GPL

%description
The set of scripts and predefined settings for ALT Linux Homeros distribution

%description -n etcskel-homeros
This package contains initial content of newly created 
home directories. This content will be copied into 
users private files on new account creation.

%description -n homeros-tools
This package contains set of scripts to simplify 
using ALT Linux distribution.

%description -n homeros-xutils
The set of scripts to run some applications in X session

%description -n homeros-mobile
The set of scripts for power control on mobile devices

%description -n homeros-media
This package contains media files for ALT Linux Homeros distribution.

%description -n homeros-emacs-menu
This package contains scripts to add starting menu to emacs for Homeros users.

%description -n homeros-live-data
The package with various data files for ALT Linux Homeros LiveCD system

%prep
%setup -q
%build
%byte_compile_file emacs-menu/homeros-menu.el

%install
./homeros-core-install %buildroot

%files -n etcskel-homeros
%config %skeldir

%files -n homeros-tools
#%_bindir/enable-orca-autostart
%_bindir/useradd-homeros

%files -n homeros-xutils
%_bindir/run-gqview-without-escape
%_bindir/show-movie
%_bindir/show-photo
%_bindir/show-pdf

%files -n homeros-mobile
%_bindir/battery-status

%files -n homeros-media
%_datadir/sounds/homeros

%files -n homeros-emacs-menu
%_datadir/homeros-emacs-menu
%_emacslispdir/*
%_sysconfdir/rc.d/init.d/homeros-emacs-menu

%files -n homeros-live-data
%_datadir/homeros-live

%changelog
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

