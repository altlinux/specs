%define dist Regexp-Bind
Name: perl-%dist
Version: 0.05
Release: alt2

Summary: Bind variables to captured buffers 
License: GPL or Artistic
Group: Development/Perl

URL: %CPAN %dist
Source: %dist-%version.tar.gz

BuildArch: noarch

# Automatically added by buildreq on Tue Oct 04 2011
BuildRequires: perl-devel

%description
This module is an extension to perl's native regexp function. It binds
anonymous hashes or named variables to matched buffers. Both normal
regexp syntax and embedded regexp syntax are supported. You can view
it as a tiny and petite data extraction system.

%prep
%setup -q -n %dist-%version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc Changes README
%perl_vendor_privlib/Regexp

%changelog
* Tue Oct 04 2011 Alexey Tourbin <at@altlinux.ru> 0.05-alt2
- rebuilt

* Mon Jul 17 2006 Alexey Tourbin <at@altlinux.ru> 0.05-alt1
- initial revision
