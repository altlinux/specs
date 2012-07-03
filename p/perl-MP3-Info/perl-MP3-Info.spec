%define dist MP3-Info
Name: perl-%dist
version: 1.24
Release: alt1

Summary: Manipulate / fetch info from MP3 audio files
License: GPL or Artistic
Group: Development/Perl

URL: %CPAN %dist
Source: %dist-%version.tar.gz

BuildArch: noarch

# Automatically added by buildreq on Fri Apr 30 2010
BuildRequires: perl-Encode perl-Module-Install

%description
This module is used for getting info out of and into MP3 files.

%prep
%setup -q -n %dist-%version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc Changes README
%perl_vendor_privlib/MP3*

%changelog
* Fri Apr 30 2010 Alexey Tourbin <at@altlinux.ru> 1.24-alt1
- 1.02 -> 1.24

* Sat Feb 19 2005 ALT QA Team Robot <qa-robot@altlinux.org> 1.02-alt1.1
- Rebuilt with rpm-build-perl-0.5.1.

* Fri Mar 21 2003 Grigory Milev <week@altlinux.ru> 1.02-alt1
- new version released
- fix spec

* Wed Apr 10 2002 Grigory Milev <week@altlinux.ru> 1.01-alt1
- new version-released

* Thu Jan 24 2002 Grigory Milev <week@altlinux.ru> 1.00-alt1
- new version released

* Fri Jun 20 2001 Grigory Milev <week@altlinux.ru> 0.91-alt1
- First build for Sisyphus.

