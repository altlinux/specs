Name: liberasurecode
Version: 1.6.0
Release: alt1
Summary: Erasure Code API library written in C with pluggable backends
Group: System/Libraries

# This is a 2-clause BSD with clause numbers edited out for some reason.
# Some files are under "heavily cut-down "BSD license", see
# src/utils/chksum/md5.c for example.
# XXX There is also GPLv3+ in m4/ that upstream is working to remove.
License: BSD
Url: https://bitbucket.org/tsg-/liberasurecode/
# Bitbucket's web export naming is like the old github (== awful), so we pull
# the tag using git CLI. Save the current command for Source0 below.
# git archive -o ../liberasurecode-1.0.7.tar.gz --prefix=liberasurecode-1.0.7/ v1.0.7
Packager: Lenar Shakirov <snejok@altlinux.ru>

Source: %name-%version.tar
Patch2: liberasurecode-1.6.0-docs.patch

BuildRequires: autoconf
BuildRequires: automake
BuildRequires: libtool
BuildRequires: doxygen
BuildRequires: zlib-devel

%set_verify_elf_method unresolved=relaxed

%description
An API library for Erasure Code, written in C. It provides a number
of pluggable backends, such as Intel ISA-L library.

%package doc
Summary: Documentation for %name
Group: System/Libraries

%description doc
The documentation for %name.

%package devel
Summary: Development files for %name
Group: System/Libraries
Requires: %name = %version-%release

%description devel
The %name-devel package contains libraries and header files for
developing applications that use %name.

%prep
%setup
%patch2 -p2

%build
autoreconf -i -v
%configure --disable-static
make V=1 %{?_smp_mflags}

%install
%makeinstall_std

%files
%doc README.md COPYING
%_libdir/*.so.*

%files doc
%_docdir/liberasurecode/html/*

%files devel
%_includedir/*
%_libdir/*.so

%changelog
* Fri May 31 2019 Grigory Ustinov <grenka@altlinux.org> 1.6.0-alt1
- Build new version.

* Wed Sep 23 2015 Lenar Shakirov <snejok@altlinux.ru> 1.0.8-alt1
- First build for ALT

