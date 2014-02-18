# BEGIN SourceDeps(oneline):
BuildRequires: perl(DBI.pm)
# END SourceDeps(oneline)
%define module_version 1.36
%define module_name DBIx-XHTML_Table
%define _unpackaged_files_terminate_build 1
BuildRequires: rpm-build-perl perl-devel perl-podlators

Name: perl-%module_name
Version: 1.36
Release: alt2
Summary: perl module %module_name
Group: Development/Perl
License: perl
Url: %CPAN %module_name

Source0: http://cpan.org.ua/authors/id/J/JE/JEFFA/%module_name-%module_version.tar.gz
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
%perl_vendor_privlib/D*

%changelog
* Tue Feb 18 2014 Igor Vlasenko <viy@altlinux.ru> 1.36-alt2
- moved to Sisyphus for Slic3r (by dd@ request)

* Fri Sep 06 2013 Igor Vlasenko <viy@altlinux.ru> 1.36-alt1
- initial import by package builder

