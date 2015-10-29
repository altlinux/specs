%define _unpackaged_files_terminate_build 1
%define dist Mojolicious-Plugin-Authentication

Name: perl-%dist
Version: 1.29
Release: alt1
Summary: A plugin to make authentication a bit easier

Group: Development/Perl
License: Perl
Url: %CPAN %dist

BuildArch: noarch
Source: http://www.cpan.org/authors/id/M/MA/MADCAT/Mojolicious-Plugin-Authentication-%{version}.tar.gz
BuildRequires: perl-Module-Build perl-Mojolicious

%description
%summary

%prep
%setup -q -n %dist-%version

%build
%perl_vendor_build INSTALLMAN1DIR=%_man1dir

%install
%perl_vendor_install
rm -f %buildroot/%perl_vendor_privlib/Mojolicious/Plugin/README.pod

%files
%doc README*
%perl_vendor_privlib/Mojolicious/Plugin/*.pm

%changelog
* Thu Oct 29 2015 Igor Vlasenko <viy@altlinux.ru> 1.29-alt1
- automated CPAN update

* Sun Oct 11 2015 Igor Vlasenko <viy@altlinux.ru> 1.28-alt1
- automated CPAN update

* Fri Oct 04 2013 Igor Vlasenko <viy@altlinux.ru> 1.26-alt1
- automated CPAN update

* Sun Mar 11 2012 Eugene Prokopiev <enp@altlinux.ru> 1.21-alt1
- initail build for Sisyphus

