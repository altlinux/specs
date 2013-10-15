%define module_version 0.05
%define module_name HTTP-Router
# BEGIN SourceDeps(oneline):
BuildRequires: perl(CPAN.pm) perl(Carp.pm) perl(Class/Accessor/Fast.pm) perl(Config.pm) perl(Cwd.pm) perl(Data/Dumper.pm) perl(Devel/Caller/Perl.pm) perl(Exporter.pm) perl(ExtUtils/MM_Unix.pm) perl(ExtUtils/MakeMaker.pm) perl(ExtUtils/Manifest.pm) perl(File/Basename.pm) perl(File/Find.pm) perl(File/Path.pm) perl(FileHandle.pm) perl(Filter/Util/Call.pm) perl(Hash/AsObject.pm) perl(JSON.pm) perl(LWP/Simple.pm) perl(Lingua/EN/Inflect/Number.pm) perl(List/MoreUtils.pm) perl(MIME/Base64.pm) perl(Module/Build.pm) perl(Net/FTP.pm) perl(Parse/CPAN/Meta.pm) perl(PerlIO.pm) perl(Pod/Perldoc/ToPod.pm) perl(Pod/Text.pm) perl(Scalar/Util.pm) perl(Socket.pm) perl(Storable.pm) perl(String/CamelCase.pm) perl(Text/Diff.pm) perl(Text/SimpleTable.pm) perl(UNIVERSAL.pm) perl(URI/Template/Restrict.pm) perl(YAML.pm) perl(YAML/Tiny.pm) perl(base.pm) perl(inc/Module/Install.pm) perl(overload.pm) perl(threads/shared.pm) perl(warnings/register.pm) perl(Test/HTTP.pm) perl(Test/Deep.pm) perl(Test/MockObject.pm)
# END SourceDeps(oneline)
%define _unpackaged_files_terminate_build 1
BuildRequires: rpm-build-perl perl-devel perl-podlators

Name: perl-%module_name
Version: 0.05
Release: alt2
Summary: Yet Another Path Router for HTTP
Group: Development/Perl
License: perl
Url: %CPAN %module_name

Source0: http://cpan.org.ua/authors/id/M/MA/MASAKI/%module_name-%module_version.tar.gz
BuildArch: noarch

%description
HTTP::Router provides a way of constructing routing tables..
If you are interested in a Merb-like constructing way,
please check the HTTP::Router::Declare manpage.


%prep
%setup -n %module_name-%module_version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc Changes README.pod README
%perl_vendor_privlib/H*
%perl_vendor_privlib/T*

%changelog
* Wed Oct 16 2013 Igor Vlasenko <viy@altlinux.ru> 0.05-alt2
- build for Sisyphus (required for perl update)

* Mon Oct 07 2013 Igor Vlasenko <viy@altlinux.ru> 0.05-alt1
- initial import by package builder

