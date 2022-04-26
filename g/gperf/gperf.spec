Name: gperf
Version: 3.2.0.1.d89c
Release: alt1

Summary: A perfect hash function generator
License: GPLv3+
Group: Development/C
Url: https://www.gnu.org/software/gperf/
%define srcname %name-%version-%release
# http://git.savannah.gnu.org/cgit/gperf.git
Source: %srcname.tar
BuildRequires: gnulib >= 0.1.4003.cfe65
BuildRequires: gcc-c++ help2man makeinfo

%description
Gperf is a perfect hash function generator written in C++.  Simply
stated, a perfect hash function is a hash function and a data structure
that allows recognition of a key word in a set of words using exactly
one probe into the data structure.

%prep
%setup -n %srcname
# Build scripts expect to find the %name version in this file.
echo -n %version > .tarball-version
# Use system help2man
ln -snf %_bindir/help2man doc/

%build
GNULIB_TOOL='gnulib-tool ' ./autogen.sh
%add_optflags -fno-strict-aliasing %(getconf LFS_CFLAGS)
%define docdir %_docdir/%name
%configure --docdir=%docdir
%make_build

%install
%makeinstall_std
install -pm644 AUTHORS NEWS README %buildroot%docdir/

%define _unpackaged_files_terminate_build 1
%define _stripped_files_terminate_build 1
%set_verify_elf_method strict

%check
%make_build -k check

%files
%_bindir/*
%_mandir/man?/*
%_infodir/*.info*
%docdir/

%changelog
* Tue Feb 08 2022 Dmitry V. Levin <ldv@altlinux.org> 3.2.0.1.d89c-alt1
- gperf: v3.1-27-gb0f961a -> v3.2-1-gd89cab8.

* Tue Apr 06 2021 Dmitry V. Levin <ldv@altlinux.org> 3.1.0.27.b0f9-alt1
- gperf: v3.1-19-g9f4f11a -> v3.1-27-gb0f961a.
- gnulib BR: v0.1-2305-g95c96b6dd -> v0.1-4003-gcfe65a873.

* Wed Dec 26 2018 Dmitry V. Levin <ldv@altlinux.org> 3.1.0.19.9f4f-alt1
- gperf: v3.1 -> v3.1-19-g9f4f11a.
- gnulib: v0.1-1213-g683b60789 -> v0.1-2305-g95c96b6dd.

* Sun Mar 26 2017 Dmitry V. Levin <ldv@altlinux.org> 3.1-alt1
- gperf: v3.0.4-33-g1a05152 -> v3.1.
- gnulib: v0.1-585-g2fda85e -> v0.1-1213-g683b607.

* Thu Dec 10 2015 Dmitry V. Levin <ldv@altlinux.org> 3.0.4.0.33.1a05-alt1
- Updated to v3.0.4-33-g1a05152.

* Fri Apr 19 2013 Dmitry V. Levin <ldv@altlinux.org> 3.0.4-alt3
- Built with LFS support enabled.

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
