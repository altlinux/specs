Name: perl-FCGI-Client
Version: 0.08
Release: alt1
Summary: FCGI::Client - client library for fastcgi protocol

Packager: Vladimir Lettiev <crux@altlinux.ru>

Group: Development/Perl
License: Perl
Url: %CPAN FCGI-Client

BuildArch: noarch
Source: %name-%version.tar
BuildRequires: perl-devel perl-Any-Moose perl-Moose

%description
%summary

%prep
%setup -q

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%perl_vendor_privlib/FCGI/Client*
%doc Changes README 

%changelog
* Thu Dec 15 2011 Vladimir Lettiev <crux@altlinux.ru> 0.08-alt1
- New version 0.08

* Sun Feb 06 2011 Vladimir Lettiev <crux@altlinux.ru> 0.06-alt1
- New version 0.06

* Mon Aug 30 2010 Vladimir Lettiev <crux@altlinux.ru> 0.05-alt1
- initial build
