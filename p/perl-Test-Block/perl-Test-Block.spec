%define dist Test-Block
Name: perl-%dist
Version: 0.13
Release: alt2

Summary: Test::Block - Specify fine granularity test plans
Group: Development/Perl
License: Perl

Url: %CPAN %dist
Source: %dist-%version.tar
Patch1: %dist-%version-debian-work-with-perl-5.23.8.patch

BuildArch: noarch
BuildRequires: perl-devel perl-pod perl-Module-Build perl-Test-Exception

%description
%summary

%prep
%setup -q -n %dist-%version
%patch1 -p1

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%perl_vendor_privlib/Test/Block*
%doc Changes README

%changelog
* Thu Aug 17 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 0.13-alt2
- Fixed build with modern perl.

* Mon Sep 10 2012 Vladimir Lettiev <crux@altlinux.ru> 0.13-alt1
- 0.11 -> 0.13

* Tue Aug 24 2010 Vladimir Lettiev <crux@altlinux.ru> 0.11-alt1
- initial build
