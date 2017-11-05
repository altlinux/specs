%filter_from_requires /^perl.Module.Compile.Ext.pm./d
%define module_version 0.35
%define module_name Module-Compile
%filter_from_requires /^perl.Module.Compile.Ext.pm./d
%filter_from_requires /^perl.Module.Compile.Ext.pm./d
# BEGIN SourceDeps(oneline):
BuildRequires: perl(Carp.pm) perl(Data/Dumper.pm) perl(Digest/SHA1.pm) perl(Exporter.pm) perl(ExtUtils/MakeMaker.pm) perl(File/Path.pm) perl(Filter/Util/Call.pm) perl(LWP/Simple.pm) perl(MIME/Base64.pm) perl(Test/Deep.pm) perl(Test/More.pm) perl(Test/Pod.pm) perl(Text/Diff.pm) perl(YAML.pm) perl(base.pm) perl(overload.pm)
# END SourceDeps(oneline)
%define _unpackaged_files_terminate_build 1
BuildRequires: rpm-build-perl perl-devel perl-podlators

Name: perl-%module_name
Version: 0.35
Release: alt2
Summary: Perl Module Compilation
Group: Development/Perl
License: perl
URL: https://github.com/ingydotnet/module-compile-pm

Source0: http://cpan.org.ua/authors/id/I/IN/INGY/%{module_name}-%{module_version}.tar.gz
BuildArch: noarch

%description
This module provides a system for writing modules that *compile* other
Perl modules.

Modules that use these compilation modules get compiled into some
altered form the first time they are run. The result is cached into
`.pmc' files.

Perl has native support for `.pmc' files. It always checks for them, before
loading a `.pm' file.


%prep
%setup -n %{module_name}-%{module_version}

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc Changes LICENSE README
%perl_vendor_privlib/M*

%changelog
* Sun Nov 05 2017 Igor Vlasenko <viy@altlinux.ru> 0.35-alt2
- to Sisyphus as perl-PDL dep

* Mon Dec 29 2014 Igor Vlasenko <viy@altlinux.ru> 0.35-alt1
- regenerated from template by package builder

* Wed Dec 17 2014 Igor Vlasenko <viy@altlinux.ru> 0.34-alt1
- regenerated from template by package builder

* Tue Oct 15 2013 Igor Vlasenko <viy@altlinux.ru> 0.23-alt2
fixed requires

* Mon Oct 14 2013 Igor Vlasenko <viy@altlinux.ru> 0.23-alt1
- initial import by package builder

