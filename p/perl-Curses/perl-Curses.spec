%define _unpackaged_files_terminate_build 1
%define dist Curses
Name: perl-%dist
Version: 1.36
Release: alt1.1.1

Summary: Terminal screen handling and optimization
License: GPL or Artistic
Group: Development/Perl

URL: %CPAN %dist
Source: http://www.cpan.org/authors/id/G/GI/GIRAFFED/Curses-%{version}.tar.gz

# Automatically added by buildreq on Fri Oct 07 2011
BuildRequires: libncursesw-devel perl-devel

%description
Curses is the interface between Perl and ncurses(3) library.
The curses library routines are a terminal-independent method of updating
character screens with reasonable optimization.  The ncurses (new curses)
library is a freely distributable replacement for the discontinued 4.4BSD
classic curses library.

%prep
%setup -q -n %dist-%version

%build
export CURSES_CFLAGS=-I%_includedir/ncursesw CURSES_LDFLAGS='-ltinfo -lncursesw'
export CURSES_PANEL_LDFLAGS=-lpanelw CURSES_MENU_LDFLAGS=-lmenuw CURSES_FORM_LDFLAGS=-lformw
%perl_vendor_build PANELS MENUS FORMS

# no tests provided, make sure Curses can be loaded
perl -Mblib -MCurses -e1

%install
%perl_vendor_install

%files
%doc HISTORY README demo*
%perl_vendor_archlib/Curses*
%perl_vendor_autolib/Curses*

%changelog
* Fri Dec 15 2017 Igor Vlasenko <viy@altlinux.ru> 1.36-alt1.1.1
- rebuild with new perl 5.26.1

* Fri Feb 03 2017 Igor Vlasenko <viy@altlinux.ru> 1.36-alt1.1
- rebuild with new perl 5.24.1

* Tue Sep 20 2016 Igor Vlasenko <viy@altlinux.ru> 1.36-alt1
- automated CPAN update

* Thu Apr 07 2016 Igor Vlasenko <viy@altlinux.ru> 1.34-alt1
- automated CPAN update

* Wed Nov 25 2015 Igor Vlasenko <viy@altlinux.ru> 1.33-alt1.1
- rebuild with new perl 5.22.0

* Sun Oct 11 2015 Igor Vlasenko <viy@altlinux.ru> 1.33-alt1
- automated CPAN update

* Tue Dec 09 2014 Igor Vlasenko <viy@altlinux.ru> 1.32-alt1.1
- rebuild with new perl 5.20.1

* Tue Aug 19 2014 Igor Vlasenko <viy@altlinux.ru> 1.32-alt1
- automated CPAN update

* Fri May 02 2014 Igor Vlasenko <viy@altlinux.ru> 1.31-alt1
- automated CPAN update

* Wed Apr 09 2014 Igor Vlasenko <viy@altlinux.ru> 1.29-alt1
- automated CPAN update

* Tue Aug 27 2013 Vladimir Lettiev <crux@altlinux.ru> 1.28-alt4
- built for perl 5.18

* Thu Aug 30 2012 Vladimir Lettiev <crux@altlinux.ru> 1.28-alt3
- rebuilt for perl-5.16

* Fri Oct 07 2011 Alexey Tourbin <at@altlinux.ru> 1.28-alt2
- rebuilt for perl-5.14

* Tue Oct 04 2011 Alexey Tourbin <at@altlinux.ru> 1.28-alt1
- 1.27 -> 1.28
- rebuilt as plain src.rpm

* Sat Nov 06 2010 Vladimir Lettiev <crux@altlinux.ru> 1.27-alt1.1
- rebuilt with perl 5.12

* Wed Jul 22 2009 Alexey Tourbin <at@altlinux.ru> 1.27-alt1
- 1.24 -> 1.27

* Tue Dec 16 2008 Alexey Tourbin <at@altlinux.ru> 1.24-alt1
- 1.14 -> 1.24

* Mon Jun 26 2006 Alexey Tourbin <at@altlinux.ru> 1.14-alt2
- fixed linkage (see #9608)

* Tue Jun 13 2006 Alexey Tourbin <at@altlinux.ru> 1.14-alt1
- 1.12 -> 1.14
- built with libncursesw (#9608)

* Fri Apr 15 2005 Alexey Tourbin <at@altlinux.ru> 1.12-alt1
- 1.11 -> 1.12
- alt-makefile-linkage.patch mreged upstream (cpan #11914)
- removed %_bindir/rep in favour of watch(1)
- added demo files

* Thu Mar 17 2005 Alexey Tourbin <at@altlinux.ru> 1.11-alt1
- 1.10 -> 1.11, VERSION was fixed upstream (cpan #11853)
- fixed linkage with libform, libmenu, and libpanel (cpan #11914)
- added %_bindir/rep (by Tom Christiansen, see perlfaq3)

* Sat Mar 12 2005 Alexey Tourbin <at@altlinux.ru> 1.10-alt2
- fuck! fixed VERSION so that Curses even work (cpan #11853)

* Sat Mar 12 2005 Alexey Tourbin <at@altlinux.ru> 1.10-alt1
- 1.06 -> 1.10
- manual pages not packaged (use perldoc)

* Sat Feb 19 2005 ALT QA Team Robot <qa-robot@altlinux.org> 1.06-alt2.1
- Rebuilt with rpm-build-perl-0.5.1.

* Fri Jul 30 2004 Alexey Tourbin <at@altlinux.ru> 1.06-alt2
- resurrected; revamped specfile
- mdk-sv_isa.patch: fix build
- updated description

* Fri Nov  9 2001 Igor Homyakov <homyakov@altlinux.ru> alt1 
- Build package for ALTLinux 
