%define _unpackaged_files_terminate_build 1

Name:    txt2pho
Version: 0.96
Release: alt1

Summary: A TTS frontend for the German inventories of the MBROLA project (Official Repository)
License: AGPL-3.0
Group:   Other
Url:     https://github.com/GHPS/txt2pho

Source: %name-%version.tar
Source4:        txt2phorc
Patch0: %name-%version-fix-gcc11+-build.patch

BuildRequires: gcc-c++
BuildRequires: make

%description
%summary

%prep
%setup
%patch0 -p1
mkdir lib obj

%build
%make_build CFLAGS="%optflags" -j1

%install
mkdir -p %buildroot%_sysconfdir
mkdir -p %buildroot%_bindir
mkdir -p %buildroot%_datadir/mbrola

install -m 755 txt2pho %buildroot%_bindir/
cp -r data %buildroot%_datadir/mbrola/
install -m 755 pipefilt %buildroot%_bindir/
install -m 644 %SOURCE4 %buildroot%_sysconfdir/txt2pho
install -m 755 preproc %buildroot%_bindir/
install -m 644 data/PPRules/rules.lst %buildroot%_datadir/mbrola/
install -m 644 data/hadifix.abk %buildroot%_datadir/mbrola/

%files
%config(noreplace) %_sysconfdir/txt2pho
%doc *.md
%_bindir/*
%_datadir/mbrola/*

%changelog
* Fri Sep 13 2024 Artem Semenov <savoptik@altlinux.org> 0.96-alt1
- Initial build for Sisyphus
