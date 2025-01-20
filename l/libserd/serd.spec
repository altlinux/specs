Name: libserd
Version: 0.32.4
Release: alt1

Summary: Lightweight C library for working with RDF data.
License: 0BSD
Group: System/Libraries
Url: https://gitlab.com/drobilla/serd

Source: %name-%version-%release.tar

BuildRequires: meson

%package devel
Summary: Lightweight C library for working with RDF data.
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
%_bindir/serdi
%_libdir/*.so.*
%_man1dir/serdi.1*

%files devel
%doc COPYING README*
%_includedir/serd-0
%_libdir/*.so
%_pkgconfigdir/*.pc

%changelog
* Mon Jan 20 2025 Sergey Bolshakov <sbolshakov@altlinux.org> 0.32.4-alt1
- 0.32.4 released

* Mon Feb 26 2024 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.32.2-alt1
- 0.32.2 released
