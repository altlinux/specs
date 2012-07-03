Name: gperf
Version: 3.0.4
Release: alt2

Summary: A perfect hash function generator
License: GPLv2+
Group: Development/C
Url: http://www.gnu.org/software/gperf/
Packager: Dmitry V. Levin <ldv@altlinux.org>

Source: ftp://ftp.gnu.org/gnu/gperf/gperf-%version.tar
Patch: gperf-%version-%release.patch

BuildRequires: gcc-c++

%description
Gperf is a perfect hash function generator written in C++.  Simply
stated, a perfect hash function is a hash function and a data structure
that allows recognition of a key word in a set of words using exactly
one probe into the data structure.

%prep
%setup -q
%patch -p1

%build
%add_optflags -fno-strict-aliasing
%define docdir %_docdir/%name-%version
%configure --docdir=%docdir
%make_build

%check
make -k check

%install
%makeinstall_std
install -pm644 AUTHORS NEWS README %buildroot%docdir/

%files
%_bindir/*
%_mandir/man?/*
%_infodir/*.info*
%docdir

%changelog
* Wed Sep 09 2009 Dmitry V. Levin <ldv@altlinux.org> 3.0.4-alt2
- Removed obsolete %%install_info/%%uninstall_info calls.
- Moved "make check" to %%check section.

* Mon Feb 16 2009 Dmitry V. Levin <ldv@altlinux.org> 3.0.4-alt1
- Updated to 3.0.4.
- Run tests during build by default.
- Fixed parallelized build (closes: #18652).

* Tue Jan 27 2009 Dmitry V. Levin <ldv@altlinux.org> 3.0.3-alt2
- Specfile cleanup.

* Mon Sep 24 2007 Dmitry V. Levin <ldv@altlinux.org> 3.0.3-alt1
- Updated to 3.0.3.

* Tue May 16 2006 Dmitry V. Levin <ldv@altlinux.org> 3.0.1-alt2
- Fixed build with gcc-4.1.0.

* Tue Jan 18 2005 ALT QA Team Robot <qa-robot@altlinux.org> 3.0.1-alt1.1
- Rebuilt with libstdc++.so.6.

* Mon Jul 21 2003 Dmitry V. Levin <ldv@altlinux.org> 3.0.1-alt1
- Updated to 3.0.1

* Fri Nov 01 2002 Dmitry V. Levin <ldv@altlinux.org> 2.7.2-ipl4mdk
- Rebuilt in new environment.

* Fri Jan 25 2002 Dmitry V. Levin <ldv@alt-linux.org> 2.7.2-ipl3mdk
- Updated buildrequires.

* Sun Jan 21 2001 Dmitry V. Levin <ldv@fandra.org> 2.7.2-ipl2mdk
- RE adaptions.
- Fixed texinfo documentation.

* Fri Oct 20 2000 François Pons <fpons@mandrakesoft.com> 2.7.2-1mdk
- removed patch and simplified a bit install step.
- 2.7.2.

* Wed Jul 26 2000 Thierry Vignaud <tvignaud@mandrakesoft.com> 2.7-13mdk
- fix bad scripts

* Wed Jul 26 2000 Thierry Vignaud <tvignaud@mandrakesoft.com> 2.7-12mdk
- major spec cleaning
- BM

* Wed Apr 05 2000 John Buswell <johnb@mandrakesoft.com> 2.7-11mdk
- fixed vendor tag

* Thu Mar 30 2000 John Buswell <johnb@mandrakesoft.com> 2.7-10mdk
- fixed groups
- uses spec-helper

* Tue Nov 23 1999 François PONS <fpons@mandrakesoft.com>
- Build release.

* Thu Jun  3 1999 Bernhard Rosenkränzer <bero@mandrakesoft.com>
- REALLY bzip2 info files rather than just renaming them ;)
  seems I'm not the only one around here who should stop working after
  4 am ;)
- replace the egcs patch with the REAL egcs patch (from the egcs server)

* Wed May 19 1999 Chmouel Boudjnah <chmouel@mandrakesoft.com>
- bzip2 info files.

* Tue May 11 1999 Bernhard Rosenkraenzer <bero@mandrakesoft.com>
- Mandrake adaptions

* Wed Mar 24 1999 Cristian Gafton <gafton@redhat.com>
- added patches for egcs from UP

* Sun Mar 21 1999 Cristian Gafton <gafton@redhat.com>
- auto rebuild in the new build environment (release 4)

* Thu Oct 29 1998 Bill Nottingham <notting@redhat.com>
- patch for latest egcs

* Sat Oct 10 1998 Cristian Gafton <gafton@redhat.com>
- strip binary

* Tue Jul 28 1998 Jeff Johnson <jbj@redhat.com>
- create.
