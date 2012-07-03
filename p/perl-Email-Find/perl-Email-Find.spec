%define module		Email-Find
%define m_distro	Email-Find
%define m_name		Email::Find
%define m_author_id	TATSUHIKO
Name: perl-%module
Version: 0.10
Release: alt1.1

Summary: Email::Find - Find RFC 822 email addresses in plain text
Group: Development/Perl
License: Unknown

Packager: Vitaly Lipatov <lav@altlinux.ru>

Url: http://search.cpan.org/dist/%m_distro/
Source: %m_distro-%version.tar.gz

BuildArch: noarch

# Automatically added by buildreq on Tue Apr 27 2010
BuildRequires: perl-Email-Valid perl-devel

%description
Email::Find is a module for finding a subset of RFC 822
email addresses in arbitrary text (see "CAVEATS"). The addresses it
finds are not guaranteed to exist or even actually be email addresses at
all (see "CAVEATS"), but they will be valid RFC 822 syntax.
Email::Find will perform some heuristics to avoid some of the more obvious
red herrings and false addresses, but there's only so much which can be
done without a human.

%prep
%setup -q -n %m_distro-%version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%perl_vendor_privlib/Email*
%doc README Changes

%changelog
* Mon Nov 22 2010 Igor Vlasenko <viy@altlinux.ru> 0.10-alt1.1
- repair after perl 5.12 upgrade using girar-nmu

* Tue Apr 27 2010 Alexey Tourbin <at@altlinux.ru> 0.10-alt1
- 0.09 -> 0.10

* Sat Sep 06 2008 Vitaly Lipatov <lav@altlinux.ru> 0.09-alt2
- fix directory ownership violation

* Sun Feb 27 2005 Vitaly Lipatov <lav@altlinux.ru> 0.09-alt1
- first build for ALT Linux Sisyphus
