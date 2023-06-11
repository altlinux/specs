Name:    sxhkd
Version: 0.6.2
Release: alt1

Summary: Simple X hotkey daemon
License: BSD-2-Clause
Group:   System/Configuration/Other
Url:     https://github.com/baskerville/sxhkd

Source:  %name-%version.tar

BuildRequires:  pkgconfig(xcb)
BuildRequires:  pkgconfig(xcb-keysyms)
BuildRequires:  pkgconfig(xcb-util)

%description
sxhkd is a simple X hotkey daemon with a powerful and compact configuration syntax.

%prep
%setup

%build
%make_build

%install
%makeinstall_std PREFIX=%_prefix

%files
%_bindir/%name
%_docdir/%name/
%_man1dir/%name.1.*

%changelog
* Fri Jun 02 2023 Roman Alifanov <ximper@altlinux.org> 0.6.2-alt1
- Initial build for Sisyphus
