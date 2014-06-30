# BEGIN SourceDeps(oneline):
BuildRequires: perl(CPAN.pm) perl(Config.pm) perl(Cwd.pm) perl(Exporter.pm) perl(ExtUtils/MM_Unix.pm) perl(ExtUtils/MakeMaker.pm) perl(ExtUtils/Manifest.pm) perl(File/Basename.pm) perl(File/Find.pm) perl(FileHandle.pm) perl(Module/Build.pm) perl(Mouse.pm) perl(Mouse/Role.pm) perl(MouseX/Types/Path/Class.pm) perl(Pod/Parser.pm) perl(Pod/Text.pm) perl(Test/More.pm) perl(YAML/Tiny.pm)
# END SourceDeps(oneline)
%define module_version 0.05
%define module_name MouseX-ConfigFromFile
%define _unpackaged_files_terminate_build 1
BuildRequires: rpm-build-perl perl-devel perl-podlators

Name: perl-%module_name
Version: 0.05
Release: alt2
Summary: An abstract Mouse role for setting attributes from a configfile
Group: Development/Perl
License: perl
Url: %CPAN %module_name

Source0: http://cpan.org.ua/authors/id/M/MA/MASAKI/%module_name-%module_version.tar.gz
BuildArch: noarch

%description
This is an abstract role which provides an alternate constructor for
creating objects using parameters passed in from a configuration file.
The actual implementation of reading the configuration file is left to
concrete subroles.

It declares an attribute `configfile' and a class method
`new_with_config', and requires that concrete roles derived from it
implement the class method `get_config_from_file'.

Attributes specified directly as arguments to `new_with_config'
supercede those in the configfile.


%prep
%setup -n %module_name-%module_version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc README Changes README.mkdn
%perl_vendor_privlib/M*

%changelog
* Mon Jun 30 2014 Igor Vlasenko <viy@altlinux.ru> 0.05-alt2
- moved to Sisyphus as dependency

* Mon Sep 09 2013 Igor Vlasenko <viy@altlinux.ru> 0.05-alt1
- initial import by package builder

