## SPEC file for Perl module Net-OAuth

%define real_name  Net-OAuth

Name: perl-Net-OAuth
Version: 0.33
Release: alt1

Summary: Perl module that provides OAuth protocol support

License: %perl_license
Group: Development/Perl
URL: https://metacpan.org/release/Net-OAuth/

Packager: Nikolay A. Fetisov <naf@altlinux.org>

Source: https://cpan.metacpan.org/authors/id/R/RR/RRWO/%real_name-%version.tar
BuildArch: noarch

AutoReqProv: perl, yes
BuildRequires(pre): perl-devel rpm-build-licenses perl-Test-Warn

# Automatically added by buildreq on Sat Nov 08 2025
# optimized out: libgpg-error openssl-config perl perl-CPAN-Meta-Requirements perl-Crypt-OpenSSL-Bignum perl-Encode perl-JSON-PP perl-Parse-CPAN-Meta perl-Sub-Name perl-Sub-Uplevel perl-URI perl-devel perl-parent python-modules python2-base python3 python3-base sh5
BuildRequires: perl-CPAN-Meta perl-Class-Accessor perl-Class-Data-Inheritable perl-Crypt-OpenSSL-RSA perl-Crypt-SysRandom perl-Crypt-URandom perl-Digest-SHA perl-Test-Warn perl-libwww

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
* Thu Oct 15 2026 Vitaly Lipatov <lav@altlinux.ru> 0.33-alt1
- New version 0.33
- Security fixes:
  + CVE-2026-72887: Fix silent downgrade of OAuth 1.0a to OAuth 1.0 in get_request_token.
  + CVE-2026-72888: Fix memory exhaustion via unbounded caching of failed module loads in smart_require.
  + CVE-2026-72889: Fix signature algorithm being chosen by the sender in verify.
  + CVE-2026-75589: Fix non-constant-time signature comparison in verify.
- Added BuildRequires: perl-Crypt-SysRandom (new upstream dependency).

* Wed Nov 12 2025 Nikolay A. Fetisov <naf@altlinux.org> 0.31-alt1
- New version
- Update package URL

* Sat May 12 2018 Nikolay A. Fetisov <naf@altlinux.org> 0.28-alt2
- Fix build with Crypt::OpenSSL::RSA >= 0.30

* Sun Oct 14 2012 Nikolay A. Fetisov <naf@altlinux.ru> 0.28-alt1
- New version

* Mon Nov 22 2010 Igor Vlasenko <viy@altlinux.ru> 0.27-alt1.1
- repair after perl 5.12 upgrade using girar-nmu

* Thu Jul 15 2010 Igor Vlasenko <viy@altlinux.ru> 0.27-alt1
- automated CPAN update

* Tue Mar 09 2010 Nikolay A. Fetisov <naf@altlinux.ru> 0.20-alt1
- Initial build for ALT Linux Sisyphus
