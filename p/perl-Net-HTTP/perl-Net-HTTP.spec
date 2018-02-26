%define dist Net-HTTP
Name: perl-%dist
Version: 6.03
Release: alt1

Summary: Low-level HTTP connection (client)
License: GPL or Artistic
Group: Development/Perl

URL: %CPAN %dist
Source: %dist-%version.tar
Patch: %name-%version-%release.patch

Conflicts: perl-libwww < 6

BuildArch: noarch

# Automatically added by buildreq on Mon Feb 20 2012 (-bi)
BuildRequires: perl-IO-Compress perl-devel

%package -n perl-Net-HTTPS
Summary: Low-level HTTP connection (client)
Group: Development/Perl
Requires: %name = %version-%release

%description
The Net::HTTP class is a low-level HTTP client.  An instance
of the Net::HTTP class represents a connection to an HTTP server.
The HTTP protocol is described in RFC 2616.  The Net::HTTP class
supports HTTP/1.0 and HTTP/1.1.

%description -n perl-Net-HTTPS
The Net::HTTP class is a low-level HTTP client.  An instance
of the Net::HTTP class represents a connection to an HTTP server.
The HTTP protocol is described in RFC 2616.  The Net::HTTP class
supports HTTP/1.0 and HTTP/1.1.

%prep
%setup -q -n %dist-%version
%patch -p1

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc Changes README
%dir %perl_vendor_privlib/Net
%perl_vendor_privlib/Net/HTTP*
%exclude %perl_vendor_privlib/Net/HTTPS*

%files -n perl-Net-HTTPS
%dir %perl_vendor_privlib/Net
%perl_vendor_privlib/Net/HTTPS*

%changelog
* Mon Feb 20 2012 Alexey Tourbin <at@altlinux.ru> 6.03-alt1
- 6.01 -> 6.03

* Mon Nov 14 2011 Alexey Tourbin <at@altlinux.ru> 6.01-alt1
- 6.00 -> 6.01
- split perl-Net-HTTPS subpackage

* Mon Mar 21 2011 Alexey Tourbin <at@altlinux.ru> 6.00-alt1
- initial reivision
