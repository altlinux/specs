%define dist HTTP-Message
Name: perl-%dist
Version: 6.03
Release: alt1

Summary: HTTP style messages
License: GPL or Artistic
Group: Development/Perl

URL: %CPAN %dist
Source: %dist-%version.tar.gz

Conflicts: perl-libwww < 6

BuildArch: noarch

# Automatically added by buildreq on Mon Feb 20 2012
BuildRequires: perl-Encode-Locale perl-HTML-Parser perl-HTTP-Date perl-IO-Compress perl-LWP-MediaTypes perl-devel

%description
An HTTP::Message object contains some headers and a content body.
The following methods are available:

%prep
%setup -q -n %dist-%version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc Changes README
%perl_vendor_privlib/HTTP

%changelog
* Mon Feb 20 2012 Alexey Tourbin <at@altlinux.ru> 6.03-alt1
- 6.02 -> 6.03

* Mon Nov 14 2011 Alexey Tourbin <at@altlinux.ru> 6.02-alt3
- rebuilt as plain src.rpm

* Tue Mar 22 2011 Alexey Tourbin <at@altlinux.ru> 6.02-alt2
- HTTP/Headers.pm: enabled explicit dependency on Sotrable

* Mon Mar 21 2011 Alexey Tourbin <at@altlinux.ru> 6.02-alt1
- initial revision
