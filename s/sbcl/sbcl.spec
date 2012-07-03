Name: sbcl
Version: 1.0.56
Release: alt1

Summary: Steel Bank Common ANSI Common Lisp
License: Distributable
Group: Development/Lisp
URL: http://sbcl.sourceforge.net/
Packager: Ilya Mashkin <oddity@altlinux.ru>

Source: %name-%version-source.tar.bz2

Patch1: %name-1.0-lib_dir.patch
Patch2: %name-1.0-no-as-needed.patch
Patch3: %name-1.0.5-test-passed.patch
Patch4: %name-1.0.44-prefix.patch
Patch5: %name-1.0.44-runtime.patch

BuildRequires: sbcl /usr/bin/tex
BuildRequires: /proc

%description
Steel Bank Common Lisp (SBCL) is an open source (free software) compiler 
and runtime system for ANSI Common Lisp. It provides an interactive 
environment including an integrated native compiler, a debugger, 
and many extensions.

SBCL runs on many UNIX and UNIX-like systems.

SBCL is a fork off of the main branch of CMU CL. Broadly speaking,
SBCL is distinguished from CMU CL by a greater emphasis on
maintainability. Maybe someday this will translate into better
stability, better ANSI compliance, and so forth, but for now, the big
advantage is that an SBCL system is built directly from scratch, as an
ordinary software system is.

SBCL also places less emphasis than CMU CL does on non-ANSI
extensions, either on backward compatibility with the old CMU CL
non-ANSI extensions or on adding new non-ANSI extensions.

SBCL derives most of its code from CMU CL, created at Carnegie Mellon
University. Radical changes have been made to some parts of the system
(particularly bootstrapping) but most fundamentals (like the mapping
of Lisp abstractions onto the underlying hardware, the basic
architecture of the compiler, and most of the runtime support code)
are only slightly changed. Enough changes have been made to the
interface and architecture that calling the new system CMU Common Lisp
would cause confusion - the world does not need multiple incompatible
systems named CMU CL. But it's appropriate to acknowledge the descent
from the CMU hackers (and post-CMU CMU CL hackers) who did most of the
heavy lifting to make the system work. So the system is named Steel
Bank after the industries where Andrew Carnegie and Andrew Mellon,
respectively, made the big bucks.

%prep
%setup -q

%patch1 -p1
%patch2 -p1
%patch3 -p1
#patch4 -p1
%patch5 -p1

#__subst "s|/usr/local/lib/sbcl/|%_libdir/sbcl/|" src/runtime/runtime.c
%__subst "s|/usr/lib/sbcl/|%_libdir/sbcl/|" src/runtime/runtime.c

%build
export CFLAGS="$RPM_OPT_FLAGS -D_LARGEFILE64_SOURCE"
#export CFLAGS="$RPM_OPT_FLAGS -D_GNU_SOURCE -D_LARGEFILE64_SOURCE"
export SBCL_HOME=%_libdir/sbcl/
export INSTALL_ROOT=%_prefix 
sh ./make.sh  

# comment 30102010
cd doc
sh ./make-doc.sh
cd ..



# docs, two strings from FC
#make -C doc/manual html info

# shorten long doc file names close to maxpathlen
#pushd doc/manual/sbcl
#method_sockets=$(basename $(ls Method-sb*sockets*.html) .html)
#mv "${method_sockets}.html" Method-sockets.html
#sed -i -e "s|${method_sockets}|Method-sockets|" General-Sockets.html
#popd





# pretending that sb-bsd-sockets and sb-posix passed 
#touch contrib/sb-bsd-sockets/test-passed
#touch contrib/sb-posix/test-passed


%install
%define _compress_method skip
mkdir -p %buildroot%_bindir
mkdir -p %buildroot%_libdir/sbcl/
mkdir -p %buildroot%_mandir/man1/

unset SBCL_HOME 
export INSTALL_ROOT=%buildroot%_prefix
export LIB_DIR=%buildroot%_libdir 
sh ./install.sh


cp BUGS COPYING CREDITS INSTALL NEWS PRINCIPLES OPTIMIZATIONS README \
   TLA TODO %buildroot%_docdir/%name/

