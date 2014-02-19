# BEGIN SourceDeps(oneline):
BuildRequires: perl(Exporter.pm)
# END SourceDeps(oneline)
%define module_version 1.13
%define module_name String-BitCount
%define _unpackaged_files_terminate_build 1
BuildRequires: rpm-build-perl perl-devel perl-podlators

Name: perl-%module_name
Version: 1.13
Release: alt2
Summary: perl module %module_name
Group: Development/Perl
License: perl
Url: %CPAN %module_name

Source0: http://cpan.org.ua/authors/id/W/WI/WINKO/%module_name-%module_version.tar.gz
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
* Wed Feb 19 2014 Igor Vlasenko <viy@altlinux.ru> 1.13-alt2
- moved to Sisyphus for Slic3r (by dd@ request)

* Tue Sep 03 2013 Igor Vlasenko <viy@altlinux.ru> 1.13-alt1
- initial import by package builder

