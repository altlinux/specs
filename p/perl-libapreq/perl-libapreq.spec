Name: perl-libapreq
Version: 1.34
Release: alt1.2

Summary: Apache Request C Library, primary for working with mod_perl
License: Apache Software Licence v. 2.0
Group: Development/Perl

URL: http://search.cpan.org/dist/libapreq/
Source: libapreq-%version.tar.gz

BuildRequires: apache-mod_perl
BuildRequires: perl-devel

%description
libapreq  -  Apache Request C Library, with 3 mod_perl modules:
Apache::Cookie, for working with HTTP Cookies, Apache::Request,
with methods for dealing with client request data and
Apache::libapreq, with general interface to C library.

%prep
%setup -q -n libapreq-%version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc Changes README eg
%perl_vendor_archlib/Apache
%perl_vendor_autolib/Apache
%perl_vendor_archlib/libapreq*
%perl_vendor_autolib/libapreq

%changelog
* Wed Oct 19 2011 Alexey Tourbin <at@altlinux.ru> 1.34-alt1.2
- rebuilt for perl-5.14

* Sun Nov 07 2010 Vladimir Lettiev <crux@altlinux.ru> 1.34-alt1.1
- rebuilt with perl 5.12

* Sat Oct 17 2009 Nikolay A. Fetisov <naf@altlinux.ru> 1.34-alt1
- New version 1.34

* Mon Dec 15 2008 Nikolay A. Fetisov <naf@altlinux.ru> 1.33-alt3
- Fix requirements on apache-mod_perl

* Fri Aug 10 2007 Nikolay A. Fetisov <naf@altlinux.ru> 1.33-alt2
- Fix typo in package description

* Mon Jan 8 2007 Nikolay A. Fetisov <naf@altlinux.ru> 1.33-alt1
- Initial build for ALT Linux Sisyphus

* Sat Sep 16 2006 Nikolay A. Fetisov <naf@altlinux.ru> 1.33-alt0
- New version 1.33

* Thu Jan 08 2004 Nikolay A. Fetisov <naf@ssc.ru> 1.3-ssc1
- Moving to 1.3

* Sat Nov 09 2002 Nikolay Fetisov <naf@ssc.ru> 1.0-ssc1
- First build
