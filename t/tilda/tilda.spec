Name: tilda
Version: 1.5.4
Release: alt1

Summary: A Linux terminal taking after the likeness of many terminals from fps games
License: GPLv2
Group: Terminals
Url: https://github.com/lanoxx/%name

Source: %url/archive/%name-%version.tar.gz

BuildRequires: flex libgtk+3-devel >= 3.10.0
BuildRequires: libconfuse-devel libvte3-devel >= 0.40 libpcre2-devel
BuildRequires: libappstream-glib-devel desktop-file-utils

Summary(ru_RU.UTF-8): Терминал Linux, имитирующий многие терминалы из FPS-игр

%description
Tilda is a Linux terminal taking after the likeness of many classic
terminals from first person shooter games, Quake, Doom and Half-Life
(to name a few), where the terminal has no border and is hidden from
the desktop until a key is pressed.

%prep
%setup -n %name-%name-%version

%build
%add_optflags %(getconf LFS_CFLAGS)
%autoreconf
%configure
%make_build

%install
%makeinstall_std
%find_lang %name

desktop-file-install --dir %buildroot%_desktopdir \
	--remove-category=Utility \
	--remove-category=Application \
	--add-category=System \
	--add-category=GTK \
	%buildroot%_desktopdir/tilda.desktop

%files -f %name.lang
%_bindir/%name
%_desktopdir/%name.desktop
%_pixmapsdir/%name.png
%_datadir/metainfo/%name.appdata.xml
%doc AUTHORS ChangeLog README.md TODO.md


%changelog
* Fri Dec 25 2020 Yuri N. Sedunov <aris@altlinux.org> 1.5.4-alt1
- 1.5.4

* Sun May 10 2020 Yuri N. Sedunov <aris@altlinux.org> 1.5.2-alt1
- 1.5.2

* Tue May 05 2020 Yuri N. Sedunov <aris@altlinux.org> 1.5.1-alt1
- 1.5.1

* Mon Feb 10 2020 Yuri N. Sedunov <aris@altlinux.org> 1.5.0-alt1
- 1.5.0

* Sat Feb 10 2018 Yuri N. Sedunov <aris@altlinux.org> 1.4.1-alt1
- 1.4.1

* Fri Jan 13 2017 Yuri N. Sedunov <aris@altlinux.org> 1.3.3-alt1
- 1.3.3

* Mon Jun 25 2012 Michael Shigorin <mike@altlinux.org> 0.9.6-alt2
- added gentoo patch to avoid crash on start (closes: #27497)
- spec cleanup

* Tue May 08 2012 Mikhail Pluzhnikov <amike@altlinux.ru> 0.9.6-alt1.qa3
- Fix description text in KOI8-R codepage
- Add description text in UTF8 codepage

* Wed Apr 04 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.9.6-alt1.qa2
- Fixed build with new glib2

* Tue Jun 07 2011 Repocop Q. A. Robot <repocop@altlinux.org> 0.9.6-alt1.qa1
- NMU (by repocop). See http://www.altlinux.org/Tools/Repocop
- applied repocop fixes:
  * freedesktop-desktop-file-proposed-patch for tilda

* Thu Oct 01 2009 Alexey Morsov <swi@altlinux.ru> 0.9.6-alt1
- initial build


                                                               
