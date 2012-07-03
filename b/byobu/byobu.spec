Name: byobu
Version: 2.38
Release: alt1.1.1

Summary: %name a set of useful profiles and a profile-switcher for GNU screen
License: GPLv3
Group: Terminals
Url: http://launchpad.net/byobu
Packager: Slava Dubrovskiy <dubrsl@altlinux.ru>
BuildArch: noarch

Requires: python-module-newt >= 0.52
Obsoletes: screen-profiles

Source: %name-%version.tar.gz
Patch: %name-%version-alt-changes.patch

%description
byobu includes a set of profiles and configuration utilities for the GNU screen window manager.
These profiles are quite useful on server machines which are not running a graphical desktop.
The 'screen' command provides a number of advanced features are not necessarily exposed in the
default profile. These profiles provide features such as status bars, clocks, notifiers
(reboot-required, updates-available), etc. The profile-switcher allows users to quickly
switch their .screenrc to any of the available profiles.

%package network
License: GPLv3
Group: Terminals
Summary: It is a part of the program byobu for show network status
Requires: %name = %version-%release
%description network
It is a part of the program byobu for show network status

%package wifi
License: GPLv3
Group: Terminals
Summary: It is a part of the program byobu for show wifi status
Requires: %name = %version-%release
%description wifi
It is a part of the program byobu for show wifi status

%package logo
License: GPLv3
Group: Terminals
Summary: It is a part of the program byobu for show logo and release
Requires: %name = %version-%release
%description logo
It is a part of the program byobu for show logo and release

%prep
%setup -q -n %name-%version
%patch -p1

#Update path to doc
%__subst "s|@version@|-%version|g" byobu-config

%build
rm -f po/%name.pot
grep -v "^#" po/POTFILES.Shell | while read po ; do \
	xgettext -o po/%name.pot -L Shell ${po} ; \
done
grep -v "^#" po/POTFILES.Python | while read po ; do \
	xgettext -o po/%name.pot -L Python ${po} ; \
done
for po in po/*.po ; do \
	msgmerge ${po} po/%name.pot -o ${po} ; \
done
for po in po/*.po ; do \
	lang=${po#po/}; lang=${lang%.po}; \
	mkdir -p po/locale/${lang}/LC_MESSAGES/; \
	msgfmt ${po} -o po/locale/${lang}/LC_MESSAGES/%name.mo ; \
done

# auto-generate the logo'd light/dark profiles
profiles_generator/generate

%install
%__mkdir_p %buildroot%_bindir
%__mkdir_p %buildroot%_datadir/%name
%__mkdir_p %buildroot%_datadir/locale
%__mkdir_p %buildroot%_datadir/%name/{profiles,keybindings,windows}
%__mkdir_p %buildroot%_man1dir
%__mkdir_p %buildroot%_sysconfdir/%name


cp -fR bin/* %buildroot%_datadir/%name
cp -fR po/locale/* %buildroot%_datadir/locale/
cp -fR profiles/* %buildroot%_datadir/%name/profiles/
cp -fR keybindings/* %buildroot%_datadir/%name/keybindings/
cp -fR windows/* %buildroot%_datadir/%name/windows
cp -f *.1 %buildroot%_man1dir/

%__install -m 755  byobu-select-profile %buildroot%_bindir
%__install -m 755  byobu %buildroot%_bindir
%__install -m 755  byobu-config %buildroot%_bindir
%__install -m 755  byobu-status %buildroot%_bindir
%__install -m 755  byobu-status-detail %buildroot%_bindir
%__install -m 755  byobu-launcher-install %buildroot%_datadir/%name
%__install -m 755  byobu-launcher-uninstall %buildroot%_datadir/%name
%__install -m 755  motd+shell %buildroot%_bindir
%__install -m 755  byobu-launcher %buildroot%_bindir
%__install -m 755  byobu-janitor %buildroot%_bindir
%__install -m 755  byobu-export %buildroot%_bindir
%__install -m 755  profiles/*_* %buildroot%_datadir/%name/profiles
%__install -m 755  statusrc %buildroot%_sysconfdir/%name

ln -sf f-keys %buildroot%_datadir/%name/keybindings/common

rm -f %buildroot%_datadir/%name/profiles/generate
rm -f %buildroot%_datadir/%name/profiles/profile.skel
# remove because not work
rm -f %buildroot%_datadir/%name/updates_available

%find_lang %name

%files -f %name.lang
%config %_sysconfdir/%name
%_bindir/*
%_datadir/%name
%_man1dir/*
%doc README COPYING debian/copyright debian/changelog
%doc doc/help.txt

%exclude %_datadir/%name/wifi_quality
%exclude %_datadir/%name/ec2_cost
%exclude %_datadir/%name/network
%exclude %_datadir/%name/ip_address
%exclude %_datadir/%name/logo
%exclude %_datadir/%name/release

%files wifi
%_datadir/%name/wifi_quality

%files network
%_datadir/%name/ec2_cost
%_datadir/%name/network
%_datadir/%name/ip_address

%files logo
%_datadir/%name/logo
%_datadir/%name/release

%changelog
* Sat Oct 22 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 2.38-alt1.1.1
- Rebuild with Python-2.7

* Tue Dec 01 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.38-alt1.1
- Rebuilt with python 2.6

* Mon Oct 19 2009 Slava Dubrovskiy <dubrsl@altlinux.org> 2.38-alt1
- New version
- Update translation ru

* Sun Sep 06 2009 Slava Dubrovskiy <dubrsl@altlinux.org> 2.30-alt1
- New version
- Split package to several subpackage

* Sat Jun 13 2009 Slava Dubrovskiy <dubrsl@altlinux.ru> 2.10-alt1
- New version
- Remove russian translation (in upstream)
- Update spec

* Sat May 23 2009 Slava Dubrovskiy <dubrsl@altlinux.ru> 2.4-alt1
- New version
- Add russian translation
- Update spec

* Thu May 14 2009 Slava Dubrovskiy <dubrsl@altlinux.org> 2.3-alt1
- New version
- Rename package to byobu

* Tue May 13 2009 Slava Dubrovskiy <dubrsl@altlinux.org> 1.54-alt1
- New version
- Relocate scripts from /var/lib/%name to %_datadir/%name/bin
- Update License

* Tue Apr 28 2009 Slava Dubrovskiy <dubrsl@altlinux.org> 1.51-alt1
- New version

* Tue Apr 28 2009 Slava Dubrovskiy <dubrsl@altlinux.ru> 1.44-alt1
- Build for ALT
