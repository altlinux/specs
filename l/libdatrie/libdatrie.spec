%define soname 1
Group: System/Libraries
Name: libdatrie
Version: 0.2.13
Release: alt2
Summary: Implementation of Double-Array structure for representing trie
License: LGPL-2.1-or-later
Url: https://linux.thai.net/projects/datrie
VCS: https://github.com/tlwg/libdatrie
Source0: %name-%version.tar
Patch0: %name-%version-%release.patch
BuildRequires: autoconf, automake, libtool
BuildRequires: autoconf-archive
BuildRequires: doxygen, graphviz

%description
datrie is an implementation of double-array structure for representing trie.

Trie is a kind of digital search tree, an efficient indexing method with O(1)
time complexity for searching. Comparably as efficient as hashing, trie also
provides flexibility on incremental matching and key spelling manipulation.
This makes it ideal for lexical analyzers, as well as spelling dictionaries.

Details of the implementation: http://linux.thai.net/~thep/datrie/datrie.html

%package devel
Group: System/Libraries
Summary: Development files for %name
Requires: %name = %EVR

%description devel
This package contains libraries and header files for
developing applications that use %name.

%prep
%setup
%patch0 -p1
# fix VERSION in pkgconfig file
sed -i 's/m4_esyscmd(build-aux\/git-version-gen)/%version/' configure.ac
# enable png files creation via graphviz
sed -i 's/^\(HAVE_DOT[[:space:]]*=[[:space:]]*\)NO/\1YES/' doc/Doxyfile.in

%build
autoreconf -f -i -v
%configure --disable-static \
           --with-html-docdir=%_docdir/%name-devel-%version
%make_build

%install
%makeinstall_std

%check
LD_LIBRARY_PATH=../datrie/.libs %make_build check

%files
%doc COPYING
%_libdir/libdatrie.so.%soname
%_libdir/libdatrie.so.%soname.*

%files devel
%doc AUTHORS ChangeLog NEWS README* doc/html
%_includedir/datrie/
%_libdir/libdatrie.so
%_libdir/pkgconfig/datrie-0.2.pc
%_bindir/trietool*
%_mandir/man1/trietool*

%changelog
* Sat Nov 01 2025 Anton Farygin <rider@altlinux.com> 0.2.13-alt2
- fixed build in new environment

* Tue Aug 29 2023 Igor Vlasenko <viy@altlinux.org> 0.2.13-alt1_7
- update to new release by fcimport

* Tue Sep 21 2021 Igor Vlasenko <viy@altlinux.org> 0.2.13-alt1_2
- update to new release by fcimport

* Sun Nov 26 2017 Igor Vlasenko <viy@altlinux.ru> 0.2.9-alt1_6
- new version

* Mon Sep 08 2014 Igor Vlasenko <viy@altlinux.ru> 0.2.8-alt1_5
- new version

