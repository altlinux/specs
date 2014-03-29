%define module_version 0.05
%define module_name Symbol-Global-Name
# BEGIN SourceDeps(oneline):
BuildRequires: perl(App/pod2pdf.pm) perl(CPAN.pm) perl(Config.pm) perl(Cwd.pm) perl(ExtUtils/MM_Unix.pm) perl(ExtUtils/MakeMaker.pm) perl(ExtUtils/Manifest.pm) perl(Fcntl.pm) perl(File/Basename.pm) perl(File/Find.pm) perl(File/Spec.pm) perl(File/Temp.pm) perl(FileHandle.pm) perl(JSON.pm) perl(LWP/Simple.pm) perl(Module/Build.pm) perl(Net/FTP.pm) perl(Parse/CPAN/Meta.pm) perl(Pod/Html.pm) perl(Pod/Man.pm) perl(Pod/Text.pm) perl(Socket.pm) perl(Test/More.pm) perl(YAML/Tiny.pm) perl(base.pm) perl(inc/Module/Install.pm)
# END SourceDeps(oneline)
%define _unpackaged_files_terminate_build 1
BuildRequires: rpm-build-perl perl-devel perl-podlators

Name: perl-%module_name
Version: 0.05
Release: alt2
Summary: finds name and type of a global variable
Group: Development/Perl
License: perl
Url: %CPAN %module_name

Source0: http://cpan.org.ua/authors/id/A/AL/ALEXMV/%module_name-%module_version.tar.gz
BuildArch: noarch

%description
Lookups symbol table to find an element by reference.


%prep
%setup -n %module_name-%module_version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc Changes README
%perl_vendor_privlib/S*

%changelog
* Sat Mar 29 2014 Igor Vlasenko <viy@altlinux.ru> 0.05-alt2
- moved to Sisyphus by lav@ request

* Mon Feb 17 2014 Igor Vlasenko <viy@altlinux.ru> 0.05-alt1
- regenerated from template by package builder

* Tue Sep 03 2013 Igor Vlasenko <viy@altlinux.ru> 0.04-alt1
- initial import by package builder

