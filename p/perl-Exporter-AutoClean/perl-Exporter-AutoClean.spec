# BEGIN SourceDeps(oneline):
BuildRequires: perl(B/Hooks/EndOfScope.pm) perl(CPAN.pm) perl(Carp.pm) perl(Config.pm) perl(Cwd.pm) perl(Data/Dumper.pm) perl(Exporter.pm) perl(ExtUtils/MM_Unix.pm) perl(ExtUtils/MakeMaker.pm) perl(ExtUtils/Manifest.pm) perl(File/Basename.pm) perl(File/Find.pm) perl(File/Path.pm) perl(FileHandle.pm) perl(Filter/Util/Call.pm) perl(FindBin.pm) perl(LWP/Simple.pm) perl(MIME/Base64.pm) perl(Module/Build.pm) perl(PerlIO.pm) perl(YAML.pm) perl(YAML/Tiny.pm) perl(overload.pm) perl(threads/shared.pm)
# END SourceDeps(oneline)
%define module_version 0.01
%define module_name Exporter-AutoClean
%define _unpackaged_files_terminate_build 1
BuildRequires: rpm-build-perl perl-devel perl-podlators

Name: perl-%module_name
Version: 0.01
Release: alt2
Summary: export instant functions available at compile time only
Group: Development/Perl
License: perl
Url: %CPAN %module_name

Source0: http://cpan.org.ua/authors/id/T/TY/TYPESTER/%module_name-%module_version.tar.gz
BuildArch: noarch

%description
This is a simple wrapper module of the B::Hooks::EndOfScope manpage, allows you to export instant functions that is only available at compile time.


%prep
%setup -n %module_name-%module_version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc Changes README LICENSE
%perl_vendor_privlib/E*

%changelog
* Thu Jun 30 2022 Igor Vlasenko <viy@altlinux.org> 0.01-alt2
- to Sisyphus for perl-Object-Container

* Fri Sep 06 2013 Igor Vlasenko <viy@altlinux.ru> 0.01-alt1
- initial import by package builder

