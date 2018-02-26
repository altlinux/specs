%define dist Module-Install-AutoManifest
Name: perl-%dist
Version: 0.003
Release: alt2

Summary: generate MANIFEST automatically
License: GPL or Artistic
Group: Development/Perl

URL: %CPAN %dist
Source: %dist-%version.tar.gz

BuildArch: noarch

# Automatically added by buildreq on Tue Nov 15 2011 (-bi)
BuildRequires: perl-Module-Install

%description
This extension to Module::Install adds behavior for automatically generating
MANIFEST.

%prep
%setup -q -n %dist-%version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc Changes README
%perl_vendor_privlib/Module

%changelog
* Tue Nov 15 2011 Alexey Tourbin <at@altlinux.ru> 0.003-alt2
- rebuilt as plain src.rpm

* Wed Mar 24 2010 Alexey Tourbin <at@altlinux.ru> 0.003-alt1
- initial revision
