%define _unpackaged_files_terminate_build 1
%define dist Archive-Tar
Name: perl-%dist
Version: 2.24
Release: alt1

Summary: Module for creation and manipulation of tar archives
License: GPL or Artistic
Group: Development/Perl

URL: %CPAN %dist
Source: http://www.cpan.org/authors/id/B/BI/BINGOS/Archive-Tar-%{version}.tar.gz

BuildArch: noarch

# Automatically added by buildreq on Mon Oct 03 2011 (-bi)
BuildRequires: perl-IO-String perl-IO-Zlib perl-Package-Constants perl-Pod-Parser perl-Test-Pod perl-Text-Diff

%description
Archive::Tar provides an object oriented mechanism for handling tar files.
It provides class methods for quick and easy files handling while also
allowing for the creation of tar file objects for custom manipulation.

%prep
%setup -q -n %dist-%version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc CHANGES README
%_bindir/ptar*
%_man1dir/*
%perl_vendor_privlib/Archive

%changelog
* Sun Dec 18 2016 Igor Vlasenko <viy@altlinux.ru> 2.24-alt1
- automated CPAN update

* Thu Nov 17 2016 Igor Vlasenko <viy@altlinux.ru> 2.18-alt1
- automated CPAN update

* Mon Oct 31 2016 Igor Vlasenko <viy@altlinux.ru> 2.14-alt1
- automated CPAN update

* Wed Oct 19 2016 Igor Vlasenko <viy@altlinux.ru> 2.12-alt1
- automated CPAN update

* Fri Jul 29 2016 Igor Vlasenko <viy@altlinux.ru> 2.10-alt1
- automated CPAN update

* Thu May 26 2016 Igor Vlasenko <viy@altlinux.ru> 2.08-alt1
- automated CPAN update

* Tue May 03 2016 Igor Vlasenko <viy@altlinux.ru> 2.06-alt1
- automated CPAN update

* Tue Dec 16 2014 Igor Vlasenko <viy@altlinux.ru> 2.04-alt1
- automated CPAN update

* Mon Sep 15 2014 Igor Vlasenko <viy@altlinux.ru> 2.02-alt1
- automated CPAN update

* Mon Jun 16 2014 Igor Vlasenko <viy@altlinux.ru> 2.00-alt1
- automated CPAN update

* Fri Oct 25 2013 Igor Vlasenko <viy@altlinux.ru> 1.96-alt1
- automated CPAN update

* Wed Jul 24 2013 Igor Vlasenko <viy@altlinux.ru> 1.92-alt1
- automated CPAN update

* Wed Sep 26 2012 Igor Vlasenko <viy@altlinux.ru> 1.90-alt1
- automated CPAN update

* Mon Oct 03 2011 Alexey Tourbin <at@altlinux.ru> 1.78-alt1
- rebuilt as plain src.rpm

* Sat Feb 26 2011 Alexey Tourbin <at@altlinux.ru> 1.76-alt1
- 1.74 -> 1.76

* Tue Dec 28 2010 Alexey Tourbin <at@altlinux.ru> 1.74-alt1
- 1.66 -> 1.74
- packaged %_bindir/ptargrep

* Fri Aug 13 2010 Alexey Tourbin <at@altlinux.ru> 1.66-alt1
- 1.60 -> 1.66

* Tue May 04 2010 Alexey Tourbin <at@altlinux.ru> 1.60-alt1
- 1.58 -> 1.60
- enabled dependency on IO::Compress::Bzip2

* Thu Apr 01 2010 Alexey Tourbin <at@altlinux.ru> 1.58-alt1
- 1.54 -> 1.58

* Wed Sep 23 2009 Alexey Tourbin <at@altlinux.ru> 1.54-alt1
- 1.52 -> 1.54

* Fri Jun 19 2009 Alexey Tourbin <at@altlinux.ru> 1.52-alt1
- 1.46 -> 1.52

* Sun Apr 12 2009 Alexey Tourbin <at@altlinux.ru> 1.46-alt1
- 1.44 -> 1.46

* Fri Feb 27 2009 Alexey Tourbin <at@altlinux.ru> 1.44-alt1
- 1.40 -> 1.44

* Tue Nov 04 2008 Alexey Tourbin <at@altlinux.ru> 1.40-alt1
- 1.38 -> 1.40

* Fri Apr 18 2008 Alexey Tourbin <at@altlinux.ru> 1.38-alt1
- 1.29 -> 1.38

* Sat Mar 25 2006 Andrey Brindeew <abr@altlinux.org> 1.29-alt1
- 1.29 release

* Tue Aug 23 2005 Andrey Brindeew <abr@altlinux.org> 1.26-alt1
- 1.26 release
- perl-PerlIO added to BuildReqs list

* Sun Nov 28 2004 Andrey Brindeew <abr@altlinux.org> 1.22-alt1
- 1.22

* Sun Oct 03 2004 Andrey Brindeew <abr@altlinux.org> 1.10-alt1
- 1.10

* Sat Mar 06 2004 Andrey Brindeew <abr@altlinux.ru> 1.08-alt1
- 1.08

* Mon Nov 24 2003 Andrey Brindeew <abr@altlinux.ru> 1.07-alt1
- 1.07

* Thu Sep 04 2003 Andrey Brindeew <abr@altlinux.ru> 1.05-alt1
- 1.05

* Thu Sep 04 2003 Andrey Brindeew <abr@altlinux.ru> 1.04-alt2
- Syntax checking will be happy now.
- URL was fixed.

* Wed Jul 30 2003 Andrey Brindeew <abr@altlinux.ru> 1.04-alt1
- First build for ALT Linux.

