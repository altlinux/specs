%define module_name ExtUtils-HasCompiler
# BEGIN SourceDeps(oneline):
BuildRequires: perl(Carp.pm) perl(Cwd.pm) perl(DynaLoader.pm) perl(Exporter.pm) perl(ExtUtils/MakeMaker.pm) perl(ExtUtils/Mksymlists.pm) perl(File/Basename.pm) perl(File/Path.pm) perl(File/Spec.pm) perl(File/Spec/Functions.pm) perl(File/Temp.pm) perl(IO/Handle.pm) perl(IPC/Open3.pm) perl(Test/More.pm) perl(base.pm) perl(strict.pm) perl(warnings.pm)
# END SourceDeps(oneline)
%define _unpackaged_files_terminate_build 1
BuildRequires: rpm-build-perl perl-devel perl-podlators

Name: perl-%module_name
Version: 0.025
Release: alt2
Summary: Check for the presence of a compiler
Group: Development/Perl
License: perl
Url: %CPAN %module_name

Source0: http://mirror.yandex.ru/mirrors/cpan/authors/id/L/LE/LEONT/%{module_name}-%{version}.tar.gz
BuildArch: noarch

%description
From summary: %summary

%prep
%setup -q -n %{module_name}-%{version}

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc LICENSE README Changes
%perl_vendor_privlib/E*

%changelog
* Wed Apr 09 2025 Igor Vlasenko <viy@altlinux.org> 0.025-alt2
- to Sisyphus as Module-Build-Tiny dep

* Mon Apr 07 2025 Igor Vlasenko <viy@altlinux.org> 0.025-alt1
- updated by package builder

* Sat Dec 26 2020 Igor Vlasenko <viy@altlinux.ru> 0.023-alt1
- updated by package builder

* Tue Jul 21 2020 Igor Vlasenko <viy@altlinux.ru> 0.022-alt1
- updated by package builder

* Wed Aug 02 2017 Igor Vlasenko <viy@altlinux.ru> 0.021-alt1
- regenerated from template by package builder

* Tue Feb 14 2017 Igor Vlasenko <viy@altlinux.ru> 0.017-alt1
- regenerated from template by package builder

* Wed Jul 06 2016 Igor Vlasenko <viy@altlinux.ru> 0.016-alt1
- regenerated from template by package builder

* Tue May 03 2016 Igor Vlasenko <viy@altlinux.ru> 0.014-alt1
- regenerated from template by package builder

* Wed Oct 14 2015 Igor Vlasenko <viy@altlinux.ru> 0.012-alt1
- regenerated from template by package builder

* Fri May 22 2015 Igor Vlasenko <viy@altlinux.ru> 0.002-alt1
- initial import by package builder

