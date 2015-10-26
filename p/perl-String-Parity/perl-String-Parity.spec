%define _unpackaged_files_terminate_build 1
# BEGIN SourceDeps(oneline):
BuildRequires: perl(Exporter.pm)
# END SourceDeps(oneline)
%define module_version 1.33
%define module_name String-Parity
BuildRequires: rpm-build-perl perl-devel perl-podlators

Name: perl-%module_name
Version: 1.33
Release: alt1
Summary: perl module %module_name
Group: Development/Perl
License: perl
Url: %CPAN %module_name

Source: http://www.cpan.org/authors/id/N/NE/NEILB/String-Parity-%{version}.tar.gz
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
* Mon Oct 26 2015 Igor Vlasenko <viy@altlinux.ru> 1.33-alt1
- automated CPAN update

* Sat Mar 29 2014 Igor Vlasenko <viy@altlinux.ru> 1.32-alt1
- automated CPAN update

* Wed Feb 19 2014 Igor Vlasenko <viy@altlinux.ru> 1.31-alt2
- moved to Sisyphus for Slic3r (by dd@ request)

* Tue Sep 03 2013 Igor Vlasenko <viy@altlinux.ru> 1.31-alt1
- initial import by package builder

