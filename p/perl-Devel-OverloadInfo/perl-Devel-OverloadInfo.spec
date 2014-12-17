# BEGIN SourceDeps(oneline):
BuildRequires: perl(Exporter.pm) perl(ExtUtils/MakeMaker.pm) perl(MRO/Compat.pm) perl(Package/Stash.pm) perl(Pod/Wordlist.pm) perl(Scalar/Util.pm) perl(Sub/Identify.pm) perl(Test/More.pm) perl(Test/Pod.pm) perl(Test/Spelling.pm) perl(overload.pm) perl(parent.pm) perl(strict.pm) perl(warnings.pm)
# END SourceDeps(oneline)
%define module_version 0.002
%define module_name Devel-OverloadInfo
%define _unpackaged_files_terminate_build 1
BuildRequires: rpm-build-perl perl-devel perl-podlators

Name: perl-%module_name
Version: 0.002
Release: alt2
Summary: introspect overloaded operators
Group: Development/Perl
License: perl
Url: %CPAN %module_name

Source0: http://cpan.org.ua/authors/id/I/IL/ILMARI/%module_name-%module_version.tar.gz
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
%doc README Changes LICENSE
%perl_vendor_privlib/D*

%changelog
* Wed Dec 17 2014 Igor Vlasenko <viy@altlinux.ru> 0.002-alt2
- moved to Sisyphus as dependency

* Mon Apr 07 2014 Igor Vlasenko <viy@altlinux.ru> 0.002-alt1
- initial import by package builder

