%define dist IRC-Utils
Name: perl-%dist
Version: 0.12
Release: alt1

Summary: Common utilities for IRC-related tasks
License: GPL or Artistic
Group: Development/Perl

URL: %CPAN %dist
Source: %dist-%version.tar.gz

BuildArch: noarch

# Automatically added by buildreq on Sun Nov 20 2011
BuildRequires: perl-Encode perl-devel

%description
The functions in this module take care of many of the tasks you are faced
with when working with IRC.  Mode lines, ban masks, message encoding and
formatting, etc.

%prep
%setup -q -n %dist-%version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc Changes README
%perl_vendor_privlib/IRC

%changelog
* Sun Nov 20 2011 Alexey Tourbin <at@altlinux.ru> 0.12-alt1
- initial revision