# remove files used by Mac OS X
find $RPM_BUILD_ROOT -name '._*' -size 1 -print0 | xargs -0 grep -lZ 'Mac OS X' -- | xargs -0 rm -f

%files
%_bindir/*
%_libdir/sbcl
%_mandir/man?/*
%_docdir/*


%changelog
* Fri Apr 27 2012 Ilya Mashkin <oddity@altlinux.ru> 1.0.56-alt1
- 1.0.56

* Sat Jan 07 2012 Ilya Mashkin <oddity@altlinux.ru> 1.0.54-alt1
- 1.0.54

* Wed Sep 14 2011 Ilya Mashkin <oddity@altlinux.ru> 1.0.51-alt1
- 1.0.51

* Mon Aug 15 2011 Ilya Mashkin <oddity@altlinux.ru> 1.0.50-alt1
- 1.0.50

* Mon Jun 13 2011 Ilya Mashkin <oddity@altlinux.ru> 1.0.49-alt1
- 1.0.49

* Sat Mar 26 2011 Ilya Mashkin <oddity@altlinux.ru> 1.0.46-alt1
- 1.0.46

* Sat Feb 19 2011 Ilya Mashkin <oddity@altlinux.ru> 1.0.45-alt1
- 1.0.45

* Tue Dec 21 2010 Ilya Mashkin <oddity@altlinux.ru> 1.0.44-alt0.M51.4
- Build for 5.1

* Sun Dec 05 2010 Ilya Mashkin <oddity@altlinux.ru> 1.0.44-alt4
- fix path to sbcl

* Sat Dec 04 2010 Ilya Mashkin <oddity@altlinux.ru> 1.0.44-alt3
- fix build again
- fix build on x86_64

* Fri Dec 03 2010 Ilya Mashkin <oddity@altlinux.ru> 1.0.44-alt2
- fix build

* Thu Nov 25 2010 Ilya Mashkin <oddity@altlinux.ru> 1.0.44-alt1
- 1.0.44

* Sat Oct 30 2010 Ilya Mashkin <oddity@altlinux.ru> 1.0.42-alt1
- 1.0.42

* Sun Jul 25 2010 Ilya Mashkin <oddity@altlinux.ru> 1.0.40-alt1
- 1.0.40

* Wed Jun 02 2010 Ilya Mashkin <oddity@altlinux.ru> 1.0.39-alt1
- 1.0.39

* Sat May 08 2010 Ilya Mashkin <oddity@altlinux.ru> 1.0.38-alt1
- 1.0.38

* Mon Dec 14 2009 Ilya Mashkin <oddity@altlinux.ru> 1.0.33-alt1
- 1.0.33
- SBCL's 10th Anniversary

* Fri Oct 30 2009 Ilya Mashkin <oddity@altlinux.ru> 1.0.32-alt1
- 1.0.32

* Sun Sep 06 2009 Ilya Mashkin <oddity@altlinux.ru> 1.0.30-alt1
- 1.0.30 (Closes: 21374)
- remove unneeded Mac OS X files

* Thu Jul 23 2009 Ilya Mashkin <oddity@altlinux.ru> 1.0.29-alt1
- 1.0.29

* Tue Mar 17 2009 Ilya Mashkin <oddity@altlinux.ru> 1.0.25-alt1
- 1.0.25

* Sat Jan 10 2009 Ilya Mashkin <oddity@altlinux.ru> 1.0.24-alt1
- 1.0.24

* Sun Dec 14 2008 Ilya Mashkin <oddity@altlinux.ru> 1.0.23-alt1
- 1.0.23
- Dedicated to the 50th birthday of Lisp

* Sat Dec 15 2007 Vadim V. Zhytnikov <vvzhy@altlinux.ru> 1.0.12-alt1
- 1.0.12

* Fri Sep 21 2007 Vadim V. Zhytnikov <vvzhy@altlinux.ru> 1.0.9-alt1
- 1.0.9
- remove Russian description

* Fri May 04 2007 Vadim V. Zhytnikov <vvzhy@altlinux.ru> 1.0.5-alt1
- 1.0.5

* Thu Jan 11 2007 Vadim V. Zhytnikov <vvzhy@altlinux.ru> 1.0.1-alt1
- 1.0.1

* Sat Dec 16 2006 Vadim V. Zhytnikov <vvzhy@altlinux.ru> 1.0-alt1
- 1.0

* Sun Oct 08 2006 Vadim V. Zhytnikov <vvzhy@altlinux.ru> 0.9.17-alt1
- 0.9.17

* Sat Mar 18 2006 Vadim V. Zhytnikov <vvzhy@altlinux.ru> 0.9.10-alt2
- rebuild with sbcl as compilation host

* Thu Mar 16 2006 Vadim V. Zhytnikov <vvzhy@altlinux.ru> 0.9.10-alt1
- new version
- using clisp as cross-compilation host
- builds on x86_64 

* Wed Jan 11 2006 Vadim V. Zhytnikov <vvzhy@altlinux.ru> 0.9.8-alt2
- package /usr/lib/sbcl

* Mon Jan 09 2006 Vadim V. Zhytnikov <vvzhy@altlinux.ru> 0.9.8-alt1
- new version 

* Fri Oct 14 2005 Vadim V. Zhytnikov <vvzhy@altlinux.ru> 0.9.5-alt1
- new version

* Sat Dec 11 2004 Vitaly Lugovsky <vsl@altlinux.ru> 0.8.17-alt1
- new varsion

* Thu Sep 23 2004 Vitaly Lugovsky <vsl@altlinux.ru> 0.8.14-alt1
- new version

* Sun Jul 18 2004 Vitaly Lugovsky <vsl@altlinux.ru> 0.8.9.55-alt0.1
- rebuild

* Thu Mar 25 2004 Vitaly Lugovsky <vsl@altlinux.ru> 0.8.8-alt3
- autoreq bug fixed

* Mon Mar 22 2004 Vitaly Lugovsky <vsl@altlinux.ru> 0.8.8-alt2
- new version

* Sun Jan 18 2004 Vitaly Lugovsky <vsl@altlinux.ru> 0.8.6-alt4
core path fixed

* Wed Jan 14 2004 Vitaly Lugovsky <vsl@altlinux.ru> 0.8.6-alt3
Install_root fixed

* Thu Dec 25 2003 Vitaly Lugovsky <vsl@altlinux.ru> 0.8.6-alt2
core path bug fixed

* Wed Dec 17 2003 Vitaly Lugovsky <vsl@altlinux.ru> 0.8.6-alt1
- New version

* Fri Aug 29 2003 Vitaly Lugovsky <vsl@altlinux.ru> 0.8.3-alt1
- new version

* Tue Jun 24 2003 Vitaly Lugovsky <vsl@altlinux.ru> 0.8.0-alt1
- new version

* Tue Jan 07 2003 Vitaly Lugovsky <vsl@altlinux.ru> 0.7.11-alt1cvs0
- new version (with some modifications from CVS)

* Mon Dec 09 2002 Vitaly Lugovsky <vsl@altlinux.ru> 0.7.10-alt2
- spec cleanup

* Tue Dec 03 2002 Vitaly Lugovsky <vsl@altlinux.ru> 0.7.10-alt1
- new version

* Sat Oct 05 2002 Vitaly Lugovsky <vsl@altlinux.ru> 0.7.8-alt1
- 0.7.8 release

* Thu Aug 15 2002 Vitaly Lugovsky <vsl@altlinux.ru> 0.7.6-alt1
- 0.7.6 release

* Tue Jun 25 2002 Vitaly Lugovsky <vsl@altlinux.ru> 0.7.5-alt1
- 0.7.5 release

* Tue Apr 30 2002 Vitaly Lugovsky <vsl@altlinux.ru> 0.7.3-alt1
- 0.7.3 release

* Sun Jan 27 2002 Vitaly Lugovsky <warlock@skeptik.net>
- Bootstrap requirement added (rebuild)

* Sun Jan 27 2002 Vitaly Lugovsky <warlock@skeptik.net>
- First RPM release.
