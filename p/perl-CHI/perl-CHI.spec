%define _unpackaged_files_terminate_build 1
Name: perl-CHI
Version: 0.58
Release: alt1
Summary: CHI - Unified cache handling interface

Group: Development/Perl
License: Perl
Url: %CPAN CHI

Source: http://www.cpan.org/authors/id/H/HA/HAARG/CHI-%{version}.tar.gz

BuildArch: noarch
BuildRequires: perl-Log-Any perl-Time-Duration perl-Data-UUID perl-Try-Tiny perl-Moose perl-JSON perl-List-MoreUtils perl-Task-Weaken perl-Hash-MoreUtils perl-Digest-JHash perl-Time-Duration perl-Time-Duration-Parse perl-Carp-Assert perl-Test-Deep perl-Test-Exception perl-TimeDate perl-Test-Warn perl-Test-Class perl-IO-Compress perl-Cache-Cache perl-Cache-FastMmap perl-String-RewritePrefix perl-Moo perl-MooX-Types-MooseLike perl-MooX-Types-MooseLike-Numeric

%description
%summary

%prep
%setup -q -n CHI-%version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%perl_vendor_privlib/CHI*
%exclude %perl_vendor_privlib/CHI/t
%doc Changes LICENSE

%changelog
* Mon Sep 30 2013 Igor Vlasenko <viy@altlinux.ru> 0.58-alt1
- automated CPAN update

* Fri Sep 28 2012 Vladimir Lettiev <crux@altlinux.ru> 0.55-alt1
- 0.52 -> 0.55
- built as plain srpm

* Tue Apr 10 2012 Vladimir Lettiev <crux@altlinux.ru> 0.52-alt1
- New version 0.52

* Mon Dec 05 2011 Vladimir Lettiev <crux@altlinux.ru> 0.50-alt1
- New version 0.50

* Fri Jul 29 2011 Vladimir Lettiev <crux@altlinux.ru> 0.49-alt1
- initial build
