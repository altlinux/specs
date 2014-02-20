# BEGIN SourceDeps(oneline):
BuildRequires: perl(B/Concise.pm) perl(Exporter.pm) perl(Math/BigRat.pm) perl(Math/Polynomial.pm) perl(Pod/Simple/HTML.pm) perl(Scalar/Util.pm) perl(Test/More.pm)
# END SourceDeps(oneline)
%define module_version 3
%define module_name Math-Polynomial-Horner
%define _unpackaged_files_terminate_build 1
BuildRequires: rpm-build-perl perl-devel perl-podlators

Name: perl-%module_name
Version: 3
Release: alt2
Summary: Stringizing Math::Polyomial objects in Horner form.
Group: Development/Perl
License: gpl
URL: http://user42.tuxfamily.org/math-polynomial-horner/index.html

Source0: http://cpan.org.ua/authors/id/K/KR/KRYDE/%module_name-%module_version.tar.gz
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
%doc Changes COPYING
%perl_vendor_privlib/M*

%changelog
* Thu Feb 20 2014 Igor Vlasenko <viy@altlinux.ru> 3-alt2
- moved to Sisyphus for Slic3r (by dd@ request)

* Mon Sep 09 2013 Igor Vlasenko <viy@altlinux.ru> 3-alt1
- initial import by package builder

