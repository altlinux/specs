Name:		qtsmbstatus
Version:	2.2.1
Release:	alt2
License:	GPLv2
Group:		Networking/Other
Source:	    %name-%version.tar.gz
Summary:	QtSmbstatus is a GUI for smbstatus
Url:		http://qtsmbstatus.free.fr/
Packager:	Motsyo Gennadi <drool@altlinux.ru>
Patch:      %name-2.2.1-alt-changes.patch
Patch1:     %name-2.1-alt-fix-gcc4.4.patch

BuildRequires: gcc-c++ /usr/bin/convert libpam-devel libqt4-devel

Requires: %name-common = %version-%release

%description
QtSmbstatus is a GUI (graphical user interface) for smbstatus.
It is meant to provide the possibility of administering remote
machines.

QtSmbstatus was designed as a client/server system secured with
SSL. A login and password is required to log on to server (PAM).
The server's application ought to be installed with samba-server.

%package -n %name-common
Summary: QtSmbstatus common files
Group: Networking/Other

%description -n %name-common
Common files for QtSmbstatus.

Include docs and translations.

%package -n %name-server
Summary: QtSmbstatus server
Group: System/Servers
Requires: samba

Requires: %name-common = %version-%release

%description -n %name-server
Server for QtSmbstatus

%package -n %name-light
Summary: QtSmbstatus for local use only
Group: System/Servers
Requires: samba

Requires: %name-common = %version-%release

%description -n %name-light
To use QtSmbstatus only locally (without qtsmbstatus client/server), just
install qtsmbstatus-light.

%prep
%setup -q
%patch -p1
%patch1 -p1

%build
export PATH=$PATH:%_qt4dir/bin
lrelease client/tr/*.ts
qmake "QMAKE_CFLAGS+=%optflags" "QMAKE_CXXFLAGS+=%optflags" %name.pro
%make_build

%install
%make INSTALL_ROOT=%buildroot install
%__mkdir -p %buildroot/{%_miconsdir,%_niconsdir,%_liconsdir}
convert -resize 16x16 client/icons/samba.png %buildroot%_miconsdir/%name.png
convert -resize 32x32 client/icons/samba.png %buildroot%_niconsdir/%name.png
convert -resize 48x48 client/icons/samba.png %buildroot%_liconsdir/%name.png

convert -resize 16x16 client/icons/qtsmbstatusl.png %buildroot%_miconsdir/qtsmbstatusl.png
convert -resize 32x32 client/icons/qtsmbstatusl.png %buildroot%_niconsdir/qtsmbstatusl.png

%find_lang %name

%post -n %name-server
%post_service %{name}d

%files
%_bindir/%name
%_man7dir/%name.*
%_desktopdir/%name.desktop
%_miconsdir/%name.png
%_niconsdir/%name.png
%_liconsdir/%name.png
%_pixmapsdir/%name.xpm

%files -f %name.lang -n %name-common
%_datadir/%name
%doc README* changelog INSTALL COPYING

%files -n %name-server
%_sbindir/%{name}d
%_initdir/%{name}d
%_man7dir/%{name}d.*
%attr(750,root,root) %_sysconfdir/%{name}d
%_sysconfdir/pam.d/%{name}d

%files -n %name-light
%_bindir/%{name}l
%_desktopdir/%{name}l.desktop
%_man7dir/%{name}l.*
%_miconsdir/%{name}l.png
%_niconsdir/%{name}l.png
%_pixmapsdir/%{name}l.xpm

%changelog
* Fri Sep 07 2012 Motsyo Gennadi <drool@altlinux.ru> 2.2.1-alt2
- fixed executable bits set

* Mon Aug 06 2012 Motsyo Gennadi <drool@altlinux.ru> 2.2.1-alt1
- 2.2.1

* Tue May 12 2009 Afanasov Dmitry <ender@altlinux.org> 2.1-alt2
- fix gcc4.4 build

* Sun Feb 08 2009 Afanasov Dmitry <ender@altlinux.org> 2.1-alt1
- 2.1

* Thu Nov 20 2008 Motsyo Gennadi <drool@altlinux.ru> 2.0.6-alt2
- delete post/postun scripts (new rpm)

* Mon Nov 10 2008 Motsyo Gennadi <drool@altlinux.ru> 2.0.6-alt1
- 2.0.6

* Thu Sep 04 2008 Motsyo Gennadi <drool@altlinux.ru> 2.0.5-alt1
- 2.0.5

* Sat May 10 2008 Motsyo Gennadi <drool@altlinux.ru> 2.0.4-alt1
- 2.0.4
- fix repocop warning (init-condrestart)
- remove preun script

* Sun Mar 02 2008 Motsyo Gennadi <drool@altlinux.ru> 2.0.3-alt2
- add condrestart to initscript
- remove ugly reload|force-reload from initscript

* Sat Feb 09 2008 Motsyo Gennadi <drool@altlinux.ru> 2.0.3-alt1
- 2.0.3

* Thu Jan 10 2008 Motsyo Gennadi <drool@altlinux.ru> 2.0.2-alt3
- disable starting %{name}d after installing
- close #13872:
	* change initscript for use /etc/init.d/functions	
- close #13875:
	* excluded COPYING from packaging
	* excluded docs from packaging %name

* Sun Dec 09 2007 Motsyo Gennadi <drool@altlinux.ru> 2.0.2-alt2
- add Url for Source

* Mon Nov 19 2007 Motsyo Gennadi <drool@altlinux.ru> 2.0.2-alt1
- 2.0.2 (initial build for Sisyphus)

* Sat Nov 10 2007 Motsyo Gennadi <drool@altlinux.ru> 2.0.2-alt0.svn51
- svn verwion

* Tue Nov 06 2007 Motsyo Gennadi <drool@altlinux.ru> 2.0.1-alt1
- Add rus/ukr translation

* Sun Nov 04 2007 Motsyo Gennadi <drool@altlinux.ru> 2.0.1-alt0
- 2.0.1

* Mon Oct 29 2007 Motsyo Gennadi <drool@altlinux.ru> 2.0-alt0
- initial build for ALT Linux
