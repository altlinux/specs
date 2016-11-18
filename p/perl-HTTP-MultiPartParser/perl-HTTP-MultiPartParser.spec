# BEGIN SourceDeps(oneline):
BuildRequires: perl(App/pod2pdf.pm) perl(CPAN.pm) perl(Carp.pm) perl(Config.pm) perl(Cwd.pm) perl(Exporter.pm) perl(ExtUtils/MM_Unix.pm) perl(ExtUtils/MakeMaker.pm) perl(ExtUtils/Manifest.pm) perl(Fcntl.pm) perl(File/Basename.pm) perl(File/Find.pm) perl(File/Spec.pm) perl(File/Spec/Functions.pm) perl(File/Temp.pm) perl(FileHandle.pm) perl(FindBin.pm) perl(HTTP/Headers/Util.pm) perl(Hash/MultiValue.pm) perl(IO/File.pm) perl(JSON.pm) perl(LWP/Simple.pm) perl(Module/Build.pm) perl(Net/FTP.pm) perl(Parse/CPAN/Meta.pm) perl(Pod/Html.pm) perl(Pod/Man.pm) perl(Pod/Text.pm) perl(Scalar/Util.pm) perl(Socket.pm) perl(Test/Deep.pm) perl(Test/More.pm) perl(YAML/Tiny.pm) perl(base.pm) perl(inc/Module/Install.pm)
# END SourceDeps(oneline)
%define module_version 0.01
%define module_name HTTP-MultiPartParser
%define _unpackaged_files_terminate_build 1
BuildRequires: rpm-build-perl perl-devel perl-podlators

Name: perl-%module_name
Version: 0.01
Release: alt2
Summary: HTTP MultiPart Parser
Group: Development/Perl
License: perl
Url: %CPAN %module_name

Source0: http://cpan.org.ua/authors/id/C/CH/CHANSEN/%module_name-%module_version.tar.gz
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
%perl_vendor_privlib/H*

%changelog
* Fri Nov 18 2016 Igor Vlasenko <viy@altlinux.ru> 0.01-alt2
- to Sisyphus

* Fri Mar 07 2014 Igor Vlasenko <viy@altlinux.ru> 0.01-alt1
- initial import by package builder

