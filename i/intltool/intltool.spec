%define ver_major 0.51

Name: intltool
Version: %ver_major.0
Release: alt2

Summary: Scripts and assorted auto* magic for i18nalizing various kinds of data files
License: %gpl2plus
Group: Development/GNOME and GTK+
Url: http://www.freedesktop.org/wiki/Software/%name

Source: https://launchpad.net/intltool/trunk/%version/+download/%name-%version.tar.gz
Patch: %name-0.50.2-alt-intltoolize.patch
# https://bugs.launchpad.net/intltool/+bug/1505260
# https://bugzilla.redhat.com/show_bug.cgi?id=1249051
Patch2: intltool-merge-Create-cache-file-atomically.patch
# Fix intltool-update to work with perl 5.26.
# Patch taken from fedora
Patch3: intltool-perl5.26-regex-fixes.patch

Requires: perl-XML-Parser
Obsoletes: xml-i18n-tools
Provides: xml-i18n-tools = %version

BuildArch: noarch

BuildPreReq: rpm-build-licenses rpm-build-gnome
BuildRequires: perl-XML-Parser perl-Encode perl-devel

%description
The intltool collection can be used to do these things:

 o Extract translatable strings from various source files (.xml.in,
   .glade, .desktop.in, .server.in, .oaf.in).

 o Collect the extracted strings together with messages from traditional
   source files (.c, .h) in po/$(PACKAGE).pot.

 o Merge back the translations from .po files into .xml, .desktop and
   .oaf files.  This merge step will happen at build resp. installation
   time.

%prep
%setup
%patch
%patch2 -p1
%patch3 -p1

%build
%configure
%make_build

%install
%makeinstall_std

%check
%make check

