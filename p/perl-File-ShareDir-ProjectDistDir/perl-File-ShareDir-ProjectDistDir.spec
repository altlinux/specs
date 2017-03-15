%define _unpackaged_files_terminate_build 1
# BEGIN SourceDeps(oneline):
BuildRequires: perl(Data/Dump.pm) perl(File/ShareDir.pm) perl(FindBin.pm) perl(IO/Handle.pm) perl(IPC/Open3.pm) perl(Module/Build.pm) perl(Path/Class/Dir.pm) perl(Path/Class/File.pm) perl(Path/FindDev.pm) perl(Path/IsDev.pm) perl(Sub/Exporter.pm) perl(Test/More.pm) perl(YAML/Dumper.pm) perl(YAML/Loader.pm)
# END SourceDeps(oneline)
%define module_name File-ShareDir-ProjectDistDir
BuildRequires: rpm-build-perl perl-devel perl-podlators

Name: perl-%module_name
Version: 1.000009
Release: alt1
Summary: Simple set-and-forget using of a '/share' directory in your projects root
Group: Development/Perl
License: perl
URL: https://github.com/kentfredric/File-ShareDir-ProjectDistDir

Source0: http://www.cpan.org/authors/id/K/KE/KENTNL/%{module_name}-%{version}.tar.gz
BuildArch: noarch

%description
%summary

%prep
%setup -q -n %{module_name}-%{version}

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc Changes README LICENSE
%perl_vendor_privlib/F*

%changelog
* Wed Mar 15 2017 Igor Vlasenko <viy@altlinux.ru> 1.000009-alt1
- automated CPAN update

* Sun Oct 11 2015 Igor Vlasenko <viy@altlinux.ru> 1.000008-alt1
- automated CPAN update

* Fri May 22 2015 Igor Vlasenko <viy@altlinux.ru> 1.000007-alt1
- automated CPAN update

* Tue Aug 19 2014 Igor Vlasenko <viy@altlinux.ru> 1.000004-alt1
- automated CPAN update

* Mon Jun 16 2014 Igor Vlasenko <viy@altlinux.ru> 1.000002-alt1
- automated CPAN update

* Wed Mar 05 2014 Igor Vlasenko <viy@altlinux.ru> 1.000001-alt1
- automated CPAN update

* Tue Mar 04 2014 Igor Vlasenko <viy@altlinux.ru> 1.000000-alt1
- automated CPAN update

* Sat Sep 28 2013 Igor Vlasenko <viy@altlinux.ru> 0.5.2-alt1
- automated CPAN update

* Tue Sep 17 2013 Igor Vlasenko <viy@altlinux.ru> 0.5.1-alt1
- regenerated from template by package builder

* Fri Sep 06 2013 Igor Vlasenko <viy@altlinux.ru> 0.4.4-alt1
- initial import by package builder

