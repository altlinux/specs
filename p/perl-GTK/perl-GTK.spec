%define dist Gtk-Perl
Name: perl-GTK
Version: 0.7009
Release: alt5.1

Summary: Perl module for the GTK+ 1.2 library
License: GPL or Artistic
Group: Development/GNOME and GTK+

URL: %CPAN %dist
Source: %dist-%version.tar.gz

Patch0: perl-GTK-0.7002-mdk-ensure_focus.patch
Patch1: perl-GTK-0.7003-mdk-gdk_event_copy-withnowindow.patch
Patch2: perl-GTK-0.7005-mdk-XSetInputFocus.patch
Patch3: perl-GTK-0.7008-mdk-GdkPixbuf-memleak.patch
Patch4: perl-GTK-0.7009-alt-gendoc-no-parent.patch
Patch5: perl-GTK-0.7009-alt-pkgconfig.patch

# Automatically added by buildreq on Fri Oct 07 2011
BuildRequires: gtk+-devel perl-XML-Parser perl-XML-Writer perl-devel

%description
This module provides Perl access to the gtk+-1.2 library.
Gtk+ is the GIMP ToolKit (GTK+), a library for creating
graphical user interfaces for the X Window System.

%prep
%setup -q -n %dist-%version
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p2

# disable build dependency on perl-podlators
sed -i- '/MAN3PODS/,/}/s/^/#/' Gtk/Makefile.PL

%build
cd Gtk
%perl_vendor_build --lazy-load
perl -Mblib -MGtk -e1
install -pD -m644 cookbook.pod blib/lib/Gtk/cookbook.pod
install -pD -m644 objects.pod blib/lib/Gtk/objects.pod
install -pD -m644 build/perl-gtk-ref.pod blib/lib/Gtk/reference.pod

%install
cd Gtk
%perl_vendor_install

# should not be packaged in legacy mode
rm -r %buildroot%perl_vendor_archlib/Gtk/Install

%files
%doc	README NOTES VERSIONS
	%perl_vendor_archlib/Gtk.pm
%dir	%perl_vendor_archlib/Gtk
	%perl_vendor_archlib/Gtk/Atoms.pm
	%perl_vendor_archlib/Gtk/Gdk.pm
	%perl_vendor_archlib/Gtk/Keysyms.pm
	%perl_vendor_archlib/Gtk/Types.pm
	%perl_vendor_archlib/Gtk/TypesLazy.pm
	%perl_vendor_archlib/Gtk/lazy.pm
