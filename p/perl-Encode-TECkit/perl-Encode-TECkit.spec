%define dist Encode-TECkit
Name: perl-%dist
Version: 0.04
Release: alt1.2

Summary: TECkit Encode interface
License: GPL or Artistic
Group: Development/Perl

URL: %CPAN %dist
Source: %dist-%version.tar.gz
Patch: perl-Encode-TECkit.patch

# Automatically added by buildreq on Sat Oct 08 2011
BuildRequires: gcc-c++ libteckit-devel perl-devel zlib-devel

%description
This module interfaces with the TECkit processor to provide a Perl
interface for data conversion.

TECkit is a binary encoding converter designed to handle complex
encoding conversions requiring multiple passes over the data and
contextual data conversion.

%prep
%setup -q -n %dist-%version
%patch

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%perl_vendor_archlib/Encode
%perl_vendor_autolib/Encode

%changelog
* Sat Oct 08 2011 Alexey Tourbin <at@altlinux.ru> 0.04-alt1.2
- rebuilt for perl-5.14

* Sat Nov 06 2010 Vladimir Lettiev <crux@altlinux.ru> 0.04-alt1.1
- rebuilt with perl 5.12

* Fri Mar 27 2009 Vitaly Lipatov <lav@altlinux.ru> 0.04-alt1
- initial build for ALT Linux Sisyphus
