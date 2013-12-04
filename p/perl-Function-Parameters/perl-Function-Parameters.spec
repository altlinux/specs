%define module_version 1.0401
%define module_name Function-Parameters
# BEGIN SourceDeps(oneline):
BuildRequires: perl(Carp.pm) perl(Dir/Self.pm) perl(ExtUtils/MakeMaker.pm) perl(Moo.pm) perl(Moose.pm) perl(Moose/Util/TypeConstraints.pm) perl(MooseX/Types.pm) perl(MooseX/Types/Moose.pm) perl(Test/Deep.pm) perl(Test/Fatal.pm) perl(Test/More.pm) perl(XSLoader.pm) perl(aliased.pm) perl(attributes.pm) perl(constant.pm) perl(overload.pm) perl(strict.pm) perl(utf8.pm) perl(warnings.pm)
# END SourceDeps(oneline)
%define _unpackaged_files_terminate_build 1
BuildRequires: rpm-build-perl perl-devel perl-podlators

Name: perl-%module_name
Version: 1.0401
Release: alt2
Summary: subroutine definitions with parameter lists
Group: Development/Perl
License: perl
Url: %CPAN %module_name

Source0: http://cpan.org.ua/authors/id/M/MA/MAUKE/%module_name-%module_version.tar.gz

%description
This module extends Perl with keywords that let you define functions with
parameter lists. It uses Perl's keyword plugin
API, so it works reliably and doesn't require a source filter.


%prep
%setup -n %module_name-%module_version
sed -i -e "s,^'ok'$,1;," lib/Function/Parameters.pm lib/Function/Parameters/*.pm

# TODO
rm t/unicode*.t

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc Changes README
%perl_vendor_archlib/F*
%perl_vendor_autolib/*

%changelog
* Wed Dec 04 2013 Igor Vlasenko <viy@altlinux.ru> 1.0401-alt2
- uploaded to Sisyphus as Scalar-Does dependency

* Thu Oct 10 2013 Igor Vlasenko <viy@altlinux.ru> 1.0401-alt1
- regenerated from template by package builder

* Thu Oct 03 2013 Igor Vlasenko <viy@altlinux.ru> 1.0301-alt1
- initial import by package builder

