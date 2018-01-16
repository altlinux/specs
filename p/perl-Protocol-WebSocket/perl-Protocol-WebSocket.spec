%define _unpackaged_files_terminate_build 1
BuildRequires: perl(Module/Build.pm) perl(Module/Build/Tiny.pm)
Name: perl-Protocol-WebSocket
Version: 0.24
Release: alt1

Summary: Protocol::WebSocket - WebSocket protocol
Group: Development/Perl
License: Perl

Url: %CPAN Protocol-WebSocket
Source0: http://www.cpan.org/authors/id/V/VT/VTI/Protocol-WebSocket-%{version}.tar.gz

BuildArch: noarch
BuildRequires: perl-Module-Install perl-Digest-SHA1 perl(Digest/SHA.pm)

%description
%summary

%prep
%setup -q -n Protocol-WebSocket-%{version}

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc README.md LICENSE Changes examples
%perl_vendor_privlib/Protocol/WebSocket*
%doc Changes

%changelog
* Tue Jan 16 2018 Igor Vlasenko <viy@altlinux.ru> 0.24-alt1
- automated CPAN update

* Mon Dec 18 2017 Igor Vlasenko <viy@altlinux.ru> 0.23-alt1
- automated CPAN update

* Tue Sep 26 2017 Igor Vlasenko <viy@altlinux.ru> 0.21-alt1
- automated CPAN update

* Thu Nov 17 2016 Igor Vlasenko <viy@altlinux.ru> 0.20-alt1
- automated CPAN update

* Fri Oct 16 2015 Igor Vlasenko <viy@altlinux.ru> 0.19-alt1
- automated CPAN update

* Fri Dec 19 2014 Igor Vlasenko <viy@altlinux.ru> 0.18-alt1
- automated CPAN update

* Fri Sep 28 2012 Vladimir Lettiev <crux@altlinux.ru> 0.11-alt1
- initial build
