Name: gocryptfs
Version: 2.5.3
Release: alt2

%define builddate 2025-04-05

Summary: An encrypted overlay filesystem written in Go
Summary(ru_RU.UTF-8): Виртуальная файловая система с шифрованием

License: MIT
Group: File tools
Url: https://github.com/rfjakob/gocryptfs
VCS: https://github.com/rfjakob/gocryptfs.git

Packager: Alexei Mezin <alexvm@altlinux.ru>

Source: %name-%version.tar
Source1: %name-development-%version.tar


BuildRequires(pre): rpm-macros-golang
BuildRequires(pre): rpm-build-compat
BuildRequires(pre): pandoc bash


ExclusiveArch: %go_arches

BuildRequires: golang
BuildRequires: pkgconfig(libcrypto)

%description
gocryptfs is an encrypted overlay filesystem build on top of go-fuse FUSE library. It can be used for
making encrypted backups with simple tools like rsync.

%description -l ru_RU.UTF-8
gocryptfs это виртуальная файловая ситема с шифрованием на основе FUSE-библиотеки go-fuse. 
Ее можно исползовть, например, для создания зашифрованных резервных копий такими простыми средствами, как rsync.


%prep
%setup -a1

%build
export GOTAGS=openssl
export GO_LDFLAGS="-X \"main.GitVersion=%version\" -X \"main.BuildDate=%builddate\""
export GO_LDFLAGS="$GO_LDFLAGS \"-extldflags=$LDFLAGS\""

# Fix build on i586. See upstream bug 907
# Remove this fix in next release!
pushd internal/syscallcompat
mv thread_credentials_linux_368_arm.go thread_credentials_linux_32.go
popd


go build -mod=vendor -buildmode=pie "-ldflags=$GO_LDFLAGS"
pushd gocryptfs-xray
go build -mod=vendor -buildmode=pie "-ldflags=$GO_LDFLAGS"
popd
pushd Documentation
bash ./MANPAGE-render.bash
popd
pandoc -t html README.md > README.html

%install
install -p -m755 -D %name %buildroot/%_bindir/%name
install -p -m755 -D %name-xray/%name-xray %buildroot/%_bindir/%name-xray
install -p -m644 -D Documentation/%name.1 %buildroot/%_man1dir/%name.1
install -p -m644 -D Documentation/%name-xray.1 %buildroot/%_man1dir/%name-xray.1



%files
%_bindir/*
%_man1dir/*
%doc LICENSE* README.html

%changelog
* Sun Apr 06 2025 Alexei Mezin <alexvm@altlinux.org> 2.5.3-alt2
- Fix build on i586

* Sat Apr 05 2025 Alexei Mezin <alexvm@altlinux.org> 2.5.3-alt1
- New version

* Sat Feb 15 2025 Alexei Mezin <alexvm@altlinux.org> 2.5.1-alt1
- Initial build

