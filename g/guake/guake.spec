%define python_sitearch %(python -c "from distutils.sysconfig import get_python_lib; print get_python_lib(1)")

Name: guake
Summary: guake - a drop-down terminal
Summary(ru.UTF-8):guake — выпадающий эмулятор терминала
Version: 0.4.4
Release: alt1
License: GPL v2+
Group: Terminals
URL: http://guake.org/
Source: http://guake.org/files/%{name}-%{version}.tar.gz

Patch1: guake-fc18-focus_gnome_shell.patch
Patch2: guake-fc18-notification.patch
Patch3: guake-fc18-port_number_regex.patch
Patch4: guake-fc18-SIGTERM_to_fail.patch


BuildRequires(pre): etersoft-build-utils libGConf-devel rpm-build-gnome python-devel rpm-build-python
BuildRequires:  glibc-devel-static intltool libgtk+2-devel python-devel python-module-pygtk-devel python-module-vte python-modules-encodings GConf
BuildRequires: desktop-file-utils

Requires: GConf
Requires: dbus
Requires: python-module-pygtk-libglade notification-daemon

%description
Guake is a drop-down terminal for Gnome Desktop Environment, so you
just need to press a key to invoke him, and press again to hide.

%prep
%setup -q

%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1

%build
libtoolize
aclocal -I m4
autoconf
autoheader
automake
%configure  --disable-static --disable-schemas-install
sed -i -e 's|pythondir = ${prefix}/lib/|pythondir = ${prefix}/%_lib/|' src/Makefile
%make_build CXXFLAGS="%{optflags}" CFLAGS="%{optflags}"

%install
export GCONF_DISABLE_MAKEFILE_SCHEMA_INSTALL=1
%makeinstall


%find_lang %name
desktop-file-install --dir %buildroot%_desktopdir \
	--remove-category=Utility \
	%buildroot%_desktopdir/%name.desktop

desktop-file-install --dir %buildroot%_desktopdir \
	--remove-category=X-GNOME-PersonalSettings \
	--add-category=Accessibility \
	%buildroot%_desktopdir/%name-prefs.desktop

rm -f %buildroot%python_sitearch/%name/globalhotkeys.la

mkdir -p %buildroot%gnome_autostartdir
ln -s %_desktopdir/%name.desktop %buildroot%gnome_autostartdir/guake.desktop

%post
%gconf2_install guake

%preun
%gconf2_uninstall guake


%files -f %name.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog COPYING README TODO
%_sysconfdir/gconf/schemas/%name.schemas
%attr(755,root,root) %_bindir/*
%python_sitearch/%name
%_desktopdir/*.desktop
%_datadir/dbus-1/services/org.guake.Guake.service
%_datadir/%name
%_pixmapsdir/guake
%_mandir/man1/guake.1*
%_datadir/icons/hicolor/*/apps/%{name}*.png
%gnome_autostartdir/guake.desktop

%changelog
* Thu Feb 07 2013 Dmitriy Kulik <lnkvisitor@altlinux.org> 0.4.4-alt1
- New version
- Update from fc18

* Wed Jul 11 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.4.2-alt2.qa2
- Fixed build

* Sat Oct 22 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.4.2-alt2.qa1.1
- Rebuild with Python-2.7

* Wed May 18 2011 Repocop Q. A. Robot <repocop@altlinux.org> 0.4.2-alt2.qa1
- NMU (by repocop). See http://www.altlinux.org/Tools/Repocop
- applied repocop fixes:
  * freedesktop-desktop-file-proposed-patch for guake
  * postclean-03-private-rpm-macros for ([not specified])
  * postclean-05-filetriggers for ([not specified])

* Tue Sep 07 2010 Dmitriy Kulik <lnkvisitor@altlinux.org> 0.4.2-alt2
- Added patch: Ticket #248. The focus would change to the terminal after click on the new tab button.

* Fri Aug 13 2010 Dmitriy Kulik <lnkvisitor@altlinux.org> 0.4.2-alt1
- 0.4.2.20100801
- Added autostart guake

* Wed May 05 2010 Dmitriy Kulik <lnkvisitor@altlinux.org> 0.4.1-alt1
- new version 0.4.1

* Tue Jan 26 2010 Dmitriy Kulik <lnkvisitor at altlinux.org> 0.4.0-alt0.1
- initial build

