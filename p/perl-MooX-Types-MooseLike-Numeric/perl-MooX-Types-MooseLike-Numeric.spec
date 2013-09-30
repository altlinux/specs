%define module_version 1.01
%define module_name MooX-Types-MooseLike-Numeric
# BEGIN SourceDeps(oneline):
BuildRequires: perl(Exporter.pm) perl(ExtUtils/MakeMaker.pm) perl(IO/Handle.pm) perl(Moo.pm) perl(MooX/Types/MooseLike.pm) perl(MooX/Types/MooseLike/Base.pm) perl(Moose.pm) perl(Test/Fatal.pm) perl(Test/More.pm)
# END SourceDeps(oneline)
%define _unpackaged_files_terminate_build 1
BuildRequires: rpm-build-perl perl-devel perl-podlators

Name: perl-%module_name
Version: 1.01
Release: alt2
Summary: Moo types for numbers
Group: Development/Perl
License: perl
Url: %CPAN %module_name

Source0: http://cpan.org.ua/authors/id/M/MA/MATEU/%module_name-%module_version.tar.gz
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
* Mon Sep 30 2013 Igor Vlasenko <viy@altlinux.ru> 1.01-alt2
- regenerated from template by package builder

* Wed Sep 04 2013 Igor Vlasenko <viy@altlinux.ru> 1.01-alt1
- initial import by package builder

