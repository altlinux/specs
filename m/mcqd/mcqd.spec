# The only release tarball is old, so we check out of git.
%define gitdate     20160901
%define commit      9ab9717cf7d1be1a85b165a8eacb71b9e5831113
%define shortcommit %(c=%commit; echo ${c:0:7})
%define soname 0

Name: mcqd
Version: 1.0.0
Release: alt1
Summary: Maximum clique in an undirected graph

License: GPL-3.0+
Group: Sciences/Mathematics
Url: http://insilab.org/maxclique/

Source: https://gitlab.com/janezkonc/mcqd/-/archive/%commit/%name-%shortcommit.tar.gz
# Sagemath patch to reduce verbosity
Patch: %name-silent.patch
# Split the main function out into its own file to facilitate building a library
Patch1: %name-library.patch

BuildRequires: gcc-c++

%description
This package provides a command line tool for computing the maximum
clique of an undirected graph.  Input is in DIMACS format.

%package -n lib%name%soname
Summary: Library for %name
Group: System/Libraries

%description -n lib%name%soname
This package computes MaxCliqueDyn, a fast exact algorithm for finding a
maximum clique in an undirected graph.

%package -n lib%name-devel
Summary: Headers and library links for %name
Group: Development/C++

%description -n lib%name-devel
Headers and library links for building applications that use %name.

%prep
%setup -n %name-%shortcommit
%patch -p0
%patch1 -p0

# Change from Windows to Unix newlines
%__subst 's/\r//' *.{cpp,h}

%build
# Build the library
g++ -fPIC -shared %optflags $RPM_LD_FLAGS -Wl,-h,lib%name.so.0 \
    -o lib%name.so.0.0.0 %name.cpp
ln -s lib%name.so.0.0.0 lib%name.so.0
ln -s lib%name.so.0 lib%name.so

# Build the binary
g++ %optflags $RPM_LD_FLAGS -o %name %name-main.cpp -L. -lmcqd

%install
# Install the library
mkdir -p %buildroot%_libdir
cp -p lib%name.so.0.0.0 %buildroot%_libdir
ln -s lib%name.so.0.0.0 %buildroot%_libdir/lib%name.so.0
ln -s lib%name.so.0 %buildroot%_libdir/lib%name.so

# Install the header file
mkdir -p %buildroot%_includedir
cp -p %name.h %buildroot%_includedir

# Install the binary
mkdir -p %buildroot%_bindir
cp -p %name %buildroot%_bindir

%check
LD_LIBRARY_PATH=$PWD ./mcqd test.clq > test.log 2>&1
[ $(grep -F 'Maximum clique:' test.log | wc -l) -eq 2 ]

%files
%doc COPYING README.md
%_bindir/%name

%files -n lib%name%soname
%_libdir/lib%name.so.%{soname}*

%files -n lib%name-devel
%_includedir/%name.h
%_libdir/lib%name.so

%changelog
* Fri Nov 26 2021 Leontiy Volodin <lvol@altlinux.org> 1.0.0-alt1
- Initial build for ALT Sisyphus (thanks fedora for the spec).
- Built as require for sagemath.
