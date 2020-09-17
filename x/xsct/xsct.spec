Name: xsct
Version: 1.5
Release: alt1
Summary: set color temperature of screen
License: distributable
Group: System/X11
Url: https://github.com/faf0/sct

Source0: %name-%version.tar

BuildRequires(pre): rpm-build-licenses
BuildRequires: libXrandr-devel

%description
Xsct (X11 set color temperature) is a UNIX tool which allows you to set the color
temperature of your screen. It is simpler than Redshift and f.lux.

%prep
%setup

%build
%make_build CFLAGS="%optflags"

%install
%makeinstall_std PREFIX=%buildroot/%prefix

%files
%_bindir/xsct
%_man1dir/%name.1*
%doc LICENSE CHANGELOG README.md

%changelog
* Thu Sep 17 2020 Denis Smirnov <mithraen@altlinux.ru> 1.5-alt1
- first build for Sisyphus

