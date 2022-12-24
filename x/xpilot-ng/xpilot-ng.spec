Group: Games/Arcade
# BEGIN SourceDeps(oneline):
BuildRequires: /usr/bin/desktop-file-install gcc-c++ imake libSDL-devel libX11-devel xorg-cf-files xorg-proto-devel
# END SourceDeps(oneline)
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
%global logwatch_root %{_datadir}/logwatch
%global logwatch_conf %{logwatch_root}/dist.conf
%global logwatch_scripts %{logwatch_root}/scripts

Name:           xpilot-ng
Version:        4.7.3
Release:        alt4_27
Summary:        Space arcade game for multiple players

License:        GPLv2+
URL:            http://xpilot.sourceforge.net
Source0:        http://downloads.sourceforge.net/sourceforge/xpilot/xpilot-ng-%{version}.tar.gz
Source1:        xpilot-ng.png
Source2:        xpilot-ng-sdl.desktop
Source3:        xpilot-ng-sdl.appdata.xml
Source4:        xpilot-ng-server.service
Source5:        xpilot-ng.sysconfig
Source6:        xpilot-ng.logrotate
Source10:       logwatch.logconf.xpilot
Source11:       logwatch.script.xpilot
Source12:       logwatch.serviceconf.xpilot
Source13:       logwatch.shared.applyxpilotdate
Source14:       xpilot-ng-server.metainfo.xml
Patch0:         xpilot-ng-4.7.2-scoreassert.patch
Patch1:         xpilot-ng-4.7.2-rhbz830640.patch
Patch2:         xpilot-ng-4.7.3-fix-alut-detect.patch
Patch3:         xpilot-ng-c99.patch
Patch4:         xpilot-ng-SDL_window.patch

BuildRequires:  gcc
BuildRequires:  desktop-file-utils libappstream-glib libappstream-glib-gir
BuildRequires:  libexpat-devel libSDL_ttf-devel libSDL_image-devel zlib-devel
BuildRequires:  libXt-devel libGLU-devel
BuildRequires:  libopenal-devel libalut-devel automake
Requires:       %{name}-data = %{version}-%{release} icon-theme-hicolor
Provides:       %{name}-engine = %{version}-%{release}
Source44: import.info

%description
A highly addictive, infinitely configurable multi-player space
arcade game.  You pilot a spaceship around space, dodging
obstacles, shooting players and bots, collecting power-ups, and
causing general mayhem.


%package x11
Group: Games/Arcade
Summary:        Xpilot-ng X11 version
Requires:       %{name}-data = %{version}-%{release}
Provides:       %{name}-engine = %{version}-%{release}

%description x11
Version of %{name} which uses libX11 rather then SDL.


%package data
Group: Games/Arcade
Summary:        Data files for %{name}
BuildArch:      noarch
Requires:       %{name}-engine = %{version}-%{release} fonts-ttf-dejavu

%description data
Data files for %{name}.


%package server
Group: Games/Arcade
Summary:        Server for hosting xpilot games
Requires:       %{name}-data = %{version}-%{release}
Requires:       logrotate
Requires(pre):  shadow-change shadow-check shadow-convert shadow-edit shadow-groups shadow-log shadow-submap shadow-utils
BuildRequires:  libsystemd-devel libudev-devel systemd systemd-analyze systemd-homed systemd-networkd systemd-portable systemd-sysvinit
Provides:       %{name}-engine = %{version}-%{release}
# Make sure the old no longer supported selinux policy from 4.7.2 gets removed
Obsoletes:      %{name}-selinux < %{version}-%{release}
Provides:       %{name}-selinux = %{version}-%{release}

%description server
The xpilot server.  This allows you to host xpilot games on your
computer and develop new xpilot maps.  This is required if you
are playing alone, but not required if you are joining one of the
public xpilot games hosted on the internet.


%package logwatch
Group: Games/Arcade
Summary:        Logwatch scripts for the xpilot game server
Requires:       %{name}-server = %{version}-%{release} logwatch

%description logwatch
logwatch scripts for the Xpilot game server


%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1

# regenerate autofoo files for patch2
autoreconf -ivf
# fixup textfile encodings
pushd doc/man
iconv --from=ISO-8859-1 --to=UTF-8 xpilot-ng-server.man > xpilot-ng-server.man.new
touch -r xpilot-ng-server.man xpilot-ng-server.man.new
mv xpilot-ng-server.man.new xpilot-ng-server.man

iconv --from=ISO-8859-1 --to=UTF-8 xpilot-ng-x11.man > xpilot-ng-x11.man.new
touch -r xpilot-ng-x11.man xpilot-ng-x11.man.new
mv xpilot-ng-x11.man.new xpilot-ng-x11.man
popd

iconv --from=ISO-8859-1 --to=UTF-8 AUTHORS > AUTHORS.new
touch -r AUTHORS AUTHORS.new
mv AUTHORS.new AUTHORS


