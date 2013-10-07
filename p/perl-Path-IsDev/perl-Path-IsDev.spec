%define module_version 0.6.0
%define module_name Path-IsDev
%define _unpackaged_files_terminate_build 1
# BEGIN SourceDeps(oneline):
BuildRequires: perl(Carp.pm) perl(Class/Tiny.pm) perl(Data/Dump.pm) perl(FindBin.pm) perl(IO/Handle.pm) perl(IPC/Open3.pm) perl(Module/Build.pm) perl(Module/Runtime.pm) perl(Path/FindDev.pm) perl(Path/Tiny.pm) perl(Role/Tiny.pm) perl(Role/Tiny/With.pm) perl(Scalar/Util.pm) perl(Sub/Exporter.pm) perl(Test/Fatal.pm) perl(Test/More.pm) perl(YAML/Dumper.pm) perl(YAML/Loader.pm)
# END SourceDeps(oneline)
BuildRequires: rpm-build-perl perl-devel perl-podlators

Name: perl-%module_name
Version: 0.6.0
Release: alt1
Summary: Determine if a given Path resembles a development source tree
Group: Development/Perl
License: perl
URL: https://github.com/kentfredric/Path-IsDev

Source0: http://cpan.org.ua/authors/id/K/KE/KENTNL/%module_name-%module_version.tar.gz
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
%doc LICENSE Changes README
%perl_vendor_privlib/P*

%changelog
* Mon Oct 07 2013 Igor Vlasenko <viy@altlinux.ru> 0.6.0-alt1
- regenerated from template by package builder

* Sat Sep 28 2013 Igor Vlasenko <viy@altlinux.ru> 0.4.0-alt1
- automated CPAN update

* Tue Sep 24 2013 Igor Vlasenko <viy@altlinux.ru> 0.3.2-alt1
- regenerated from template by package builder

* Tue Sep 17 2013 Igor Vlasenko <viy@altlinux.ru> 0.3.0-alt1
- initial import by package builder

