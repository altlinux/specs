# -*- rpm-spec -*-

Name: jpilot
Summary: Palm pilot desktop for Linux
Summary(ru_RU.KOI8-R): Palm pilot desktop для Linux
Version: 0.99.9
Release: alt7.qa4

Packager: Pavlov Konstantin <thresh@altlinux.ru>

License: GPL
Group: Communications
Url: http://www.jpilot.org
Source: %name-%{version}.tar
Source1: jpilot-icons.tar
Source2: jpilot-ru.po
Source3: mkinstalldirs
Requires: pilot-link >= 0.12.1-alt1

Patch0: jpilot-0.99.8-alt-fixes.patch
Patch1: jpilot-0.99.8-1-alt-fixes.patch
#Patch2: %name-0.99.8-alt-gettext.patch
Patch2: jpilot-0.99.9pre2-alt-gettext.patch
Patch3: jpilot-0.99.8-sync.patch
Patch4: jpilot-0.99.9-keyring.patch
#Patch5: jpilot-0.99.9-keyring-br.patch
Patch6: jpilot-0.99.9-configure-lib64.patch

BuildRequires: libpilot-link-devel >= 0.12.1-alt1

BuildRequires: fontconfig freetype2 gcc-c++ glib2-devel intltool libatk-devel
BuildRequires: libcairo-devel libg2c-devel libgtk+2-devel libpango-devel
BuildRequires: libssl-devel libstdc++-devel perl-XML-Parser pkgconfig

%description
J-Pilot is a desktop organizer application for the palm pilot that runs
under Linux and UNIX.  It is similar in functionality to the one that 3com
distributes for a well known rampant legacy operating system.

%description -l ru_RU.KOI8-R
J-Pilot - настольное приложение для Palm pilot, которое работает под Linux и UNIX.
Его функциональность похожа на оригинальную версию, которую 3com распространяет для
хорошо известной операционной системы.

%package plugins-devel
Summary: Library and header file needed for jpilot plugin development
Group: Communications
Requires: %name = %version-%release

%description plugins-devel
J-Pilot is a desktop organizer application for the palm pilot that runs
under Linux and UNIX.  It is similar in functionality to the one that 3com
distributes for a well known rampant legacy operating system.

The library and header file required for plugin development

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1
#%patch3 -p0
%patch4 -p0
#%patch5 -p0
%patch6 -p1

cp %SOURCE2 po/ru.po
cp %SOURCE3 .
chmod +x mkinstalldirs

%build
NOCONFIGURE=1 ./autogen.sh
export ABILIB=%_lib
%configure \
	--enable-stock-buttons \
	--libdir=%_libdir/jpilot

%make_build

%install
install -d %buildroot/{%_mandir/man1,%_bindir}
%makeinstall

