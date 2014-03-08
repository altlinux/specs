Name: perl-B-Debug
Version: 1.19
Release: alt1
Summary: B::Debug - Walk Perl syntax tree, printing debug info about ops

Group: Development/Perl
License: Perl
Url: %CPAN B-Debug

Source: http://www.cpan.org/authors/id/R/RU/RURBAN/B-Debug-%{version}.tar.gz
BuildArch: noarch
BuildRequires: perl-devel

%description
%summary

%prep
%setup -q -n B-Debug-%version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%perl_vendor_privlib/B/Debug.pm
%doc Changes README Artistic Copying

%changelog
* Sat Mar 08 2014 Igor Vlasenko <viy@altlinux.ru> 1.19-alt1
- automated CPAN update

* Fri Sep 28 2012 Vladimir Lettiev <crux@altlinux.ru> 1.18-alt1
- 1.17 -> 1.18
- built as plain srpm

* Fri Dec 02 2011 Vladimir Lettiev <crux@altlinux.ru> 1.17-alt1
- New version 1.17

* Mon Nov 29 2010 Vladimir Lettiev <crux@altlinux.ru> 1.16-alt1
- initial build
