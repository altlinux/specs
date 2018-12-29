Name: cproto
Version: 4.7o
Release: alt1

Summary: Generates function prototypes and variable declarations from C code
License: Public Domain
Group: Development/Tools
Url: https://invisible-island.net/cproto/cproto.html

# ftp://ftp.invisible-island.net/cproto/cproto-%version.tgz
Source: %name-%version.tar

BuildRequires: bison flex

%description
Cproto is a program that generates function prototypes and variable
declarations from C source code.  It can also convert function
definitions between the old style and the ANSI C style.  This conversion
overwrites the original files, however, so be sure to make a backup copy
of your original files in case something goes wrong.

The program isn't confused by complex function definitions as much as
other prototype generators because it uses a yacc generated parser.
By ignoring all the input between braces, the author has avoided
implementing the entire C language grammar.

%prep
%setup

%build
%add_optflags %(getconf LFS_CFLAGS)
%configure --enable-llib
%make_build

%install
%makeinstall_std

%set_verify_elf_method strict
%define _unpackaged_files_terminate_build 1

%check
%make_build -k check

%files
%_bindir/cproto
%_man1dir/cproto.*
%doc AUTHORS CHANGES README

%changelog
* Sat Dec 29 2018 Dmitry V. Levin <ldv@altlinux.org> 4.7o-alt1
- 4.7l -> 4.7o.
- Rewritten spec file.

* Wed May 28 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.7l-alt1
- Version 4.7l

* Mon Nov 11 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.7k-alt1
- Version 4.7k

* Thu Dec 01 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.7j-alt2
- Changed URL

* Mon Aug 22 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.7j-alt1
- Version 4.7j (thnx viy@)

* Sun Mar 13 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.6-alt2
- Rebuilt for debuginfo

* Fri May 29 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.6-alt1
- Initial build for Sisyphus

