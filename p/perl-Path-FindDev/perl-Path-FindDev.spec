%define _unpackaged_files_terminate_build 1
# BEGIN SourceDeps(oneline):
BuildRequires: perl(Carp.pm) perl(Class/Tiny.pm) perl(Data/Dump.pm) perl(File/Spec.pm) perl(FindBin.pm) perl(IO/Handle.pm) perl(IPC/Open3.pm) perl(Module/Build.pm) perl(Path/IsDev/Object.pm) perl(Path/Tiny.pm) perl(Scalar/Util.pm) perl(Sub/Exporter.pm) perl(Test/More.pm) perl(YAML/Dumper.pm) perl(YAML/Loader.pm)
# END SourceDeps(oneline)
%define module_version 0.4.1
%define module_name Path-FindDev
BuildRequires: rpm-build-perl perl-devel perl-podlators

Name: perl-%module_name
Version: 0.4.1
Release: alt1
Summary: Find a development path somewhere in an upper hierarchy.
Group: Development/Perl
License: perl
URL: https://github.com/kentfredric/Path-FindDev

Source: http://www.cpan.org/authors/id/K/KE/KENTNL/Path-FindDev-%{version}.tar.gz
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
%doc LICENSE README Changes
%perl_vendor_privlib/P*

%changelog
* Fri Oct 25 2013 Igor Vlasenko <viy@altlinux.ru> 0.4.1-alt1
- automated CPAN update

* Wed Oct 02 2013 Igor Vlasenko <viy@altlinux.ru> 0.4.0-alt1
- automated CPAN update

* Sat Sep 28 2013 Igor Vlasenko <viy@altlinux.ru> 0.3.2-alt1
- automated CPAN update

* Tue Sep 24 2013 Igor Vlasenko <viy@altlinux.ru> 0.3.1-alt1
- regenerated from template by package builder

* Tue Sep 17 2013 Igor Vlasenko <viy@altlinux.ru> 0.2.0-alt1
- initial import by package builder

