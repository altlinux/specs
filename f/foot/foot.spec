Name: foot
Version: 1.18.1
Release: alt1

Summary: A fast, lightweight and minimalistic Wayland terminal emulator
License: MIT
Group: Terminals
Url: https://codeberg.org/dnkl/foot

Source: %name-%version-%release.tar

BuildRequires: meson scdoc
BuildRequires: pkgconfig(tllist)
BuildRequires: pkgconfig(pixman-1)
BuildRequires: pkgconfig(wayland-protocols)
BuildRequires: pkgconfig(wayland-client)
BuildRequires: pkgconfig(wayland-cursor)
BuildRequires: pkgconfig(xkbcommon)
BuildRequires: pkgconfig(fontconfig)
BuildRequires: pkgconfig(fcft) >= 3.0.0
BuildRequires: pkgconfig(systemd)
BuildRequires: pkgconfig(libutf8proc)

%description
%summary

%prep
%setup

%build
%meson -Dterminfo=disabled
%meson_build

%install
%meson_install

%files
%doc %_defaultdocdir/foot
%_sysconfdir/xdg/foot
%_bindir/foot
%_bindir/footclient
%_libexecdir/systemd/user/foot-server*
%_datadir/foot
%_desktopdir/*
%_datadir/bash-completion/*/*
%_datadir/fish/vendor_completions.d/*
%_datadir/zsh/site-functions/*
%_iconsdir/*/*/*/*
%_mandir/*/*

%changelog
* Thu Aug 29 2024 Sergey Bolshakov <sbolshakov@altlinux.org> 1.18.1-alt1
- 1.18.1 released

* Wed Apr 17 2024 Sergey Bolshakov <sbolshakov@altlinux.org> 1.17.2-alt1
- 1.17.2 released

* Thu Apr 11 2024 Sergey Bolshakov <sbolshakov@altlinux.org> 1.17.1-alt1
- 1.17.1 released

* Tue Apr 02 2024 Sergey Bolshakov <sbolshakov@altlinux.org> 1.17.0-alt1
- 1.17.0 released

* Tue Oct 17 2023 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.16.2-alt1
- 1.16.2 released

* Thu Oct 12 2023 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.16.1-alt1
- 1.16.1 released

* Thu Oct 12 2023 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.16.0-alt2
- do not fail miserably on pre-6.3 kernels

* Thu Oct 12 2023 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.16.0-alt1
- 1.16.0 released

* Mon Aug 14 2023 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.15.3-alt1
- 1.15.3 released

* Fri Jul 21 2023 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.15.1-alt1
- 1.15.1 released

* Fri Jul 14 2023 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.15.0-alt1
- 1.15.0 released

* Tue Jul 04 2023 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.14.0-alt2
- fix build with recent wayland proto

* Tue Apr 04 2023 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.14.0-alt1
- 1.14.0 released

* Thu Sep 01 2022 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.13.1-alt1
- 1.13.1 released

* Mon Aug 08 2022 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.13.0-alt1
- 1.13.0 released

* Thu Apr 28 2022 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.12.1-alt1
- 1.12.1 released

* Tue Apr 26 2022 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.12.0-alt2
- workarounds for sway issue 6960

* Mon Apr 25 2022 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.12.0-alt1
- 1.12.0 released

* Sat Feb 05 2022 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.11.0-alt1
- 1.11.0 released

* Fri Jan 28 2022 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.10.3-alt1
- initial
