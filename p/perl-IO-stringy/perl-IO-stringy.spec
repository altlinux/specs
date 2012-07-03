%define dist IO-stringy
Name: perl-%dist
Version: 2.110
Release: alt2

Summary: Filehandle-like I/O support for Perl in-core objects
Group: Development/Perl
License: GPL or Artistic

URL: %CPAN %dist
Source: %dist-%version.tar.gz

BuildArch: noarch

# Automatically added by buildreq on Mon Sep 26 2011
BuildRequires: perl-devel

%description
This toolkit primarily provides modules for performing both traditional
and object-oriented I/O) on things other than normal filehandles; in
particular, IO::Scalar, IO::ScalarArray, and IO::Lines.

%prep
%setup -q -n %dist-%version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc README
%perl_vendor_privlib/IO

%changelog
* Mon Sep 26 2011 Alexey Tourbin <at@altlinux.ru> 2.110-alt2
- rebuilt

* Thu Mar 03 2005 Alexey Tourbin <at@altlinux.ru> 2.110-alt1
- 2.109 -> 2.110
- manual pages not packaged (use perldoc)

* Sat Feb 19 2005 ALT QA Team Robot <qa-robot@altlinux.org> 2.109-alt1.1
- Rebuilt with rpm-build-perl-0.5.1.

* Mon Mar 15 2004 Alexey Tourbin <at@altlinux.ru> 2.109-alt1
- 2.109

* Sat Jun 21 2003 Alexey Tourbin <at@altlinux.ru> 2.108-alt3
- specfile cleanup

* Tue Nov 05 2002 Alexey Tourbin <at@altlinux.ru> 2.108-alt2
- rebuilt for perl-5.8 with new rpm macros

* Tue Sep 25 2001 Grigory Milev <week@altlinux.ru> 2.108-alt1
- New version released.

* Mon Jun 25 2001 Stanislav Ievlev <inger@altlinux.ru> 1.220-alt3
- Rebuilt with perl-5.6.1

* Fri Jun 13 2001 Grigory Milev <week@altlinux.ru> 1.220-alt2
- Rewrite spec for compatible with new police

* Fri Jun 08 2001 Grigory Milev <week@altlinux.ru> 1.220-alt1
- new version (1.220)

* Sun Feb 4 2001 AEN <aen@logic.ru>
- RE adaptation
- cleanup spec

* Thu Oct 12 2000 François Pons <fpons@mandrakesoft.com> 1.216-1mdk
- 1.216.

* Tue Aug 29 2000 François Pons <fpons@mandrakesoft.com> 1.213-1mdk
- 1.213.

* Thu Aug 03 2000 François Pons <fpons@mandrakesoft.com> 1.212-2mdk
- macroszifications.
- added missing clean.
- add doc.

* Tue Jul 18 2000 François Pons <fpons@mandrakesoft.com> 1.212-1mdk
- added requires on perl.
- 1.212.

* Mon Apr  3 2000 Guillaume Cottenceau <gc@mandrakesoft.com> 1.209-1mdk
- 1.209
- fixed group
- rebuild with new perl
- fixed location

* Thu Dec  2 1999 Jerome Dumonteil <jd@mandrakesoft.com>
- first version of rpm.
