%define module_version 1.302016
%define module_name Test-Stream
%filter_from_requires /^perl.Sub.Util.pm/d
# BEGIN SourceDeps(oneline):
BuildRequires: perl(B.pm) perl(Carp.pm) perl(Config.pm) perl(ExtUtils/MakeMaker.pm) perl(File/Spec.pm) perl(File/Temp.pm) perl(List/Util.pm) perl(PerlIO.pm) perl(Scalar/Util.pm) perl(Storable.pm) perl(Test/Harness.pm) perl(Unicode/GCString.pm) perl(base.pm) perl(overload.pm) perl(threads.pm) perl(threads/shared.pm) perl(utf8.pm)
# END SourceDeps(oneline)
%define _unpackaged_files_terminate_build 1
BuildRequires: rpm-build-perl perl-devel perl-podlators

Name: perl-%module_name
Version: 1.302016
Release: alt1
Summary: Comming soon
Group: Development/Perl
License: perl
Url: %CPAN %module_name

Source0: http://cpan.org.ua/authors/id/E/EX/EXODIST/%{module_name}-%{module_version}.tar.gz
BuildArch: noarch

%description
From summary: %summary

%prep
%setup -n %{module_name}-%{module_version}
# TODO fix
rm -f t/modules/Table.t

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc TODO LICENSE README Changes
%perl_vendor_privlib/T*

%changelog
* Thu Oct 15 2015 Igor Vlasenko <viy@altlinux.ru> 1.302016-alt1
- regenerated from template by package builder

* Mon Jan 05 2015 Igor Vlasenko <viy@altlinux.ru> 0.000003-alt1
- regenerated from template by package builder

* Thu Sep 04 2014 Igor Vlasenko <viy@altlinux.ru> 0.000002-alt1
- initial import by package builder

