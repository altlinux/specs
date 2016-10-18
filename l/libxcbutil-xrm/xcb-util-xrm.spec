%def_disable static
%define origname xcb-util-xrm 
Name: libxcbutil-xrm 
Version: 1.0
Release: alt1

Summary: The XCB util modules provides a number of libraries which sit on top of libxcb
License: MIT
Group: System/Libraries

Url: https://github.com/Airblader/xcb-util-xrm 
Source: %origname-%version.tar
Packager: Konstantin Artyushkin <akv@altlinux.org>
BuildRequires: libxcb-devel
BuildRequires: libxcbutil-devel
BuildRequires: xorg-util-macros
BuildRequires: doxygen


%description
The XCB util modules provides a number of libraries which sit on top
of libxcb, the core X protocol library, and some of the extension
libraries. These experimental libraries provide convenience functions
and interfaces which make the raw X protocol more usable. Some of the
libraries also provide client-side code which is not strictly part of
the X protocol but which have traditionally been provided by Xlib.

#--------------------------------------------------------------------------------
%package devel
Summary: Headers for %name
Group: Development/C
Requires: %name = %version-%release

%description devel
Headers for building software that uses %name

%if_enabled static
    %package devel-static
    Summary: Static libraries for %name
    Group: Development/C
    Requires: %name-devel = %version-%release

    %description devel-static
    Static libs for building statically linked software that uses %name
%endif
#--------------------------------------------------------------------------------

%prep
%setup -n %origname-%version

%build
%configure %{subst_enable static}
%make_build

%install
%makeinstall_std

%files
%_libdir/libxcb-xrm.so.0
%_libdir/libxcb-xrm.so.0.0.0
%doc ChangeLog README COPYING

#--------------------------------------------------------------------------------
%files devel
%_includedir/xcb/*.h
%_libdir/*.so
%_pkgconfigdir/*.pc

%if_enabled static
    %files devel-static
    %_libdir/lib%name.a
%endif
#--------------------------------------------------------------------------------


%changelog
* Tue Oct 18 2016 Konstantin Artyushkin <akv@altlinux.org> 1.0-alt1
- initial build for ALT Linux Sisyphus

