Name: libtllist-devel
Version: 1.0.5
Release: alt1

Summary: A C header file only implementation of a typed linked list. 
License: MIT
Group: Development/C
Url: https://codeberg.org/dnkl/tllist

Source: %name-%version-%release.tar

BuildRequires: meson

%description
%summary

%prep
%setup

%build
%meson
%meson_build

%install
%meson_install

%files
%doc README* LICENSE
%_includedir/tllist.h
%_pkgconfigdir/tllist.pc

%changelog
* Mon Aug 02 2021 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.0.5-alt1
- 1.0.5 released
