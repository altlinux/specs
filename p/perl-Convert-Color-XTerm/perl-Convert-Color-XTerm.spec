%define module_name Convert-Color-XTerm
# BEGIN SourceDeps(oneline):
BuildRequires: perl(Convert/Color.pm) perl(Module/Build.pm) perl(Test/More.pm) perl(base.pm)
# END SourceDeps(oneline)
%define _unpackaged_files_terminate_build 1
BuildRequires: rpm-build-perl perl-devel perl-podlators

Name: perl-%module_name
Version: 0.06
Release: alt2
Summary: indexed colors used by XTerm
Group: Development/Perl
License: perl
Url: %CPAN %module_name

Source0: http://mirror.yandex.ru/mirrors/cpan/authors/id/P/PE/PEVANS/%{module_name}-%{version}.tar.gz
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
%doc LICENSE Changes README examples
%perl_vendor_privlib/C*

%changelog
* Wed Nov 24 2021 Igor Vlasenko <viy@altlinux.org> 0.06-alt2
- to Sisyphus for libtickit

* Thu Jul 01 2021 Igor Vlasenko <viy@altlinux.ru> 0.06-alt1
- updated by package builder

* Thu Sep 19 2013 Igor Vlasenko <viy@altlinux.ru> 0.05-alt1
- initial import by package builder

