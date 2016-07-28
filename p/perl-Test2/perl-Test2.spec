%define module_version 0.000044
%define module_name Test2
# BEGIN SourceDeps(oneline):
BuildRequires: perl(Carp.pm) perl(ExtUtils/MakeMaker.pm) perl(File/Spec.pm) perl(File/Temp.pm) perl(IPC/SysV.pm) perl(PerlIO.pm) perl(Scalar/Util.pm) perl(Storable.pm) perl(threads.pm) perl(utf8.pm)
# END SourceDeps(oneline)
%define _unpackaged_files_terminate_build 1
BuildRequires: rpm-build-perl perl-devel perl-podlators

Name: perl-%module_name
Version: 0.000044
Release: alt2
Summary: Just grabbing the namespace
Group: Development/Perl
License: perl
Url: %CPAN %module_name

Source0: http://mirror.yandex.ru/mirrors/cpan/authors/id/E/EX/EXODIST/%{module_name}-%{module_version}.tar.gz
BuildArch: noarch

%description
From summary: %summary

%prep
%setup -q -n %{module_name}-%{module_version}

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc README.md Changes README LICENSE Examples
%perl_vendor_privlib/T*

%changelog
* Thu Jul 28 2016 Igor Vlasenko <viy@altlinux.ru> 0.000044-alt2
- to Sisyphus

* Tue May 03 2016 Igor Vlasenko <viy@altlinux.ru> 0.000044-alt1
- regenerated from template by package builder

* Thu Apr 07 2016 Igor Vlasenko <viy@altlinux.ru> 0.000039-alt1
- regenerated from template by package builder

* Sun Mar 27 2016 Igor Vlasenko <viy@altlinux.ru> 0.000031-alt1
- regenerated from template by package builder

* Sat Mar 19 2016 Igor Vlasenko <viy@altlinux.ru> 0.000030-alt1
- regenerated from template by package builder

* Fri Feb 19 2016 Igor Vlasenko <viy@altlinux.ru> 0.000025-alt1
- regenerated from template by package builder

* Thu Dec 17 2015 Igor Vlasenko <viy@altlinux.ru> 0.000006-alt1
- regenerated from template by package builder

* Tue Dec 15 2015 Igor Vlasenko <viy@altlinux.ru> 0.000005-alt1
- regenerated from template by package builder

* Fri May 22 2015 Igor Vlasenko <viy@altlinux.ru> 0.000003-alt1
- initial import by package builder

