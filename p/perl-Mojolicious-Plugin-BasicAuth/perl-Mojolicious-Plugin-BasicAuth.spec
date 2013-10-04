%define dist Mojolicious-Plugin-BasicAuth

Name: perl-%dist
Version: 0.07
Release: alt1
Summary: helper for basic http authentication

Group: Development/Perl
License: Perl
Url: %CPAN %dist

BuildArch: noarch
Source: http://www.cpan.org/authors/id/T/TE/TEMPIRE/Mojolicious-Plugin-BasicAuth-%{version}.tar.gz
BuildRequires: perl-Mojolicious

%description
%name

%prep
%setup -q -n %dist-%version

%build
%perl_vendor_build INSTALLMAN1DIR=%_man1dir

%install
%perl_vendor_install

%files
%perl_vendor_privlib/Mojolicious/Plugin/*.pm
%doc README.pod

%changelog
* Fri Oct 04 2013 Igor Vlasenko <viy@altlinux.ru> 0.07-alt1
- automated CPAN update

* Wed Mar 07 2012 Eugene Prokopiev <enp@altlinux.ru> 0.06-alt1
- initail build for Sisyphus


