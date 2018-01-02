# BEGIN SourceDeps(oneline):
BuildRequires: perl(Test/More.pm)
# END SourceDeps(oneline)
%define module_version 0.2
%define module_name Path-Iter
%define _unpackaged_files_terminate_build 1
BuildRequires: rpm-build-perl perl-devel perl-podlators

Name: perl-%module_name
Version: 0.2
Release: alt2
Summary: perl module %module_name
Group: Development/Perl
License: perl
Url: %CPAN %module_name

Source0: http://cpan.org.ua/authors/id/D/DM/DMUEY/%module_name-%module_version.tar.gz
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
%perl_vendor_privlib/P*

%changelog
* Tue Jan 02 2018 Igor Vlasenko <viy@altlinux.ru> 0.2-alt2
- to Sisyphus as File-Copy-Recursive dep

* Wed Sep 04 2013 Igor Vlasenko <viy@altlinux.ru> 0.2-alt1
- initial import by package builder

