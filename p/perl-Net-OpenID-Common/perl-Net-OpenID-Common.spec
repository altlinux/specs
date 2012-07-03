%define module Net-OpenID-Common

Name: perl-%module
Version: 1.14
Release: alt1

Summary: Libraries shared between Net::OpenID::Consumer and Net::OpenID::Server
License: Perl
Group: Development/Perl

Url: %CPAN %module
Source: http://www.cpan.org/modules/by-module/Net/%module-%version.tar.gz

BuildArch: noarch

# Automatically added by buildreq on Fri Mar 09 2012
BuildRequires: perl-Crypt-DH-GMP perl-HTTP-Message perl-Math-BigInt perl-XML-Simple perl-devel

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
* Fri Mar 09 2012 Victor Forsiuk <force@altlinux.org> 1.14-alt1
- Initial build.
