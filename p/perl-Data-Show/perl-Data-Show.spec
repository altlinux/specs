%define _unpackaged_files_terminate_build 1
%define module_version 0.002004
%define module_name Data-Show
# BEGIN SourceDeps(oneline):
BuildRequires: perl(Contextual/Return.pm) perl(Data/Dump.pm) perl(ExtUtils/MakeMaker.pm) perl(Module/Build.pm) perl(Test/More.pm) perl(re.pm) perl(version.pm)
# END SourceDeps(oneline)
BuildRequires: rpm-build-perl perl-devel perl-podlators

Name: perl-%module_name
Version: 0.002004
Release: alt1
Summary: Dump data structures with name and point-of-origin
Group: Development/Perl
License: perl
Url: %CPAN %module_name

Source: http://www.cpan.org/authors/id/D/DC/DCONWAY/Data-Show-%{version}.tar.gz
BuildArch: noarch

%description
%summary

%prep
%setup -n %module_name-%module_version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc Changes README
%perl_vendor_privlib/D*

%changelog
* Thu May 26 2016 Igor Vlasenko <viy@altlinux.ru> 0.002004-alt1
- automated CPAN update

* Sun Oct 11 2015 Igor Vlasenko <viy@altlinux.ru> 0.002003-alt1
- automated CPAN update

* Thu Feb 20 2014 Igor Vlasenko <viy@altlinux.ru> 0.002002-alt2
- moved to Sisyphus for Slic3r (by dd@ request)

* Tue Oct 29 2013 Igor Vlasenko <viy@altlinux.ru> 0.002002-alt1
- regenerated from template by package builder

* Fri Sep 06 2013 Igor Vlasenko <viy@altlinux.ru> 0.002001-alt1
- initial import by package builder

