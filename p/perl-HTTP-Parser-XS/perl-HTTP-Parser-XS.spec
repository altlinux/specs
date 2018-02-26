%define dist HTTP-Parser-XS
Name: perl-%dist
Version: 0.14
Release: alt2

Summary: A fast, primitive HTTP request parser
License: Perl
Group: Development/Perl

URL: %CPAN %dist
Source: %dist-%version.tar.gz

# Automatically added by buildreq on Tue Oct 11 2011
BuildRequires: perl-Module-Install

%description
HTTP::Parser::XS is a fast, primitive HTTP request parser that can be
used either for writing a synchronous HTTP server or a event-driven
server.

%prep
%setup -q -n %dist-%version
#rm -rv inc/

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc Changes README 
%perl_vendor_archlib/HTTP
%perl_vendor_autolib/HTTP

%changelog
* Tue Oct 11 2011 Alexey Tourbin <at@altlinux.ru> 0.14-alt2
- rebuilt for perl-5.14

* Thu Sep 22 2011 Igor Vlasenko <viy@altlinux.ru> 0.14-alt1
- automated CPAN update

* Sun Dec 12 2010 Vladimir Lettiev <crux@altlinux.ru> 0.13-alt1
- New version 0.13

* Wed Nov 17 2010 Vladimir Lettiev <crux@altlinux.ru> 0.12-alt1
- New version 0.12

* Sat Nov 06 2010 Vladimir Lettiev <crux@altlinux.ru> 0.09-alt1.1
- rebuilt with perl 5.12

* Sun Sep 12 2010 Vladimir Lettiev <crux@altlinux.ru> 0.09-alt1
- New version 0.09

* Mon Aug 30 2010 Vladimir Lettiev <crux@altlinux.ru> 0.07-alt1
- initial build
