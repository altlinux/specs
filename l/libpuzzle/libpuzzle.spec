Name: libpuzzle
Version: 0.11
Release: alt2

Summary: A library for finding visually similar bitmap pictures
License: BSD
Group: System/Libraries

URL: http://libpuzzle.pureftpd.org/
Source: http://download.pureftpd.org/pub/pure-ftpd/misc/libpuzzle/releases/libpuzzle-%version.tar.bz2

# Automatically added by buildreq on Tue Sep 29 2009
BuildRequires: gcc-c++ libgd2-devel

%description
The Puzzle library is designed to quickly find visually similar images (GIF,
PNG, JPG), even if they have been resized, recompressed, recolored, or slightly
modified. The library is lightweight yet very fast, configurable, and easy to
use, and was designed with security in mind.

%package devel
Summary: Development tools for programs which will use the %name library
Group: Development/C
Requires: %name = %version-%release

%description devel
The %name-devel package includes the header files necessary for developing
programs which will use the %name library.

%prep
%setup

%build
%configure --disable-static
# fix rpath libtool issues
subst 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' libtool
subst 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' libtool
%make_build

%install
%makeinstall_std

%files
%doc COPYING README THANKS
%_bindir/*
%_libdir/lib*.so.*
%_man8dir/*

%files devel
%_includedir/*
%_libdir/lib*.so
%_man3dir/*

%changelog
* Tue Dec 27 2011 Victor Forsiuk <force@altlinux.org> 0.11-alt2
- Fix RPATH issue.

* Tue Sep 29 2009 Victor Forsyuk <force@altlinux.org> 0.11-alt1
- 0.11
- Remove obsolete ldconfig calls.

* Mon Nov 26 2007 Victor Forsyuk <force@altlinux.org> 0.9-alt1
- 0.9

* Thu Sep 20 2007 Victor Forsyuk <force@altlinux.org> 0.6-alt1
- Initial build.
