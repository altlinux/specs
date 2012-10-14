## SPEC file for Perl module Net-Twitter-Lite

%define real_name  Net-Twitter-Lite

Name: perl-Net-Twitter-Lite
Version: 0.11002
Release: alt1

Summary: a Perl interface to the Twitter API

License: %artistic_license
Group: Development/Perl
URL: http://search.cpan.org/dist/Net-Twitter-Lite/

Packager: Nikolay A. Fetisov <naf@altlinux.ru>

Source: %real_name-%version.tar
BuildArch: noarch

AutoReqProv: perl, yes
BuildRequires(pre): perl-devel rpm-build-licenses

# Automatically added by buildreq on Sun Oct 14 2012
# optimized out: perl-Class-Accessor perl-Class-Data-Inheritable perl-Devel-Symdump perl-Digest-HMAC perl-Digest-SHA perl-Encode perl-Encode-Locale perl-HTTP-Date perl-HTTP-Message perl-JSON-XS perl-Pod-Coverage perl-Pod-Escapes perl-Pod-Parser perl-Sub-Name perl-URI perl-common-sense perl-devel perl-libnet
BuildRequires: perl-Crypt-SSLeay perl-JSON perl-Memoize perl-Net-OAuth perl-Test-Pod-Coverage perl-libwww

%description
This module provides a perl interface to the Twitter APIs. It uses the
same API definitions as Net::Twitter, but without the extra bells and
whistles and without the additional dependencies. Same great taste, less
filling.

This module is related to, but is not part of the "Net::Twitter"
distribution. It's API methods and API method documentation are
generated from "Net::Twitter"'s internals. It exists for those who
cannot, or prefer not to install Moose and its dependencies.

You should consider upgrading to "Net::Twitter" for additional
functionality, finer grained control over features, full backwards
compatibility with older versions of "Net::Twitter", and additional
error handling options.

%prep
%setup  -n %real_name-%version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc README Changes
%perl_vendor_privlib/Net/Twitter/Lite*

%changelog
* Sun Oct 14 2012 Nikolay A. Fetisov <naf@altlinux.ru> 0.11002-alt1
- New version

* Mon Nov 22 2010 Igor Vlasenko <viy@altlinux.ru> 0.08006-alt1.1
- repair after perl 5.12 upgrade using girar-nmu

* Tue Mar 09 2010 Nikolay A. Fetisov <naf@altlinux.ru> 0.08006-alt1
- Initial build for ALT Linux Sisyphus
