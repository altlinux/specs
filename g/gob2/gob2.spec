%define ver_major 2.0

Name: gob2
Version: %ver_major.17
Release: alt1

Summary: The GObject Builder
License: %gpl2plus
Group: Development/GNOME and GTK+

Url: http://www.5z.com/jirka/gob.html
Source: %gnome_ftp/%name/%ver_major/%name-%version.tar.bz2

Packager: GNOME Maintainers Team <gnome@packages.altlinux.org>

BuildPreReq: glib2-devel >= 2.5.3
BuildRequires: rpm-build-licenses rpm-build-gnome flex pkg-config

%description
GOB is a simple preprocessor for making GObject objects (glib objects).
It makes objects from a single file which has inline C code so that you
don't have to edit the generated files.  Syntax is somewhat inspired by
java and yacc. It supports generating C++ code.

%prep
%setup -q

%build
%configure
%make_build

%install
%makeinstall

%files
%_bindir/*
%_datadir/aclocal/*
%_man1dir/*
%doc README AUTHORS NEWS TODO ChangeLog
%doc examples

%changelog
* Wed Apr 07 2010 Yuri N. Sedunov <aris@altlinux.org> 2.0.17-alt1
- 2.0.17

* Thu Jul 23 2009 Alexey Rusakov <ktirf@altlinux.org> 2.0.16-alt1
- new version (2.0.16)

* Thu Dec 25 2008 Alexey Rusakov <ktirf@altlinux.org> 2.0.15-alt1
- new version (2.0.15)
- specfile cleanup
- made license tag contents more exact (GPL -> %gpl2plus)
- updated Url tag, simplified Source tag thanks to rpm-build-gnome
- added Packager tag (thanks to repocop for a reminder)

* Sun Jan 22 2006 Alexey Rusakov <ktirf@altlinux.ru> 2.0.14-alt1
- new version

* Wed Oct 27 2004 Yuri N. Sedunov <aris@altlinux.ru> 2.0.11-alt1
- 2.0.11

* Thu Sep 23 2004 Yuri N. Sedunov <aris@altlinux.ru> 2.0.10-alt1
- 2.0.10

* Mon May 17 2004 Yuri N. Sedunov <aris@altlinux.ru> 2.0.7-alt1
- 2.0.7.

* Fri Jan 17 2003 Yuri N. Sedunov <aris@altlinux.ru> 2.0.5-alt1
- 2.0.5

* Sat Dec 14 2002 Yuri N. Sedunov <aris@altlinux.ru> 2.0.4-alt1
- 2.0.4

* Sat Nov 02 2002 Yuri N. Sedunov <aris@altlinux.ru> 2.0.3-alt1
- First build for Sisyphus.
