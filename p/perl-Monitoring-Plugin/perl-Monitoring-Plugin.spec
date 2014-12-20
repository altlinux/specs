# BEGIN SourceDeps(oneline):
BuildRequires: perl(CPAN.pm) perl(Carp.pm) perl(Class/Accessor.pm) perl(Class/Accessor/Fast.pm) perl(Config.pm) perl(Config/Tiny.pm) perl(Cwd.pm) perl(Exporter.pm) perl(ExtUtils/MM_Unix.pm) perl(ExtUtils/MakeMaker.pm) perl(ExtUtils/Manifest.pm) perl(Fcntl.pm) perl(File/Basename.pm) perl(File/Find.pm) perl(File/Spec.pm) perl(File/Temp.pm) perl(FileHandle.pm) perl(IO/File.pm) perl(JSON.pm) perl(LWP/Simple.pm) perl(Math/Calc/Units.pm) perl(Module/Build.pm) perl(Net/FTP.pm) perl(Params/Validate.pm) perl(Parse/CPAN/Meta.pm) perl(Socket.pm) perl(Test/More.pm) perl(YAML/Tiny.pm) perl(base.pm) perl(inc/Module/Install.pm) perl(overload.pm)
# END SourceDeps(oneline)
%define module_version 0.37
%define module_name Monitoring-Plugin
%define _unpackaged_files_terminate_build 1
BuildRequires: rpm-build-perl perl-devel perl-podlators

Name: perl-%module_name
Version: 0.37
Release: alt2
Summary: A family of perl modules to streamline writing Naemon, Nagios,
Group: Development/Perl
License: perl
Url: %CPAN %module_name

Source0: http://cpan.org.ua/authors/id/N/NI/NIERLEIN/%module_name-%module_version.tar.gz
BuildArch: noarch

%description
Monitoring::Plugin and its associated Monitoring::Plugin::* modules are a
family of perl modules to streamline writing Monitoring plugins. The main
end user modules are Monitoring::Plugin, providing an object-oriented
interface to the entire Monitoring::Plugin::* collection, and
Monitoring::Plugin::Functions, providing a simpler functional interface to
a useful subset of the available functionality.

The purpose of the collection is to make it as simple as possible for
developers to create plugins that conform the Monitoring Plugin guidelines
(https://www.monitoring-plugins.org/doc/guidelines.html).



%prep
%setup -n %module_name-%module_version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc README Changes
%perl_vendor_privlib/M*

%changelog
* Sat Dec 20 2014 Igor Vlasenko <viy@altlinux.ru> 0.37-alt2
- moved to Sisyphus as dependency

* Fri Mar 07 2014 Igor Vlasenko <viy@altlinux.ru> 0.37-alt1
- initial import by package builder

