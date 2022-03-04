%define _unpackaged_files_terminate_build 1
%define _stripped_files_terminate_build 1
%set_verify_elf_method strict

%{?optflags_lto:%global optflags_lto %optflags_lto -ffat-lto-objects}

Name: colm
Version: 0.14.7
Release: alt1
Summary: The Colm Programming Language 
Group: Development/Other
License: MIT
Url: http://www.colm.net/open-source/colm/

# https://github.com/adrian-thurston/colm.git
Source: %name-%version.tar

# watch file
Source1000: %name.watch

Patch1: %name-0.14.7-disable-tests.patch

BuildRequires: gcc-c++
BuildRequires: asciidoc

Requires: lib%name = %EVR

%description
Colm = COmputer Language Machinery

Colm is a programming language designed for the analysis
and transformation of computer languages.
Colm is influenced primarily by TXL.
What is a transformation language?

A transformation language has a type system based on formal languages.
Rather than defining classes or data structures, one defines grammars.

A parser is constructed automatically from the grammar,
and the parser is used for two purposes:
*   to parse the input language,
*and to parse the structural patterns in the program that performs the analysis.

In this setting, grammar-based parsing is critical because it guarantees
that both the input and the structural patterns are parsed
into trees from the same set of types, allowing comparison.

Colm's features

Colm is not-your-typical-scripting-language (tm):
*   Colm's main contribution lies in the parsing method.
*   Colm's parsing engine is generalized, but it also allows
    for the construction of arbitrary global data structures
    that can be queried during parsing. In other generalized methods,
    construction of global data requires some very careful consideration
    because of inherent concurrency in the parsing method.
    It is such a tricky task that it is often avoided altogether and the problem
    is deferred to a post-parse disambiguation of the parse forest.
*   By default Colm will create an elf executable that can be used standalone
    for that actual transformations.
*   Colm is a static and strong typed scripting language.
*   Colm is very tiny and fast and can easily be embedded/linked with c/cpp programs.
*   Colm's runtime is a stackbased VM that starts with the bare minimum
    of the language and bootstraps itself.

%package -n lib%name
Summary: Colm libraries
Group: System/Libraries

%description -n lib%name
Colm libraries

%prep
%setup
%patch1 -p1

%build
%add_optflags -D_FILE_OFFSET_BITS=64

./autogen.sh
%configure \
	--disable-static \
	%nil

%make_build

%install
%makeinstall_std

%files
%doc COPYING
%doc CREDITS README
%_bindir/*
%_includedir/*
%_defaultdocdir/%name

%files -n lib%name
%doc COPYING
%doc CREDITS README
%_libdir/*.so
%_datadir/*.lm

%changelog
* Fri Mar 04 2022 Aleksei Nikiforov <darktemplar@altlinux.org> 0.14.7-alt1
- Initial build for ALT.
