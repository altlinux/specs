%define _unpackaged_files_terminate_build 1
%define module Any-Moose

Name: perl-%module
Version: 0.27
Release: alt1

Packager: Victor Forsiuk <force@altlinux.org>

Summary: Use Moose or Mouse automagically
License: Perl
Group: Development/Perl

Url: %CPAN %module
Source: http://www.cpan.org/authors/id/E/ET/ETHER/Any-Moose-%{version}.tar.gz

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
* Thu Nov 17 2016 Igor Vlasenko <viy@altlinux.ru> 0.27-alt1
- automated CPAN update

* Mon Jan 26 2015 Igor Vlasenko <viy@altlinux.ru> 0.26-alt1
- automated CPAN update

* Thu Jun 26 2014 Igor Vlasenko <viy@altlinux.ru> 0.24-alt1
- automated CPAN update

* Mon Jun 23 2014 Igor Vlasenko <viy@altlinux.ru> 0.22-alt1
- automated CPAN update

* Wed Jul 24 2013 Igor Vlasenko <viy@altlinux.ru> 0.21-alt1
- automated CPAN update

* Mon Sep 24 2012 Igor Vlasenko <viy@altlinux.ru> 0.18-alt1
- automated CPAN update

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
