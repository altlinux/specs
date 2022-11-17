Name: wvkbd
Version: 0.12
Release: alt1

Summary: On-screen keyboard for wlroots
License: GPLv3
Group: Graphical desktop/Other
Url: https://github.com/jjsullivan5196/wvkbd

Source: %name-%version.tar

BuildRequires: pkgconfig(pangocairo)
BuildRequires: pkgconfig(wayland-client)
BuildRequires: pkgconfig(xkbcommon)

%description
This project aims to deliver a minimal but practically usable
implementation of a wlroots on-screen keyboard in legible C.

%prep
%setup
sed -ri '/^VERSION/ s,=.+$,= %version-%release\\\\n,' config.mk

%build
make OPTFLAGS="%optflags"

%install
install -pm0755 -D wvkbd-mobintl %buildroot%_bindir/wvkbd
install -pm0644 -D wvkbd.1 %buildroot%_man1dir/wvkbd.1

%files
%doc LICENSE README.md
%_bindir/wvkbd
%_man1dir/wvkbd.1*

%changelog
* Thu Nov 17 2022 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.12-alt1
- 0.12 released

* Mon Oct 10 2022 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.11-alt1
- 0.11 released

* Fri Aug 26 2022 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.10-alt1
- 0.10 released

* Wed Jul 27 2022 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.9-alt1
- 0.9 released

* Mon Jun 20 2022 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.8.2-alt1
- 0.8.2 released

* Fri Apr 22 2022 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.7-alt1
- initial
