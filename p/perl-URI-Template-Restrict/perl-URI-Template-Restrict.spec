%define module_version 0.06
%define module_name URI-Template-Restrict
# BEGIN SourceDeps(oneline):
BuildRequires: perl(CPAN.pm) perl(Carp.pm) perl(Class/Accessor/Fast.pm) perl(Config.pm) perl(Cwd.pm) perl(Data/Dumper.pm) perl(Exporter.pm) perl(ExtUtils/MM_Unix.pm) perl(ExtUtils/MakeMaker.pm) perl(ExtUtils/Manifest.pm) perl(File/Basename.pm) perl(File/Find.pm) perl(File/Path.pm) perl(FileHandle.pm) perl(Filter/Util/Call.pm) perl(JSON.pm) perl(LWP/Simple.pm) perl(List/MoreUtils.pm) perl(MIME/Base64.pm) perl(Module/Build.pm) perl(Net/FTP.pm) perl(Parse/CPAN/Meta.pm) perl(PerlIO.pm) perl(Scalar/Util.pm) perl(Socket.pm) perl(Text/Diff.pm) perl(URI.pm) perl(URI/Escape.pm) perl(Unicode/Normalize.pm) perl(YAML.pm) perl(YAML/Tiny.pm) perl(base.pm) perl(inc/Module/Install.pm) perl(overload.pm) perl(threads/shared.pm)
# END SourceDeps(oneline)
%define _unpackaged_files_terminate_build 1
BuildRequires: rpm-build-perl perl-devel perl-podlators

Name: perl-%module_name
Version: 0.06
Release: alt2
Summary: restricted URI Templates handler
Group: Development/Perl
License: perl
Url: %CPAN %module_name

Source0: http://cpan.org.ua/authors/id/M/MA/MASAKI/%module_name-%module_version.tar.gz
BuildArch: noarch

%description
This is a restricted URI Templates handler. URI Templates is described at
http://bitworking.org/projects/URI-Templates/.

This module supports draft-gregorio-uritemplate-03 except -opt and
-neg operators.


%prep
%setup -n %module_name-%module_version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc Changes README
%perl_vendor_privlib/U*

%changelog
* Wed Oct 16 2013 Igor Vlasenko <viy@altlinux.ru> 0.06-alt2
- build for Sisyphus (required for perl update)

* Tue Sep 10 2013 Igor Vlasenko <viy@altlinux.ru> 0.06-alt1
- initial import by package builder

