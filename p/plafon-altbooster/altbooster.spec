%define oname altbooster

Name: plafon-altbooster
Version: 5.6.3
Release: alt1

Summary: GTK4 App Booster for ALT Linux
License: MIT
Group: System/Configuration/Other

Url: https://github.com/plafonlinux/altbooster
Vcs: https://github.com/plafonlinux/altbooster

BuildRequires(pre): rpm-build-python3

BuildArch: noarch
AutoReq: nopython3

Source: %name-%version.tar
Source1: Makefile
Source2: altbooster.desktop
Source3: altbooster

%description
%summary. 

%prep
%setup
cp -a %SOURCE1 ./
cp -a %SOURCE2 ./
cp -a %SOURCE3 ./

%build
%install
install -d %buildroot
%make_install \
    SHAREDIR=%buildroot%_datadir \
    PREFIXBIN=%buildroot%_bindir

%files
%doc LICENSE *.md
%_datadir/%oname
%_datadir/applications/%oname.desktop
%_iconsdir/hicolor/*/apps/*.svg
%_bindir/%%oname

%changelog
* Tue Mar 03 2026 Aleksandr Shamaraev <shad@altlinux.org> 5.6.3-alt1
- Initial build for ALT Linux.

