%define _unpackaged_files_terminate_build 1

Name: perl-Mojolicious-Plugin-OAuth2
Version: 1.58
Release: alt1
Summary: A Mojolicious plugin that allows OAuth2 authentication
License: Artistic-2.0
Group: Development/Perl
Url: https://github.com/marcusramberg/Mojolicious-Plugin-OAuth2
Source: %name-%version.tar
BuildArch: noarch

BuildRequires: perl(ExtUtils/MakeMaker.pm) 
BuildRequires: perl(Mojo/Base.pm)
BuildRequires: perl(Mojolicious/Lite.pm)
BuildRequires: perl(IO/Socket/SSL.pm)

Requires:  perl(IO/Socket/SSL.pm)
Requires:  perl(Mojolicious.pm)
Requires:  perl(Mojolicious/Plugin.pm)

%description
This Mojolicious plugin allows you to easily authenticate against a OAuth2
provider. It includes configurations for a few popular providers, but you can
add your own easily as well.

%prep
%setup

%build
%perl_vendor_build

%install
%perl_vendor_install
rm -f %buildroot%perl_vendorlib/Mojolicious/Plugin/README.pod

%files
%doc Changes
%perl_vendorlib/Mojolicious/Plugin*

%changelog
* Wed Jul 15 2020 Alexandr Antonov <aas@altlinux.org> 1.58-alt1
- initial build for ALT
