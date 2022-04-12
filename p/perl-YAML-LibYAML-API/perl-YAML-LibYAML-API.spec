%define _unpackaged_files_terminate_build 1
%define module_name YAML-LibYAML-API
# BEGIN SourceDeps(oneline):
BuildRequires: libsowing-devel libyaml-devel perl(Encode.pm) perl(Encode/CN.pm) perl(Encode/JP.pm) perl(Encode/KR.pm) perl(Encode/TW.pm) perl(ExtUtils/MakeMaker.pm) perl(File/Spec.pm) perl(FindBin.pm) perl(IO/Handle.pm) perl(IPC/Open3.pm) perl(Test/More.pm) perl(XSLoader.pm) perl(YAML/PP.pm) perl(YAML/PP/Common.pm) perl(strict.pm) perl(warnings.pm)
# END SourceDeps(oneline)
BuildRequires: rpm-build-perl perl-devel perl-podlators

Name: perl-%module_name
Version: 0.013
Release: alt1
Summary: Wrapper around the C libyaml library
Group: Development/Perl
License: perl
Url: %CPAN %module_name

Source0: http://www.cpan.org/authors/id/T/TI/TINITA/%{module_name}-%{version}.tar.gz

%description
This module provides a thin wrapper around the C libyaml API.

Currently it provides functions for parsing and emitting events.

libyaml also provides a loader/dumper API to load/dump YAML into a list
of nodes. There's no wrapper for these functions yet.

This is just one of the first releases. The function names will eventually be
changed.

`libyaml-dev' has to be installed. It might be included in a future release.

%prep
%setup -q -n %{module_name}-%{version}

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc Changes README
%perl_vendor_archlib/Y*
%perl_vendor_autolib/*

%changelog
* Tue Apr 12 2022 Igor Vlasenko <viy@altlinux.org> 0.013-alt1
- automated CPAN update

* Tue May 18 2021 Igor Vlasenko <viy@altlinux.org> 0.012-alt3
- to Sisyphus as YAML-PP dep

* Thu Oct 01 2020 Igor Vlasenko <viy@altlinux.ru> 0.012-alt2
- rebuild with perl 5.30

* Tue Sep 08 2020 Igor Vlasenko <viy@altlinux.ru> 0.012-alt1
- updated by package builder

* Fri Aug 28 2020 Igor Vlasenko <viy@altlinux.ru> 0.010-alt1
- updated by package builder

* Mon May 18 2020 Igor Vlasenko <viy@altlinux.ru> 0.009-alt1
- updated by package builder

* Mon Feb 24 2020 Igor Vlasenko <viy@altlinux.ru> 0.008-alt1
- updated by package builder

* Sat Jul 13 2019 Igor Vlasenko <viy@altlinux.ru> 0.007-alt1
- updated by package builder

* Fri Jun 21 2019 Igor Vlasenko <viy@altlinux.ru> 0.006-alt1
- updated by package builder

* Sun May 26 2019 Igor Vlasenko <viy@altlinux.ru> 0.005-alt1
- updated by package builder

* Sun May 12 2019 Igor Vlasenko <viy@altlinux.ru> 0.004-alt1
- updated by package builder

* Fri Feb 01 2019 Cronbuild Service <cronbuild@altlinux.org> 0.003-alt1.1
- rebuild with perl 5.28.1

* Tue Oct 02 2018 Igor Vlasenko <viy@altlinux.ru> 0.003-alt1
- initial import by package builder

