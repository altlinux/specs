%define module_version 0.17
%define module_name Text-MicroTemplate-Extended
# BEGIN SourceDeps(oneline):
BuildRequires: perl(CPAN.pm) perl(Carp.pm) perl(Config.pm) perl(Cwd.pm) perl(Data/Dumper.pm) perl(Exporter.pm) perl(ExtUtils/MM_Unix.pm) perl(ExtUtils/MakeMaker.pm) perl(ExtUtils/Manifest.pm) perl(Fcntl.pm) perl(File/Basename.pm) perl(File/Find.pm) perl(File/Path.pm) perl(File/Spec.pm) perl(File/Temp.pm) perl(FileHandle.pm) perl(Filter/Util/Call.pm) perl(FindBin.pm) perl(JSON.pm) perl(LWP/Simple.pm) perl(MIME/Base64.pm) perl(Module/Build.pm) perl(Mouse.pm) perl(Net/FTP.pm) perl(Parse/CPAN/Meta.pm) perl(PerlIO.pm) perl(Socket.pm) perl(Test/Deep.pm) perl(Text/Diff.pm) perl(Text/MicroTemplate.pm) perl(Text/MicroTemplate/File.pm) perl(YAML.pm) perl(YAML/Tiny.pm) perl(base.pm) perl(inc/Module/Install.pm) perl(overload.pm) perl(threads/shared.pm)
# END SourceDeps(oneline)
%define _unpackaged_files_terminate_build 1
BuildRequires: rpm-build-perl perl-devel perl-podlators

Name: perl-%module_name
Version: 0.17
Release: alt2
Summary: Extended MicroTemplate
Group: Development/Perl
License: perl
Url: %CPAN %module_name

Source0: http://cpan.org.ua/authors/id/T/TY/TYPESTER/%module_name-%module_version.tar.gz
BuildArch: noarch

%description
the Text::MicroTemplate::Extended manpage is an extended template engine based on the Text::MicroTemplate::File manpage.


%prep
%setup -n %module_name-%module_version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc README LICENSE Changes example
%perl_vendor_privlib/T*

%changelog
* Wed Oct 16 2013 Igor Vlasenko <viy@altlinux.ru> 0.17-alt2
- build for Sisyphus (required for perl update)

* Tue Sep 10 2013 Igor Vlasenko <viy@altlinux.ru> 0.17-alt1
- initial import by package builder

