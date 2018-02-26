%define dist Sys-Virt
Name: perl-%dist
Version: 0.9.5
Release: alt1

Summary: Represent and manage a libvirt hypervisor connection
License: GPL or Artistic
Group: Development/Perl

URL: %CPAN %dist
Source: %dist-%version.tar.gz

# Automatically added by buildreq on Wed Oct 19 2011
BuildRequires: libvirt-devel perl-Test-Pod perl-Test-Pod-Coverage perl-XML-XPath

%description
The Sys::Virt module provides a Perl XS binding to the libvirt
virtual machine management APIs. This allows machines running
within arbitrary virtualization containers to be managed with
a consistent API.

%prep
%setup -q -n %dist-%version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc AUTHORS CHANGES README examples
%perl_vendor_archlib/Sys
%perl_vendor_autolib/Sys

%changelog
* Wed Oct 19 2011 Alexey Tourbin <at@altlinux.ru> 0.9.5-alt1
- 0.2.6 -> 0.9.5
- built for perl-5.14

* Tue Apr 19 2011 Alexey Shabalin <shaba@altlinux.ru> 0.2.6-alt1
- 0.2.6

* Thu Nov 04 2010 Vladimir Lettiev <crux@altlinux.ru> 0.2.2-alt1.1
- rebuilt with perl 5.12

* Thu Oct 29 2009 Andriy Stepanov <stanv@altlinux.ru> 0.2.2-alt1
- Package for ALT Linux.
