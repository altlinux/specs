%define _unpackaged_files_terminate_build 1
%define dist Email-MIME-Encodings
Name: perl-%dist
Version: 1.317
Release: alt1

Summary: A unified interface to MIME encoding and decoding
License: GPL or Artistic
Group: Development/Perl

URL: %CPAN %dist
Source0: http://www.cpan.org/authors/id/R/RJ/RJBS/%{dist}-%{version}.tar.gz

BuildArch: noarch

# Automatically added by buildreq on Wed Oct 05 2011
BuildRequires: perl-Test-Pod perl(Capture/Tiny.pm)

%description
This module simply wraps MIME::Base64 and MIME::QuotedPrint
so that you can throw the contents of a Content-Transfer-Encoding
header at some text and have the right thing happen.

%prep
%setup -q -n %{dist}-%{version}

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc Changes README
%perl_vendor_privlib/Email

%changelog
* Thu Jan 12 2023 Igor Vlasenko <viy@altlinux.org> 1.317-alt1
- automated CPAN update

* Fri Oct 28 2022 Igor Vlasenko <viy@altlinux.org> 1.316-alt1
- automated CPAN update

* Mon Sep 16 2013 Igor Vlasenko <viy@altlinux.ru> 1.315-alt1
- automated CPAN update

* Wed Jul 24 2013 Igor Vlasenko <viy@altlinux.ru> 1.314-alt1
- automated CPAN update

* Wed Oct 05 2011 Alexey Tourbin <at@altlinux.ru> 1.313-alt2
- rebuilt as plain src.rpm

* Sun Apr 19 2009 Alexey Tourbin <at@altlinux.ru> 1.313-alt1
- 1.311 -> 1.313

* Mon Sep 01 2008 Alexey Tourbin <at@altlinux.ru> 1.311-alt1
- 1.3 -> 1.311

* Mon Jul 17 2006 Alexey Tourbin <at@altlinux.ru> 1.3-alt1
- initial revision
