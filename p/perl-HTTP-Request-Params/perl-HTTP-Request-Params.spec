%define dist HTTP-Request-Params
Name: perl-%dist
Version: 1.01
Release: alt2

Summary: Retrieve GET/POST Parameters from HTTP Requests
License: GPL or Artistic
Group: Development/Perl

URL: %CPAN %dist
Source: %dist-%version.tar.gz

BuildArch: noarch

# Automatically added by buildreq on Tue Oct 04 2011
BuildRequires: perl-CGI perl-Class-Accessor perl-Email-MIME perl-HTTP-Message perl-devel

%description
This software does all the dirty work of parsing HTTP Requests to find
incoming query parameters.

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
* Tue Oct 04 2011 Alexey Tourbin <at@altlinux.ru> 1.01-alt2
- rebuilt

* Mon Jul 17 2006 Alexey Tourbin <at@altlinux.ru> 1.01-alt1
- initial revision
