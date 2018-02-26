%define dist Chart
Name: perl-%dist
Version: 2.4.2
Release: alt1

Summary: A series of charting modules
License: GPL or Artistic
Group: Development/Perl

URL: %CPAN %dist
Source: %dist-%version.tar.gz

BuildArch: noarch

# Automatically added by buildreq on Sun Apr 24 2011
BuildRequires: perl-GD perl-devel

%description
This module is an attempt to build a general purpose graphing module that
is easily modified and expanded.  Chart uses Lincoln Stein's GD module for
all of its graphics primitives calls.

%prep
%setup -q -n %dist-%version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc README
%dir %perl_vendor_privlib/Chart
%perl_vendor_privlib/Chart/*.pm
%doc %perl_vendor_privlib/Chart.pod

%changelog
* Mon Apr 25 2011 Alexey Tourbin <at@altlinux.ru> 2.4.2-alt1
- 2.4.1 -> 2.4.2

* Fri Jun 06 2008 Vitaly Lipatov <lav@altlinux.ru> 2.4.1-alt1
- new version 2.4.1 (fix bug #14993), change packager
- cleanup spec, update buildreq

* Sat Feb 19 2005 ALT QA Team Robot <qa-robot@altlinux.org> 2.2-alt1.1
- Rebuilt with rpm-build-perl-0.5.1.

* Thu May 01 2003 Alexey Gladkov <legion@altlinux.ru> 2.2-alt1
- First build for ALTLinux
- spec modifications for Sisyphus
- new version 2.2

* Tue Jul 23 2002 Pixel <pixel@mandrakesoft.com> 1.0.1-3mdk
- rebuild for new perl

* Mon Jul 22 2002 Lenny Cartier <lenny@mandrakesoft.com> 1.0.1-2mdk
- rebuild for new perl

* Fri Jan 18 2002 François Pons <fpons@mandrakesoft.com> 1.0.1-1mdk
- make package as noarch.
- removed MANIFEST from %%doc.
- fixed access right to %%doc files.
- 1.0.1

* Thu Aug 23 2001 Lenny Cartier <lenny@mandrakesoft.com> 0.99c_pre3-3mdk
- rebuild

* Sun Apr 01 2001 David BAUDENS <baudens@mandrakesoft.com> 0.99c_pre3-2mdk
- Re-allow build on non %%ix86 architectures

* Mon Feb 19 2001 Lenny Cartier <lenny@mandrakesoft.com> 0.99c_pre3-1mdk
- updated by Don Head <donhead@linux-certified.org>

* Mon Jan 08 2001 Stefan van der Eijk <s.vandereijk@chello.nl> 0.99b-2mdk
- i386 --> %%{_arch}

* Wed Nov 29 2000 Lenny Cartier <lenny@mandrakesoft.com> 0.99b-1mdk
- new in contribs
