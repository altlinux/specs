%define module Any-Moose

Name: perl-%module
Version: 0.17
Release: alt1

Packager: Victor Forsiuk <force@altlinux.org>

Summary: Use Moose or Mouse automagically
License: Perl
Group: Development/Perl

Url: %CPAN %module
Source: http://www.cpan.org/authors/id/S/SA/SARTAK/Any-Moose-0.17.tar.gz

BuildArch: noarch

# Automatically added by buildreq on Fri Aug 27 2010
BuildRequires: perl-Moose perl-Mouse

%description
Any::Moose - use Moose or Mouse modules.

%prep
%setup -n %module-%version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%perl_vendor_privlib/Any

%changelog
* Mon Sep 19 2011 Igor Vlasenko <viy@altlinux.ru> 0.17-alt1
- automated CPAN update

* Mon Nov 22 2010 Igor Vlasenko <viy@altlinux.ru> 0.13-alt2.1
- repair after perl 5.12 upgrade using girar-nmu

* Fri Aug 27 2010 Victor Forsiuk <force@altlinux.org> 0.13-alt2
- Fix wrong description.

* Tue Jul 13 2010 Igor Vlasenko <viy@altlinux.ru> 0.13-alt1
- automated CPAN update

* Thu Oct 15 2009 Victor Forsyuk <force@altlinux.org> 0.10-alt1
- Initial build.
