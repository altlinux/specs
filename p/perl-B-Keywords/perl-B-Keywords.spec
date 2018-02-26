## SPEC file for Perl module B::Keywords

%define version    1.10
%define release    alt1

Name: perl-B-Keywords
Version: %version
Release: alt1.1

Summary: Perl module with lists of reserved barewords and symbol names

License: %perl_license
Group: Development/Perl

%define real_name B-Keywords
URL: http://search.cpan.org/~jjore/B-Keywords/

Packager: Nikolay A. Fetisov <naf@altlinux.ru>

Source: %real_name-%version.tar
BuildArch: noarch

AutoReqProv: perl, yes
BuildPreReq: rpm-build-licenses perl-devel

%description
Perl module B::Keywords supplies seven arrays of keywords: @Scalars, 
@Arrays, @Hashes, @Filehandles, @Symbols, @Functions and @Barewords.
The @Symbols array includes the contents of each of @Scalars, 
@Arrays, @Hashes and @Filehandles. Similarly, @Barewords adds a few
non-function keywords (like __DATA__, NULL) to the @Functions array.


%prep
%setup -q -n %real_name-%version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc Changes README
%perl_vendor_privlib/B/Keywords*

%changelog
* Mon Nov 22 2010 Igor Vlasenko <viy@altlinux.ru> 1.10-alt1.1
- repair after perl 5.12 upgrade using girar-nmu

* Sun Oct 10 2010 Nikolay A. Fetisov <naf@altlinux.ru> 1.10-alt1
- New version 1.10

* Sat Oct 17 2009 Nikolay A. Fetisov <naf@altlinux.ru> 1.09-alt1
- New version 1.09

* Thu Feb 28 2008 Nikolay A. Fetisov <naf@altlinux.ru> 1.08-alt1
- New version 1.08

* Mon May 07 2007 Nikolay A. Fetisov <naf@altlinux.ru> 1.06-alt1
- Initial build for ALT Linux Sisyphus

