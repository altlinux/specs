# vim: set ft=spec: -*- rpm-spec -*-

%define platform %(%_datadir/automake/config.sub %_target_platform | sed -e 's,-%_vendor,,')

Name: librep
Version: 0.92.2
Release: alt1

Summary: An embeddable LISP environment
License: GPL
Group: Development/Other
Url: http://librep.sourceforge.net/

Provides: %_datadir/rep/%version/lisp
Provides: %_datadir/rep/site-lisp
Provides: %_libdir/rep/%version/%platform
Provides: %_libdir/rep/%platform

Source: %name-%version.tar
Patch: %name-%version-%release.patch

# Automatically added by buildreq on Fri Dec 26 2008
BuildRequires: libffi-devel libgdbm-devel libgmp-devel libncurses-devel libreadline-devel

%description
This is a lightweight LISP environment for UNIX. It contains a LISP
interpreter, byte-code compiler and virtual machine. Applications may
use the LISP interpreter as an extension language, or it may be used for
standalone scripts.

Originally inspired by Emacs Lisp, the language dialect combines many of
the elisp features while trying to remove some of the main deficiencies,
with features from Common Lisp and Scheme.

%package devel
Summary: librep include files and link libraries
Group: Development/Other
Requires: %name = %version-%release

%description devel
Link libraries and C header files for librep development.

%prep
%setup -q
%patch -p1
cp -pfv %_datadir/automake/config.{guess,sub} .

%build
%autoreconf
%configure \
	--disable-static \
	--with-readline \
	--with-ffi \
	--with-extra-cflags=-fstrength-reduce
# Fix platform name
sed -ie 's,^host_type=.*$,host_type=%platform,g' librep.pc
%make_build host_type=%platform

%install
%make_build install host_type=%platform DESTDIR=%buildroot
mkdir -p %buildroot%_datadir/rep/site-lisp
find %buildroot%_libdir/rep -type f -name '*.la' -delete

mkdir -p %buildroot%_rpmlibdir
cat <<EOF >%buildroot%_rpmlibdir/librep-files.req.list
# librep dirlist for %_rpmlibdir/files.req
%_datadir/rep/lisp librep
%_datadir/rep/site-lisp librep
%_libdir/rep/ librep
EOF

