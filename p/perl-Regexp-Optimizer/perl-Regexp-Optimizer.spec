# BEGIN SourceDeps(oneline):
BuildRequires: perl(Regexp/Assemble.pm) perl(Test/More.pm) perl(re.pm)
# END SourceDeps(oneline)
%define module_version 0.23
%define module_name Regexp-Optimizer
%define _unpackaged_files_terminate_build 1
BuildRequires: rpm-build-perl perl-devel perl-podlators

Name: perl-%module_name
Version: 0.23
Release: alt2
Summary: optimizes regular expressions
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
%doc README Changes
%perl_vendor_privlib/R*

%changelog
* Sat Mar 17 2018 Igor Vlasenko <viy@altlinux.ru> 0.23-alt2
- to Sisyphus as firefox-noscript dep

* Wed Sep 04 2013 Igor Vlasenko <viy@altlinux.ru> 0.23-alt1
- initial import by package builder

