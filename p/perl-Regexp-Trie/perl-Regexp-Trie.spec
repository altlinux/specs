# BEGIN SourceDeps(oneline):
BuildRequires: perl(Test/More.pm) perl(Time/HiRes.pm)
# END SourceDeps(oneline)
%define module_version 0.02
%define module_name Regexp-Trie
%define _unpackaged_files_terminate_build 1
BuildRequires: rpm-build-perl perl-devel perl-podlators

Name: perl-%module_name
Version: 0.02
Release: alt2
Summary: perl module %module_name
Group: Development/Perl
License: perl
Url: %CPAN %module_name

Source0: http://cpan.org.ua/authors/id/D/DA/DANKOGAI/%module_name-%module_version.tar.gz
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
%doc Changes README
%perl_vendor_privlib/R*

%changelog
* Mon Feb 25 2019 Igor Vlasenko <viy@altlinux.ru> 0.02-alt2
- to Sisyphus as Module-CPANTS-Analyse dep

* Wed Sep 04 2013 Igor Vlasenko <viy@altlinux.ru> 0.02-alt1
- initial import by package builder

