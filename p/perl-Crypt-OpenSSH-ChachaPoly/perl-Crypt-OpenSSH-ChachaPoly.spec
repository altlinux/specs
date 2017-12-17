%define _unpackaged_files_terminate_build 1
%define dist Crypt-OpenSSH-ChachaPoly


Name: perl-%dist
Version: 0.02_reupload1
Release: alt1.1.1

Summary: This module serves as a wrapper to the OpenSSH Chacha20 and Poly1305 functions
License: %perl_license
Group: Development/Perl

URL: http://github.com/lkinley/Crypt-OpenSSH-ChachaPoly
Source0: http://www.cpan.org/authors/id/S/SC/SCHWIGON/%{dist}-0.02-reupload1.tar.gz

BuildRequires: rpm-build-licenses

# Automatically added by buildreq on Thu Feb 18 2016
BuildRequires: perl-Encode perl-devel

%description
This module serves as a wrapper to the OpenSSH Chacha20 and Poly1305 functions

%prep
%setup -q -n %{dist}-0.02

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc Changes README
%perl_vendor_archlib/Crypt
%perl_vendor_autolib/Crypt

%changelog
* Fri Dec 15 2017 Igor Vlasenko <viy@altlinux.ru> 0.02_reupload1-alt1.1.1
- rebuild with new perl 5.26.1

* Fri Feb 03 2017 Igor Vlasenko <viy@altlinux.ru> 0.02_reupload1-alt1.1
- rebuild with new perl 5.24.1

* Sun Jan 15 2017 Igor Vlasenko <viy@altlinux.ru> 0.02_reupload1-alt1
- automated CPAN update

* Thu Apr 21 2016 Sergey Y. Afonin <asy@altlinux.ru> 0.02-alt1
- new version

* Thu Feb 18 2016 Sergey Y. Afonin <asy@altlinux.ru> 0.01-alt1
- initial build
