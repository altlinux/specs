%define module_version 0.30
%define module_name MouseX-App-Cmd
# BEGIN SourceDeps(oneline):
BuildRequires: perl(App/Cmd.pm) perl(App/Cmd/Command.pm) perl(Data/Dumper.pm) perl(English.pm) perl(ExtUtils/MakeMaker.pm) perl(File/Basename.pm) perl(File/Spec.pm) perl(Getopt/Long/Descriptive.pm) perl(Mouse.pm) perl(Mouse/Object.pm) perl(MouseX/ConfigFromFile.pm) perl(MouseX/Getopt.pm) perl(Test/More.pm) perl(Test/Output.pm) perl(YAML.pm) perl(base.pm) perl(lib.pm) perl(namespace/autoclean.pm) perl(strict.pm) perl(warnings.pm)
# END SourceDeps(oneline)
%define _unpackaged_files_terminate_build 1
BuildRequires: rpm-build-perl perl-devel perl-podlators

Name: perl-%module_name
Version: 0.30
Release: alt2
Summary: Mashes up MouseX::Getopt and App::Cmd
Group: Development/Perl
License: perl
URL: https://github.com/karenetheridge/MouseX-App-Cmd

Source0: http://cpan.org.ua/authors/id/E/ET/ETHER/%{module_name}-%{module_version}.tar.gz
BuildArch: noarch

%description
From summary: %summary

%prep
%setup -q -n %{module_name}-%{module_version}
[ %version = 0.30 ] && rm t/build_emulates_new.t

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc TODO Changes LICENSE README
%perl_vendor_privlib/M*

%changelog
* Mon Dec 07 2015 Igor Vlasenko <viy@altlinux.ru> 0.30-alt2
- to Sisyphus as perl-Package dependency

* Mon Jan 12 2015 Igor Vlasenko <viy@altlinux.ru> 0.30-alt1
- initial import by package builder

