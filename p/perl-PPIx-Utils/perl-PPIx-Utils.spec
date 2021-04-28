%define module_name PPIx-Utils
# BEGIN SourceDeps(oneline):
BuildRequires: perl(B/Keywords.pm) perl(Data/Dumper.pm) perl(Exporter.pm) perl(ExtUtils/MakeMaker.pm) perl(File/Spec.pm) perl(PPI.pm) perl(PPI/Dumper.pm) perl(Scalar/Util.pm) perl(Test/More.pm)
# END SourceDeps(oneline)
%define _unpackaged_files_terminate_build 1
BuildRequires: rpm-build-perl perl-devel perl-podlators

Name: perl-%module_name
Version: 0.003
Release: alt2
Summary: Utility functions for PPI
Group: Development/Perl
License: perl
URL: https://github.com/Grinnz/PPIx-Utils

Source0: http://mirror.yandex.ru/mirrors/cpan/authors/id/D/DB/DBOOK/%{module_name}-%{version}.tar.gz
BuildArch: noarch

%description
`PPIx::Utils' is a collection of utility functions for working with the PPI manpage
documents. The functions are organized into submodules, and may be imported
from the appropriate submodule or via this module.

These functions were originally from the Perl::Critic::Utils manpage and related
modules, and have been split off to this distribution for use outside of
the Perl::Critic manpage.
%prep
%setup -q -n %{module_name}-%{version}

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc LICENSE README CONTRIBUTING.md Changes
%perl_vendor_privlib/P*

%changelog
* Wed Apr 28 2021 Igor Vlasenko <viy@altlinux.org> 0.003-alt2
- to Sisyphus as Perl-MinimumVersion dep

* Mon Apr 29 2019 Igor Vlasenko <viy@altlinux.ru> 0.003-alt1
- updated by package builder

* Sat Aug 25 2018 Igor Vlasenko <viy@altlinux.ru> 0.002-alt1
- regenerated from template by package builder

* Thu Aug 03 2017 Igor Vlasenko <viy@altlinux.ru> 0.001-alt1
- initial import by package builder

