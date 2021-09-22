Name: libmimetic
Version: 0.9.8
Release: alt2
Summary: A full featured C++ MIME library
License: MIT
Group: System/Libraries
Url: http://www.codesink.org/mimetic_mime_library.html

Packager: Leontiy Volodin <lvol@altlinux.org>

Source: http://www.codesink.org/download/mimetic-%version.tar.gz
Patch: mimetic-%version-signedness-fix.patch
Patch1: mimetic-gcc11.patch

BuildRequires(pre): automake_1.11
BuildRequires: gcc-c++ doxygen findutils

%description
mimetic is an Email library (MIME) written in C++ designed to be easy to use
and integrate but yet fast and efficient.

It has been built around the standard lib. This means that you'll not find yet
another string class or list implementation and that you'll feel comfortable
in using this library from the very first time.

Most classes functionalities and behavior will be clear if you ever studied
MIME and its components; if you don't know anything about Internet messages
you'll probably want to read some RFCs to understand the topic and, therefore,
easily use the library whose names, whenever possible, overlap terms adopted
in the standard RFC documents. At the very least: RFC 822, RFC 2045 and RFC
2046.

%package devel
Summary: Development files for %name
Group: Development/Other

%description devel
This package contains libraries and header files for
developing applications that use %name.

%prep
%setup -n mimetic-%version
%patch -p1
%patch1 -p1

%build
%set_automake_version 1.11
%configure --disable-static
%make_build
make docs -C doc

%install
%makeinstall_std

# %%check
# make check

%files
%doc COPYING LICENSE
%doc AUTHORS ChangeLog README
%_libdir/libmimetic.so.*

%files devel
%doc doc/html/*
%_includedir/mimetic/
%_libdir/libmimetic.so

%changelog
* Wed Sep 22 2021 Leontiy Volodin <lvol@altlinux.org> 0.9.8-alt2
- Enabled the patch for gcc11.

* Tue Oct 06 2020 Leontiy Volodin <lvol@altlinux.org> 0.9.8-alt1
- Initial build for ALT Sisyphus (thanks fedora for this spec).
