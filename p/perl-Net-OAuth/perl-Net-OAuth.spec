## SPEC file for Perl module Net-OAuth

%define real_name  Net-OAuth

Name: perl-Net-OAuth
Version: 0.27
Release: alt1.1

Summary: Perl module that provides OAuth protocol support

License: %perl_license
Group: Development/Perl
URL: http://search.cpan.org/~kgrennan/Net-OAuth/

Packager: Nikolay A. Fetisov <naf@altlinux.ru>

Source: http://search.cpan.org/CPAN/authors/id/K/GR/KGRENNAN/%real_name-%version.tar
BuildArch: noarch

AutoReqProv: perl, yes
BuildRequires(pre): perl-devel rpm-build-licenses perl-Test-Warn

# Automatically added by buildreq on Tue Mar 09 2010
BuildRequires: perl-Class-Accessor perl-Class-Data-Inheritable perl-Digest-HMAC perl-Module-Build perl-UNIVERSAL-require perl-URI

%description
Perl module Net::OAuth is an implementation of the OAuth protocol.

OAuth is an open protocol to allow secure API authentication in a 
simple and standard method from desktop and web applications, see
http://oauth.net/ for details.

%prep
%setup  -n %real_name-%version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc README Changes
%perl_vendor_privlib/Net/OAuth*

%changelog
* Mon Nov 22 2010 Igor Vlasenko <viy@altlinux.ru> 0.27-alt1.1
- repair after perl 5.12 upgrade using girar-nmu

* Thu Jul 15 2010 Igor Vlasenko <viy@altlinux.ru> 0.27-alt1
- automated CPAN update

* Tue Mar 09 2010 Nikolay A. Fetisov <naf@altlinux.ru> 0.20-alt1
- Initial build for ALT Linux Sisyphus
