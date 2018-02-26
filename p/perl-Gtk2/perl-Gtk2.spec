%define dist Gtk2
Name: perl-%dist
Version: 1.242
Release: alt1

Summary: Perl bindings to the gtk+-2.x library
License: LGPL
Group: Development/Perl

URL: http://gtk2-perl.sourceforge.net/
Source: %dist-%version.tar.gz

Patch0: perl-Gtk2-1.224-alt-gtk_version.patch
Patch1: perl-Gtk2-1.224-alt-gtk_init.patch
Patch2: perl-Gtk2-1.242-alt-cairo.patch

%define base_ver 1.240
Requires: perl-Glib >= %base_ver
Requires: perl-Pango >= 1.220
BuildPreReq: perl-Glib-devel >= %base_ver
BuildPreReq: perl-Pango-devel >= 1.220

# Automatically added by buildreq on Sun Oct 09 2011
BuildRequires: fonts-ttf-dejavu gnome-icon-theme libgtk+2-devel perl-ExtUtils-Depends perl-ExtUtils-PkgConfig perl-Pango-devel perl-podlators xvfb-run

%package devel
Summary: Perl bindings to the gtk+-2.x library (development files)
Group: Development/Perl
Requires: %name = %version-%release
Requires: libgtk+2-devel
# Gtk2/Install/Files.pm:deps
Requires: perl-Glib-devel
Requires: perl-Cairo-devel
Requires: perl-Pango-devel

%description
This module provides perl access to the gtk+-2.x library.
Gtk+ is the GIMP ToolKit (GTK+), a library for creating graphical
user interfaces for the X Window System.  GTK+ was originally written
for the GIMP (GNU Image Manipulation Program) image processing program,
but is now used by several other programs as well.

%description devel
This module provides perl access to the gtk+-2.x library.
Gtk+ is the GIMP ToolKit (GTK+), a library for creating graphical
user interfaces for the X Window System.  GTK+ was originally written
for the GIMP (GNU Image Manipulation Program) image processing program,
but is now used by several other programs as well.

This package contains Gtk2 development files and documentation
for developers (overview of internals and internal API reference).

%prep
%setup -q -n %dist-%version
%patch0 -p1
%patch1 -p1
%patch2 -p2

%build
%ifndef _build_display
%def_without test
%endif

%perl_vendor_build

xvfb-run -a make test

%install
%perl_vendor_install

%define pkgdocdir %_docdir/%name-%version
mkdir -p %buildroot%pkgdocdir
cp -av AUTHORS NEWS README gtk-demo examples %buildroot%pkgdocdir/

%files
%dir	%pkgdocdir
	%pkgdocdir/AUTHORS
	%pkgdocdir/NEWS
	%pkgdocdir/README
	%perl_vendor_archlib/Gtk2.pm
%dir	%perl_vendor_archlib/Gtk2
%dir	%perl_vendor_archlib/Gtk2/Gdk
	%perl_vendor_archlib/Gtk2/Gdk/Keysyms.pm
	%perl_vendor_archlib/Gtk2/Helper.pm
	%perl_vendor_archlib/Gtk2/Pango.pm
	%perl_vendor_archlib/Gtk2/SimpleList.pm
	%perl_vendor_archlib/Gtk2/SimpleMenu.pm
%dir	%perl_vendor_autolib/Gtk2
	%perl_vendor_autolib/Gtk2/Gtk2.so

%files devel
%dir	%pkgdocdir
	%pkgdocdir/gtk-demo
	%pkgdocdir/examples
%dir	%perl_vendor_archlib/Gtk2
	%perl_vendor_archlib/Gtk2/CodeGen.pm
	%perl_vendor_archlib/Gtk2/TestHelper.pm
