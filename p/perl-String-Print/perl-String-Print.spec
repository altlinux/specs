%define _unpackaged_files_terminate_build 1
%define module_name String-Print
# BEGIN SourceDeps(oneline):
BuildRequires: perl(Encode.pm) perl(ExtUtils/MakeMaker.pm) perl(Test/More.pm) perl(Unicode/GCString.pm) perl(HTML/Entities.pm) perl(Date/Parse.pm)
# END SourceDeps(oneline)
BuildRequires: rpm-build-perl perl-devel perl-podlators
BuildRequires: perl-Encode-CN perl-Encode-TW perl-Encode-JP perl-Encode-KR perl-Encode-devel


Name: perl-%module_name
Version: 1.02
Release: alt1
Summary: printf extensions
Group: Development/Perl
License: perl
Url: %CPAN %module_name

Source0: http://www.cpan.org/authors/id/M/MA/MARKOV/%{module_name}-%{version}.tar.gz
BuildArch: noarch

%description
%summary

%prep
%setup -q -n %{module_name}-%{version}

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc ChangeLog README.md
%perl_vendor_privlib/S*

%changelog
* Thu Oct 15 2026 Vitaly Lipatov <lav@altlinux.ru> 1.02-alt1
- new version 1.02

* Wed Sep 17 2025 Igor Vlasenko <viy@altlinux.org> 0.96-alt1
- automated CPAN update

* Tue Mar 03 2020 Igor Vlasenko <viy@altlinux.ru> 0.94-alt1
- automated CPAN update

* Thu Feb 01 2018 Igor Vlasenko <viy@altlinux.ru> 0.93-alt1
- automated CPAN update

* Mon Oct 02 2017 Igor Vlasenko <viy@altlinux.ru> 0.92-alt1
- automated CPAN update

* Mon Jun 23 2014 Igor Vlasenko <viy@altlinux.ru> 0.15-alt1
- regenerated from template by package builder

* Thu Sep 26 2013 Igor Vlasenko <viy@altlinux.ru> 0.12-alt1
- initial import by package builder

