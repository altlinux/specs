%define module_name Email-FolderType

Name: perl-%module_name
Version: 0.814
Release: alt1

Packager: Victor Forsiuk <force@altlinux.org>

Summary: Email::FolderType - determine the type of a mail folder
License: Perl
Group: Development/Perl

Url: %CPAN %module_name
Source: http://www.cpan.org/authors/id/R/RJ/RJBS/Email-FolderType-%{version}.tar.gz

BuildArch: noarch

# Automatically added by buildreq on Thu Feb 18 2010
BuildRequires: perl-Test-Pod perl-Test-Pod-Coverage perl(Capture/Tiny.pm)
BuildRequires: perl-Module-Pluggable

%description
Provides a utility subroutine for detecting the type of a given mail folder.

%prep
%setup -n %module_name-%version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%perl_vendor_privlib/Email

%changelog
* Tue Sep 24 2013 Igor Vlasenko <viy@altlinux.ru> 0.814-alt1
- automated CPAN update

* Thu Nov 25 2010 Igor Vlasenko <viy@altlinux.ru> 0.813-alt1.1
- repair after perl 5.12 upgrade using girar-nmu

* Thu Feb 18 2010 Victor Forsiuk <force@altlinux.org> 0.813-alt1
- Initial build.
