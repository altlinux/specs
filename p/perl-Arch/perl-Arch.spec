%define dist Arch
Name: perl-%dist
Version: 0.5.2
Release: alt1

Summary: GNU Arch Perl library
License: GPL
Group: Development/Perl

URL: %CPAN %dist
Source: %dist-%version.tar.gz

Requires: tla >= 1.2

BuildArch: noarch

# Automatically added by buildreq on Wed Apr 27 2011
BuildRequires: perl-Test-Pod perl-Test-Pod-Coverage tla

%description
The Arch-Perl library allows Perl developers to create GNU Arch front-ends
in an object oriented fashion. GNU Arch is a decentralized, changeset-oriented
revision control system.

%prep
%setup -q -n %dist-%version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc NEWS README
%perl_vendor_privlib/Arch*

%changelog
* Wed Apr 27 2011 Alexey Tourbin <at@altlinux.ru> 0.5.2-alt1
- 0.5.1 -> 0.5.2
- fixed unpackaged directory

* Mon Nov 22 2010 Igor Vlasenko <viy@altlinux.ru> 0.5.1-alt1.1
- repair after perl 5.12 upgrade using girar-nmu

* Tue Oct 11 2005 Alexey Voinov <voins@altlinux.ru> 0.5.1-alt1
- new version (0.5.1)

* Tue Apr 26 2005 Alexey Voinov <voins@altlinux.ru> 0.5.0-alt1
- new version (0.5.0)

* Mon Jan 31 2005 Alexey Voinov <voins@altlinux.ru> 0.4.1-alt1
- initial build.
