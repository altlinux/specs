%define _unpackaged_files_terminate_build 1
# BEGIN SourceDeps(oneline):
BuildRequires: perl(Carp.pm) perl(Exporter.pm) perl(ExtUtils/MakeMaker.pm) perl(File/Spec.pm) perl(Pod/Coverage/TrustPod.pm) perl(Scalar/Util.pm) perl(Test/CPAN/Meta.pm) perl(Test/More.pm) perl(Test/Pod.pm) perl(Test/Pod/Coverage.pm) perl(namespace/clean.pm) perl(strict.pm) perl(warnings.pm) perl(Test/NoWarnings.pm)
# END SourceDeps(oneline)
%define module_name Git-Version-Compare
BuildRequires: rpm-build-perl perl-devel perl-podlators

Name: perl-%module_name
Version: 1.005
Release: alt1
Summary: Functions to compare Git versions
Group: Development/Perl
License: perl
Url: %CPAN %module_name

Source0: http://www.cpan.org/authors/id/B/BO/BOOK/%{module_name}-%{version}.tar.gz
BuildArch: noarch

%description
the Git::Version::Compare manpage contains a selection of subroutines that make
dealing with Git-related things (like versions) a little bit easier.

The strings to compare can be version numbers, tags from `git.git'
or the output of `git version' or `git describe'.

These routines collect the knowledge about Git versions that
was accumulated while developing the Git::Repository manpage.
%prep
%setup -q -n %{module_name}-%{version}

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc Changes README
%perl_vendor_privlib/G*

%changelog
* Mon Jan 16 2023 Igor Vlasenko <viy@altlinux.org> 1.005-alt1
- automated CPAN update

* Thu May 26 2016 Igor Vlasenko <viy@altlinux.ru> 1.004-alt1
- automated CPAN update

* Tue May 03 2016 Igor Vlasenko <viy@altlinux.ru> 1.003-alt1
- automated CPAN update

* Mon Mar 28 2016 Igor Vlasenko <viy@altlinux.ru> 1.001-alt2
 - to Sisyphus as dependency

* Tue Mar 22 2016 Igor Vlasenko <viy@altlinux.ru> 1.001-alt1
- initial import by package builder

