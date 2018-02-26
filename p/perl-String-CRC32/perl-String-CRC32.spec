%define dist String-CRC32
Name: perl-%dist
Version: 1.4
Release: alt1.2

Summary: Cyclic redundency check generation
License: Public Domain
Group: Development/Perl

URL: %CPAN %dist
Source: %dist-%version.tar.gz

# Automatically added by buildreq on Fri Oct 07 2011
BuildRequires: perl-devel

%description
This packages provides a perl module to generate checksums from strings
and from files.

%prep
%setup -q -n %dist-%version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc	README
%dir	%perl_vendor_archlib/String
	%perl_vendor_archlib/String/CRC32.pm
%doc	%perl_vendor_archlib/String/CRC32.pod
	%perl_vendor_autolib/String

%changelog
* Fri Oct 07 2011 Alexey Tourbin <at@altlinux.ru> 1.4-alt1.2
- rebuilt for perl-5.14

* Sun Nov 07 2010 Vladimir Lettiev <crux@altlinux.ru> 1.4-alt1.1
- rebuilt with perl 5.12

* Tue Dec 16 2008 Alexey Tourbin <at@altlinux.ru> 1.4-alt1
- 1.2 -> 1.4

* Sat Feb 19 2005 ALT QA Team Robot <qa-robot@altlinux.org> 1.2-alt2.1
- Rebuilt with rpm-build-perl-0.5.1.

* Tue Nov 05 2002 Stanislav Ievlev <inger@altlinux.ru> 1.2-alt2
- rebuild with new perl

* Tue Oct  9 2001 Grigory Milev <week@altlinux.ru> 1.2-alt1
- Initial build for ALT Linux distribution.
