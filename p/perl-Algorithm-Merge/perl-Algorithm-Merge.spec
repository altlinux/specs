%define dist Algorithm-Merge
Name: perl-%dist
Version: 0.08
Release: alt2

Summary: Three-way merge and diff
License: GPL or Artistic
Group: Development/Perl

URL: %CPAN %dist
Source: %dist-%version.tar.gz

BuildArch: noarch

# Automatically added by buildreq on Tue Apr 26 2011
BuildRequires: perl-Algorithm-Diff perl-devel

%description
This module complements Algorithm::Diff by providing three-way merge and
diff functions.

%prep
%setup -q -n %dist-%version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc CHANGES README
%perl_vendor_privlib/Algorithm

%changelog
* Tue Apr 26 2011 Alexey Tourbin <at@altlinux.ru> 0.08-alt2
- fixed unpackaged directory

* Fri Mar 27 2009 Vitaly Lipatov <lav@altlinux.ru> 0.08-alt1
- initial build for ALT Linux Sisyphus
