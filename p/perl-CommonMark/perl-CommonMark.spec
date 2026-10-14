%define _unpackaged_files_terminate_build 1

Name: perl-CommonMark
Version: 0.310100
Release: alt1.1
Summary: Interface to the CommonMark C library
License: GPL+ or Artistic
Group: Development/Perl
Url: https://github.com/nwellnhof/perl-commonmark
VCS: git+https://github.com/nwellnhof/perl-commonmark
Source: %name-%version.tar
Patch: perl-CommonMark-c23-interface-prototype.patch

BuildRequires: perl(ExtUtils/MakeMaker.pm) perl(Devel/CheckLib.pm) cmark-devel  perl(Encode.pm) perl(Encode/CN.pm) perl(Encode/JP.pm) perl(Encode/KR.pm) perl(Encode/TW.pm) perl(Exporter.pm) perl(Symbol.pm) perl(Test/LeakTrace.pm) perl(Test/More.pm)

%description
This module is a wrapper around the official CommonMark C library libcmark.
It closely follows the original API.

%prep
%setup
%patch -p1

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc README.pod LICENSE Changes
%perl_vendor_archlib/CommonMark*
%perl_vendor_autolib/*

%changelog
* Tue Oct 13 2026 Vitaly Lipatov <lav@altlinux.ru> 0.310100-alt1.1
- NMU: fix build with gcc 15 (C23): give XS INTERFACE function pointers a real prototype

* Sat Apr 05 2025 Igor Vlasenko <viy@altlinux.org> 0.310100-alt1
- New version 0.310100.

* Tue Oct 01 2019 Alexandr Antonov <aas@altlinux.org> 0.290000-alt1
- initial build for ALT
