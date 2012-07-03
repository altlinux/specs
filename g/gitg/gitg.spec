Name: gitg
Version: 0.1.0
Release: alt1.qa1
Summary: git repository viewer targeting gtk+/GNOME

Group: Development/Other
License: GPL
URL: http://trac.novowork.com/gitg/

Source: %name-%version.tar
Packager: Vladimir Lettiev <crux@altlinux.ru>

PreReq: lib%name = %version-%release

BuildRequires: libgtk+2-devel libgio-devel libGConf-devel gnome-common intltool libgtksourceview-devel gsettings-desktop-schemas-devel
BuildRequires: desktop-file-utils

%description
gitg is a git repository viewer targeting gtk+/GNOME. One of its main
objectives is to provide a more unified user experience for git
frontends across multiple desktops. It does this not be writing a
cross-platform application, but by close collaboration with similar
clients for other operating systems (like GitX for OS X).

gitg targets cases where it is useful to provide a graphical
representation of git data or actions. The history view is a good
example where graphical representation helps to get an overview of the
repository. gitg does not aim to be an advanced tool which allows access
to every feature of git through a graphical interface, it will however
try to incorporate common actions which might require multiple actions
on the command line (like staging, unstaging, reverting and committing).

%package -n lib%name
Summary: lib%name library
Group: Development/C

%description -n lib%name
%summary

%package -n lib%name-devel
Summary: lib%name library development files
Group: Development/C
PreReq: lib%name = %version-%release

%description -n lib%name-devel
%summary

%prep
%setup

%build
NOCONFIGURE=true ./autogen.sh
%configure --disable-static
%make_build

%install
%makeinstall_std
%find_lang %name
desktop-file-install --dir %buildroot%_desktopdir \
	--add-category=RevisionControl \
	%buildroot%_desktopdir/gitg.desktop

%files -f %name.lang
%_datadir/glib-2.0/schemas/org.gnome.gitg.gschema.xml
%_desktopdir/%name.desktop
%_datadir/%name
%_bindir/%name
%_man1dir/%{name}*
%_miconsdir/*
%_niconsdir/*
%_liconsdir/*
%_iconsdir/hicolor/scalable/*
%_iconsdir/hicolor/22x22/apps/*
%_iconsdir/hicolor/24x24/apps/*
%doc AUTHORS COPYING MAINTAINERS NEWS README

%files -n lib%name
%_libdir/lib%name-1.0.so.*

%files -n lib%name-devel
%_includedir/lib%name-1.0
%_libdir/lib%name-1.0.so
%_libdir/pkgconfig/lib%name-1.0.pc

%changelog
* Tue May 24 2011 Repocop Q. A. Robot <repocop@altlinux.org> 0.1.0-alt1.qa1
- NMU (by repocop). See http://www.altlinux.org/Tools/Repocop
- applied repocop fixes:
  * freedesktop-desktop-file-proposed-patch for gitg

* Fri Feb 18 2011 Vladimir Lettiev <crux@altlinux.ru> 0.1.0-alt1
- New version 0.1.0
- Updated buildreqs

* Mon Jan 03 2011 Vladimir Lettiev <crux@altlinux.ru> 0.0.8-alt1
- New version 0.0.8
- Separated lib%name{,-devel} subpackages

* Mon Feb 22 2010 Vladimir Lettiev <crux@altlinux.ru> 0.0.6-alt1
- New version 0.0.6

* Wed Sep 30 2009 Vladimir Lettiev <crux@altlinux.ru> 0.0.5-alt1
- 0.0.5
- patch from ktirf@ (closes: #21305)

* Sun Apr 26 2009 Vladimir Lettiev <crux@altlinux.ru> 0.0.3-alt1
- initial build

