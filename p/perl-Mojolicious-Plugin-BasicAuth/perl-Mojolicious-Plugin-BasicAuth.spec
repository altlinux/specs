%define _unpackaged_files_terminate_build 1
%define dist Mojolicious-Plugin-BasicAuth

Name: perl-%dist
Version: 0.08
Release: alt1
Summary: helper for basic http authentication

Group: Development/Perl
License: Perl
Url: %CPAN %dist

BuildArch: noarch
Source: http://www.cpan.org/authors/id/T/TE/TEMPIRE/Mojolicious-Plugin-BasicAuth-%{version}.tar.gz
BuildRequires: perl-Mojolicious perl(Pod/Text.pm)

%description
%name

%prep
%setup -q -n %dist-%version

%build
%perl_vendor_build INSTALLMAN1DIR=%_man1dir

%install
%perl_vendor_install

rm %buildroot%perl_vendor_privlib/Mojolicious/Plugin/README.pod

%files
%perl_vendor_privlib/Mojolicious/Plugin/*.pm
%doc README.pod

%changelog
* Tue Dec 16 2014 Igor Vlasenko <viy@altlinux.ru> 0.08-alt1
- automated CPAN update

* Fri Oct 04 2013 Igor Vlasenko <viy@altlinux.ru> 0.07-alt1
- automated CPAN update

* Wed Mar 07 2012 Eugene Prokopiev <enp@altlinux.ru> 0.06-alt1
- initail build for Sisyphus


