%define dist String-CRC
Name: perl-%dist
Version: 1.0
Release: alt1.2

Summary: Cyclic redundency check generation
License: Public Domain
Group: Development/Perl

URL: %CPAN %dist
Source: %dist-%version.tar.gz

# Automatically added by buildreq on Sat Oct 08 2011
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
	%perl_vendor_archlib/String/CRC.pm
%doc	%perl_vendor_archlib/String/CRC.pod
	%perl_vendor_autolib/String

%changelog
* Sat Oct 08 2011 Alexey Tourbin <at@altlinux.ru> 1.0-alt1.2
- rebuilt for perl-5.14

* Sun Nov 07 2010 Vladimir Lettiev <crux@altlinux.ru> 1.0-alt1.1
- rebuilt with perl 5.12

* Wed Jul 01 2009 Grigory Milev <week@altlinux.ru> 1.0-alt1
- Initial build for ALT Linux distribution.
