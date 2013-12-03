%define module_version 0.03
%define module_name MouseX-Types-URI
# BEGIN SourceDeps(oneline):
BuildRequires: perl(CPAN.pm) perl(Config.pm) perl(Cwd.pm) perl(Exporter.pm) perl(ExtUtils/MM_Unix.pm) perl(ExtUtils/MakeMaker.pm) perl(ExtUtils/Manifest.pm) perl(File/Basename.pm) perl(File/Find.pm) perl(FileHandle.pm) perl(JSON.pm) perl(LWP/Simple.pm) perl(Module/Build.pm) perl(Mouse.pm) perl(Mouse/Util/TypeConstraints.pm) perl(MouseX/Types.pm) perl(MouseX/Types/Mouse.pm) perl(MouseX/Types/Path/Class.pm) perl(Net/FTP.pm) perl(Parse/CPAN/Meta.pm) perl(Pod/Parser.pm) perl(Pod/Text.pm) perl(Scalar/Util.pm) perl(Socket.pm) perl(Test/More.pm) perl(URI.pm) perl(URI/FromHash.pm) perl(URI/WithBase.pm) perl(URI/data.pm) perl(URI/file.pm) perl(YAML/Tiny.pm) perl(base.pm) perl(inc/Module/Install.pm)
# END SourceDeps(oneline)
%define _unpackaged_files_terminate_build 1
BuildRequires: rpm-build-perl perl-devel perl-podlators

Name: perl-%module_name
Version: 0.03
Release: alt2
Summary: A URI type library for Mouse
Group: Development/Perl
License: perl
Url: %CPAN %module_name

Source0: http://cpan.org.ua/authors/id/M/MA/MASAKI/%module_name-%module_version.tar.gz
BuildArch: noarch

%description
MouseX::Types::URI creates common the Mouse manpage types,
coercions and option specifications useful for dealing
with the URI manpages as the Mouse manpage attributes.

Coercions (see the Mouse::Util::TypeConstraints manpage) are made from
`Str', `ScalarRef', `HashRef',
the Path::Class::Dir manpage and the Path::Class::File manpage to
the URI manpage, the URI::data manpage and the URI::file manpage objects.


%prep
%setup -n %module_name-%module_version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc Changes README.mkdn README
%perl_vendor_privlib/M*

%changelog
* Tue Dec 03 2013 Igor Vlasenko <viy@altlinux.ru> 0.03-alt2
- uploaded to Sisyphus as Scalar-Does dependency

* Mon Sep 09 2013 Igor Vlasenko <viy@altlinux.ru> 0.03-alt1
- initial import by package builder

