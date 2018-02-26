Name: perl-iec104
Version: 0.02
Release: alt1

Summary: Perl implementation of IEC 60870-5-104 standard (server and client)

License: GPL, Artistic
Group: Development/Perl
Url: https://github.com/vlet/iec104

Packager: Vladimir Lettiev <crux@altlinux.ru>

Source: iec104-%version.tar.gz

BuildArch: noarch

BuildRequires: perl-devel perl-Event-Lib perl-Date-Manip

%description
This module implement IEC 60870-5-104 standard (also known as
IEC 870-5-104). IEC 870-5-104 is a network access for IEC 60870-5-101
using standard transport profiles (TCP/IP), its application layer is
based on IEC 60870-5-101. IEC 60870-5-104 enables communication between
control station and substation via a standard TCP/IP network. The TCP
protocol is used for connection-oriented secure data transmission.
Current implementation supports only ASDU NN 30,35,36,37,100,103.
Its enough for now.

%prep
%setup -q -n iec104-%version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc Changes README
%perl_vendor_privlib/iec104.pm

%changelog
* Fri Nov 19 2010 Vladimir Lettiev <crux@altlinux.ru> 0.02-alt1
- New version 0.02 from github

* Wed Sep 17 2008 Vladimir Lettiev <crux@altlinux.ru> 0.01-alt1
- Initial build for Sisyphus

