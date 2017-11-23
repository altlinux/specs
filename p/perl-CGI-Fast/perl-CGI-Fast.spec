%define _unpackaged_files_terminate_build 1
# BEGIN SourceDeps(oneline):
BuildRequires: perl(CGI.pm) perl(ExtUtils/MakeMaker.pm) perl(FCGI.pm) perl(Test/More.pm) perl(if.pm) perl(Test/Deep.pm)
# END SourceDeps(oneline)
%define module_name CGI-Fast
BuildRequires: rpm-build-perl perl-devel perl-podlators

Name: perl-%module_name
Version: 2.13
Release: alt1
Summary: CGI::Fast is a subclass of the CGI object created by CGI.pm
Group: Development/Perl
License: perl
URL: https://metacpan.org/module/CGI::Fast

Source0: http://www.cpan.org/authors/id/L/LE/LEEJO/%{module_name}-%{version}.tar.gz
BuildArch: noarch

%description
CGI::Fast is a subclass of the CGI object created by CGI.pm.  It is
specialized to work well FCGI module, which greatly speeds up CGI
scripts by turning them into persistently running server processes.
Scripts that perform time-consuming initialization processes, such as
loading large modules or opening persistent database connections, will
see large performance improvements.


%prep
%setup -q -n %{module_name}-%{version}

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc README Changes README.md
%perl_vendor_privlib/C*

%changelog
* Thu Nov 23 2017 Igor Vlasenko <viy@altlinux.ru> 2.13-alt1
- automated CPAN update

* Mon Sep 25 2017 Igor Vlasenko <viy@altlinux.ru> 2.12-alt2
- fixed Summary (closes: #33638)

* Wed Nov 30 2016 Igor Vlasenko <viy@altlinux.ru> 2.12-alt1
- automated CPAN update

* Sat Nov 19 2016 Igor Vlasenko <viy@altlinux.ru> 2.11-alt1
- automated CPAN update

* Sun Oct 11 2015 Igor Vlasenko <viy@altlinux.ru> 2.10-alt1
- automated CPAN update

* Wed Apr 01 2015 Igor Vlasenko <viy@altlinux.ru> 2.09-alt1
- automated CPAN update

* Tue Dec 16 2014 Igor Vlasenko <viy@altlinux.ru> 2.05-alt1
- automated CPAN update

* Mon Oct 20 2014 Igor Vlasenko <viy@altlinux.ru> 2.04-alt1
- automated CPAN update

* Tue Sep 09 2014 Igor Vlasenko <viy@altlinux.ru> 2.03-alt1
- automated CPAN update

* Tue Jun 10 2014 Igor Vlasenko <viy@altlinux.ru> 2.02-alt1
- automated CPAN update

* Tue Jun 03 2014 Igor Vlasenko <viy@altlinux.ru> 2.00-alt2
- moved to Sisyphus as dependency

* Mon May 26 2014 Igor Vlasenko <viy@altlinux.ru> 2.00-alt1
- initial import by package builder

