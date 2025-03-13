%define _unpackaged_files_terminate_build 1

Name: gstm
Version: 1.3.7
Release: alt1

Summary: SSH tunnel manager for GNOME
License: GPL-2.0
Group: Networking/Remote access
Url: https://github.com/dallenwilson/gstm

Source: %name-%version.tar

Patch: %name-%version-%release.patch

BuildRequires: pkgconfig(gtk+-3.0)
BuildRequires: pkgconfig(libxml-2.0)
BuildRequires: pkgconfig(ayatana-appindicator3-0.1)

%description
GNOME Secure shell Tunnel Manager is a front-end to manage secure shell
tunneled port redirects. A port redirect is when you use secure shell to
tunnel from your machine through another machine.

%prep
%setup
%patch -p1

%build
./autogen.sh
%configure
%make_build

%install
%makeinstall_std

%check
%make_build check

%files
%doc AUTHORS ChangeLog COPYING NEWS README README.md
%_bindir/*
%_desktopdir/*.desktop
%exclude %_datadir/doc/gstm
%dir %_datadir/%name
%_datadir/%name/*
%_pixmapsdir/*

%changelog
* Thu Mar 13 2025 Nikolay Strelkov <snk@altlinux.org> 1.3.7-alt1
- Initial build for Sisyphus
