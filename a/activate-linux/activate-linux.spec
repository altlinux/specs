Name:     activate-linux
Version:  0.0.2
Release:  alt1

Summary:  The "Activate Windows" watermark ported to Linux

License:  GPL-3.0
Group:    Other
Url:      https://github.com/MrGlockenspiel/activate-linux

Packager: Grigory Ustinov <grenka@altlinux.org>

Source:   %name-%version.tar

# BuildRequires from upstream spec
BuildRequires: clang libcairo-devel libXi-devel libX11-devel
BuildRequires: xorg-proto-devel xorg-xcbproto-devel libXt-devel
# What they didn't mention
BuildRequires: libXinerama-devel

%description
The "Activate Windows" watermark ported to Linux with Xlib and cairo in C.
Science isn't about WHY. It's about WHY NOT. Why is so much of our
science dangerous? Why not marry safe science if you love it so much.
In fact, why not invent a special safety door that won't hit you...

%prep
%setup

%build
%make_build

%install
export PREFIX=""
export BINDIR="%_bindir"
%makeinstall_std

%files
%_bindir/%name
%doc *.md

%changelog
* Fri May 20 2022 Grigory Ustinov <grenka@altlinux.org> 0.0.2-alt1
- Automatically updated to 0.0.2.

* Wed May 18 2022 Grigory Ustinov <grenka@altlinux.org> 0.0.1-alt1
- Initial build for Sisyphus.
