# BEGIN SourceDeps(oneline):
BuildRequires: perl(Exporter.pm) perl(Module/Build.pm) perl(Test/More.pm)
# END SourceDeps(oneline)
%define module_version 0.01
%define module_name List-PowerSet
%define _unpackaged_files_terminate_build 1
BuildRequires: rpm-build-perl perl-devel perl-podlators

Name: perl-%module_name
Version: 0.01
Release: alt2
Summary: perl module %module_name
Group: Development/Perl
License: perl
Url: %CPAN %module_name

Source0: http://cpan.org.ua/authors/id/N/NI/NIKC/%module_name-%module_version.tar.gz
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
%perl_vendor_privlib/L*

%changelog
* Mon Mar 21 2016 Igor Vlasenko <viy@altlinux.ru> 0.01-alt2
- to Sisyphus

* Wed Sep 04 2013 Igor Vlasenko <viy@altlinux.ru> 0.01-alt1
- initial import by package builder

