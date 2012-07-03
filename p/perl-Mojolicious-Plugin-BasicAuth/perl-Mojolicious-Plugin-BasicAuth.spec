%define dist Mojolicious-Plugin-BasicAuth

Name: perl-%dist
Version: 0.06
Release: alt1
Summary: helper for basic http authentication

Group: Development/Perl
License: Perl
Url: %CPAN %dist

BuildArch: noarch
Source: %name-%version.tar
BuildRequires: perl-Mojolicious

%description
%name

%prep
%setup -q

%build
%perl_vendor_build INSTALLMAN1DIR=%_man1dir

%install
%perl_vendor_install

%files
%perl_vendor_privlib/Mojolicious/Plugin/*.pm
%doc README.pod

%changelog
* Wed Mar 07 2012 Eugene Prokopiev <enp@altlinux.ru> 0.06-alt1
- initail build for Sisyphus


