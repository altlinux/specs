# BEGIN SourceDeps(oneline):
BuildRequires: perl(ExtUtils/Typemaps.pm) perl(ExtUtils/Typemaps/InputMap.pm) perl(ExtUtils/Typemaps/OutputMap.pm) perl(ExtUtils/Typemaps/Type.pm) perl(Test/More.pm)
# END SourceDeps(oneline)
%define module_version 1.00
%define module_name ExtUtils-Typemap
%define _unpackaged_files_terminate_build 1
BuildRequires: rpm-build-perl perl-devel perl-podlators

Name: perl-%module_name
Version: 1.00
Release: alt2
Summary: Read/Write/Modify Perl/XS typemap files
Group: Development/Perl
License: perl
Url: %CPAN %module_name

Source0: http://cpan.org.ua/authors/id/S/SM/SMUELLER/%module_name-%module_version.tar.gz
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
%perl_vendor_privlib/E*

%changelog
* Wed Feb 26 2014 Igor Vlasenko <viy@altlinux.ru> 1.00-alt2
- moved to Sisyphus for Slic3r (by dd@ request)

* Fri Sep 06 2013 Igor Vlasenko <viy@altlinux.ru> 1.00-alt1
- initial import by package builder

