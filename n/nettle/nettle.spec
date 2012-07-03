Summary: Cryptographic library
Name: nettle
Version: 1.15
Release: alt1.2
License: GPL
Group: System/Libraries
URL: http://www.lysator.liu.se/~nisse/nettle/
Packager: Boris Savelev <boris@altlinux.org>
Source: nettle-%version.tar
Patch0: nettle-1.14-make-as-needed.patch

# Automatically added by buildreq on Thu Oct 20 2011
BuildRequires: gcc-c++ libgmp-devel libssl-devel

%description
Nettle is a cryptographic library that is designed to fit easily in more or
less any context: in crypto toolkits for object-oriented languages (C++,
Python, Pike, etc.), in applications like LSH or GNUPG, or even in kernel
space. In most contexts, you need more than the basic cryptographic
algorithms; you also need some way to keep track of available algorithms and
their properties and variants. You often have some algorithm selection
process, often dictated by a protocol you want to implement. And as the
requirements of applications differ in subtle and not so subtle ways, an API
that fits one application well can be a pain to use in a different context,
which is why there are so many different cryptographic libraries around.
Nettle tries to avoid this problem by doing one thing, the low-level crypto
stuff, and providing a simple but general interface to it. In particular,
Nettle doesn't do algorithm selection. It doesn't do memory allocation. It
doesn't do any I/O. The idea is that one can build several application- and
context-specific interfaces on top of Nettle and share the code, testcases,
benchmarks, documentation, etc.

%package -n lib%name
Summary: Cryptographic library
Group: System/Libraries

%description -n lib%name
Nettle is a cryptographic library that is designed to fit easily in more or
less any context: in crypto toolkits for object-oriented languages (C++,
Python, Pike, etc.), in applications like LSH or GNUPG, or even in kernel
space. In most contexts, you need more than the basic cryptographic
algorithms; you also need some way to keep track of available algorithms and
their properties and variants. You often have some algorithm selection
process, often dictated by a protocol you want to implement. And as the
requirements of applications differ in subtle and not so subtle ways, an API
that fits one application well can be a pain to use in a different context,
which is why there are so many different cryptographic libraries around.
Nettle tries to avoid this problem by doing one thing, the low-level crypto
stuff, and providing a simple but general interface to it. In particular,
Nettle doesn't do algorithm selection. It doesn't do memory allocation. It
doesn't do any I/O. The idea is that one can build several application- and
context-specific interfaces on top of Nettle and share the code, testcases,
benchmarks, documentation, etc.

%package -n lib%name-devel
Summary: Header files, libraries and development documentation for %name
Group: Development/C
Requires: lib%name = %version-%release

%description -n lib%name-devel
This package contains the header files, libraries and development
documentation for %name. If you like to develop programs using %name,
you will need to install %name-devel.

%prep
%setup
%patch0 -p1

%build
sed -i -e '/CFLAGS/s:-ggdb3::' configure.ac
%autoreconf
%configure --enable-shared
%make_build

%install
%makeinstall_std

%files -n lib%name
%doc AUTHORS NEWS README
%_bindir/*
%_libdir/*.so.*

%files -n lib%name-devel
%_includedir/*
%_libdir/*.so
%_infodir/*.*

%changelog
* Thu Oct 20 2011 Alexey Tourbin <at@altlinux.ru> 1.15-alt1.2
- rebuilt for debuginfo

* Mon Nov 08 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.15-alt1.1
- Rebuilt for soname set-versions

* Sat Feb 14 2009 Boris Savelev <boris@altlinux.org> 1.15-alt1
- initial build for Sisyphus

* Sat Jun 12 2004 Dries Verachtert <dries@ulyssis.org> - 1.10-1 #1833
- Fix ownership of devel package.

* Tue Jun 08 2004 Dries Verachtert <dries@ulyssis.org> - 1.10-1
- Initial package.
