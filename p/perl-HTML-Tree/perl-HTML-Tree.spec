%define dist HTML-Tree
Name: perl-%dist
Version: 4.2
Release: alt1

Summary: Perl modules for HTML syntax tree processing
License: GPL or Artistic
Group: Development/Perl

URL: %CPAN %dist
Source: %dist-%version.tar.gz

BuildArch: noarch

# Automatically added by buildreq on Fri Apr 22 2011
BuildRequires: perl-HTML-Parser perl-Module-Build perl-Test-Exception

%description
This package contains a suite of modules for representing, creating,
and extracting information from HTML syntax trees

%prep
%setup -q -n %dist-%version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc	Changes README
	/usr/bin/htmltree
%dir	%perl_vendor_privlib/HTML
	%perl_vendor_privlib/HTML/*.pm
%dir	%perl_vendor_privlib/HTML/Element
	%perl_vendor_privlib/HTML/Element/*.pm
%dir	%perl_vendor_privlib/HTML/Tree
%doc	%perl_vendor_privlib/HTML/Tree/*.pod

%changelog
* Fri Apr 22 2011 Alexey Tourbin <at@altlinux.ru> 4.2-alt1
- 4.1 -> 4.2

* Wed Dec 22 2010 Alexey Tourbin <at@altlinux.ru> 4.1-alt1
- 3.23 -> 4.1
- packaged /usr/bin/htmltree

* Tue Nov 14 2006 Alexey Tourbin <at@altlinux.ru> 3.23-alt1
- 3.21 -> 3.23

* Tue Aug 08 2006 Alexey Tourbin <at@altlinux.ru> 3.21-alt1
- 3.20 -> 3.21

* Wed Jun 07 2006 Alexey Tourbin <at@altlinux.ru> 3.20-alt1
- 3.18 -> 3.20

* Sat Feb 19 2005 ALT QA Team Robot <qa-robot@altlinux.org> 3.18-alt1.1
- Rebuilt with rpm-build-perl-0.5.1.

* Fri Oct 03 2003 Alexey Tourbin <at@altlinux.ru> 3.18-alt1
- 3.18

* Thu Sep 04 2003 Alexey Tourbin <at@altlinux.ru> 3.17-alt2
- fixed tests that fail because of recent HTML::Parser changes

* Tue Mar 18 2003 Stanislav Ievlev <inger@altlinux.ru> 3.17-alt1
- Initial release for Sisyphus