install -d html
install docs/*.html docs/*.png html

install -d %buildroot%_datadir/%name
install jpilotrc.* %buildroot%_datadir/%name
install empty/*.pdb %buildroot%_datadir/%name

install -m 644 {libplugin,prefs}.h %buildroot%_libdir/jpilot/plugins/

tar xvf %SOURCE1
install -D -m644 jpilot.xpm %buildroot/%_niconsdir/jpilot.xpm
install -D -m644 mini/jpilot.xpm %buildroot/%_miconsdir/jpilot.xpm
install -D -m644 large/jpilot.xpm %buildroot/%_liconsdir/jpilot.xpm

if grep '^Categories=Application;Office;$' %buildroot%_desktopdir/jpilot.desktop; then
    cat > %buildroot%_desktopdir/jpilot.desktop <<EOF
[Desktop Entry]
Name=J-Pilot
Comment=Desktop organizer application for the Palm Pilot
Exec=jpilot
Icon=jpilot
Terminal=false
Type=Application
Categories=Office;PDA;
EOF
    else
	echo "desktop above is deprecated. PLEASE, merge Categories to the new upstream desktop file"
	exit 1
fi

# Fix jpilot doc bug
rm -rf %buildroot/usr/doc

rm -f %buildroot%_libdir/%name/plugins/*.la

%find_lang %name

%files -f %name.lang
#%doc AUTHORS BUGS ChangeLog INSTALL README TODO html
%_bindir/*
%_datadir/jpilot/jpilotrc.*
%_datadir/jpilot/*.pdb
%_miconsdir/*xpm
%_niconsdir/*xpm
%_liconsdir/*xpm
%_datadir/applications/*
%dir %_datadir/jpilot
%dir %_libdir/%name
%dir %_libdir/%name/plugins
%_libdir/%name/plugins/*.so*
%_mandir/man1/*
%_datadir/doc/%name-%version

%files plugins-devel
%dir %_libdir/%name
%dir %_libdir/%name/plugins
%_libdir/jpilot/plugins/libplugin.h
%_libdir/jpilot/plugins/prefs.h

%changelog
* Thu Mar 31 2011 Igor Vlasenko <viy@altlinux.ru> 0.99.9-alt7.qa4
- NMU: converted debian menu to freedesktop

* Tue Dec 07 2010 Igor Vlasenko <viy@altlinux.ru> 0.99.9-alt7.1.qa1.1
- rebuild with new openssl and/or boost by request of git.alt administrator

* Thu Nov 19 2009 Repocop Q. A. Robot <repocop@altlinux.org> 0.99.9-alt7.1.qa1
- NMU (by repocop): the following fixes applied:
  * post_ldconfig for jpilot
  * postun_ldconfig for jpilot
  * update_menus for jpilot
  * pixmap-in-deprecated-location for jpilot
  * postclean-05-filetriggers for spec file

* Sat Aug 09 2008 ALT QA Team Robot <qa-robot@altlinux.org> 0.99.9-alt7.1
- Automated rebuild due to libcrypto.so.6 -> libcrypto.so.7 soname change.

* Thu Mar 13 2008 Pavlov Konstantin <thresh@altlinux.ru> 0.99.9-alt7
- Fix #14189.

* Thu Sep 07 2006 Pavlov Konstantin <thresh@altlinux.ru> 0.99.9-alt6
- 0.99.9 release.
- Removed patch5.
- Stricted build requires for pilot-link >= 0.12.1-alt1.

* Mon Jul 10 2006 Pavlov Konstantin <thresh@altlinux.ru> 0.99.9-alt5.pre2
- Build with new pilot-link.
- Removed xorg-x11-devel from buildrequires.
- Added patch6 to build on x86_64.

* Fri Jun 16 2006 Pavlov Konstantin <thresh@altlinux.ru> 0.99.9-alt4.pre2
- Real fix for #9386, #9390.

* Tue Apr 18 2006 Pavlov Konstantin <thresh@altlinux.ru> 0.99.9-alt3.pre2
- Fixed #9386, #9390 (thx naf@ for patches).

* Tue Apr 04 2006 Pavlov Konstantin <thresh@altlinux.ru> 0.99.9-alt2.pre2
- Fixed #9238.

* Tue Feb 28 2006 Pavlov Konstantin <thresh@altlinux.ru> 0.99.9-alt1.pre2
- 0.99.9-pre2 release.
- removed patch3 (sync).
- modified gettext patch.
- removed --enable-gtk2 as it is default now.
- added packager line.

* Sat Nov 26 2005 Pavlov Konstantin <thresh@altlinux.ru> 0.99.8-alt1
- 0.99.8 release.
- updated patches.
- turning on GTK2.
- added .desktop file.
- updated buildreqs.
- fixed specfile to build&run on x86_64 platform.
- updated translation by abr@.

* Sun Dec 12 2004 Andrey Brindeew <abr@altlinux.org> 0.99.7-alt3
- update-gmo hack removed
- package now owns /usr/share/jpilot dir
- specfile fixes (thanks to Yuri N. Sedunov)
- intltool-related patch applied (thanks to Yuri N. Sedunov again)

* Mon May 10 2004 ALT QA Team Robot <qa-robot@altlinux.org> 0.99.7-alt2.1
- Rebuilt with openssl-0.9.7d.

* Fri Mar 19 2004 Andrey Brindeew <abr@altlinux.ru> 0.99.7-alt2
- Russian translation corrected

* Sat Mar 06 2004 Andrey Brindeew <abr@altlinux.ru> 0.99.7-alt1
- 0.99.7
- Russian translation updated

* Tue Sep 09 2003 Andrey Brindeew <abr@altlinux.ru> 0.99.6-alt3
- Specfile minor fix
- BuilRequires list updated

* Sat Sep 06 2003 Andrey Brindeew <abr@altlinux.ru> 0.99.6-alt2
- Russian translation updated

* Fri Jul 18 2003 Andrey Brindeew <abr@altlinux.ru> 0.99.6-alt1
- 0.99.6

* Mon May 12 2003 Andrey Brindeew <abr@altlinux.ru> 0.99.5-alt1
- 0.99.5
- Patches were reorganized
- Moved from "Applications/Communictions" to "Office/PDA" in menu
- Russian translation updated
- Fixed a bug with illegal cats names recoding

* Wed Oct 16 2002 Alexander Bokovoy <ab@altlinux.ru> 0.99.3-alt2
- Russian translation updated
- Spec file cleaned and updated to 0.99.3

* Tue Oct 15 2002 Alexander Bokovoy <ab@altlinux.ru> 0.99.3-alt1
- 0.99.3
- Rebuild against pilot-link 0.11.5

* Sat Mar 02 2002 Alexander Bokovoy <ab@altlinux.ru> 0.99.2-alt2
- Minor fix in Russian translation

* Wed Feb 06 2002 Alexander Bokovoy <ab@altlinux.ru> 0.99.2-alt1
- 0.99.2
- Russian translation updated
- Charset clarification added (English -> English/No Conversion)

* Fri Nov 16 2001 Alexander Bokovoy <ab@altlinux.ru> 0.99.1-alt2
- Added Russian translation

* Tue Oct 09 2001 Konstantin Volckov <goldhead@altlinux.ru> 0.99.1-alt1
- First build for ALT Linux

* Sat Sep 29 2001 Chmouel Boudjnah <chmouel@mandrakesoft.com> 0.99.1-0.4mdk
- rpmlint fixes.

* Sat Jun 23 2001 Stefan van der Eijk <stefan@eijk.nu> 0.99.1-0.3mdk
- BuildRequires:	gtk+-devel

* Wed Jun 20 2001 Chmouel Boudjnah <chmouel@mandrakesoft.com> 0.99.1-0.2mdk
- Fix plugins loading.

* Wed Jun 20 2001 Chmouel Boudjnah <chmouel@mandrakesoft.com> 0.99.1-0.1mdk
- Sanitize spec file.
- 0.99.1 pre.

* Sun Jun 10 2001 Stefan van der Eijk <stefan@eijk.nu> 0.99-3mdk
- BuildRequires: pilot-link-devel

* Sun Apr 22 2001 Stew Benedict <sbenedict@mandrakesoft.com> 0.99-2mdk
- need prefs.h in plugins for jpilot-syncmal

* Thu Feb 08 2001 Geoffrey lee <snailtalk@mandrakesoft.com> 0.99-1mdk
- new and shiny source.
- change the URL.
- change the URL on the source tag.
- Don't apply patch1 anymore. (security mode 0700 fix.)
- remove libplugin.a (can't find it anymore.)
- when using tar use -j to pass through the bzip2 filter, not -I.

* Fri Dec 15 2000 Chmouel Boudjnah <chmouel@mandrakesoft.com> 0.98.1-7mdk
- Create directory as 0700.

* Fri Nov 03 2000 Christopher Molnar <molnarc@mandrakesoft.com> 0.98.1-6mdk
- Rebuilt for gcc 2.96

* Wed Sep 13 2000 Chmouel Boudjnah <chmouel@mandrakesoft.com> 0.98.1-4mdk
- Add info about usb.

* Fri Aug 11 2000 Christopher Molnar <molnarc@mandrakesoft.com> 0.98.1-3mdk
- fixed stupid error in changelog

* Fri Aug 11 2000 Vincent Danen <molnarc@mandrakesoft.com> 0.98.1-2mdk
- Added plugin lib for future development
- Added plugindevel package

* Wed Jul 26 2000 Vincent Danen <vdanen@mandrakesoft.com> 0.98.1-1mdk
- initial mandrake build
- remove expense plugin
