# BEGIN SourceDeps(oneline):
BuildRequires: perl(Clone.pm) perl(Math/Symbolic.pm) perl(Math/Symbolic/Custom/Base.pm) perl(Module/Build.pm) perl(Test/More.pm)
# END SourceDeps(oneline)
%define module_version 2.01
%define module_name Math-Symbolic-Custom-Pattern
%define _unpackaged_files_terminate_build 1
BuildRequires: rpm-build-perl perl-devel perl-podlators

Name: perl-%module_name
Version: 2.01
Release: alt2
Summary: Pattern matching on Math::Symbolic trees
Group: Development/Perl
License: perl
Url: %CPAN %module_name

Source0: http://cpan.org.ua/authors/id/S/SM/SMUELLER/%module_name-%module_version.tar.gz
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
%perl_vendor_privlib/M*

%changelog
* Wed Feb 19 2014 Igor Vlasenko <viy@altlinux.ru> 2.01-alt2
- moved to Sisyphus for Slic3r (by dd@ request)

* Mon Sep 09 2013 Igor Vlasenko <viy@altlinux.ru> 2.01-alt1
- initial import by package builder

