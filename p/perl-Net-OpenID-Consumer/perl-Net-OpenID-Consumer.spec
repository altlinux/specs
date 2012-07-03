%define module Net-OpenID-Consumer

Name: perl-%module
Version: 1.13
Release: alt1

Summary: Library for consumers of OpenID identities
License: Perl
Group: Development/Perl

Url: %CPAN %module
Source: http://www.cpan.org/modules/by-module/Net/%module-%version.tar.gz

BuildArch: noarch

# Automatically added by buildreq on Fri Mar 09 2012
BuildRequires: perl-CGI perl-Digest-SHA perl-JSON perl-Net-OpenID-Common perl-devel perl-libwww

%description
This is the Perl API for (the consumer half of) OpenID, a distributed identity
system based on proving you own a URL, which is then your identity.

%prep
%setup -n %module-%version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%perl_vendor_privlib/Net/OpenID/

%changelog
* Fri Mar 09 2012 Victor Forsiuk <force@altlinux.org> 1.13-alt1
- 1.13

* Mon Nov 22 2010 Igor Vlasenko <viy@altlinux.ru> 1.03-alt1.1
- repair after perl 5.12 upgrade using girar-nmu

* Sun Nov 08 2009 Victor Forsyuk <force@altlinux.org> 1.03-alt1
- 1.03

* Tue Oct 07 2008 Igor Vlasenko <viy@altlinux.ru> 0.14-alt1.1
- NMU: fix for perlarchdir ownership

* Sat May 03 2008 Igor Zubkov <icesik@altlinux.org> 0.14-alt1
- first build for ALT Linux Sisyphus
