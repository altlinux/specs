%define _unpackaged_files_terminate_build 1
%define dist Parallel-ForkManager
Name: perl-%dist
Version: 1.04
Release: alt1

Summary: A simple parallel processing fork manager
License: GPL or Artistic
Group: Development/Perl

URL: %CPAN %dist
Source: http://www.cpan.org/authors/id/S/SZ/SZABGAB/Parallel-ForkManager-%{version}.tar.gz

BuildArch: noarch

# Automatically added by buildreq on Sat Apr 23 2011
BuildRequires: perl-devel

%description
This module is intended for use in operations that can be done in parallel
where the number of processes to be forked off should be limited. Typical
use is a downloader which will be retrieving hundreds/thousands of files.

%prep
%setup -q -n %dist-%version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc Changes
%dir %perl_vendor_privlib/Parallel
%perl_vendor_privlib/Parallel/ForkManager.pm

%changelog
* Thu Sep 12 2013 Igor Vlasenko <viy@altlinux.ru> 1.04-alt1
- automated CPAN update

* Wed Jul 24 2013 Igor Vlasenko <viy@altlinux.ru> 1.03-alt1
- automated CPAN update

* Sat Apr 23 2011 Alexey Tourbin <at@altlinux.ru> 0.7.9-alt1
- 0.7.5 -> 0.7.9

* Mon Jul 17 2006 Alexey Tourbin <at@altlinux.ru> 0.7.5-alt1
- initial revision
