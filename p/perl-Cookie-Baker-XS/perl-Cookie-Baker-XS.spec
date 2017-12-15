%define _unpackaged_files_terminate_build 1
# BEGIN SourceDeps(oneline):
BuildRequires: libsowing-devel perl(CPAN/Meta.pm) perl(CPAN/Meta/Prereqs.pm) perl(Exporter.pm) perl(Module/Build.pm) perl(Test/More.pm) perl(XSLoader.pm) perl(base.pm)
# END SourceDeps(oneline)
%define module_name Cookie-Baker-XS
BuildRequires: rpm-build-perl perl-devel perl-podlators

Name: perl-%module_name
Version: 0.08
Release: alt1.1
Summary: boost Cookie::Baker's crush_cookie
Group: Development/Perl
License: perl
URL: https://github.com/kazeburo/Cookie-Baker-XS

Source0: http://www.cpan.org/authors/id/K/KA/KAZEBURO/%{module_name}-%{version}.tar.gz

%description
%summary

%prep
%setup -q -n %{module_name}-%{version}

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc Changes LICENSE README.md
%perl_vendor_archlib/C*
%perl_vendor_autolib/*

%changelog
* Fri Dec 15 2017 Igor Vlasenko <viy@altlinux.ru> 0.08-alt1.1
- rebuild with new perl 5.26.1

* Wed Aug 02 2017 Igor Vlasenko <viy@altlinux.ru> 0.08-alt1
- automated CPAN update

* Fri Feb 03 2017 Igor Vlasenko <viy@altlinux.ru> 0.07-alt1.1
- rebuild with new perl 5.24.1

* Sun Sep 25 2016 Igor Vlasenko <viy@altlinux.ru> 0.07-alt1
- automated CPAN update

* Wed Nov 25 2015 Igor Vlasenko <viy@altlinux.ru> 0.06-alt1.1
- rebuild with new perl 5.22.0

* Sun Oct 11 2015 Igor Vlasenko <viy@altlinux.ru> 0.06-alt1
- automated CPAN update

* Tue Dec 09 2014 Igor Vlasenko <viy@altlinux.ru> 0.04-alt1.1
- rebuild with new perl 5.20.1

* Tue Nov 25 2014 Igor Vlasenko <viy@altlinux.ru> 0.04-alt1
- automated CPAN update

* Sun Jun 29 2014 Igor Vlasenko <viy@altlinux.ru> 0.03-alt2
- moved to Sisyphus as dependency

* Fri Mar 07 2014 Igor Vlasenko <viy@altlinux.ru> 0.03-alt1
- initial import by package builder

