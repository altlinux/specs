# BEGIN SourceDeps(oneline):
BuildRequires: perl(Exporter.pm) perl(ExtUtils/MakeMaker.pm) perl(List/MoreUtils.pm) perl(List/Util.pm) perl(Module/Runtime.pm) perl(Role/Tiny.pm) perl(Role/Tiny/With.pm) perl(Scalar/Util.pm) perl(Test/Deep.pm) perl(Test/Fatal.pm) perl(Test/More.pm) perl(Test/Output.pm) perl(parent.pm) perl(strictures.pm)
# END SourceDeps(oneline)
%define module_version 0.002008
%define module_name Data-Perl
%define _unpackaged_files_terminate_build 1
BuildRequires: rpm-build-perl perl-devel perl-podlators

Name: perl-%module_name
Version: 0.002008
Release: alt1
Summary: Base classes wrapping fundamental Perl data types.
Group: Development/Perl
License: perl
Url: %CPAN %module_name

Source: http://www.cpan.org/authors/id/M/MA/MATTP/Data-Perl-%{version}.tar.gz
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
%doc Changes README LICENSE README.mkdn
%perl_vendor_privlib/D*

%changelog
* Thu Jun 26 2014 Igor Vlasenko <viy@altlinux.ru> 0.002008-alt1
- automated CPAN update

* Mon Mar 24 2014 Igor Vlasenko <viy@altlinux.ru> 0.002007-alt2
- moved to Sisyphus for perl update

* Thu Sep 26 2013 Igor Vlasenko <viy@altlinux.ru> 0.002007-alt1
- initial import by package builder

