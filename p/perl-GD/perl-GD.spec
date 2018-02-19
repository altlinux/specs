%define _unpackaged_files_terminate_build 1
Name: perl-GD
Version: 2.68
Release: alt1
Epoch: 1

Summary: Perl interface to the GD graphics library
License: Perl
Group: Development/Perl

URL: %CPAN GD
Source0: http://www.cpan.org/authors/id/R/RU/RURBAN/GD-%{version}.tar.gz
Patch: GD-2.66-GD.t-fonts.patch

Conflicts: perl-GD1
Provides: perl-GD2 = %version
Obsoletes: perl-GD2 < %version

# Automatically added by buildreq on Sun Oct 09 2011
BuildRequires: libgd2-devel perl-Math-Complex perl-devel perl-podlators perl(Module/Build.pm) perl(ExtUtils/PkgConfig.pm)

%description
This is a autoloadable interface module for GD, a popular library for creating
and manipulating PNG files. With this library you can create PNG images on the
fly or modify existing files.

%prep
%setup -q -n GD-%{version}
%patch -p1

# do not override default CCFLAGS
sed -i- '/CCFLAGS/d' Makefile.PL

%build
%perl_vendor_build

%install
%perl_vendor_install

#rm %buildroot%_bindir/bdf2gdfont.PLS
#rm %buildroot%_man1dir/bdf2gdfont.PLS.*

%files
%doc README* demos bdf_scripts ChangeLog
%_bindir/bdf2gdfont.pl
%_man1dir/bdf2gdfont.*
# for older libgd - not installed by default
#%_bindir/bdftogd
#%_bindir/cvtbdf.pl
%perl_vendor_archlib/GD*
%perl_vendor_autolib/GD
#%perl_vendor_archlib/qd.pl

%changelog
* Mon Feb 19 2018 Igor Vlasenko <viy@altlinux.ru> 1:2.68-alt1
- automated CPAN update

* Fri Dec 15 2017 Igor Vlasenko <viy@altlinux.ru> 1:2.67-alt1.1
- rebuild with new perl 5.26.1

* Thu Nov 23 2017 Igor Vlasenko <viy@altlinux.ru> 1:2.67-alt1
- automated CPAN update

* Tue May 09 2017 Igor Vlasenko <viy@altlinux.ru> 1:2.66-alt1
- automated CPAN update

* Fri Feb 03 2017 Igor Vlasenko <viy@altlinux.ru> 1:2.56-alt1.1.1
- rebuild with new perl 5.24.1

* Wed Nov 25 2015 Igor Vlasenko <viy@altlinux.ru> 1:2.56-alt1.1
- rebuild with new perl 5.22.0

* Tue Dec 16 2014 Igor Vlasenko <viy@altlinux.ru> 1:2.56-alt1
- automated CPAN update

* Tue Dec 09 2014 Igor Vlasenko <viy@altlinux.ru> 1:2.53-alt1.1
- rebuild with new perl 5.20.1

* Wed Apr 02 2014 Igor Vlasenko <viy@altlinux.ru> 1:2.53-alt1
- automated CPAN update

* Thu Feb 20 2014 Igor Vlasenko <viy@altlinux.ru> 1:2.52-alt1
- automated CPAN update

* Wed Feb 05 2014 Igor Vlasenko <viy@altlinux.ru> 1:2.51-alt1
- automated CPAN update

* Wed Aug 28 2013 Vladimir Lettiev <crux@altlinux.ru> 1:2.50-alt2
- built for perl 5.18

* Wed Jul 24 2013 Igor Vlasenko <viy@altlinux.ru> 1:2.50-alt1
- automated CPAN update

* Sat Sep 01 2012 Vladimir Lettiev <crux@altlinux.ru> 1:2.46-alt3
- rebuilt for perl-5.16

* Sun Oct 09 2011 Alexey Tourbin <at@altlinux.ru> 1:2.46-alt2
- rebuilt for perl-5.14

* Sat Aug 13 2011 Victor Forsiuk <force@altlinux.org> 1:2.46-alt1
- 2.46

* Sat Nov 06 2010 Vladimir Lettiev <crux@altlinux.ru> 1:2.44-alt1.1
- rebuilt with perl 5.12

* Fri Dec 25 2009 Victor Forsyuk <force@altlinux.org> 1:2.44-alt1
- 2.44

* Wed Aug 05 2009 Victor Forsyuk <force@altlinux.org> 1:2.41-alt1
- 2.41

* Wed Jun 25 2008 Victor Forsyuk <force@altlinux.org> 1:2.39-alt1
- 2.39

* Tue Oct 02 2007 Victor Forsyuk <force@altlinux.org> 1:2.35-alt2
- Package renamed from perl-GD2 to perl-GD.
- Inactivate test that fails due to patched fonts in our libgd.

* Sat Jan 20 2007 Victor Forsyuk <force@altlinux.org> 1:2.35-alt1
- 2.35

* Mon May 23 2005 DH <dh@altlinux.ru> 1:2.23-alt1
- New version
- Minor changes in spec

* Sun Apr 17 2005 DH <dh@altlinux.ru> 1:2.19-alt1
- New version

* Sat Feb 19 2005 ALT QA Team Robot <qa-robot@altlinux.org> 1:2.18-alt1.1
- Rebuilt with rpm-build-perl-0.5.1.

* Sat Nov 13 2004 DH <dh@altlinux.ru> 1:2.18-alt1
- New version

* Thu Aug 26 2004 DH <dh@altlinux.ru> 1:2.16-alt1
- New version

* Sun Dec 14 2003 DH <dh@altlinux.ru> 2.041-alt4
- Minor changes in spec

* Sun Sep 7 2003 DH <dh@dh.net.ru> 2.041-alt3
- Patch for t/GD.t (Freetype Support test excluded)

* Wed Nov 13 2002 DH <dh@dh.net.ru> 2.041-alt2
- Changes in spec (for perl-5.8.0).

* Wed Nov 6 2002 DH <dh@dh.net.ru> 2.041-alt1
- First release.