%dir	%perl_vendor_archlib/Gtk2/Install
	%perl_vendor_archlib/Gtk2/Install/*
# pod
%doc	%perl_vendor_archlib/Gtk2/*.pod
%dir	%perl_vendor_archlib/Gtk2/Buildable
%doc	%perl_vendor_archlib/Gtk2/Buildable/*.pod
%dir	%perl_vendor_archlib/Gtk2/Gdk
%doc	%perl_vendor_archlib/Gtk2/Gdk/*.pod
%dir	%perl_vendor_archlib/Gtk2/Gdk/Cairo
%doc	%perl_vendor_archlib/Gtk2/Gdk/Cairo/*.pod
%dir	%perl_vendor_archlib/Gtk2/Gdk/Event
%doc	%perl_vendor_archlib/Gtk2/Gdk/Event/*.pod
%dir	%perl_vendor_archlib/Gtk2/Gdk/Pango
%doc	%perl_vendor_archlib/Gtk2/Gdk/Pango/*.pod
%dir	%perl_vendor_archlib/Gtk2/Pango
%doc	%perl_vendor_archlib/Gtk2/Pango/*.pod
%dir	%perl_vendor_archlib/Gtk2/Pango/Cairo
%doc	%perl_vendor_archlib/Gtk2/Pango/Cairo/*.pod

%changelog
* Wed Apr 11 2012 Vladimir Lettiev <crux@altlinux.ru> 1.242-alt1
- 1.224 -> 1.242

* Sun Oct 09 2011 Alexey Tourbin <at@altlinux.ru> 1.224-alt1
- 1.223 -> 1.224
- built for perl-5.14

* Thu Mar 03 2011 Vladimir Lettiev <crux@altlinux.ru> 1.223-alt1
- New version 1.223

* Fri Feb 25 2011 Vladimir Lettiev <crux@altlinux.ru> 1.222-alt3
- merge commit from upstream branch stable-1-22:
  + Fix a test failure in GtkBuilder.t

* Sun Nov 28 2010 Vladimir Lettiev <crux@altlinux.ru> 1.222-alt2
- merge commits from upstream branch stable-1-22:
  + fixed Gtk2::Gdk::Keysyms with gtk+ 2.22 (Closes: #24619)
  + fixed failing tests

* Sun Nov 07 2010 Vladimir Lettiev <crux@altlinux.ru> 1.222-alt1.1
- rebuilt with perl 5.12
- disabled a failing tests for a while

* Fri Jun 04 2010 Vladimir Lettiev <crux@altlinux.ru> 1.222-alt1
- New version 1.222

* Mon Apr 12 2010 Vladimir Lettiev <crux@altlinux.ru> 1.221-alt4
- fixed tests:
  + GtkAction.t         (fix from upstream git, commit 71800dd9)
  + GtkBuildableIface.t (fix from upstream git, commit d0b0e0ba)

* Sun Mar 21 2010 Vladimir Lettiev <crux@altlinux.ru> 1.221-alt3
- fixed GtkAssistant.t test (fix from upstream git, commit ca7f1494)

* Tue Feb 02 2010 Vladimir Lettiev <crux@altlinux.ru> 1.221-alt2
- fixed tests:
  + GtkPrintSettings.t (patch from debian bug #549465)
  + GtkTreeView.t      (patch from debian bug #545616)
  + GtkRecentChooser.t (patch from debian bug #519864)

* Fri Jul 17 2009 Alexey Tourbin <at@altlinux.ru> 1.221-alt1
- 1.220 -> 1.221

* Fri Apr 03 2009 Alexey Tourbin <at@altlinux.ru> 1.220-alt3
- Gtk2.xs (gtk_init): do gtk_init_check in PL_minus_c mode, so that
  syntax check is possible even when the GUI cannot be initialized

* Thu Mar 26 2009 Alexey Tourbin <at@altlinux.ru> 1.220-alt2
- updated dependencies

* Tue Mar 24 2009 Alexey Tourbin <at@altlinux.ru> 1.220-alt1
- 1.200 -> 1.220

* Mon Sep 29 2008 Alexey Tourbin <at@altlinux.ru> 1.200-alt1
- 1.132 -> 1.200
- removed Mandriva patches
- disabled t/GdkKeys.t and t/GtkTreeView.t tests which fail under Xvfb

* Sat Aug 26 2006 Alexey Tourbin <at@altlinux.ru> 1.132-alt2
- fixed dependency on Cairo

* Tue Aug 15 2006 Alexey Tourbin <at@altlinux.ru> 1.132-alt1
- 1.120 -> 1.132 (with Cairo)

* Sat Mar 18 2006 LAKostis <lakostis at altlinux.ru> 1.120-alt1
- NMU.
- 1.101 -> 1.120.
- remove GtkFileChooser patch (fixed upstream).

* Mon Oct 17 2005 Alexey Tourbin <at@altlinux.ru> 1.101-alt1
- 1.093 -> 1.101
- fixed GtkFileChooser test

* Fri Sep 02 2005 Alexey Tourbin <at@altlinux.ru> 1.093-alt1
- 1.082 -> 1.093
- built with libgtk+2 2.8, updated dependencies on libgtk+2

* Thu Jun 23 2005 Alexey Tourbin <at@altlinux.ru> 1.082-alt1
- 1.081 -> 1.082
- license: LGPL, not GPL

* Thu Apr 14 2005 Alexey Tourbin <at@altlinux.ru> 1.081-alt1
- 1.080 -> 1.081
- alt-gtk_version.patch: don't warn on gtk_micro_version change

* Mon Mar 21 2005 Alexey Tourbin <at@altlinux.ru> 1.080-alt1
- 1.072 -> 1.080

* Fri Jan 14 2005 Alexey Tourbin <at@altlinux.ru> 1.072-alt1
- 1.061 -> 1.072
- new subpackage: %name-devel
- manual pages not packaged (use perldoc)
- always run tests (by utilizing xvfb-run)
- disabled some tests because of failures under Test::More 0.53

* Wed Oct 06 2004 Alexey Tourbin <at@altlinux.ru> 1.061-alt1
- 1.053 -> 1.061

* Mon Aug 09 2004 Alexey Tourbin <at@altlinux.ru> 1.053-alt1
- 1.042 -> 1.053

* Fri Apr 16 2004 Alexey Tourbin <at@altlinux.ru> 1.042-alt1
- 1.023 -> 1.042, Mandrake patches updated
- skip Test::More dependency

* Wed Feb 18 2004 Alexey Tourbin <at@altlinux.ru> 1.023-alt1
- 1.023
- in sync with 1.023-2mdk

* Tue Oct 14 2003 Alexey Tourbin <at@altlinux.ru> 1.00-alt1
- 1.00

* Thu Aug 28 2003 Alexey Tourbin <at@altlinux.ru> 0.95-alt1
- initial revision; mandrake patches applied
