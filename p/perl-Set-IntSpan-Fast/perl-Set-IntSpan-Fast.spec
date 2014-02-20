# BEGIN SourceDeps(oneline):
BuildRequires: perl(Data/Types.pm) perl(List/Util.pm) perl(Test/More.pm)
# END SourceDeps(oneline)
%define module_version 1.15
%define module_name Set-IntSpan-Fast
%define _unpackaged_files_terminate_build 1
BuildRequires: rpm-build-perl perl-devel perl-podlators

Name: perl-%module_name
Version: 1.15
Release: alt2
Summary: Fast handling of sets containing integer spans.
Group: Development/Perl
License: perl
Url: %CPAN %module_name

Source0: http://cpan.org.ua/authors/id/A/AN/ANDYA/%module_name-%module_version.tar.gz
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
%perl_vendor_privlib/S*

%changelog
* Thu Feb 20 2014 Igor Vlasenko <viy@altlinux.ru> 1.15-alt2
- moved to Sisyphus for Slic3r (by dd@ request)

* Tue Sep 03 2013 Igor Vlasenko <viy@altlinux.ru> 1.15-alt1
- initial import by package builder

