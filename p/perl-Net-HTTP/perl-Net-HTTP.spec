%define _unpackaged_files_terminate_build 1
%define dist Net-HTTP
Name: perl-%dist
Version: 6.13
Release: alt1

Summary: Low-level HTTP connection (client)
License: GPL or Artistic
Group: Development/Perl

URL: %CPAN %dist
Source0: http://www.cpan.org/authors/id/O/OA/OALDERS/%{dist}-%{version}.tar.gz
Patch: %name-6.07-alt.patch

Conflicts: perl-libwww < 6

BuildArch: noarch

# Automatically added by buildreq on Mon Feb 20 2012 (-bi)
BuildRequires: perl-IO-Compress perl-devel perl(IO/Socket/IP.pm) perl(URI.pm)

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
%setup -q -n %{dist}-%{version}
%patch -p1

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc Changes LICENSE README.md CONTRIBUTORS
%dir %perl_vendor_privlib/Net
%perl_vendor_privlib/Net/HTTP*
%exclude %perl_vendor_privlib/Net/HTTPS*

%files -n perl-Net-HTTPS
%dir %perl_vendor_privlib/Net
%perl_vendor_privlib/Net/HTTPS*

%changelog
* Wed Mar 15 2017 Igor Vlasenko <viy@altlinux.ru> 6.13-alt1
- automated CPAN update

* Mon Jan 16 2017 Igor Vlasenko <viy@altlinux.ru> 6.12-alt1
- automated CPAN update

* Fri May 22 2015 Igor Vlasenko <viy@altlinux.ru> 6.09-alt1
- automated CPAN update

* Tue Dec 16 2014 Igor Vlasenko <viy@altlinux.ru> 6.07-alt1
- automated CPAN update

* Sun Sep 15 2013 Igor Vlasenko <viy@altlinux.ru> 6.06-alt1
- automated CPAN update

* Mon Feb 20 2012 Alexey Tourbin <at@altlinux.ru> 6.03-alt1
- 6.01 -> 6.03

* Mon Nov 14 2011 Alexey Tourbin <at@altlinux.ru> 6.01-alt1
- 6.00 -> 6.01
- split perl-Net-HTTPS subpackage

* Mon Mar 21 2011 Alexey Tourbin <at@altlinux.ru> 6.00-alt1
- initial reivision
