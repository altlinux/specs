%define module Mail-GnuPG

Name: perl-%module
Version: 0.17
Release: alt1

Summary: Process email with GPG
License: Perl
Group: Development/Perl

BuildArch: noarch

Url: %CPAN %module
Source: http://search.cpan.org/CPAN/authors/id/D/DD/DDB/Mail-GnuPG-%version.tar.gz

# Automatically added by buildreq on Fri Dec 17 2010
BuildRequires: gnupg perl-GnuPG-Interface perl-MIME-tools perl-Module-Build perl-Mouse perl-Test-Pod

%description
Use GnuPG::Interface to process or create PGP signed or encrypted email.

%prep
%setup -n %module-%version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%perl_vendor_privlib/Mail

%changelog
* Sun Jan 15 2012 Victor Forsiuk <force@altlinux.org> 0.17-alt1
- 0.17

* Fri Dec 17 2010 Victor Forsiuk <force@altlinux.org> 0.16-alt1
- 0.16

* Mon Nov 22 2010 Igor Vlasenko <viy@altlinux.ru> 0.15-alt1.1
- repair after perl 5.12 upgrade using girar-nmu

* Thu Oct 15 2009 Victor Forsyuk <force@altlinux.org> 0.15-alt1
- Initial build.
