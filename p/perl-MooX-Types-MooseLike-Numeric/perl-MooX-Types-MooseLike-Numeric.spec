%define _unpackaged_files_terminate_build 1
%define module_version 1.02
%define module_name MooX-Types-MooseLike-Numeric
# BEGIN SourceDeps(oneline):
BuildRequires: perl(Exporter.pm) perl(ExtUtils/MakeMaker.pm) perl(IO/Handle.pm) perl(Moo.pm) perl(MooX/Types/MooseLike.pm) perl(MooX/Types/MooseLike/Base.pm) perl(Moose.pm) perl(Test/Fatal.pm) perl(Test/More.pm)
# END SourceDeps(oneline)
BuildRequires: rpm-build-perl perl-devel perl-podlators

Name: perl-%module_name
Version: 1.02
Release: alt1.1
Summary: Moo types for numbers
Group: Development/Perl
License: perl
Url: %CPAN %module_name

Source: http://www.cpan.org/authors/id/M/MA/MATEU/MooX-Types-MooseLike-Numeric-%{version}.tar.gz
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
* Sat Apr 09 2016 Igor Vlasenko <viy@altlinux.ru> 1.02-alt1.1
- rebuild to restore role requires

* Mon Nov 25 2013 Igor Vlasenko <viy@altlinux.ru> 1.02-alt1
- automated CPAN update

* Mon Sep 30 2013 Igor Vlasenko <viy@altlinux.ru> 1.01-alt2
- regenerated from template by package builder

* Wed Sep 04 2013 Igor Vlasenko <viy@altlinux.ru> 1.01-alt1
- initial import by package builder

