Name: libsord
Version: 0.16.16
Release: alt1

Summary: Lightweight C library for storing RDF statements in memory
License: 0BSD
Group: System/Libraries
Url: https://gitlab.com/drobilla/sord

Source: %name-%version-%release.tar

BuildRequires: meson
BuildRequires: pkgconfig(serd-0)
BuildRequires: pkgconfig(zix-0)

%package devel
Summary: Lightweight C library for storing RDF statements in memory
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
%_bindir/sordi
%_libdir/*.so.*
%_man1dir/sord*.1*

%files devel
%doc COPYING README*
%_includedir/sord-0
%_libdir/*.so
%_pkgconfigdir/*.pc

%changelog
* Mon Feb 26 2024 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.16.16-alt1
- 0.16.16 released
