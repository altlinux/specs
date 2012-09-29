%define dist ORLite-Migrate
Name: perl-ORLite-Migrate
Version: 1.10
Release: alt1

Summary: ORLite::Migrate - Extremely light weight SQLite-specific schema
License: Perl
Group: Development/Perl

Url: %CPAN %dist
Source: %dist-%version.tar.gz

BuildRequires: perl-devel perl-File-Which perl-File-pushd perl-IPC-Run3 perl-Probe-Perl perl-Params-Util perl-DBI perl-DBD-SQLite perl-ORLite
BuildArch: noarch

%description
%summary

%prep
%setup -q -n %dist-%version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%perl_vendor_privlib/ORLite/Migrate*
%doc Changes README 

%changelog
* Sat Sep 29 2012 Vladimir Lettiev <crux@altlinux.ru> 1.10-alt1
- 1.09 -> 1.10
- built as plain srpm

* Mon Nov 14 2011 Vladimir Lettiev <crux@altlinux.ru> 1.09-alt1
- New version 1.09

* Tue Apr 06 2010 Vladimir Lettiev <crux@altlinux.ru> 1.07-alt1
- New version 1.07

* Fri Jan 29 2010 Vladimir Lettiev <crux@altlinux.ru> 1.06-alt1
- initial build