%build
%configure --enable-sound
iconv --from=ISO-8859-1 --to=UTF-8 README -o README
touch -r README.in README
%make_build


%install
%makeinstall_std INSTALL="install -p"

# Drop old Python 2 only map conversion script
rm $RPM_BUILD_ROOT/%{_datadir}/%{name}/mapconvert.py

desktop-file-install --dir ${RPM_BUILD_ROOT}%{_datadir}/applications %{SOURCE2}
mkdir -p $RPM_BUILD_ROOT/%{_datadir}/icons/hicolor/48x48/apps/
install -p -m 644 %{SOURCE1} $RPM_BUILD_ROOT/%{_datadir}/icons/hicolor/48x48/apps/
mkdir -p $RPM_BUILD_ROOT%{_datadir}/appdata
install -p -m 644 %{SOURCE3} %{SOURCE14} $RPM_BUILD_ROOT%{_datadir}/appdata
appstream-util validate-relax --nonet $RPM_BUILD_ROOT%{_datadir}/appdata/*.xml

install -p -D -m 644 %{SOURCE4} $RPM_BUILD_ROOT/lib/systemd/system/%{name}-server.service

# Copy certain configuration files to /etc so that they can be properly managed
# as config files.
install -p -D -m 644 %{SOURCE5} $RPM_BUILD_ROOT/%{_sysconfdir}/%{name}/%{name}-server-cmdline-opts
install -p -D -m 644 lib/defaults.txt $RPM_BUILD_ROOT/%{_sysconfdir}/%{name}/defaults.txt
install -p -D -m 600 lib/password.txt $RPM_BUILD_ROOT/%{_sysconfdir}/%{name}/password.txt

install -p -D -m 644 %{SOURCE6} \
    $RPM_BUILD_ROOT/%{_sysconfdir}/logrotate.d/%{name}-server

# Replace bundled fonts with system fonts

rm $RPM_BUILD_ROOT%{_datadir}/%{name}/fonts/FreeSansBoldOblique.ttf
ln -s %{_datadir}/fonts/ttf/dejavu/DejaVuSans-BoldOblique.ttf $RPM_BUILD_ROOT%{_datadir}/%{name}/fonts/FreeSansBoldOblique.ttf
rm $RPM_BUILD_ROOT%{_datadir}/%{name}/fonts/VeraMoBd.ttf
ln -s %{_datadir}/fonts/ttf/dejavu/DejaVuSansMono-Bold.ttf $RPM_BUILD_ROOT%{_datadir}/%{name}/fonts/VeraMoBd.ttf


# Install logwatch files
install -pD -m 0644 %{SOURCE10} $RPM_BUILD_ROOT%{logwatch_conf}/logfiles/%{name}.conf
install -pD -m 0644 %{SOURCE11} $RPM_BUILD_ROOT%{logwatch_scripts}/services/%{name}
install -pD -m 0644 %{SOURCE12} $RPM_BUILD_ROOT%{logwatch_conf}/services/%{name}.conf
install -pD -m 0644 %{SOURCE13} $RPM_BUILD_ROOT%{logwatch_scripts}/shared/applyxpilotdate

%pre server
getent group xpilot >/dev/null || groupadd -r xpilot
getent passwd xpilot >/dev/null || \
useradd -r -g xpilot -d %{_datadir}/%{name} -s /sbin/nologin \
    -c "xpilot game server" xpilot
exit 0

%post server
%post_service xpilot-ng-server

%preun server
%preun_service xpilot-ng-server

%files
%{_bindir}/xpilot-ng-replay
%{_bindir}/xpilot-ng-sdl
%{_datadir}/appdata/xpilot-ng-sdl.appdata.xml
%{_datadir}/applications/xpilot-ng-sdl.desktop
%{_datadir}/icons/hicolor/48x48/apps/xpilot-ng.png
%{_mandir}/man6/xpilot-ng-replay.6*
%{_mandir}/man6/xpilot-ng-sdl.6*

%files data
%doc AUTHORS BUGS ChangeLog FEATURES README TODO
%doc --no-dereference COPYING
%dir %{_datadir}/%{name}
%{_datadir}/%{name}/textures
%{_datadir}/%{name}/fonts
%{_datadir}/%{name}/sound

%files x11
%{_bindir}/xpilot-ng-x11
%{_mandir}/man6/xpilot-ng-x11.6*

%files server
%{_bindir}/xpilot-ng-xp-mapedit
%{_bindir}/xpilot-ng-server
/lib/systemd/system/xpilot-ng-server.service
%config(noreplace) %{_sysconfdir}/logrotate.d/%{name}-server
%{_datadir}/%{name}
%exclude %{_datadir}/%{name}/textures
%exclude %{_datadir}/%{name}/fonts
%exclude %{_datadir}/%{name}/sound
%{_datadir}/appdata/xpilot-ng-server.metainfo.xml
%dir %{_sysconfdir}/%{name}
%config(noreplace) %attr(0600,xpilot,root) %{_sysconfdir}/%{name}/password.txt
%config(noreplace) %{_sysconfdir}/%{name}/defaults.txt
%config(noreplace) %{_sysconfdir}/%{name}/xpilot-ng-server-cmdline-opts
%{_mandir}/man6/xpilot-ng-server.6*
%{_mandir}/man6/xpilot-ng-xp-mapedit.6*

%files logwatch
%{logwatch_conf}/logfiles/%{name}.conf
%{logwatch_conf}/services/%{name}.conf
%{logwatch_scripts}/services/%{name}
%{logwatch_scripts}/shared/applyxpilotdate


%changelog
* Sat Dec 24 2022 Igor Vlasenko <viy@altlinux.org> 4.7.3-alt4_27
- update to new release by fcimport

* Wed May 19 2021 Igor Vlasenko <viy@altlinux.org> 4.7.3-alt4_23
- fixed build - replaced by import

* Wed Feb 20 2019 Gleb F-Malinovskiy <glebfm@altlinux.org> 4.7.3-alt4
- %%build: run autoreconf to fix build on modern architectures.

* Tue Jun 26 2018 Grigory Ustinov <grenka@altlinux.org> 4.7.3-alt3
- Remove bundled fonts (Closes: 25329).

* Wed Oct 26 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 4.7.3-alt2.1
- Rebuild with Python-2.7

* Sat Mar 26 2011 Igor Vlasenko <viy@altlinux.ru> 4.7.3-alt2
- converted debian menu to freedesktop

* Mon Jan 24 2011 Ilya Mashkin <oddity@altlinux.ru> 4.7.3-alt1
- 4.7.3
- update xpilot-ng-4.7.3-alt-getline.patch

* Fri Jan 15 2010 Igor Vlasenko <viy@altlinux.ru> 4.7.2-alt1
- new version (renamed to xpilot-ng) 

* Tue Oct 06 2008 Ilya Mashkin <oddity@altlinux.ru> 4.5.4-alt3.1
- rebuild
- update url

* Fri Feb 24 2006 Michael Shigorin <mike@altlinux.org> 4.5.4-alt3
- picked up an orphan (road companion ;-)
- spec cleanup/update for xorg7
- updated buildrequires

* Thu Oct 31 2002 Stanislav Ievlev <inger@altlinux.ru> 4.5.4-alt2
- rebuild with gcc3
- fixed menu file (xpm -> png icon)

* Wed Aug 14 2002 Stanislav Ievlev <inger@altlinux.ru> 4.5.4-alt1
- 4.5.4

* Wed Apr 03 2002 Stanislav Ievlev <inger@altlinux.ru> 4.5.0-alt1
- 4.5.0

* Mon Oct 15 2001 Stanislav Ievlev <inger@altlinux.ru> 4.4.2-alt1
- 4.4.2

* Wed Jan 17 2001 AEN <aen@logic.ru>
- RE adaptation

* Tue Nov 28 2000 Geoffrey Lee <snailtalk@mandrakesoft.com> 4.2.0-8mdk
- use optflags.

* Fri Sep 15 2000 David BAUDENS <baudens@mandrakesoft.com> 4.2.0-7mdk
- Fix Title in Menu entry
- Complete macros

* Wed Aug 30 2000 Geoffrey Lee <snailtalk@mandrakesoft.com> 4.2.0-6mdk
- rebuild to use the new macros.

* Tue Aug 08 2000 Frederic Lepied <flepied@mandrakesoft.com> 4.2.0-5mdk
- automatically added BuildRequires

* Wed May 03 2000 dam's <damien@mandrakesoft.com> 4.2.0-4mdk
- Corrected menu entry.

* Tue Apr 18 2000 dam's <damien@mandrakesoft.com> 4.2.0-3mdk
- Convert gif icon to xpm.

* Mon Apr 17 2000 dam's <damien@mandrakesoft.com> 4.2.0-2mdk
- Added menu entry.

* Wed Mar 22 2000 dam's <damien@mandrakesoft.com> 4.2.0-1mdk
- updade to 4.2.0

* Fri Nov 5 1999 dam's <damien@mandrakesoft.com>
- Mandrake adaptation

* Fri Jul 30 1999 Bill Nottingham <notting@redhat.com>
- update to 4.1.0

* Sun Mar 21 1999 Cristian Gafton <gafton@redhat.com>
- auto rebuild in the new build environment (release 6)

* Thu Dec 17 1998 Michael Maher <mike@redhat.com>
- built package for 6.0

* Thu Aug 13 1998 Jeff Johnson <jbj@redhat.com>
- add sparc
- build root

* Fri May 08 1998 Prospector System <bugs@redhat.com>
- translations modified for de, fr, tr

* Mon Nov  3 1997 Otto Hammersmith <otto@redhat.com>
- made exlusivearch to i386

* Thu Oct 23 1997 Marc Ewing <marc@redhat.com>
- new version
- wmconfig

* Thu Jul 31 1997 Erik Troan <ewt@redhat.com>
- built against glibc