%files
%_bindir/*
%_datadir/%name/
%_datadir/aclocal/*
%_man8dir/*
%doc AUTHORS README TODO NEWS ChangeLog doc/*-HOWTO

%changelog
* Tue Dec 19 2017 Yuri N. Sedunov <aris@altlinux.org> 0.51.0-alt2
- fixed incompatibility with perl-5.26

* Thu Dec 17 2015 Yuri N. Sedunov <aris@altlinux.org> 0.51.0-alt1
- updated to 0.51.0
- fixed potential incompatibility with perl > 5.22

* Mon Jun 04 2012 Yuri N. Sedunov <aris@altlinux.org> 0.50.2-alt1
- 0.50.2
- fixed intltoolize for (ALT #27397)

* Thu Oct 13 2011 Yuri N. Sedunov <aris@altlinux.org> 0.50.0-alt1
- 0.50.0

* Wed Nov 17 2010 Yuri N. Sedunov <aris@altlinux.org> 0.41.1-alt3
- removed Requires: perl-devel (re.so moved to perl-base)

* Sun Nov 14 2010 Yuri N. Sedunov <aris@altlinux.org> 0.41.1-alt2
- Added explicit Requires: perl-devel (re.so)

* Fri May 28 2010 Yuri N. Sedunov <aris@altlinux.org> 0.41.1-alt1
- 0.41.1

* Mon Mar 16 2009 Yuri N. Sedunov <aris@altlinux.org> 0.40.6-alt1
- 0.40.6
- updated buildreqs

* Wed Oct 08 2008 Yuri N. Sedunov <aris@altlinux.org> 0.40.5-alt1
- 0.40.5

* Fri Sep 19 2008 Yuri N. Sedunov <aris@altlinux.org> 0.40.4-alt1
- 0.40.4

* Sat Jul 26 2008 Yuri N. Sedunov <aris@altlinux.org> 0.40.3-alt1
- 0.40.3

* Tue Jul 22 2008 Yuri N. Sedunov <aris@altlinux.org> 0.40.1-alt1
- 0.40.1

* Sun Jun 08 2008 Yuri N. Sedunov <aris@altlinux.org> 0.40.0-alt1
- 0.40.0

* Mon Mar 10 2008 Alexey Rusakov <ktirf@altlinux.org> 0.37.1-alt2
- There was an explicit Requires: perl-XML-Parser, that was actually
  needed; so now it's back.

* Wed Mar 05 2008 Alexey Rusakov <ktirf@altlinux.org> 0.37.1-alt1
- New version (0.37.1).
- Use macros from rpm-build-licenses and rpm-build-gnome.

* Thu Sep 20 2007 Igor Zubkov <icesik@altlinux.org> 0.36.2-alt1
- 0.35.5 -> 0.36.2

* Thu Jul 12 2007 Alexey Rusakov <ktirf@altlinux.org> 0.35.5-alt2
- added a fix for intltool-extract searching.

* Sun Apr 29 2007 Igor Zubkov <icesik@altlinux.org> 0.35.5-alt1
- 0.35.0 -> 0.35.5

* Tue May 16 2006 Alexey Rusakov <ktirf@altlinux.ru> 0.35.0-alt1
- new version 0.35.0 (with rpmrb script)

* Wed Mar 15 2006 Alexey Rusakov <ktirf@altlinux.ru> 0.34.2-alt1
- new version 0.34.2 (with rpmrb script)

* Mon Aug 29 2005 Alexey Rusakov <ktirf@altlinux.ru> 0.34.1-alt1
- 0.34.1

* Mon Mar 07 2005 Yuri N. Sedunov <aris@altlinux.ru> 0.33-alt1
- 0.33

* Wed Nov 10 2004 Yuri N. Sedunov <aris@altlinux.ru> 0.32.1-alt1
- 0.32.1

* Thu Sep 30 2004 Yuri N. Sedunov <aris@altlinux.ru> 0.31.3-alt1
- 0.31.3

* Thu Sep 02 2004 Yuri N. Sedunov <aris@altlinux.ru> 0.31.2-alt1
- 0.31.2

* Tue Jun 29 2004 Yuri N. Sedunov <aris@altlinux.ru> 0.31-alt1
- 0.31

* Wed Feb 04 2004 Yuri N. Sedunov <aris@altlinux.ru> 0.30-alt1
- 0.30

* Fri Jan 16 2004 Yuri N. Sedunov <aris@altlinux.ru> 0.29-alt1
- 0.29

* Thu Dec 11 2003 Yuri N. Sedunov <aris@altlinux.ru> 0.28-alt1
- 0.28

* Mon Aug 18 2003 Yuri N. Sedunov <aris@altlinux.ru> 0.27.2-alt1
- 0.27.2

* Sun May 18 2003 Yuri N. Sedunov <aris@altlinux.ru> 0.26-alt1
- 0.26

* Tue Jan 07 2003 Yuri N. Sedunov <aris@altlinux.ru> 0.25-alt1
- 0.25

* Thu Dec 19 2002 Yuri N. Sedunov <aris@altlinux.ru> 0.24-alt1
- 0.24

* Sat Nov 02 2002 Yuri N. Sedunov <aris@altlinux.ru> 0.23-alt1
- 0.23

* Tue Jun 18 2002 Yuri N. Sedunov <aris@altlinux.ru> 0.22-alt1
- 0.22

* Mon Feb 25 2002 AEN <aen@logic.ru> 0.15-alt1
- new name
- new version

* Wed Aug 22 2001 AEN <aen@logic.ru> 0.9-alt1
- new version

* Sat May 19 2001 Mikhail Zabaluev <mhz@altlinux.ru> 0.8.4-alt1
- Release 0.8.4
- Added BuildReqs after buildreq tip
- Added AutoReq: perl

* Sun Feb 18 2001 AEN <aen@logic.ru>
- adopted for Sisyphus

* Fri Feb 16 2001 Frederic Crozat <fcrozat@mandrakesoft.com> 0.8.1-1mdk
- Release 0.8.1

* Wed Feb 14 2001 Frederic Crozat <fcrozat@mandrakesoft.com> 0.8-1mdk
- Release 0.8

* Mon Feb  5 2001 Frederic Crozat <fcrozat@mandrakesoft.com> 0.6-2mdk
- Correct location of perl script

* Tue Jan 30 2001 Frederic Crozat <fcrozat@mandrakesoft.com> 0.6-1mdk
- Release 0.6

* Fri Jan 19 2001 Frederic Crozat <fcrozat@mandrakesoft.com> 0.5-1mdk
- Initial mdk package


