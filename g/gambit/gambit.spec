%define _unpackaged_files_terminate_build 1

Name: gambit
Version: 4.9.4
Release: alt1

Summary: Gambit-C Scheme programming system
License: Apache-2.0
Group: Development/Other
URL: http://www.iro.umontreal.ca/~gambit/
Conflicts: ghostscript-minimal < 8.64-alt5

Packager: Paul Wolneykien <manowar@altlinux.org>

Source: %name-%version.tar

Patch0: gambit-4.9.4-alt-e2k-lcc123.patch
Patch1: gambit-4.9.4-fix-texi-utf-bytes.patch

%ifarch %e2k
%def_without emacs
%else
%def_with emacs
%endif

%if_with emacs
BuildRequires: emacs-nox
%endif
BuildRequires: makeinfo
BuildPreReq: alternatives
BuildPreReq: /proc

%description
Gambit-C includes a Scheme interpreter and a Scheme compiler which can be used
to build standalone executables. Because the compiler generates portable C
code it is fairly easy to port to any platform with a decent C compiler.

The Gambit-C system conforms to the R4RS and IEEE Scheme standards.  The full
numeric tower is implemented, including: infinite precision integers (bignums),
rationals, inexact reals (floating point numbers), and complex numbers.

%if_with emacs
%package -n emacs-gambit
Summary: Emacs mode for Gambit-C
Group: Editors
Requires: gambit emacs-common
BuildArch: noarch

%description -n emacs-gambit
Emacs mode for running Gambit-C
%endif

%package docs
Summary: Gambit-C manuals ang examples
Group: Development/Documentation
Requires: gambit = %version-%release
BuildArch: noarch

%description docs
Gambit-C manuals ang examples

%package info
Summary: Gambit-C manual in info format
Group: Development/Documentation
Requires: gambit = %version-%release
BuildArch: noarch

%description info
Gambit-C manual in info format

%package devel
Summary: Development files for Gambit-C Scheme
Group: Development/Other
Requires: gambit = %version-%release

%description devel
Development files for Gambit-C Scheme

%package devel-java
Summary: Development files for Gambit Scheme (Java backend)
Group: Development/Other
Requires: gambit = %version-%release

%description devel-java
Development files for Gambit Scheme (Java backend)

%package devel-php
Summary: Development files for Gambit Scheme (PHP backend)
Group: Development/Other
Requires: gambit = %version-%release
Requires: /usr/bin/php

%description devel-php
Development files for Gambit Scheme (PHP backend)

%package devel-python
Summary: Development files for Gambit Scheme (Python backend)
Group: Development/Other
Requires: gambit = %version-%release
Requires: /usr/bin/python3

%description devel-python
Development files for Gambit Scheme (Python backend)

%package devel-js
Summary: Development files for Gambit Scheme (JavaScript backend)
Group: Development/Other
Requires: gambit = %version-%release
Requires: /usr/bin/node

%description devel-js
Development files for Gambit Scheme (JavaScript backend)

%package devel-ruby
Summary: Development files for Gambit Scheme (Ruby backend)
Group: Development/Other
Requires: gambit = %version-%release
Requires: /usr/bin/ruby

%description devel-ruby
Development files for Gambit Scheme (Ruby backend)

%package devel-arm
Summary: Development files for Gambit Scheme (ARM processor family)
Group: Development/Other
Requires: gambit = %version-%release

%description devel-arm
Development files for Gambit Scheme (ARM processor family)

%package devel-riscv
Summary: Development files for Gambit Scheme (RISC-V processor family)
Group: Development/Other
Requires: gambit = %version-%release

%description devel-riscv
Development files for Gambit Scheme (RISC-V processor family)

%package devel-x86
Summary: Development files for Gambit Scheme (x86 processor family)
Group: Development/Other
Requires: gambit = %version-%release

%description devel-x86
Development files for Gambit Scheme (x86 processor family)

