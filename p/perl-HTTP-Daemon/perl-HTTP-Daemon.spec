%define _unpackaged_files_terminate_build 1
%define dist HTTP-Daemon
Name: perl-%dist
Version: 6.16
Release: alt1

Summary: a simple http server class
License: GPL or Artistic
Group: Development/Perl

URL: %CPAN %dist
Source0: http://www.cpan.org/authors/id/O/OA/OALDERS/%{dist}-%{version}.tar.gz

Conflicts: perl-libwww < 6

BuildArch: noarch

# Automatically added by buildreq on Mon Nov 14 2011
BuildRequires: perl-HTTP-Message perl-devel perl(Module/Build.pm) perl(Test/Needs.pm) perl(IO/Socket/IP.pm) perl(HTTP/Tiny.pm)

%description
Instances of the HTTP::Daemon class are HTTP/1.1 servers that listen
on a socket for incoming requests. The HTTP::Daemon is a subclass of
IO::Socket::INET, so you can perform socket operations directly on it
too.

%prep
%setup -q -n %{dist}-%{version}

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc Changes README CONTRIBUTING
%perl_vendor_privlib/HTTP

%changelog
* Sat Feb 25 2023 Igor Vlasenko <viy@altlinux.org> 6.16-alt1
- automated CPAN update

* Fri Mar 25 2022 Igor Vlasenko <viy@altlinux.org> 6.14-alt1
- automated CPAN update

* Sun Feb 13 2022 Igor Vlasenko <viy@altlinux.org> 6.13-alt1
- automated CPAN update

* Tue Jun 09 2020 Igor Vlasenko <viy@altlinux.ru> 6.12-alt1
- automated CPAN update

* Wed Sep 11 2019 Igor Vlasenko <viy@altlinux.ru> 6.06-alt1
- automated CPAN update

* Wed Jul 31 2019 Igor Vlasenko <viy@altlinux.ru> 6.05-alt1
- automated CPAN update

* Wed Apr 03 2019 Igor Vlasenko <viy@altlinux.ru> 6.04-alt1
- automated CPAN update

* Tue Apr 02 2019 Igor Vlasenko <viy@altlinux.ru> 6.03-alt1
- automated CPAN update

* Mon Sep 24 2012 Igor Vlasenko <viy@altlinux.ru> 6.01-alt1
- automated CPAN update

* Mon Nov 14 2011 Alexey Tourbin <at@altlinux.ru> 6.00-alt2
- rebuilt as plain src.rpm

* Mon Mar 21 2011 Alexey Tourbin <at@altlinux.ru> 6.00-alt1
- initial revision
