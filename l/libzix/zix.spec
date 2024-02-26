Name: libzix
Version: 0.4.2
Release: alt1

Summary: Lightweight C library of portability wrappers and data structures.
License: 0BSD
Group: System/Libraries
Url: https://gitlab.com/drobilla/zix

Source: %name-%version-%release.tar

BuildRequires: meson

%package devel
Summary: Lightweight C library of portability wrappers and data structures.
Group: Development/C

%description
%summary

%description devel
%summary

%prep
%setup

%build
%meson
%meson_build

%install
%meson_install

%files
%_libdir/*.so.*

%files devel
%doc COPYING README*
%_includedir/zix-0
%_libdir/*.so
%_pkgconfigdir/*.pc

%changelog
* Mon Feb 26 2024 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.4.2-alt1
- initial
