%define _unpackaged_files_terminate_build 1
%define dist HTTP-Message
Name: perl-%dist
Version: 6.14
Release: alt1

Summary: HTTP style messages
License: GPL or Artistic
Group: Development/Perl

URL: %CPAN %dist
Source0: http://www.cpan.org/authors/id/O/OA/OALDERS/%{dist}-%{version}.tar.gz

Conflicts: perl-libwww < 6
Provides: perl(HTTP/Request/Common.pm) = 6.060

BuildArch: noarch

# Automatically added by buildreq on Mon Feb 20 2012
BuildRequires: perl-Encode-Locale perl-HTML-Parser perl-HTTP-Date perl-IO-Compress perl-LWP-MediaTypes perl-devel perl(IO/HTML.pm) perl(Try/Tiny.pm)

%description
An HTTP::Message object contains some headers and a content body.
The following methods are available:

%prep
%setup -q -n %{dist}-%{version}

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc Changes CONTRIBUTORS README.md
%perl_vendor_privlib/HTTP

%changelog
* Tue Dec 26 2017 Igor Vlasenko <viy@altlinux.ru> 6.14-alt1
- automated CPAN update

* Wed Aug 02 2017 Igor Vlasenko <viy@altlinux.ru> 6.13-alt1
- automated CPAN update

* Sun Oct 11 2015 Igor Vlasenko <viy@altlinux.ru> 6.11-alt1
- automated CPAN update

* Tue Oct 15 2013 Igor Vlasenko <viy@altlinux.ru> 6.06-alt2
- updated provides

* Tue Oct 23 2012 Igor Vlasenko <viy@altlinux.ru> 6.06-alt1
- automated CPAN update

* Wed Oct 03 2012 Igor Vlasenko <viy@altlinux.ru> 6.04-alt1
- automated CPAN update

* Mon Feb 20 2012 Alexey Tourbin <at@altlinux.ru> 6.03-alt1
- 6.02 -> 6.03

* Mon Nov 14 2011 Alexey Tourbin <at@altlinux.ru> 6.02-alt3
- rebuilt as plain src.rpm

* Tue Mar 22 2011 Alexey Tourbin <at@altlinux.ru> 6.02-alt2
- HTTP/Headers.pm: enabled explicit dependency on Sotrable

* Mon Mar 21 2011 Alexey Tourbin <at@altlinux.ru> 6.02-alt1
- initial revision
