%define dist B-Graph
Name: perl-%dist
Version: 0.51
Release: alt2.1

Summary: Perl compiler backend to produce graphs of OP trees
License: GPL or Artistic
Group: Development/Perl

URL: %CPAN %dist
Source: %dist-%version.tar.gz

BuildArch: noarch

# Automatically added by buildreq on Thu Apr 29 2010
BuildRequires: perl-devel
BuildRequires: perl-B-C

%description
This module is a layer between the perl-internals-examining parts of
Malcolm Beattie's perl compiler (the B::* classes) and your favorite
graph layout tool (currently Dot and VGC are supported, but adding
others would be easy). It examines the internal structures that perl
builds to represent your code (OPs and SVs), and generates
specifications for multicolored boxes and arrows to represent them.

%prep
%setup -q -n %dist-%version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc Changes README
%perl_vendor_privlib/B*

%changelog
* Fri Nov 05 2010 Vladimir Lettiev <crux@altlinux.ru> 0.51-alt2.1
- rebuilt with perl 5.12

* Thu Apr 29 2010 Alexey Tourbin <at@altlinux.ru> 0.51-alt2
- rebuild

* Sat Feb 19 2005 ALT QA Team Robot <qa-robot@altlinux.org> 0.51-alt1.1
- Rebuilt with rpm-build-perl-0.5.1.

* Fri Nov 01 2002 Stanislav Ievlev <inger@altlinux.ru> 0.51-alt1
- Inital Build for ALT

