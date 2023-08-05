%define _iconsscaldir  %_iconsdir/hicolor/scalable/apps

Name: byobu
Version: 5.133
Release: alt1

Summary: Light-weight, configurable window manager built upon GNU screen

License: GPLv3
Group: Terminals
Url: https://www.byobu.org/

BuildArch: noarch

Obsoletes: screen-profiles

# source code git mirror: https://github.com/dustinkirkland/byobu
# Source-url: https://launchpad.net/byobu/trunk/%version/+download/byobu_%version.orig.tar.gz
Source: %name-%version.tar

Patch1: byobu-python.patch

%filter_from_requires /\/etc\/eucalyptus\/eucalyptus.conf/d
# optional
%filter_from_requires /\/sbin\/iwconfig/d
%filter_from_requires /\/bin\/tmux/d
%filter_from_requires /\/bin\/screen/d

BuildRequires: rpm-build-python3
BuildRequires: desktop-file-utils

%description
Byobu is a GPLv3 open source text-based window manager and terminal multiplexer.
It was originally designed to provide elegant enhancements to the otherwise functional,
plain, practical GNU Screen, for the Ubuntu server distribution.
Byobu now includes an enhanced profiles, convenient keybindings,
configuration utilities, and toggle-able system status notifications
for both the GNU Screen window manager and the more modern Tmux terminal multiplexer,
and works on most Linux, BSD, and Mac distributions.

%prep
%setup
%patch1 -p2

rm -fv usr/bin/*.swp

%build
%configure
%make_build

%install
%makeinstall_std
rm -rv %buildroot%_sysconfdir/profile.d
rm -v %buildroot/%_libexecdir/%name/apport
%__subst 's#status\[\"apport\"\]=0##g' %buildroot%_bindir/byobu-config

for po in po/*.po
do
    lang=${po#po/}
    lang=${lang%.po}
    mkdir -p %buildroot%_datadir/locale/${lang}/LC_MESSAGES/
    msgfmt ${po} -o %buildroot%_datadir/locale/${lang}/LC_MESSAGES/%name.mo
done

#use the old xterm .desktop style for while
cp -a usr/share/%{name}/desktop/%{name}.desktop.old usr/share/%{name}/desktop/%{name}.desktop
desktop-file-install usr/share/%{name}/desktop/%{name}.desktop --dir %{buildroot}%{_datadir}/applications

# remove vigpg
rm %buildroot%_bindir/vigpg
rm %buildroot%_man1dir/vigpg.1

# add icon into %_iconsdir/hicolor/scalable/apps/ from %_datadir/byobu/pixmaps/byobu.svg
mkdir -p %buildroot%_iconsscaldir
cp -p usr/share/byobu/pixmaps/byobu.svg %buildroot%_iconsscaldir

%find_lang %name

%files -f %name.lang
%_docdir/%name/
%config %_sysconfdir/%name
%_bindir/*
%_datadir/%name
%_man1dir/*
%_libexecdir/%name/
%_desktopdir/%name.desktop
%_datadir/dbus-1/services/us.kirkland.terminals.byobu.service
%_iconsscaldir/*.svg

%changelog
* Sat Aug 05 2023 Vitaly Lipatov <lav@altlinux.ru> 5.133-alt1
- new version (5.133) with rpmgs script
- switch to build from tarball, sync with Fedora

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