%doc	%perl_vendor_archlib/Gtk/*.pod
	%perl_vendor_autolib/Gtk

%changelog
* Fri Oct 07 2011 Alexey Tourbin <at@altlinux.ru> 0.7009-alt5.1
- rebuilt for perl-5.14

* Wed Oct 05 2011 Alexey Tourbin <at@altlinux.ru> 0.7009-alt5
- rebuilt as plain src.rpm

* Sat Nov 06 2010 Vladimir Lettiev <crux@altlinux.ru> 0.7009-alt4.1
- rebuilt with perl 5.12

* Mon Sep 29 2008 Alexey Tourbin <at@altlinux.ru> 0.7009-alt4
- packaged only perl-GTK (perl-GTK-GdkImlib, perl-GTK-GdkPixbuf,
  and perl-GTK-Gnome are gone for good and all)

* Tue Apr 10 2007 Alexey Tourbin <at@altlinux.ru> 0.7009-alt3
- fixed build with new MakeMaker

* Sun Feb 25 2007 Alexey Tourbin <at@altlinux.ru> 0.7009-alt2
- fixed linkage and build errors

* Sat Apr 16 2005 Alexey Tourbin <at@altlinux.ru> 0.7009-alt1
- build only Gtk, GdkImlib, GdkPixbuf, and Gnome
- specfile cleanup and policy enforcement

* Sat Feb 19 2005 ALT QA Team Robot <qa-robot@altlinux.org> 0.7009-alt0.2.1
- Rebuilt with rpm-build-perl-0.5.1.

* Tue Sep 09 2003 Alexey Tourbin <at@altlinux.ru> 0.7009-alt0.2
- 0.7009; modules built: Gtk GdkImlib GdkPixbuf Glade Gnome GtkHTML

* Mon Sep 08 2003 Alexey Tourbin <at@altlinux.ru> 0.7009-alt0.1
- 0.7009; modules built: Gtk GdkImlib GdkPixbuf Glade Gnome

* Wed Sep 03 2003 AEN <aen@altlinux.ru> 0.7008-alt11
- rebuild w/o gnomeprint

* Wed Dec 04 2002 AEN <aen@altlinux.ru> 0.7008-alt10
- new package: perl-GTK-LWP

* Thu Nov 14 2002 AEN <aen@altlinux.ru> 0.7008-alt9
- rebuilt with gtkhtml20 

* Tue Nov 12 2002 AEN <aen@altlinux.ru> 0.7008-alt8
- GLArea module disabled

* Fri Nov 01 2002 AEN <aen@altlinux.ru> 0.7008-alt7
- rebuilt with perl-5.8.0
- mozilla module disabled

* Tue Mar 05 2002 Mikhail Zabaluev <mhz@altlinux.ru> 0.7008-alt6
- Fixed build subdirectories disarray
- Completed file list
- Added GtkXmHTML subpackage

* Thu Feb 28 2002 Mikhail Zabaluev <mhz@altlinux.ru> 0.7008-alt5
- Fixed CFLAGS for GtkHTML (again)

* Mon Feb 25 2002 Mikhail Zabaluev <mhz@altlinux.ru> 0.7008-alt4
- Added manpages, READMEs and samples
- Split GnomeApplet and GnomePrint subpackages off Gnome

* Mon Jan 21 2002 Mikhail Zabaluev <mhz@altlinux.ru> 0.7008-alt3
- Patched Applet/Makefile.PL for ORBit cflags
- Updated build requires

* Mon Jan 14 2002 AEN <aen@logic.ru> 0.7008-alt2
- rebuilt with gal-0.19

* Wed Nov 08 2001 Konstantin Volckov <goldhead@altlinux.ru> 0.7008-alt1
- Build for Sisyphus

* Mon Oct 29 2001 Frederic Crozat <fcrozat@mandrakesoft.com> 0.7008-12mdk
- Recompiled against mozilla 0.9.5 and latest libgal/libgtkhtml
- Update patch 4 for mozilla 0.9.5

* Mon Oct  1 2001 Frederic Crozat <fcrozat@mandrakesoft.com> 0.7008-11mdk
- Recompiled against libgtkhtml16/libgal12

* Tue Sep 18 2001 Daouda LO <daouda@mandrakesoft.com> 0.7008-10mdk
- Recomplied against mozilla-0.9.4

* Thu Aug 30 2001 Frederic Crozat <fcrozat@mandrakesoft.com> 0.7008-9mdk
- Recompiled against libgtkhtml15

* Wed Aug 22 2001 Frederic Crozat <fcrozat@mandrakesoft.com> 0.7008-8mdk
- Recompiled against libgal11

* Tue Aug 21 2001 Gwenole Beauchesne <gbeauchesne@mandrakesoft.com> 0.7008-7mdk
- Don't build perl-GTK-MozEmbed on ia64

* Mon Aug 20 2001 Daouda LO <daouda@mandrakesoft.com> 0.7008-6mdk
- add gtk_html_set_default_content_type support to GtkHtml.xs

* Fri Aug 10 2001 Frederic Crozat <fcrozat@mandrakesoft.com> 0.7008-5mdk
- Patch5 : fix binding for latest gtkhtml
- Update patch4 to build with latest mozilla

* Fri Jul 20 2001 Pixel <pixel@mandrakesoft.com> 0.7008-4mdk
- use older gtkhtml so that it works
- add perl-GTK-MozEmbed

* Wed Jul 18 2001 Frederic Crozat <fcrozat@mandrakesoft.com> 0.7008-3mdk
- Recompiled against latest gal/gtkhtml

* Thu Jul  5 2001 Frederic Crozat <fcrozat@mandrakesoft.com> 0.7008-2mdk
- Really remove dependency against libgal6

* Sat Jun 30 2001 Pixel <pixel@mandrakesoft.com> 0.7008-1mdk
- new version

* Thu Jun 28 2001 Frederic Crozat <fcrozat@mandrakesoft.com> 0.7007-2mdk
- Recompiled against latest gtkhtml/gal

* Mon Jun  4 2001 Pixel <pixel@mandrakesoft.com> 0.7007-1mdk
- new version

* Fri May 18 2001 Frederic Crozat <fcrozat@mandrakesoft.com> 0.7006-2mdk
- Recompiled against latest gtkhtml

* Wed Mar 28 2001 Pixel <pixel@mandrakesoft.com> 0.7006-1mdk
- new version

* Wed Mar  7 2001 Frederic Crozat <fcrozat@mandrakesoft.com> 0.7005-3mdk
- Recompiled against latest gnomeprint

* Mon Mar  5 2001 Pixel <pixel@mandrakesoft.com> 0.7005-2mdk
- add XSetInputFocus (hack for drakxtools)

* Thu Feb 22 2001 Pixel <pixel@mandrakesoft.com> 0.7005-1mdk
- new version

* Mon Feb 19 2001 Pixel <pixel@mandrakesoft.com> 0.7004-9mdk
- really compile against latest gtkhtml

* Thu Feb 15 2001 Frederic Crozat <fcrozat@mandrakesoft.com> 0.7004-8mdk
- Recompiled against latest gtkhtml

* Mon Feb 12 2001 Pixel <pixel@mandrakesoft.com> 0.7004-7mdk
- added gtk_ctree_pre_recursive
- gtk_ctree_post_recursive now accepts CTreeNode_OrNULL instead CTreeNode

* Wed Jan 10 2001 Pixel <pixel@mandrakesoft.com> 0.7004-6mdk
- GtkTable-attach--add-functionality.patch.bz2

* Mon Jan  8 2001 Pixel <pixel@mandrakesoft.com> 0.7004-5mdk
- add GdkPixbuf

* Sun Dec  3 2000 Pixel <pixel@mandrakesoft.com> 0.7004-4mdk
- update the buildReq

* Tue Nov  7 2000 Pixel <pixel@mandrakesoft.com> 0.7004-3mdk
- rebuild with new perl

* Tue Nov  7 2000 Pixel <pixel@mandrakesoft.com> 0.7004-2mdk
- add descriptions to make rpmlint happy

* Thu Oct 26 2000 Pixel <pixel@mandrakesoft.com> 0.7004-1mdk
- new version

* Wed Aug 30 2000 François Pons <fpons@mandrakesoft.com> 0.7003-4mdk
- created patch to fix list access in GtkList.xs and GtkTree.xs.

* Thu Aug 24 2000 Pixel <pixel@mandrakesoft.com> 0.7003-3mdk
- workaround-gdk_event_copy-withnowindow

* Fri Aug 18 2000 Pixel <pixel@mandrakesoft.com> 0.7003-2mdk
- rebuild with clean_perl in spec-helper

* Thu Aug 17 2000 Pixel <pixel@mandrakesoft.com> 0.7003-1mdk
- new version
- replace XmHTML by GtkHTML (seems to work, at least it builds now ;)

* Mon Aug 07 2000 Frederic Lepied <flepied@mandrakesoft.com> 0.7002-9mdk
- automatically added BuildRequires

* Thu Aug  3 2000 Alexander Skwar <ASkwar@DigitalProjects.com>, Pixel <pixel@mandrakesoft.com> 0.7002-8mdk
- More macroziatification *g*
- Man pages are always to be globbed
- removed .packlist's
- added %clean section

* Wed Jul 19 2000 Pixel <pixel@mandrakesoft.com> 0.7002-7mdk
- macroziation

* Wed Apr 26 2000 Pixel <pixel@mandrakesoft.com> 0.7002-6mdk
- add buildrequires xpm-devel

* Mon Apr 10 2000 Pixel <pixel@mandrakesoft.com> 0.7002-5mdk
- fix groups

* Sun Apr  2 2000 Pixel <pixel@mandrakesoft.com> 0.7002-4mdk
- rebuild for new libgtkgl

* Thu Mar 30 2000 Pixel <pixel@mandrakesoft.com> 0.7002-3mdk
- changed 5.005 to 5.* to build with new perl

* Sun Mar 12 2000 Pixel <pixel@mandrakesoft.com> 0.7002-2mdk
- add ensure_focus

* Mon Feb 28 2000 Pixel <pixel@mandrakesoft.com> 0.7002-1mdk
- new version

* Wed Jan 26 2000 Pixel <pixel@mandrakesoft.com>
- major rework for 0.7000
- oups %%{_arch}
- added test.pl in perl-GTK-gnome

* Tue Nov 23 1999 Pixel <pixel@linux-mandrake.com>
- replaced i386 by %%_arch (for alpha)

* Sun Nov 21 1999 Pixel <pixel@mandrakesoft.com>
- strip .so (nice rpmlint :)

* Sun Nov  7 1999 Chmouel Boudjnah <chmouel@mandrakesoft.com>
- Build release.

* Mon Oct 18 1999 Pixel <pixel@linux-mandrake.com>
- 0.6123

* Tue Jul 13 1999 Chmouel Boudjnah <chmouel@mandrakesoft.com>
- initialization of spec file.
