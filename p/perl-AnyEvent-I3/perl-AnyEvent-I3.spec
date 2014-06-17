Name: perl-AnyEvent-I3
Version: 0.12
Release: alt1
Summary: AnyEvent::I3 - module for communication with the i3 window manager

Group: Development/Perl
License: Perl
Url: %CPAN AnyEvent-I3

BuildArch: noarch
Source: %name-%version.tar

BuildRequires: i3 perl-JSON-XS perl-Pod-Escapes perl-AnyEvent perl-devel

%description
%summary

%prep
%setup -q

%build

%perl_vendor_build

%install
%perl_vendor_install

%files
%perl_vendor_privlib/AnyEvent/I3*
%doc Changes README

%changelog
* Tue Jun 17 2014 Andrey Bergman <vkni@altlinux.org> 0.12-alt1
- Initial release for Sisyphus

