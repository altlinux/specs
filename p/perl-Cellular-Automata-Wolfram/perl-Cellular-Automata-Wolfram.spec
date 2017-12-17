# BEGIN SourceDeps(oneline):
BuildRequires: perl(AutoLoader.pm) perl(Carp.pm) perl(Class/MethodMaker.pm) perl(DynaLoader.pm) perl(Exporter.pm) perl(GD.pm) perl(Graphics/ColorNames.pm) perl(Math/BaseCalc.pm)
# END SourceDeps(oneline)
%define module_version 1.1
%define module_name Cellular-Automata-Wolfram
%define _unpackaged_files_terminate_build 1
BuildRequires: rpm-build-perl perl-devel perl-podlators

Name: perl-%module_name
Version: 1.1
Release: alt2.1.1.1.1
Summary: perl module %module_name
Group: Development/Perl
License: perl
Url: %CPAN %module_name

Source0: http://cpan.org.ua/authors/id/J/JM/JMFREEMAN/%module_name-%module_version.tar.gz

%description
%summary

%prep
%setup -n %module_name-%module_version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc README Changes
%perl_vendor_archlib/C*
%perl_vendor_autolib/*

%changelog
* Fri Dec 15 2017 Igor Vlasenko <viy@altlinux.ru> 1.1-alt2.1.1.1.1
- rebuild with new perl 5.26.1

* Fri Feb 03 2017 Igor Vlasenko <viy@altlinux.ru> 1.1-alt2.1.1.1
- rebuild with new perl 5.24.1

* Wed Nov 25 2015 Igor Vlasenko <viy@altlinux.ru> 1.1-alt2.1.1
- rebuild with new perl 5.22.0

* Tue Dec 09 2014 Igor Vlasenko <viy@altlinux.ru> 1.1-alt2.1
- rebuild with new perl 5.20.1

* Thu Feb 20 2014 Igor Vlasenko <viy@altlinux.ru> 1.1-alt2
- moved to Sisyphus for Slic3r (by dd@ request)

* Tue Sep 03 2013 Igor Vlasenko <viy@altlinux.ru> 1.1-alt1
- initial import by package builder

