Name: perl-Mojolicious-Plugin-PlainAuth
Version: 0.1
Release: alt1
Summary: Authentication helper from plain text files with hosts/networks or logins/passwords

Group: Development/Perl
License: Perl
Url: http://github.com/kvorg/mojolicious-plugin-tag_helpers_extra

BuildArch: noarch
Source: %name-%version.tar
BuildRequires: perl-Mojolicious perl-NetAddr-IP

%description
%summary

%prep
%setup -q

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%perl_vendor_privlib/Mojolicious/Plugin/*.pm
%doc README.pod

%changelog
* Wed Mar 21 2012 Eugene Prokopiev <enp@altlinux.ru> 0.1-alt1
- initial build for Sisyphus

