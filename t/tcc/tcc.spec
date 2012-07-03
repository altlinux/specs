%def_disable cross
%define ccomp gcc

%define Alias TinyCC
%define alias tinycc
%define Name TCC
Name: tcc
%define lname lib%name
Version: 0.9.25
Release: alt4
Summary: A small but hyper fast C compiler
Group: Development/C
License: %lgpl21plus
URL: http://bellard.org/%name
Source: http://download.savannah.nongnu.org/releases/tinycc//%name-%version.tar
Patch: %name-%version-%release.patch
Provides: %alias = %version-%release
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

BuildRequires(pre): rpm-build-licenses
%if %ccomp == tcc
BuildRequires: tcc >= 0.9.23-alt3
%endif
BuildPreReq: perl-podlators

%description
%Alias (aka %Name) is a small but hyper fast C compiler. Unlike other C
compilers, it is meant to be self-sufficient: you do not need an
external assembler or linker because %Name does that for you.
%Name compiles so fast that even for big projects Makefiles may not be
necessary.
%Name not only supports ANSI C, but also most of the new ISO C99 standard
and many GNUC extensions.
%Name can also be used to make C scripts, i.e. pieces of C source that
you run as a Perl or Python script. Compilation is so fast that your
script will be as fast as if it was an executable.
%Name can also automatically generate memory and bound checks while
allowing all C pointers operations. %Name can do these checks even if non
patched libraries are used.
With %lname, you can use %Name as a backend for dynamic code generation.


%package -n %lname-devel
Summary: %Name backend for dynamic code generation
Group: Development/C
Provides: %lname-devel-static = %version-%release

%description -n %lname-devel
%Alias (aka %Name) is a small but hyper fast C compiler. Unlike other C
compilers, it is meant to be self-sufficient: you do not need an
external assembler or linker because %Name does that for you.
%Name compiles so fast that even for big projects Makefiles may not be
necessary.
%Name not only supports ANSI C, but also most of the new ISO C99 standard
and many GNUC extensions.
%Name can also be used to make C scripts, i.e. pieces of C source that
you run as a Perl or Python script. Compilation is so fast that your
script will be as fast as if it was an executable.
%Name can also automatically generate memory and bound checks while
allowing all C pointers operations. %Name can do these checks even if non
patched libraries are used.

With %lname, you can use %Name as a backend for dynamic code generation.


%package doc
Summary: Documentation for %Name
Group: Development/Documentation
BuildArch: noarch

%description doc
%Alias (aka %Name) is a small but hyper fast C compiler. Unlike other C
compilers, it is meant to be self-sufficient: you do not need an
external assembler or linker because %Name does that for you.
%Name compiles so fast that even for big projects Makefiles may not be
necessary.
%Name not only supports ANSI C, but also most of the new ISO C99 standard
and many GNUC extensions.
%Name can also be used to make C scripts, i.e. pieces of C source that
you run as a Perl or Python script. Compilation is so fast that your
script will be as fast as if it was an executable.
%Name can also automatically generate memory and bound checks while
allowing all C pointers operations. %Name can do these checks even if non
patched libraries are used.

This package contains documentation for %Name.


%prep
%setup
%patch -p1
sed -i -e 's|/usr/local/bin/|%_bindir/|g' %name-doc.* examples/ex1.c


%build
%define _optlevel 3
%configure \
    %{subst_enable cross} \
    %{?ccomp:--cc=%ccomp} \
    --docdir=%_docdir/%name-%version

sed -i 's|\(\$(INSTALL)\) -s|\1|' Makefile
%make_build
bzip2 -9fk Changelog


%install
%make_install DESTDIR=%buildroot install
install -m 0644 Changelog.* README TODO %buildroot%_docdir/%name-%version/


%files
%_bindir/*
%_man1dir/*
%_libdir/%name


%files -n %lname-devel
%_includedir/*
%_libdir/%lname.a


%files doc
%doc %dir %_docdir/%name-%version
%doc %_docdir/%name-%version/Changelog.*
%doc %_docdir/%name-%version/README
%doc %_docdir/%name-%version/TODO
%doc %_docdir/%name-%version/*.html


%changelog
* Wed Mar 23 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.9.25-alt4
- Really rebuilt for debuginfo

* Tue Mar 22 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.9.25-alt3
- Rebuilt for debuginfo

* Tue Nov 16 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.9.25-alt2
- Fixed build

* Sun Nov 15 2009 Led <led@altlinux.ru> 0.9.25-alt2
- warning instead error for unsupported linker options

* Tue Jun 02 2009 Led <led@altlinux.ru> 0.9.25-alt1
- 0.9.25
- updated URL
- cleaned up spec
- updated description and summary
- fixed License

* Thu Feb 22 2007 Led <led@altlinux.ru> 0.9.23-alt4
- added ExclusiveArch: %%ix86
- fixed %%files

* Thu Oct 12 2006 Led <led@altlinux.ru> 0.9.23-alt3
- added %name-0.9.23-union-abstract.patch for parse unnamed unions
- added %name-0.9.23-linker-error.patch
- added %name-0.9.23-linker-lib_search_order.patch
- updated %name-0.9.23-linker-group_as_needed.patch
- added %%optflags for compile

* Wed Oct 04 2006 Led <led@altlinux.ru> 0.9.23-alt2
- fixed linker: added %name-0.9.23-linker-defined_twice.patch
- added %name-0.9.23-linker-group_as_needed.patch (fixed by Kim Lux)
- added %name-0.9.23-pointer-operators.patch

* Tue Oct 03 2006 Led <led@altlinux.ru> 0.9.23-alt1
- 0.9.23
- cleaned up spec

* Wed Dec 29 2004 Alexey Tourbin <at@altlinux.ru> 0.9.22-alt1
- 0.9.20 -> 0.9.22

* Mon Nov 10 2003 Alexey Tourbin <at@altlinux.ru> 0.9.20-alt1
- initial revision
