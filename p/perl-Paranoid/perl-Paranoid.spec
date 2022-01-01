%define _unpackaged_files_terminate_build 1
%define module Paranoid
%define intmodule Paranoid
%define m_name Paranoid

Name: perl-%module
Version: 2.09
Release: alt1

Summary: More secure programming in Perl
License: GPLv2+
Group: Development/Perl
BuildArch: noarch
Url: %CPAN %module
Packager: Sergei Epiphanov <serpiph@altlinux.ru>

Source0: http://www.cpan.org/authors/id/C/CO/CORLISS/%{module}/Paranoid-%{version}.tar.gz

# Automatically added by buildreq on Mon Oct 06 2003
BuildRequires: perl-devel perl(BerkeleyDB.pm) perl(Net/SMTP.pm) perl(Unix/Syslog.pm) perl(CGI.pm)

%description
The Paranoid::* series of modules are intended enforce safer programming by
providing functions that perform more sanity checks as well as enforcing taint
mode.

%prep
%setup -q -n %{module}-%{version}

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc README CHANGELOG CREDITS
%perl_vendor_privlib/Paranoid*

%changelog
* Sat Jan 01 2022 Igor Vlasenko <viy@altlinux.org> 2.09-alt1
- automated CPAN update

* Wed Jan 06 2021 Igor Vlasenko <viy@altlinux.ru> 2.08-alt1
- automated CPAN update

* Tue Apr 23 2019 Igor Vlasenko <viy@altlinux.ru> 2.07-alt1
- automated CPAN update

* Wed Aug 08 2018 Igor Vlasenko <viy@altlinux.ru> 2.06-alt1
- automated CPAN update

* Sat Mar 25 2017 Igor Vlasenko <viy@altlinux.ru> 2.05-alt1
- automated CPAN update

* Sun Sep 25 2016 Igor Vlasenko <viy@altlinux.ru> 2.04-alt1
- automated CPAN update

* Tue Sep 20 2016 Igor Vlasenko <viy@altlinux.ru> 2.03-alt1
- automated CPAN update

* Sun Jul 03 2016 Igor Vlasenko <viy@altlinux.ru> 2.01-alt1
- automated CPAN update

* Thu May 26 2016 Igor Vlasenko <viy@altlinux.ru> 2.00-alt1
- automated CPAN update

* Mon Nov 22 2010 Igor Vlasenko <viy@altlinux.ru> 0.20-alt1.1
- repair after perl 5.12 upgrade using girar-nmu

* Thu Dec 18 2008 Sergei Epiphanov <serpiph@altlinux.ru> 0.20-alt1
- Built for Sisyphus
