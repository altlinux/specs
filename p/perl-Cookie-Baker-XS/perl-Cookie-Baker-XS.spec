%define _unpackaged_files_terminate_build 1
# BEGIN SourceDeps(oneline):
BuildRequires: libsowing-devel perl(CPAN/Meta.pm) perl(CPAN/Meta/Prereqs.pm) perl(Exporter.pm) perl(Module/Build.pm) perl(Test/More.pm) perl(XSLoader.pm) perl(base.pm)
# END SourceDeps(oneline)
%define module_name Cookie-Baker-XS
BuildRequires: rpm-build-perl perl-devel perl-podlators

Name: perl-%module_name
Version: 0.12
Release: alt1
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
%doc Changes README.md
%perl_vendor_archlib/C*
%perl_vendor_autolib/*

%changelog
* Thu Apr 07 2022 Igor Vlasenko <viy@altlinux.org> 0.12-alt1
- automated CPAN update

* Mon Jun 17 2019 Igor Vlasenko <viy@altlinux.ru> 0.11-alt1
- automated CPAN update

* Thu Jan 24 2019 Igor Vlasenko <viy@altlinux.ru> 0.10-alt1.1
- rebuild with new perl 5.28.1

* Mon Oct 08 2018 Igor Vlasenko <viy@altlinux.ru> 0.10-alt1
- automated CPAN update

* Wed Mar 07 2018 Igor Vlasenko <viy@altlinux.ru> 0.09-alt1
- automated CPAN update

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

