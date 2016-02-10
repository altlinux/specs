%define _unpackaged_files_terminate_build 1
%define module Net-OpenID-Common

Name: perl-%module
Version: 1.20
Release: alt1

Summary: Libraries shared between Net::OpenID::Consumer and Net::OpenID::Server
License: Perl
Group: Development/Perl

Url: %CPAN %module
Source: http://www.cpan.org/authors/id/W/WR/WROG/Net-OpenID-Common-%{version}.tar.gz

BuildArch: noarch

# Automatically added by buildreq on Fri Mar 09 2012
BuildRequires: perl-Crypt-DH-GMP perl-HTTP-Message perl-Math-BigInt perl-XML-Simple perl-devel perl-HTML-Parser

%description
Libraries shared between Net::OpenID::Consumer and Net::OpenID::Server.

%prep
%setup -n %module-%version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%perl_vendor_privlib/Net/OpenID/

%changelog
* Wed Feb 10 2016 Igor Vlasenko <viy@altlinux.ru> 1.20-alt1
- automated CPAN update

* Tue Oct 07 2014 Igor Vlasenko <viy@altlinux.ru> 1.19-alt1
- automated CPAN update

* Thu Sep 12 2013 Igor Vlasenko <viy@altlinux.ru> 1.18-alt1
- automated CPAN update

* Wed Jul 24 2013 Igor Vlasenko <viy@altlinux.ru> 1.17-alt1
- automated CPAN update

* Fri Apr 12 2013 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1.14-alt2
- build fixed

* Fri Mar 09 2012 Victor Forsiuk <force@altlinux.org> 1.14-alt1
- Initial build.
