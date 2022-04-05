# BEGIN SourceDeps(oneline):
BuildRequires: perl(ExtUtils/MakeMaker.pm) perl(File/Spec.pm) perl(FindBin.pm) perl(IO/Handle.pm) perl(IPC/Open3.pm) perl(Scalar/Util.pm) perl(Test/More.pm) perl(YAML/PP.pm) perl(YAML/PP/Common.pm) perl(YAML/PP/Parser.pm) perl(YAML/Parser.pm) perl(base.pm) perl(strict.pm) perl(utf8.pm) perl(warnings.pm)
# END SourceDeps(oneline)
%define module_name YAML-PP-Ref
%define _unpackaged_files_terminate_build 1
BuildRequires: rpm-build-perl perl-devel perl-podlators

Name: perl-%module_name
Version: 0.02
Release: alt1
Summary: Generated Reference Parser backend for YAML::PP
Group: Development/Perl
License: perl
Url: %CPAN %module_name

Source0: http://cpan.org.ua/authors/id/T/TI/TINITA/%{module_name}-%{version}.tar.gz
BuildArch: noarch

%description
The https://yaml.org/ YAML Specification can be used to generate a YAML
Parser from it.

Ingy has done that for several languages, and the one for Perl can be found
here: https://metacpan.org/dist/YAML-Parser.

This module exchanges the default the YAML::PP::Parser manpage parsing backend with
the YAML::Parser manpage. So you can profit from a Parser 100%% compliant to
the spec, but the YAML::PP manpage's functionalities on top of that, like loading
the parsing events into a data structure, and using the various the YAML::PP manpage
plugins.

At the time of this release, it is quite slow compared to other Perl YAML
modules, but it might not make a difference for you depending on your
application. The grammar for YAML 1.2 is not optimized for speed.

Also the error messages are not really helpful currently.

Check out the documentation of the YAML::Parser manpage regularly, these things might
have changed meanwhile.

%prep
%setup -q -n %{module_name}-%{version}

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc README.md Changes LICENSE examples
%perl_vendor_privlib/Y*

%changelog
* Tue Apr 05 2022 Igor Vlasenko <viy@altlinux.org> 0.02-alt1
- initial import by package builder

