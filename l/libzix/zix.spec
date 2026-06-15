Name: libzix
Version: 0.8.2
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
* Mon Jun 15 2026 Sergey Bolshakov <sbolshakov@altlinux.org> 0.8.2-alt1
- 0.8.2 released

* Thu Nov 13 2025 Sergey Bolshakov <sbolshakov@altlinux.org> 0.8.0-alt1
- 0.8.0 released

* Mon Jan 20 2025 Sergey Bolshakov <sbolshakov@altlinux.org> 0.6.2-alt1
- 0.6.2 released

* Mon Feb 26 2024 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.4.2-alt1
- initial
