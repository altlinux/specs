Name: libsrs_alt
Version: 1.0
Release: alt4

Summary: Implementation of the SRS specification
License: GPLv2
Group: System/Libraries

URL: http://srs.mirtol.com/
Source0: http://srs.mirtol.com/libsrs_alt-%version.tar.bz2

# Automatically added by buildreq on Fri Jan 09 2009
BuildRequires: gcc-c++
# c++ not needed for compilation (code is plain C) but configure panics
# without it... :-\

%description
Libsrs_alt is an implementation of the SRS specification as found at
http://spf.pobox.com/srs.html.

%package devel
Summary: Development files for libsrs_alt library
Group: Development/C
Requires: %name = %version-%release

%description devel
Development files for libsrs_alt library.

%prep
%setup

%build
%configure --with-base64compat --disable-static
%make_build srs_LDFLAGS="-lsrs_alt -Lsrc/" test_LDFLAGS="-lsrs_alt -Lsrc/"

%install
%makeinstall_std

%files
%doc MTAs/README.EXIM
%_bindir/*
%_libdir/lib*.so.*
%exclude %_libdir/*.a

%files devel
%_libdir/lib*.so
%_includedir/*

%changelog
* Tue May 10 2011 Victor Forsiuk <force@altlinux.org> 1.0-alt4
- Rebuilt for debuginfo.

* Thu Jan 27 2011 Victor Forsiuk <force@altlinux.org> 1.0-alt3
- Rebuilt for soname set-versions.

* Fri Jan 09 2009 Victor Forsyuk <force@altlinux.org> 1.0-alt2
- Remove obsolete ldconfig calls.

* Tue Jul 12 2005 Victor Forsyuk <force@altlinux.ru> 1.0-alt1
- Enabled "--with-base64compat" as suggested by author.

* Tue Jan 18 2005 Victor Forsyuk <force@altlinux.ru> 0.5-alt1
- Initial build for Sysiphus.
