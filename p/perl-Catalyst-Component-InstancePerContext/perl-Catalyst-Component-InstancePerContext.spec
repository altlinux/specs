%define dist Catalyst-Component-InstancePerContext
Name: perl-%dist
Version: 0.001001
Release: alt1

Summary: Moose role to create only one instance of component per context
License: GPL or Artistic
Group: Development/Perl

URL: %CPAN %dist
Source: %dist-%version.tar.gz

BuildArch: noarch

# Automatically added by buildreq on Tue Nov 15 2011
BuildRequires: perl-Catalyst-Runtime

%description
Catalyst::Component::InstancePerContext -
Return a new instance a component on each request

%prep
%setup -q -n %dist-%version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc Changes README
%perl_vendor_privlib/Catalyst

%changelog
* Tue Nov 15 2011 Alexey Tourbin <at@altlinux.ru> 0.001001-alt1
- initial revision
