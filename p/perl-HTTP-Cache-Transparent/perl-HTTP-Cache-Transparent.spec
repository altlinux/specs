%define _unpackaged_files_terminate_build 1
%define dist HTTP-Cache-Transparent
Name: perl-%dist
Version: 1.4
Release: alt1

Summary: Cache the result of http get-requests persistently
License: GPL or Artistic
Group: Development/Perl

URL: %CPAN %dist
Source0: http://www.cpan.org/authors/id/M/MA/MATTIASH/%{dist}-%{version}.tar.gz

Buildarch: noarch

# Automatically added by buildreq on Thu Apr 29 2010
BuildRequires: perl-Test-Pod perl-Test-Pod-Coverage perl-libwww perl(Test/RequiresInternet.pm)

%description
HTTP::Cache::Transparent is an implementation of http get that keeps
a local cache of fetched pages to avoid fetching the same data from
the server if it hasn't been updated.  The cache is stored on disk
and is thus persistent between invocations.

%prep
%setup -q -n %{dist}-%{version}

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc Changes README.md examples
%perl_vendor_privlib/HTTP*

%changelog
* Tue May 09 2017 Igor Vlasenko <viy@altlinux.ru> 1.4-alt1
- automated CPAN update

* Wed Jul 24 2013 Igor Vlasenko <viy@altlinux.ru> 1.1-alt1
- automated CPAN update

* Thu Apr 29 2010 Alexey Tourbin <at@altlinux.ru> 1.0-alt1
- 0.5 -> 1.0

* Sat Mar 26 2005 Vyacheslav Dikonov <slava@altlinux.ru> 0.5-alt1
- ALTLinux build
