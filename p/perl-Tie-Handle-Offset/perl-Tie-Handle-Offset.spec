# BEGIN SourceDeps(oneline):
BuildRequires: perl(Test/More.pm)
# END SourceDeps(oneline)
%define module_version 0.003
%define module_name Tie-Handle-Offset
%define _unpackaged_files_terminate_build 1
BuildRequires: rpm-build-perl perl-devel perl-podlators

Name: perl-%module_name
Version: 0.003
Release: alt2
Summary: Tied handle that hides the beginning of a file
Group: Development/Perl
License: apache
URL: https://github.com/dagolden/tie-handle-offset

Source0: http://cpan.org.ua/authors/id/D/DA/DAGOLDEN/%module_name-%module_version.tar.gz
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
%doc LICENSE README Changes README.PATCHING
%perl_vendor_privlib/T*

%changelog
* Sat Dec 20 2014 Igor Vlasenko <viy@altlinux.ru> 0.003-alt2
- moved to Sisyphus as dependency

* Tue Sep 03 2013 Igor Vlasenko <viy@altlinux.ru> 0.003-alt1
- initial import by package builder

