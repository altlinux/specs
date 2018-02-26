Name: splint
Version: 3.1.2
Release: alt2

Summary: Secure Programming Lint - annotation-assisted static program checker
Group: Development/C
License: GPLv2+
Url: http://www.splint.org
Packager: Slava Semushin <php-coder@altlinux.ru>

Source0: %url/downloads/%name-%version.src.tar.bz2
Source1: %url/manual/manual.html
Source2: %url/manual/manual.ps.bz2
Source3: %url/faq.html
Source4: %name-COPYRIGHT

Patch: %name-3.1.1-alt-man-hidden_links_fix.patch

Provides: lclint = %version
Obsoletes: lclint

# Automatically added by buildreq on Fri Sep 12 2003
BuildRequires: flex

%description
Splint is a tool for statically checking C programs for security
vulnerabilities and coding mistakes.  With minimal effort, Splint
can be used as a better lint.  If additional effort is invested
adding annotations to programs, Splint can perform stronger
checking than can be done by any standard lint.

%prep
%setup

install -p -m644 %SOURCE1 %SOURCE2 %SOURCE3 .
install -p -m644 %SOURCE4 COPYRIGHT

%patch -p1

%build
%configure
# SMP-incompatible build.
make

%install
%make_install install DESTDIR=%buildroot
ln -s %name %buildroot%_bindir/lclint

%files
%doc COPYRIGHT README *.html *.ps*
%_bindir/*
%_datadir/%name
%_man1dir/%name.1.*

%changelog
* Tue Jul 29 2008 Slava Semushin <php-coder@altlinux.ru> 3.1.2-alt2
- Added Packager tag (noted by repocop)
- More proper License tag
- Removed trailing space from %%description

* Wed Jan 02 2008 Slava Semushin <php-coder@altlinux.ru> 3.1.2-alt1
- Bump release and move package to Sisyphus

* Sun Aug 26 2007 Slava Semushin <php-coder@altlinux.ru> 3.1.2-alt0
- Updated to 3.1.2 version

* Tue Jun 19 2007 Slava Semushin <php-coder@altlinux.ru> 3.1.1-alt2.1
- NMU
- Fixed displaying links in man page (#8934)
- Compressed man page
- Spec cleanup:
  + s|%%setup -q|%%setup|
  + s|$RPM_BUILD_ROOT|%%buildroot|
  + s|%%_mandir/man?|%%_man1dir|
  + Don't use macros for ln and install commands

* Fri Sep 12 2003 Dmitry V. Levin <ldv@altlinux.org> 3.1.1-alt2
- Updated build dependencies.

* Thu Jun 05 2003 Dmitry V. Levin <ldv@altlinux.org> 3.1.1-alt1
- Updated to 3.1.1.

* Fri Oct 11 2002 Dmitry V. Levin <ldv@altlinux.org> 3.0.1.6-alt2
- Provides: lclint.
- Added manpage.

* Wed Oct 09 2002 Dmitry V. Levin <ldv@altlinux.org> 3.0.1.6-alt1
- Updated to splint-3.0.1.6 (successor to lclint).
- Added postscript documentation.

* Tue Sep 11 2001 Dmitry V. Levin <ldv@altlinux.ru> 2.5q-alt1
- 2.5r.
- ALT adaptions.

* Thu Feb 15 2001 Trond Eivind Glomsrød <teg@redhat.com>
- <time.h> fix

* Mon Dec 11 2000 Bill Nottingham <notting@redhat.com>
- fix build on ia64

* Mon Aug 21 2000 Jeff Johnson <jbj@redhat.com>
- set default configuration appropriately.

* Fri Jul 28 2000 Eric Veldhuyzen <eric@terra.nu>
- upgraded to 2.5q

* Mon Jul 24 2000 Prospector <prospector@redhat.com>
- rebuilt

* Mon Jul 17 2000 Tim Powers <timp@redhat.com>
- added defattr

* Wed Jul 12 2000 Tim Powers <timp@redhat.com>
- fixed build section so that it links with flex properly

* Mon Jul 10 2000 Tim Powers <timp@redhat.com>
- rebuilt

* Wed Jun 7 2000 Tim Powers <timp@redhat.com>
- minor spec file cleanups, built for Powertools-7.0

* Fri May 26 2000 Eric Veldhuyzen <eric@terra.nu>
- upgraded to 2.5m
- reorganized specfile

* Sat Oct 31 1998 Justin Cormack <jpc1@doc.ic.ac.uk>

- found correct 2.4b source (was actually 2.3)
- no longer an emacs mode
- added documentation

* Wed Oct 14 1998 Justin Cormack <jpc1@doc.ic.ac.uk>
- fixed library directories not to point at buildroot

* Mon Oct 12 1998 Justin Cormack <jpc1@doc.ic.ac.uk>
- fixed executable

* Mon Jun 06 1998 Michael Maher <mike@redhat.com>
- fixed paths for executable link

* Mon May 17 1998 Michael Maher <mike@redhat.com>
- updated to newest version
- added buildroot
- added wmconfig

* Mon Feb 16 1998 Otto Hammersmith <otto@redhat.com>
- added Summary

* Tue Feb  3 1998 Otto Hammersmith <otto@redhat.com>
- %%doc'ed some stuff

* Mon Feb  2 1998 Otto Hammersmith <otto@redhat.com>
- made /usr/lib/lclint/bin a directory, not the executable

* Fri Jan 23 1998 Otto Hammersmith <otto@redhat.com>
- built the package
