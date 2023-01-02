%define gobuild go build

Name: goredo
Version: 1.28.0
Release: alt1

Summary: Go implementation of djb's redo, Makefile replacement that sucks less

Group: Development/Tools
License: GPLv3
Url: http://www.goredo.cypherpunks.ru/index.html

Packager: Vitaly Lipatov <lav@altlinux.ru>

# Source-url: http://www.goredo.cypherpunks.ru/download/goredo-%version.tar.zst
Source: %name-%version.tar

ExclusiveArch: %go_arches

BuildRequires(pre): rpm-macros-golang

BuildRequires: golang >= 1.7

%description
Originally it was just a rewrite of redo-c,
but later most features of apenwarr/redo were also implemented.
Why yet another implementation? It is feature full and has better performance
comparing to shell and Python implementation.

%prep
%setup

%build
cd src
go build -mod=vendor
./goredo -symlinks

%install
mkdir -p %buildroot%_bindir/
cp -a src/goredo src/redo* %buildroot%_bindir/
# TODO: install-info: warning: no info dir entry in
#mkdir -p %buildroot%_infodir/
#install -m644 goredo.info %buildroot%_infodir/

%files
%doc NEWS INSTALL README THANKS
%_bindir/goredo
%_bindir/redo*
#%_infodir/*

%changelog
* Mon Jan 02 2023 Vitaly Lipatov <lav@altlinux.ru> 1.28.0-alt1
- new version

* Sat Jan 23 2021 Vitaly Lipatov <lav@altlinux.ru> 1.0.0-alt1
- initial build for ALT Sisyphus
