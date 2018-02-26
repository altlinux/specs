%define dist XML-Writer
Name: perl-%dist
Version: 0.612
Release: alt2

Summary: Simple Perl module for writing XML documents
License: distributable
Group: Development/Perl

URL: %CPAN %dist
Source: %dist-%version.tar.gz

BuildArch: noarch

# Automatically added by buildreq on Tue Nov 15 2011
BuildRequires: perl-Test-Pod perl-Test-Pod-Coverage

%description
XML::Writer is a simple Perl module for writing XML documents: it
takes care of constructing markup and escaping data correctly, and by
default, it also performs a significant amount of well-formedness
checking on the output, to make certain (for example) that start and
end tags match, that there is exactly one document element, and that
there are not duplicate attribute names.

%prep
%setup -q -n %dist-%version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc Changes README
%perl_vendor_privlib/XML

%changelog
* Tue Nov 15 2011 Alexey Tourbin <at@altlinux.ru> 0.612-alt2
- rebuilt as plain src.rpm

* Tue Aug 17 2010 Alexey Tourbin <at@altlinux.ru> 0.612-alt1
- 0.610 -> 0.612
- License: distributable ("Redistribution and use in source and compiled forms,
  with or without modification, are permitted under any circumstances.")

* Mon Mar 29 2010 Alexey Tourbin <at@altlinux.ru> 0.610-alt1
- 0.606 -> 0.610
- License: distributable ("Commercial and non-commercial use freely permitted.")

* Wed Jul 22 2009 Alexey Tourbin <at@altlinux.ru> 0.606-alt1
- 0.604 -> 0.606
- License: MIT

* Mon Sep 29 2008 Alexey Tourbin <at@altlinux.ru> 0.604-alt1
- 0.600 -> 0.604

* Sat Sep 24 2005 Alexey Tourbin <at@altlinux.ru> 0.600-alt1
- 0.545 -> 0.600

* Mon May 30 2005 Alexey Tourbin <at@altlinux.ru> 0.545-alt1
- 0.540 -> 0.545

* Thu May 12 2005 Alexey Tourbin <at@altlinux.ru> 0.540-alt1
- 0.531 -> 0.540

* Thu Mar 17 2005 Alexey Tourbin <at@altlinux.ru> 0.531-alt1
- 0.530 -> 0.531

* Wed Feb 02 2005 Alexey Tourbin <at@altlinux.ru> 0.530-alt1
- 0.520 -> 0.530
- manual pages not packaged (use perldoc)

* Wed Sep 08 2004 Alexey Tourbin <at@altlinux.ru> 0.520-alt1
- 0.510 -> 0.520

* Mon Aug 09 2004 Alexey Tourbin <at@altlinux.ru> 0.510-alt1
- 0.500 -> 0.510

* Fri Apr 16 2004 Alexey Tourbin <at@altlinux.ru> 0.500-alt1
- 0.4.6 -> 0.500

* Fri Mar 05 2004 Alexey Tourbin <at@altlinux.ru> 0.4.6-alt1
- 0.4.6

* Tue Feb 24 2004 Alexey Tourbin <at@altlinux.ru> 0.4.2-alt1
- 0.4.2

* Wed Oct 08 2003 Stanislav Ievlev <inger@altlinux.ru> 0.4-alt2.1
- fix building in hasher

* Fri Nov 01 2002 Sergey V Turchin <zerg@altlinux.org> 0.4-alt2
- rebuild with new perl

* Mon Jan 07 2002 Mikhail Zabaluev <mhz@altlinux.ru> 0.4-alt1
- Initial release
