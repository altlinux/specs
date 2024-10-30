%define _unpackaged_files_terminate_build 1

Name:    txt2pho
Version: 0.96
Release: alt2

Summary: A TTS frontend for the German inventories of the MBROLA project (Official Repository)
License: AGPL-3.0
Group:   Other
Url:     https://github.com/GHPS/txt2pho

Source: %name-%version.tar
Source3:        say
Source4:        txt2phorc
Patch0: %name-%version-fix-gcc11+-build.patch

Requires: mbrola-voices-de6

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
install -m 755 %SOURCE3 %buildroot%_bindir/mbrola-de6-say

%files
%config(noreplace) %_sysconfdir/txt2pho
%doc *.md
%_bindir/preproc
%_bindir/pipefilt
%_bindir/txt2pho
%_bindir/mbrola-de6-say
%_datadir/mbrola/*

%changelog
* Tue Oct 22 2024 Artem Semenov <savoptik@altlinux.org> 0.96-alt2
- Add req to mbrola-voices-de6
- Add say script

* Fri Sep 13 2024 Artem Semenov <savoptik@altlinux.org> 0.96-alt1
- Initial build for Sisyphus
