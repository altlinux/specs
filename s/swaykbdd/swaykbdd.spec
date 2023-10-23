Name: swaykbdd
Version: 1.4
Release: alt1

Summary: Per-window keyboard layout for Sway
License: MIT
Group: Graphical desktop/Other
Url: https://github.com/artemsen/swaykbdd

Source: %name-%version-%release.tar

BuildRequires: meson
BuildRequires: pkgconfig(json-c)

%description
The swaykbdd utility can be used to automatically change the keyboard layout
on a per-window basis

%prep
%setup

%build
%meson
%meson_build

%install
%meson_install

%files
%doc README* LICENSE
%_bindir/swaykbdd
%_man1dir/swaykbdd.1*

%changelog
* Mon Oct 23 2023 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.4-alt1
- 1.4 released

* Thu Oct 12 2023 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.2-alt1
- 1.2 released

* Wed Apr 20 2022 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.1-alt1
- 1.1 released

* Mon Aug 09 2021 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.0-alt1
- initial
