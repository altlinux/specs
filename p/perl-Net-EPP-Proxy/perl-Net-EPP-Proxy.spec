%define module Net-EPP-Proxy

Name: perl-%module
Version: 0.04
Release: alt2

Packager: Victor Forsiuk <force@altlinux.org>

Summary: A proxy server for the EPP protocol
License: Perl
Group: Development/Perl

Url: %CPAN %module
Source: http://search.cpan.org/CPAN/authors/id/G/GB/GBROWN/%module-%version.tar.gz
Patch1: perl-Net-EPP-Proxy-0.03-versioncheck.patch

BuildArch: noarch

# Automatically added by buildreq on Tue Jun 15 2010
BuildRequires: perl-Net-EPP perl-Net-Server perl-devel perl(Digest/SHA1.pm)

%description
A proxy server for the EPP protocol.

%prep
%setup -n %module-%version
%patch1 -p1

%build
find lib/Net/EPP -type f -name '*.pm' -print0 |xargs -r0 chmod -x
%perl_vendor_build

%install
%perl_vendor_install

%files
%perl_vendor_privlib/Net/*

%changelog
* Sun Oct 23 2011 Igor Vlasenko <viy@altlinux.ru> 0.04-alt2
- fixed build: added BR: Digest/SHA1.pm

* Mon Nov 22 2010 Igor Vlasenko <viy@altlinux.ru> 0.04-alt1.1
- repair after perl 5.12 upgrade using girar-nmu

* Tue Jun 15 2010 Victor Forsiuk <force@altlinux.org> 0.04-alt1
- 0.04

* Sun Nov 08 2009 Victor Forsyuk <force@altlinux.org> 0.03-alt1
- Initial build.
