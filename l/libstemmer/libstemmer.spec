Name: libstemmer
Version: 2.2.0
Release: alt1
Summary: C stemming algorithm library

Group: System/Libraries
License: BSD-2-Clause
Url: https://snowballstem.org/
VCS: https://github.com/snowballstem/snowball

Source0: %name-%version.tar

# perl: GNUmakefile generates algorithms.mk / modules.h via libstemmer/*.pl
BuildRequires: perl-base

%description
Snowball stemming algorithms for use in Information Retrieval Snowball
provides access to efficient algorithms for calculating a "stemmed"
form of a word.  This is a form with most of the common morphological
endings removed; hopefully representing a common linguistic base form.
This is most useful in building search engines and information
retrieval software; for example, a search with stemming enabled should
be able to find a document containing "cycling" given the query
"cycles".

Snowball provides algorithms for several (mainly European) languages.
It also provides access to the classic Porter stemming algorithm for
English: although this has been superseded by an improved algorithm,
the original algorithm may be of interest to information retrieval
researchers wishing to reproduce results of earlier experiments.

%package -n %name-devel
Summary: libstemmer development libraries and includes
Group: Development/C
Requires: %name = %version-%release

%description -n %name-devel
Development files for C stemmer library

%prep
%setup

%build
# Upstream git tree: compile snowball, generate C sources, then static lib.
# Shared library is not shipped; link it from PIC objects.
%make_build libstemmer.a CFLAGS="%optflags -fPIC"
%__cc %optflags -shared -Wl,-soname,%name.so.0 \
	-o %name.so.0.0.0 -Wl,--whole-archive libstemmer.a -Wl,--no-whole-archive

%install
mkdir -p %buildroot%_libdir
mkdir -p %buildroot%_includedir
install -p -m755 %name.so.0.0.0 %buildroot%_libdir/
ln -s %name.so.0.0.0 %buildroot%_libdir/%name.so.0
ln -s %name.so.0.0.0 %buildroot%_libdir/%name.so
install -p -m644 include/* %buildroot%_includedir/

%files -n %name
%doc README.rst COPYING
%_libdir/%name.so.*

%files -n %name-devel
%_includedir/*
%_libdir/%{name}.so

%changelog
* Thu Sep 17 2026 Anton Farygin <rider@altlinux.org> 2.2.0-alt1
- 2.0.0 -> 2.2.0
- switch to build from upstream git (GNUmakefile, generated C sources)

* Wed Aug 5 2020 Vladimir Didenko <cow@altlinux.org> 2.0.0-alt1
- New version

* Wed Nov 20 2019 Vladimir Didenko <cow@altlinux.org> 0-alt2.svn585
- Fix license name

* Tue Mar 24 2015 Vladimir Didenko <cow@altlinux.org> 0-alt1.svn585
- Initial build
