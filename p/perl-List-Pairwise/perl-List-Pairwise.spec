%define _unpackaged_files_terminate_build 1
%define module_version 1.03
%define module_name List-Pairwise
# BEGIN SourceDeps(oneline):
BuildRequires: perl(CPAN.pm) perl(Config.pm) perl(Cwd.pm) perl(Devel/Cover.pm) perl(Exporter.pm) perl(ExtUtils/MM_Unix.pm) perl(ExtUtils/MakeMaker.pm) perl(ExtUtils/Manifest.pm) perl(Fcntl.pm) perl(File/Basename.pm) perl(File/Find.pm) perl(File/Spec.pm) perl(File/Temp.pm) perl(FileHandle.pm) perl(JSON.pm) perl(LWP/Simple.pm) perl(List/Util.pm) perl(Module/Build.pm) perl(Net/FTP.pm) perl(Parse/CPAN/Meta.pm) perl(Socket.pm) perl(Test/More.pm) perl(YAML/Tiny.pm) perl(inc/Module/Install.pm)
# END SourceDeps(oneline)
BuildRequires: rpm-build-perl perl-devel perl-podlators

Name: perl-%module_name
Version: 1.03
Release: alt1
Summary: map/grep arrays and hashes pairwise
Group: Development/Perl
License: perl
Url: %CPAN %module_name

Source: http://www.cpan.org/authors/id/T/TD/TDRUGEON/List-Pairwise-%{version}.tar.gz
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
%doc Changelog
%perl_vendor_privlib/L*

%changelog
* Tue Jul 08 2014 Igor Vlasenko <viy@altlinux.ru> 1.03-alt1
- automated CPAN update

* Thu Feb 20 2014 Igor Vlasenko <viy@altlinux.ru> 1.02-alt2
- moved to Sisyphus for Slic3r (by dd@ request)

* Tue Nov 26 2013 Igor Vlasenko <viy@altlinux.ru> 1.02-alt1
- regenerated from template by package builder

* Wed Sep 04 2013 Igor Vlasenko <viy@altlinux.ru> 1.01-alt1
- initial import by package builder

