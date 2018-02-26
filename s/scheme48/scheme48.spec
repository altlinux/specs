Name:		scheme48
Version:	1.8
Release:	alt2

Summary:	S48 is an implementation of the Scheme programming language
License:	BSD
Group:		Development/Scheme
URL:		http://www.s48.org/
Requires:	%name-vm = %version-%release

Packager:       Alexey Voinov <voins@altlinux.ru>

Source:		%name-%version.tar
Source1:	%name.alternatives

BuildPreReq:	alternatives

# Automatically added by buildreq on Tue Apr 14 2009
BuildRequires: emacs-leim emacs-nox emacs-w3

%package vm
Summary:	Virtual Machine for Scheme48
Group:		System/Libraries

%package doc
Summary:	Documentation for Scheme48
Group:		Development/Scheme

%package prescheme
Summary:	PreScheme compiler
Group:		Development/Scheme
Requires:	%name = %version-%release

%package -n emacs-scheme48
Summary:	CMUScheme48 emacs mode
Group:		Editors
Requires:	%name = %version-%release, emacs-common

%description
Scheme 48 is an implementation of the Scheme programming language as described
in the Revised^5 Report on the Algorithmic Language Scheme [6]. It is based on
a compiler and interpreter for a virtual Scheme machine. Scheme 48 tries to be
faithful to the Revised^5 Scheme Report, providing neither more nor less in the
initial user environment. (This is not to say that more isn't available in
other environments; see below.) Support for numbers is weak: bignums are slow
and floating point is almost nonexistent (see description of floatnums, below).

%description vm
Use this package to distribute your own Scheme48-images without whole
development environment.

%description doc
This package contains all documentation distributed with Scheme48.

%description prescheme
Pre-Scheme is a low-level dialect of Scheme, designed for systems programming
with higher-level abstractions. For example, the Scheme48 virtual machine is
written in Pre-Scheme. Pre-Scheme is a particularly interesting alternative to
C for many systems programming tasks, because not only does it operate at about
the same level as C, but it also may be run in a regular high-level Scheme
development with no changes to the source, without resorting to low-level stack
munging with tools such as gdb. Pre-Scheme also supports two extremely
important high-level abstractions of Scheme: macros and higher-order, anonymous
functions. Richard Kelsey's Pre-Scheme compiler, based on his PhD research on
transformational compilation, compiles Pre-Scheme to efficient C, applying
numerous intermediate source transformations in the process.

%description -n emacs-scheme48
Scheme process in a buffer.  Adapted from cmuscheme.el

%prep
%setup -q
%autoreconf

%build
%configure
make
cd ps-compiler
../go -h 20000000 -a batch << EOF
,config ,load ../scheme/prescheme/interface.scm
,config ,load ../scheme/prescheme/package-defs.scm
,exec ,load load-ps-compiler.scm
,in prescheme-compiler prescheme-compiler
,user (define prescheme-compiler ##)
,dump ../ps-compiler.image "(Pre-Scheme)"
,exit
EOF
cd ..
ar cru libprescheme.a c/unix/misc.o c/unix/fd-io.o c/unix/io.o
ranlib libprescheme.a
emacs -q -no-site-file -batch -eval "(byte-compile-file \"emacs/cmuscheme48.el\")"

%install
make install DESTDIR=$RPM_BUILD_ROOT mandir=%_man1dir
for f in $RPM_BUILD_ROOT%_bindir/scheme-*; do
	mv $f $f-s48
done
cat > $RPM_BUILD_ROOT%_bindir/prescheme << EOF
#!/bin/sh

lib=%_libdir/%name
exec \$lib/scheme48vm -o \$lib/scheme48vm -i \$lib/ps-compiler.image -h 20000000 "\$@"
EOF
chmod a+x $RPM_BUILD_ROOT%_bindir/prescheme

install -d $RPM_BUILD_ROOT%_altdir
install -m644 %SOURCE1 $RPM_BUILD_ROOT%_altdir/%name
install -m644 ps-compiler.image $RPM_BUILD_ROOT%_libdir/%name-%version/ps-compiler.image
install -m644 c/prescheme.h $RPM_BUILD_ROOT%_includedir/prescheme.h
install -m644 c/io.h $RPM_BUILD_ROOT%_includedir/io.h
install -m644 libprescheme.a $RPM_BUILD_ROOT%_libdir/libprescheme.a
mkdir -p %buildroot%_emacslispdir/
install -m644 emacs/cmuscheme48.el* %buildroot%_emacslispdir/

%files vm
%_libdir/%name-%version/%{name}vm

%files
%_altdir/*
%_bindir/scheme*

%_includedir/%{name}*
%dir %_libdir/%name-%version/
%dir %_datadir/%name-%version/
%_libdir/%name-%version/%name.image
%_libdir/%name-%version/*.so
%_datadir/%name-%version/*
%_man1dir/*

%files doc
%doc doc/*.txt doc/html/ doc/*.pdf doc/*.ps

%files prescheme
%_bindir/prescheme
%_libdir/%name-%version/ps-compiler.image
%_includedir/prescheme.h
%_includedir/io.h
%_libdir/libprescheme.a

%files -n emacs-scheme48
%_emacslispdir/*

%changelog
* Tue Apr 14 2009 Alexey Voinov <voins@altlinux.ru> 1.8-alt2
- textrel fixed
- buildreqs updated

* Mon Dec 29 2008 Alexey Voinov <voins@altlinux.ru> 1.8-alt1
- new version (1.8)
- deps on scheme48-vm fixed
- build fixed (netdb patch)
- makefile patch fixed
- calls to %%(un)register_alternatives removed

* Thu Sep 13 2007 Alexey Voinov <voins@altlinux.ru> 1.7-alt1
- new version (1.7)

* Thu May 31 2007 Alexey Voinov <voins@altlinux.ru> 1.6-alt1
- new version (1.6)

* Tue Jan 16 2007 Alexey Voinov <voins@altlinux.ru> 1.5-alt1
- new version (1.5)
- increased heap size for prescheme compiler

* Mon Dec 25 2006 Alexey Voinov <voins@altlinux.ru> 1.4-alt1
- new version (1.4)

* Sun Mar 26 2006 Alexey Voinov <voins@altlinux.ru> 1.3-alt2
- makefile patch updated, fixes build with --as-needed
- cmuscheme48 emacs mode packaged [#7023]
- buildreq updated

* Fri Jul 15 2005 Alexey Voinov <voins@altlinux.ru> 1.3-alt1
- new version (1.3)
- makefile patch updated

* Tue Jun 07 2005 Alexey Voinov <voins@altlinux.ru> 1.2-alt2
- prescheme compiler also packaged

* Sat Jan 15 2005 Alexey Voinov <voins@altlinux.ru> 1.2-alt1
- initial build
