%define _unpackaged_files_terminate_build 1
%define dist Net-HTTP
Name: perl-%dist
Version: 6.22
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
%doc Changes README.md CONTRIBUTORS
%dir %perl_vendor_privlib/Net
%perl_vendor_privlib/Net/HTTP*
%exclude %perl_vendor_privlib/Net/HTTPS*

%files -n perl-Net-HTTPS
%dir %perl_vendor_privlib/Net
%perl_vendor_privlib/Net/HTTPS*

%changelog
* Thu Jan 27 2022 Igor Vlasenko <viy@altlinux.org> 6.22-alt1
- automated CPAN update

* Wed Mar 24 2021 Igor Vlasenko <viy@altlinux.org> 6.21-alt1
- automated CPAN update

* Tue Jan 12 2021 Igor Vlasenko <viy@altlinux.ru> 6.20-alt1
- automated CPAN update

* Tue May 21 2019 Igor Vlasenko <viy@altlinux.ru> 6.19-alt1
- automated CPAN update

* Thu May 17 2018 Igor Vlasenko <viy@altlinux.ru> 6.18-alt1
- automated CPAN update

* Tue Sep 26 2017 Igor Vlasenko <viy@altlinux.ru> 6.17-alt1
- automated CPAN update

* Wed Aug 02 2017 Igor Vlasenko <viy@altlinux.ru> 6.16-alt1
- automated CPAN update

* Tue May 09 2017 Igor Vlasenko <viy@altlinux.ru> 6.14-alt1
- automated CPAN update

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
