%define dist HTML-Tagset
Name: perl-%dist
Version: 3.20
Release: alt2

Summary: Data tables useful in dealing with HTML
License: GPL or Artistic
Group: Development/Perl

URL: %CPAN %dist
Source: %dist-%version.tar.gz

BuildArch: noarch

# Automatically added by buildreq on Tue Oct 04 2011
BuildRequires: perl-Test-Pod

%description
This module contains data tables useful in dealing with HTML.
It provides no functions or methods.

%prep
%setup -q -n %dist-%version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc Changes README
%perl_vendor_privlib/HTML

%changelog
* Tue Oct 04 2011 Alexey Tourbin <at@altlinux.ru> 3.20-alt2
- rebuilt

* Sun Mar 02 2008 Alexey Tourbin <at@altlinux.ru> 3.20-alt1
- 3.10 -> 3.20

* Tue Oct 10 2006 Alexey Tourbin <at@altlinux.ru> 3.10-alt1
- 3.04 -> 3.10
- imported sources into git and built with gear

* Thu Jun 30 2005 Alexey Tourbin <at@altlinux.ru> 3.04-alt1
- 3.03 -> 3.04 (no code changes, just rebundling)

* Thu Dec 16 2004 Alexey Tourbin <at@altlinux.ru> 3.03-alt5
- rebuild in new environment
- manual pages not packaged (use perldoc)

* Fri Mar 14 2003 Alexey Tourbin <at@altlinux.ru> 3.03-alt4
- specfile cleanup

* Tue Oct 22 2002 Alexey Tourbin <at@altlinux.ru> 3.03-alt3
- rebuilt for perl-5.8 with new rpm macros

* Mon Jul 23 2001 Stanislav Ievlev <inger@altlinux.ru> 3.03-alt2
- Rebuilt with new perl

* Mon Jun 25 2001 Konstantin Volckov <goldhead@altlinux.ru> 3.03-alt1
- First build for Sisyphus
- Cleanup spec

* Wed Jun 20 2001 Christian Belisle <cbelisle@mandrakesoft.com> 3.03-1mdk
- First Mandrake Release.
