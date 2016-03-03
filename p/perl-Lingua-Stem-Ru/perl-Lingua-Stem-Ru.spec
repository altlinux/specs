%define _unpackaged_files_terminate_build 1
%define dist Lingua-Stem-Ru
Name: perl-%dist
Version: 0.04
Release: alt1

Summary: Porter's stemming algorithm for Russian
License: GPL or Artistic
Group: Development/Perl

URL: %CPAN %dist
Source: http://www.cpan.org/authors/id/N/NE/NEILB/Lingua-Stem-Ru-%{version}.tar.gz

BuildArch: noarch

# Automatically added by buildreq on Sun Jan 16 2011
BuildRequires: perl-devel

%description
This module applies the Porter Stemming Algorithm to its parameters,
returning the stemmed words.

%prep
%setup -q -n %dist-%version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc Changes README
%perl_vendor_privlib/Lingua

%changelog
* Thu Mar 03 2016 Igor Vlasenko <viy@altlinux.ru> 0.04-alt1
- automated CPAN update

* Wed Feb 10 2016 Igor Vlasenko <viy@altlinux.ru> 0.03-alt1
- automated CPAN update

* Sun Jan 16 2011 Alexey Tourbin <at@altlinux.ru> 0.01-alt1
- decoupled from perl-Lingua-Stem
