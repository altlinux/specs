%def_enable static
%def_disable cross
%def_without selinux
%def_without libgcc

%define Alias TinyCC
%define alias tinycc
%define Name TCC
Name: tcc
%define lname lib%name
Version: 0.9.27
Release: alt1
Summary: A small but hyper fast C compiler
Group: Development/C
License: LGPLv2.1+
URL: http://bellard.org/%name
Source: %name-%version.tar
Patch: %name-0.9.27-alt1.patch
Provides: %alias = %version-%release

# Automatically added by buildreq on Mon Feb 05 2018
# optimized out: glibc-kernheaders-generic glibc-kernheaders-x86 perl perl-Encode perl-Pod-Escapes perl-Pod-Simple perl-Text-Unidecode perl-Unicode-EastAsianWidth perl-Unicode-Normalize perl-libintl perl-parent perl-podlators python-base
BuildRequires: makeinfo perl-Pod-Usage
BuildPreReq: perl-podlators

%if "%__cc" == tcc
BuildRequires: tcc >= 0.9.23-alt3
%endif

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
%setup -q
%patch -p1
#sed -i 's|/usr/local/bin/|%_bindir/|g' README %name-doc.* examples/ex[14].c
#sed -i '/^TCCFLAGS/s/^.*$/& -lm/' tests/tests2/Makefile


%build
./configure \
	--prefix=%_prefix \
	--libdir=%_libdir \
	%{?__cc:--cc=%__cc} \
	--extra-cflags="%optflags" \
	--docdir=%_docdir/%name-%version \
	%{?_disable_static:--disable-static} \
	%{?_enable_cross:--enable-cross} \
	%{?_with_selinux:--with-selinux} \
	%{?_with_libgcc:--with-libgcc} \
	--disable-rpath
%make_build

%install
%makeinstall_std

%check
make test


%files
%doc README Changelog RELICENSING TODO VERSION
%_bindir/*
%_libdir/%name
%_man1dir/*
%_infodir/*


%files -n %lname-devel
%doc examples *html
%_includedir/*
%_libdir/%lname.a


%changelog
* Mon Feb 05 2018 Fr. Br. George <george@altlinux.ru> 0.9.27-alt1
- Resurrect with packaging schheme changed
- Update to 0.9.27

* Mon Jul 18 2016 Fr. Br. George <george@altlinux.ru> 0.9.26.0.727.4134994-alt1
- Upstream changed to http://repo.or.cz/tinycc.git
- Update to 0.9.26-727-g4134994

* Thu Dec 03 2015 Igor Vlasenko <viy@altlinux.ru> 0.9.26-alt1.1
- NMU: added BR: texinfo

* Thu Apr 18 2013 Led <led@altlinux.ru> 0.9.26-alt1
- 0.9.26
- Makefile:
  + don't strip binaries when install
  + dont' link with libm
- updated BuildRequires
- cleaned up spec
- build with default %%_optlevel
- added %%check section

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
