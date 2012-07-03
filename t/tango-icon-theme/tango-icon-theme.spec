Name: tango-icon-theme
Version: 0.8.90
Release: alt2

Summary: Tango Icon Library
License: Creative Commons Attribution Share-Alike license 2.5
Group: Graphical desktop/Other
Url: http://tango.freedesktop.org/Tango_Desktop_Project

Source0: http://tango-project.org/releases/%name-%version.tar
Source1: Globe-with-clock.svg
Patch1: tango-icon-theme-0.8.90-alt-fix-icons-convert.patch

BuildArch: noarch

BuildPreReq: intltool >= 0.33
BuildPreReq: icon-naming-utils >= 0.8.90
BuildPreReq: ImageMagick libImageMagick-devel >= 5.5.7
BuildPreReq: libGraphicsMagick-devel >= 1.1
# For AM_GLIB_GNU_GETTEXT
BuildPreReq: glib2-devel

BuildRequires: perl-XML-Parser

%description
This is an icon theme that follows the Tango visual guidelines.

%prep
%setup -q
%patch1 -p1

%build
%autoreconf
%configure
%make_build

%install
%make_install DESTDIR=%buildroot install
install -m0644 %SOURCE1 %buildroot%_datadir/icons/Tango/scalable/apps/clock.svg

%files
%doc AUTHORS COPYING ChangeLog README
%dir %_datadir/icons/Tango/
%_datadir/icons/Tango/*

%changelog
* Wed Jul 13 2011 Mikhail Efremov <sem@altlinux.org> 0.8.90-alt2
- Fix icons convert type (closes: #25711).
- Add Globe-with-clock.svg as clock.svg.

* Thu Jun 02 2011 Igor Vlasenko <viy@altlinux.ru> 0.8.90-alt1.1
- NMU: build w/o undefine _configure_target hack

* Mon Mar 09 2009 Alexey Rusakov <ktirf@altlinux.org> 0.8.90-alt1
- moved to git/git.alt
- updated sources from the latest upstream version
- updated buildreqs

* Tue Aug 14 2007 Igor Zubkov <icesik@altlinux.org> 0.8.1-alt2
- fix building

* Tue Aug 14 2007 Igor Zubkov <icesik@altlinux.org> 0.8.1-alt1
- 0.8.0 -> 0.8.1

* Thu Mar 01 2007 Igor Zubkov <icesik@altlinux.org> 0.8.0-alt1
- build for Sisyphus


