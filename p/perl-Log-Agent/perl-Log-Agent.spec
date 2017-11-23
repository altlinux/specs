%define _unpackaged_files_terminate_build 1
%define module_name Log-Agent

Name: perl-%module_name
Version: 1.003
Release: alt1

Summary: %module_name module for perl
License: Artistic
Group: Development/Perl

Url: %CPAN %module_name
Source0: http://www.cpan.org/authors/id/M/MR/MROGASKI/%{module_name}-%{version}.tar.gz

# Automatically added by buildreq on Fri May 21 2010 (-bi)
BuildRequires: perl-MailTools perl-devel sendmail-common

BuildArch: noarch

%description
Log::Agent is a general logging framework aimed at reusable modules. Instead
of having modules insist on using their own logging reporting (by hardwiring
calls to warn() or syslog()) which can conflict with the final application's
choice, one may use logwarn() for instance to emit a warning.

%prep
%setup -q -n %{module_name}-%{version}

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc README CHANGELOG.md
%perl_vendor_privlib/Log*
%perl_vendor_privlib/auto/Log*

%changelog
* Thu Nov 23 2017 Igor Vlasenko <viy@altlinux.ru> 1.003-alt1
- automated CPAN update

* Wed Nov 01 2017 Igor Vlasenko <viy@altlinux.ru> 1.002-alt1
- automated CPAN update

* Mon Dec 07 2015 Igor Vlasenko <viy@altlinux.ru> 1.001-alt1
- automated CPAN update

* Tue Sep 24 2013 Igor Vlasenko <viy@altlinux.ru> 1.000-alt1
- automated CPAN update

* Tue Sep 11 2012 Vladimir Lettiev <crux@altlinux.ru> 0.307-alt3
- fixed build with perl-5.16

* Mon Nov 22 2010 Igor Vlasenko <viy@altlinux.ru> 0.307-alt2.1
- repair after perl 5.12 upgrade using girar-nmu

* Fri May 21 2010 Victor Forsiuk <force@altlinux.org> 0.307-alt2
- This package is really noarch.

* Thu Jun 14 2007 Victor Forsyuk <force@altlinux.org> 0.307-alt1
- 0.307

* Sat Feb 19 2005 ALT QA Team Robot <qa-robot@altlinux.org> 0.306-alt2.1
- Rebuilt with rpm-build-perl-0.5.1.

* Sun Nov 28 2004 Maxim Tkachenko <tma@altlinux.ru> 0.306-alt2
- rebuild for fix error

* Tue May 25 2004 Maxim Tkachenko <tma@altlinux.ru> 0.306-alt1
- build for AltLinux