# See GAMBCDIR_LIB (doesn't work, TODO)
#define _libdir %_prefix/%_lib/gambit
%define pkgdocdir %_docdir/%name-%version

%prep
%setup
%patch0 -p2
%patch1 -p2

%build
%ifarch %e2k
%add_optflags -D___LITTLE_ENDIAN
%endif
%configure --enable-single-host --enable-shared \
	   --disable-absolute-shared-libs \
	   --docdir=%pkgdocdir
%make_build

%if_with emacs
emacs -q -no-site-file -batch -eval "(byte-compile-file \"misc/gambit.el\")"
%endif

%install
%makeinstall_std
for f in $RPM_BUILD_ROOT%_bindir/scheme-*; do
    mv $f $f-%name
done

cp -R examples/* %buildroot%pkgdocdir/
rm -f %buildroot%pkgdocdir/makefile*
rm -f %buildroot%pkgdocdir/*/makefile*

%if_with emacs
install -m644 misc/*.el* %buildroot%_emacslispdir/
%endif

install -d $RPM_BUILD_ROOT%_altdir
cat > $RPM_BUILD_ROOT%_altdir/%name <<EOF
%_bindir/scheme-r5rs		%_bindir/scheme-r5rs-gambit		10
%_bindir/scheme-r4rs		%_bindir/scheme-r4rs-gambit		10
%_bindir/scheme-srfi-0		%_bindir/scheme-srfi-0-gambit		10
%_bindir/scheme-ieee-1178-1990	%_bindir/scheme-ieee-1178-1990-gambit	10
EOF

%check
%make check GAMBOPT=~~lib=../lib

%files
%_altdir/*
%_bindir/*-%name
%_bindir/gsc*
%_bindir/gsi*
%_bindir/six*
%_includedir/*.h
%_libdir/*.so*
%_man1dir/*.1.*
%_libdir/*.js

%if_with emacs
%files -n emacs-gambit
%_emacslispdir/*
%endif

%files docs
%pkgdocdir/

%files info
%_infodir/*.info*

%files devel
%_bindir/gambdoc
%_bindir/gambuild-C
%_bindir/gambvcs
%_libdir/gambit
%_libdir/scheme
%_libdir/srfi
%_libdir/termite
%exclude %_libdir/_define-library
%exclude %_libdir/_digest
%exclude %_libdir/_geiser
%exclude %_libdir/_git
%exclude %_libdir/_hamt
%exclude %_libdir/_http
%exclude %_libdir/_match
%exclude %_libdir/_pkg
%exclude %_libdir/_six
%exclude %_libdir/_tar
%exclude %_libdir/_test
%exclude %_libdir/_uri
%exclude %_libdir/_zlib
%exclude %_libdir/_*.scm
%exclude %_libdir/_*.c
%exclude %_libdir/gambit#.scm
%exclude %_libdir/r4rs#.scm
%exclude %_libdir/r5rs#.scm
%exclude %_libdir/r7rs#.scm
%exclude %_libdir/syntax-case.scm

%files devel-java
%_bindir/gambuild-java

%files devel-js
%_bindir/gambuild-js

%files devel-php
%_bindir/gambuild-php

%files devel-python
%_bindir/gambuild-python

%files devel-ruby
%_bindir/gambuild-ruby

%files devel-arm
%_bindir/gambuild-arm

%files devel-riscv
%_bindir/gambuild-riscv-32
%_bindir/gambuild-riscv-64

%files devel-x86
%_bindir/gambuild-x86
%_bindir/gambuild-x86-64

%changelog
* Sat Feb 11 2023 Paul Wolneykien <manowar@altlinux.org> 4.9.4-alt1
- New version 4.9.4.
- Updated e2k-lcc123 patch.
- Fixed illegal UTF-8 bytes in gambit.txi (patch).
- New development packages (arm, riscv, x86).

* Mon Nov 25 2019 Paul Wolneykien <manowar@altlinux.org> 4.9.3-alt2
- Fixed the ambiguous Python requirement: Require Python v3.

* Thu Feb 07 2019 Cronbuild Service <cronbuild@altlinux.org> 4.9.3-alt1
- new version 4.9.3

* Tue Jan 22 2019 Cronbuild Service <cronbuild@altlinux.org> 4.9.2-alt1
- new version 4.9.2

* Tue Jan 22 2019 Paul Wolneykien <manowar@altlinux.org> 4.9.1-alt5
- Setup for "cronbuild" automatic building of new versions.

* Wed Jan 09 2019 Michael Shigorin <mike@altlinux.org> 4.9.1-alt4
- E2K: workaround for lcc-1.23 lacking some gcc5 builtins

* Tue Nov 27 2018 Paul Wolneykien <manowar@altlinux.org> 4.9.1-alt3
- Extract backend sub-packages.

* Tue Nov 27 2018 Paul Wolneykien <manowar@altlinux.org> 4.9.1-alt2
- Conditional build on E2K.

* Thu Nov 22 2018 Paul Wolneykien <manowar@altlinux.org> 4.9.1-alt1
- New version 4.9.1.

* Thu Nov 22 2018 Paul Wolneykien <manowar@altlinux.org> 4.7.3-alt2
- New version 4.7.3 from the tarball.

* Sat Mar 03 2018 Igor Vlasenko <viy@altlinux.ru> 4.7.7-alt1.1.1
- NMU: rebuild with TeXLive instead of TeTeX

* Thu Dec 03 2015 Igor Vlasenko <viy@altlinux.ru> 4.7.7-alt1.1
- NMU: added BR: texinfo

* Thu Jul 16 2015 Cronbuild Service <cronbuild@altlinux.org> 4.7.7-alt1
- repocop cronbuild 20150716. At your service.

* Sun May 10 2015 Cronbuild Service <cronbuild@altlinux.org> 4.7.6-alt1
- repocop cronbuild 20150510. At your service.

* Wed Apr 22 2015 Cronbuild Service <cronbuild@altlinux.org> 4.7.5-alt1
- repocop cronbuild 20150422. At your service.

* Mon Mar 02 2015 Cronbuild Service <cronbuild@altlinux.org> 4.7.4-alt1
- repocop cronbuild 20150302. At your service.

* Tue Sep 23 2014 Paul Wolneykien <manowar@altlinux.org> 4.7.3-alt1
- New version 4.7.3.

* Mon Mar 10 2014 Paul Wolneykien <manowar@altlinux.ru> 4.7.2-alt1
- repocop cronbuild 20140310. At your service.

* Sun Jan 19 2014 Cronbuild Service <cronbuild@altlinux.org> 4.7.1-alt1
- repocop cronbuild 20140119. At your service.

* Thu Jun 20 2013 Cronbuild Service <cronbuild@altlinux.org> 4.7.0-alt1
- repocop cronbuild 20130620. At your service.

* Sat May 11 2013 Cronbuild Service <cronbuild@altlinux.org> 4.6.9-alt1
- repocop cronbuild 20130511. At your service.

* Thu May 09 2013 Cronbuild Service <cronbuild@altlinux.org> 4.6.8-alt1
- repocop cronbuild 20130509. At your service.

* Mon Apr 08 2013 Paul Wolneykien <manowar@altlinux.ru> 4.6.7-alt1
- Build without bootstrap.
- Add TODO for --enable-poll option (to be tested with the latest
  Gambit).
- Update the building scheme following README inctructions.
- Make bootclean prior to make.
- Rename: gsc-comp -> gsc-boot.
- Update the sources up to v4.6.7 with the help of repocop cronbuild
  scripts.

* Thu Dec 06 2012 Paul Wolneykien <manowar@altlinux.ru> 4.6.6-alt1
- repocop cronbuild 20121206. At your service.

* Sun Dec 02 2012 Paul Wolneykien <manowar@altlinux.ru> 4.6.5-alt1
- repocop cronbuild 20121202. At your service.

* Thu Apr 12 2012 Paul Wolneykien <manowar@altlinux.ru> 4.6.4-alt1
- New version built with the help of cronbuild scripts.

* Fri Jan 20 2012 Paul Wolneykien <manowar@altlinux.ru> 4.6.3-alt1
- New Gambit Scheme release 4.6.3.
- Normalize-NAN modification already included (remove the patch).
- Restore the .gitignore file to merge cleanly with the upstream.
- Cronbuild script fix: determine the current branch properly.

* Sat Oct 22 2011 Cronbuild Service <cronbuild@altlinux.org> 4.6.2-alt1
- repocop cronbuild 20111022. At your service.

* Fri Oct 21 2011 Paul Wolneykien <manowar@altlinux.ru> 4.6.1-alt2
- Normalize C representation of the +nan.0 value (thanx Marc).
- Became the packager.

* Sun May 08 2011 Cronbuild Service <cronbuild@altlinux.org> 4.6.1-alt1
- repocop cronbuild 20110508. At your service.

* Thu May 05 2011 Paul Wolneykien <manowar@altlinux.ru> 4.6.0-alt2
- Build v4.6.0 from git using v4.5.3 as the bootstrap compiler.

* Thu May 05 2011 Paul Wolneykien <manowar@altlinux.ru> 4.6.0-alt1
- Build v4.6.0 from the upstream package with genereted C sources.

* Thu May 05 2011 Paul Wolneykien <manowar@altlinux.ru> 4.5.3-alt8
- Rebuild v4.5.3 from the upstream package with genereted C sources.

* Thu Apr 07 2011 Paul Wolneykien <manowar@altlinux.ru> 4.5.3-alt7
- Fix the master branch problem in the Cronbuild update script.

* Thu Apr 07 2011 Paul Wolneykien <manowar@altlinux.ru> 4.5.3-alt6
- Fix the Shell options for the Cronbuild update script.
- Read the spec file name from the command line.

* Thu Apr 07 2011 Paul Wolneykien <manowar@altlinux.ru> 4.5.3-alt5
- Try to fix PATH in the Cronbuild update script.

* Wed Apr 06 2011 Paul Wolneykien <manowar@altlinux.ru> 4.5.3-alt4
- Add Cronbuild scripts.

* Mon Apr 04 2011 Paul Wolneykien <manowar@altlinux.ru> 4.5.3-alt3
- Mark emacs-gambit as noarch.

* Wed Mar 09 2011 Paul Wolneykien <manowar@altlinux.ru> 4.5.3-alt2
- Use two dir scheme to optinally compile a bootstrap compiler.

* Fri Nov 06 2009 Alexey Voinov <voins@altlinux.ru> 4.5.3-alt1
- new release (4.5.3)

* Thu Sep 17 2009 Alexey Voinov <voins@altlinux.ru> 4.5.2-alt1
- new release (4.5.2)

* Wed Aug 19 2009 Alexey Voinov <voins@altlinux.ru> 4.5.1-alt1
- new release (4.5.1)

* Fri Jun 19 2009 Alexey Voinov <voins@altlinux.ru> 4.4.4-alt1
- new release (4.4.4)
- gsc is back to normal, README.ALT removed
- docs and info in separate noarch subpackages

* Sun May 31 2009 Alexey Voinov <voins@altlinux.ru> 4.4.3-alt1
- new release (4.4.3)
- directory structure simplification
- spec simplification

* Tue May 26 2009 Alexey Voinov <voins@altlinux.ru> 4.3.0-alt1
- new release (4.3.0)

* Tue Oct 07 2008 Alexey Voinov <voins@altlinux.ru> 4.2.9-alt1
- new release (4.2.9)
- buildreqs updated

* Wed May 07 2008 Alexey Voinov <voins@altlinux.ru> 4.2.6-alt1
- new release (4.2.6)
- post_ldconfig/postun_ldconfig

* Tue Mar 25 2008 Alexey Voinov <voins@altlinux.ru> 4.2.5-alt1
- new release (4.2.5)

* Mon Mar 17 2008 Alexey Voinov <voins@altlinux.ru> 4.2.4-alt2
- fix for -prelude and -postlude options from upstream
  mercury repository

* Sun Mar 16 2008 Alexey Voinov <voins@altlinux.ru> 4.2.4-alt1
- new release (4.2.4)

* Mon Mar 03 2008 Alexey Voinov <voins@altlinux.ru> 4.2.3-alt1
- new release (4.2.3)
- symlinks fixed

* Tue Feb 12 2008 Alexey Voinov <voins@altlinux.ru> 4.2.2-alt1
- new release (4.2.2)

* Fri Feb 08 2008 Alexey Voinov <voins@altlinux.ru> 4.2.1-alt1
- new release (4.2.1)

* Fri Feb 08 2008 Alexey Voinov <voins@altlinux.ru> 4.2.0-alt1
- new release (4.2.0)

* Sat Dec 22 2007 Alexey Voinov <voins@altlinux.ru> 4.1.2-alt1
- new release (4.1.2)
- alt-so patch updated

* Sun Dec 16 2007 Alexey Voinov <voins@altlinux.ru> 4.1.1-alt1
- new release (4.1.1)
- alt-so patch

* Sat Nov 17 2007 Alexey Voinov <voins@altlinux.ru> 4.1.0-alt1
- new release (4.1.0)

* Thu Sep 13 2007 Alexey Voinov <voins@altlinux.ru> 4.0.1-alt1
- new release (4.0.1)

* Thu Sep 13 2007 Alexey Voinov <voins@altlinux.ru> 4.0.0-alt1
- new release (4.0.0)

* Wed May 30 2007 Alexey Voinov <voins@altlinux.ru> 4.0-alt0.22.1
- new release (4.0b22)

* Sat Oct 14 2006 Alexey Voinov <voins@altlinux.ru> 4.0-alt0.20.2
- files layout changes, compiler should work now

* Sun Oct 08 2006 Alexey Voinov <voins@altlinux.ru> 4.0-alt0.20.1
- new release (4.0b20)

* Tue Jan 10 2006 Alexey Voinov <voins@altlinux.ru> 4.0-alt0.17.2
- actual b17 tarball... 

* Mon Jan 09 2006 Alexey Voinov <voins@altlinux.ru> 4.0-alt0.17.1
- new release (4.0b17)

* Sat Jan 07 2006 Alexey Voinov <voins@altlinux.ru> 4.0-alt0.16.1
- new release (4.0b16)
- emacs subpackage added
- buildreqs fixed

* Sun Oct 02 2005 Alexey Voinov <voins@altlinux.ru> 4.0-alt0.15.1
- new release (4.0b15)

* Sat Jul 16 2005 Alexey Voinov <voins@altlinux.ru> 4.0-alt0.14.1
- new release (4.0b14)

* Thu Jun 02 2005 Alexey Voinov <voins@altlinux.ru> 4.0-alt0.13.2
- license info fixed

* Thu May 12 2005 Alexey Voinov <voins@altlinux.ru> 4.0-alt0.13.1
- new release (4.0b13)
- files rearranged

* Mon Jan 17 2005 Alexey Voinov <voins@altlinux.ru> 4.0-alt0.12.1
- alternatives for scheme-* scripts added (to prevent conflicts with scheme48)

* Tue Jan 11 2005 Alexey Voinov <voins@altlinux.ru> 4.0-alt0.12
- new release (4.0b12)

* Sun Nov 2 2004 Alexey Voinov <voins@altlinux.ru> 4.0-alt0.11
- initial build
