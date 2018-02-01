%define _unpackaged_files_terminate_build 1
%define module_name JSON-MaybeXS
# BEGIN SourceDeps(oneline):
BuildRequires: perl(Cpanel/JSON/XS.pm) perl(Exporter.pm) perl(ExtUtils/MakeMaker.pm) perl(File/Spec.pm) perl(File/Temp.pm) perl(JSON/PP.pm) perl(Test/More.pm) perl(Test/Without/Module.pm) perl(base.pm) perl(if.pm)
# END SourceDeps(oneline)
BuildRequires: rpm-build-perl perl-devel perl-podlators

Name: perl-%module_name
Version: 1.003010
Release: alt1
Summary: use L<Cpanel::JSON::XS> with a fallback to L<JSON::PP>
Group: Development/Perl
License: perl
Url: %CPAN %module_name

Source0: http://www.cpan.org/authors/id/H/HA/HAARG/%{module_name}-%{version}.tar.gz
BuildArch: noarch
Requires: perl(Cpanel/JSON/XS.pm)

%description
%summary

%prep
%setup -q -n %{module_name}-%{version}

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc Changes README
%perl_vendor_privlib/J*

%changelog
* Thu Feb 01 2018 Igor Vlasenko <viy@altlinux.ru> 1.003010-alt1
- automated CPAN update

* Sun Oct 15 2017 Igor Vlasenko <viy@altlinux.ru> 1.003009-alt2
- added JSON requires

* Wed Mar 15 2017 Igor Vlasenko <viy@altlinux.ru> 1.003009-alt1
- automated CPAN update

* Wed Oct 19 2016 Igor Vlasenko <viy@altlinux.ru> 1.003008-alt1
- automated CPAN update

* Tue Sep 20 2016 Igor Vlasenko <viy@altlinux.ru> 1.003007-alt1
- automated CPAN update

* Wed Apr 01 2015 Igor Vlasenko <viy@altlinux.ru> 1.003005-alt1
- automated CPAN update

* Tue Dec 16 2014 Igor Vlasenko <viy@altlinux.ru> 1.003003-alt1
- automated CPAN update

* Tue Nov 25 2014 Igor Vlasenko <viy@altlinux.ru> 1.003002-alt1
- automated CPAN update

* Mon Oct 27 2014 Igor Vlasenko <viy@altlinux.ru> 1.002006-alt1
- automated CPAN update

* Mon Oct 20 2014 Igor Vlasenko <viy@altlinux.ru> 1.002005-alt1
- automated CPAN update

* Fri May 02 2014 Igor Vlasenko <viy@altlinux.ru> 1.002002-alt1
- automated CPAN update

* Sun Dec 22 2013 Igor Vlasenko <viy@altlinux.ru> 1.001000-alt1
- automated CPAN update

* Thu Nov 14 2013 Igor Vlasenko <viy@altlinux.ru> 1.000000-alt2
- moved to Sisyphus (for Catalyst-Runtime update)

* Mon Oct 14 2013 Igor Vlasenko <viy@altlinux.ru> 1.000000-alt1
- initial import by package builder

