%define dist XML-Dumper
Name: perl-%dist
Version: 0.81
Release: alt2

Summary: Perl module for dumping Perl objects from/to XML
License: GPL
Group: Development/Perl

URL: %CPAN %dist
Source: %dist-%version.tar.gz

BuildArch: noarch

# Automatically added by buildreq on Tue Oct 04 2011
BuildRequires: perl-IO-Compress perl-XML-Parser perl-devel

%description
XML::Dumper dumps Perl data to a structured XML format.
XML::Dumper can also read XML data that was previously dumped
by the module and convert it back to Perl.

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
* Tue Oct 04 2011 Alexey Tourbin <at@altlinux.ru> 0.81-alt2
- rebuilt

* Tue Aug 12 2008 Alexey Tourbin <at@altlinux.ru> 0.81-alt1
- 0.79 -> 0.81

* Sat Sep 24 2005 Alexey Tourbin <at@altlinux.ru> 0.79-alt1
- 0.75 -> 0.79

* Wed Jun 29 2005 Alexey Tourbin <at@altlinux.ru> 0.75-alt1
- 0.73 -> 0.75

* Fri Jun 03 2005 Alexey Tourbin <at@altlinux.ru> 0.73-alt1
- 0.71 -> 0.73
- alt-req-zlib.patch: clarified dependency on Compress::Zlib
- manual pages not packaged (use perldoc)

* Sat Feb 19 2005 ALT QA Team Robot <qa-robot@altlinux.org> 0.71-alt1.1
- Rebuilt with rpm-build-perl-0.5.1.

* Tue Mar 16 2004 Alexey Tourbin <at@altlinux.ru> 0.71-alt1
- 0.67 -> 0.71

* Thu Sep 04 2003 Alexey Tourbin <at@altlinux.ru> 0.67-alt1
- updated from 0.4 (20 Jun 1999) to 0.67 (19 Aug 2003)

* Mon Nov 04 2002 Stanislav Ievlev <inger@altlinux.ru> 0.4-alt2
- rebuild with new perl

* Thu Aug 09 2001 Stanislav Ievlev <inger@altlinux.ru> 0.4-alt1
- Adopted for ALT. We need it for foomatic too.

* Thu Jun 21 2001 Christian Belisle <cbelisle@mandrakesoft.com> 0.4-3mdk
- Fixed an error in changelog.

* Thu Jun 21 2001 Christian Belisle <cbelisle@mandrakesoft.com> 0.4-2mdk
- Clean up spec.
- Fixed distribution tag.
- Needed by eGrail.

* Mon Jun 18 2001 Till Kamppeter <till@mandrakesoft.com> 0.4-1mdk
- Newly introduced for Foomatic.