%files
%doc ChangeLog COPYING MAINTAINERS README TODO
%_bindir/rep
%_bindir/rep-remote
%_libdir/librep.so.*
%dir %_datadir/rep
%dir %_datadir/rep/lisp
%dir %_datadir/rep/site-lisp
%_datadir/rep/lisp/*
%dir %_libdir/rep
%_libdir/rep/rep
%_libdir/rep/*.so
%_libdir/rep/emulate-gnu-tar
%_libdir/rep/doc-strings
%_rpmlibdir/librep-files.req.list
%_man1dir/rep.1*
%_man1dir/rep-remote.1*
%_infodir/librep*
%_emacslispdir/rep-debugger.el

%files devel
%doc doc/*
%_bindir/rep-xgettext
%_bindir/repdoc
%_libdir/librep.so
%_includedir/*
%_pkgconfigdir/*
%_libdir/rep/install-aliases
%_libdir/rep/libtool
%_libdir/rep/rules.mk
%_man1dir/rep-xgettext.1*
%_man1dir/repdoc.1*

%changelog
* Fri Nov 25 2011 Dmitry Derjavin <dd@altlinux.org> 0.92.2-alt1
- [0.92.2];
- *.la files skipped;
- architecture and version removed from installation paths;
- doc files cleanup;
- ChangeLog moved to the main package.

* Sun Feb 14 2010 Alexey I. Froloff <raorn@altlinux.org> 0.90.5-alt1
- [0.90.5]

* Wed Nov 25 2009 Alexey I. Froloff <raorn@altlinux.org> 0.90.3-alt1
- [0.90.3]

* Wed Apr 29 2009 Alexey I. Froloff <raorn@altlinux.org> 0.17.3-alt2
- Fixed tar output parser (closes: #19837)

* Tue Mar 17 2009 Sir Raorn <raorn@altlinux.ru> 0.17.3-alt1
- [0.17.3]

* Fri Dec 26 2008 Sir Raorn <raorn@altlinux.ru> 0.17.2-alt1
- [0.17.2]
- Sanitized rep platform name
- Packaged site-lisp directory
- Packaged pkgconfig file
- Use files.req for extension dependencies
- Removed obsolete %%post_ldconfig/%%postun_ldconfig calls

* Wed Jun 04 2008 Alexey Voinov <voins@altlinux.ru> 0.17-alt1
- new version (0.17)
- buildreq updated
- ffi enabled

* Fri Dec 30 2005 ALT QA Team Robot <qa-robot@altlinux.org> 0.16.2-alt2.1
- Rebuilt with libreadline.so.5.

* Sat Dec 13 2003 Ott Alex <ott@altlinux.ru> 0.16.2-alt2
- Remove .la files

* Sun Apr 27 2003 Ott Alex <ott@altlinux.ru> 0.16.2-alt1
- New release

* Wed Nov 06 2002 AEN <aen@altlinux.ru> 0.16.1-alt2
- rebuilt with new libgdmb

* Fri Jul 12 2002 Yuri N. Sedunov <aris@altlinux.ru> 0.16.1-alt1
- 0.16.1

* Wed Jul 10 2002 Yuri N. Sedunov <aris@altlinux.ru> 0.16-alt1
- 0.16
- 0.15.1-exec.patch removed 
- buildreq updated 

* Fri Jan 11 2002 Konstantin Timoshenko <kt@altlinux.ru> 0.15.2-alt1
- 0.15.2

* Mon Oct 22 2001 Konstantin Timoshenko <kt@altlinux.ru> 0.15.1-alt2
- fix build requires

* Tue Oct 16 2001 Konstantin Timoshenko <kt@altlinux.ru> 0.15.1-alt1
- 0.15.1

* Sat Aug 04 2001 Mikhail Zabaluev <mhz@altlinux.ru> 0.14-alt4
- Corrected incorrectly packaged and missing files

* Thu Aug 02 2001 Dmitry V. Levin <ldv@altlinux.ru> 0.14-alt3
- Fixed %_bindir/rep-xgettext dependence.
- Specfile cleanup.

* Thu Aug 02 2001 Mikhail Zabaluev <mhz@altlinux.ru> 0.14-alt2
- set architecture to i386 for ix86 family
- filelist fixes

* Mon Jul 16 2001 AEN <aen@logic.ru> 0.14-alt1
- new version

* Tue Apr 24 2001 Kostya Timoshenko <kt@altlinux.ru> 0.13.6-alt1
- 0.13.6

* Mon Jan  8 2001 Kostya Timoshenko <kt@petr.kz>
- 0.13.4

* Wed Dec 27 2000 Kostya Timoshenko <kt@petr.kz>
- Build for RE

* Fri Dec  8 2000 Vincent Danen <vdanen@mandrakesoft.com> 0.13.3-1mdk
- 0.13.3

* Mon Nov  6 2000 Vincent Danen <vdanen@mandrakesoft.com> 0.13.2-2mdk
- rebuild for new libstdc++

* Fri Oct 27 2000 Vincent Danen <vdanen@mandrakesoft.com> 0.13.2-1mdk
- 0.13.2

* Fri Sep 29 2000 Vincent Danen <vdanen@mandrakesoft.com> 0.13.1-1mdk
- 0.13.1

* Fri Sep 22 2000 Vincent Danen <vdanen@mandrakesoft.com> 0.13-1mdk
- 0.13
- added buildprereq/buildrequires: texinfo

* Mon Aug 07 2000 Frederic Lepied <flepied@mandrakesoft.com> 0.12.4-4mdk
- automatically added BuildRequires

* Thu Aug  3 2000 Vincent Danen <vdanen@mandrakesoft.com> 0.12.4-3mdk
- force version dependencies
- remove Packager

* Thu Jul 27 2000 Vincent Danen <vdanen@mandrakesoft.com> 0.12.4-2mdk
- rebuild with new rpm

* Fri Jul 21 2000 Vincent Danen <vdanen@mandrakesoft.com> 0.12.4-1mdk
- 0.12.4

* Wed Jul 19 2000 Vincent Danen <vdanen@mandrakesoft.com> 0.12.3-3mdk
- rebuild for directory changes

* Thu Jul 13 2000 Vincent Danen <vdanen@mandrakesoft.com> 0.12.3-2mdk
- fix bad preun

* Wed Jul 12 2000 Vincent Danen <vdanen@mandrakesoft.com> 0.12.3-1mdk
- 0.12.3
- more macroization

* Sun Jul  9 2000 Vincent Danen <vdanen@mandrakesoft.com> 0.12.2-1mdk
- 0.12.2
- added --with-readline
- many specfile cleanups
- macroization
- removed patch to compile with gmp 3.x

* Sat Jun 24 2000 Vincent Danen <vdanen@linux-mandrake.com> 0.12.1-1mdk
- 0.12.1
- changed files from _host to _target_cpu (thanks Chmouel)

* Fri Apr 14 2000 Vincent Danen <vdanen@linux-mandrake.com> 0.11.3-2mdk
- build with libgmp 3.0.1
- include patch to compile with gmp 3.x

* Fri Apr 14 2000 Vincent Danen <vdanen@linux-mandrake.com>
- fix group
- specfile fixes, should work with helixcode for gnome
- 0.11.3

* Sun Mar 19 2000 Vincent Danen <vdanen@linux-mandrake.com>
- 0.11.1

* Sat Mar 11 2000 Vincent Danen <vdanen@linux-mandrake.com>
- specfile cleanups
- 0.11

* Fri Feb 04 2000 Lenny Cartier <lenny@mandrakesoft.com>
- new in contribs
- used srpm provided by Vincent Danen <vdanen@linux-mandrake.com>

* Sun Jan 30 2000 Vincent Danen <vdanen@linux-mandrake.com>
- initial specfile
- bzip sources
