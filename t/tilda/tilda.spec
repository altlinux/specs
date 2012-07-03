Name: tilda
Version: 0.9.6
Release: alt2

Summary: A Linux terminal taking after the likeness of many terminals from fps games
License: GPLv2
Group: Terminals

Url: http://tilda.sourceforge.net/
Source: %name-%version.tar
Patch0: %name-0.9.6-alt-glib2-2.32.0.patch
Patch1: tilda-0.9.6-gdk_resources.patch
Packager: Alexey Morsov <swi@altlinux.ru>

BuildRequires: flex libglade-devel libXrandr-devel
BuildRequires: libconfuse-devel libvte-devel
BuildRequires: desktop-file-utils

Summary(ru_RU.UTF-8): Терминал Linux, имитирующий многие терминалы из FPS-игр

%description
Tilda is a Linux terminal taking after the likeness of many classic
terminals from first person shooter games, Quake, Doom and Half-Life
(to name a few), where the terminal has no border and is hidden from
the desktop until a key is pressed.

%prep
%setup
%patch0 -p0
%patch1 -p0

%build
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
%doc AUTHORS ChangeLog NEWS README TODO
%_bindir/*
%_desktopdir/*
%_pixmapsdir/*
%_datadir/%name.glade
%_datadir/locale/*/LC_MESSAGES/%{name}.mo

%changelog
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


                                                               
