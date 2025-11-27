%define _unpackaged_files_terminate_build 1
%define import_path github.com/GianlucaP106/mynav

Name:       mynav
Version:    2.2.0
Release:    alt1

License:    MIT
Group:      Terminals
Summary:    Workspace and session management TUI

Url:        https://github.com/GianlucaP106/mynav
Source:     %name-%version.tar
Source1:    vendor.tar

Patch:      %name-%version-%release.patch

BuildRequires(pre): rpm-build-golang

ExclusiveArch: %go_arches

%description
The terminal-based workspace navigator and session manager built in Go.
MyNav helps developers organize and manage multiple projects through an
intuitive interface, seamlessly integrating with tmux sessions.

%prep
%setup -a 1 -q
%patch -p1

%build
export BUILDDIR="$PWD/.build"
export IMPORT_PATH="%import_path"
export GOFLAGS="-mod=vendor"
export GOROOT="%_libexecdir/golang"

%golang_prepare

%golang_build .

%install
export BUILDDIR="$PWD/.build"
export IGNORE_SOURCES=1
export GOROOT="%_libexecdir/golang"
mkdir -p %buildroot%_datadir/%name

%golang_install

%files
%doc LICENSE README.*
%_bindir/%name

%changelog
* Fri Nov 21 2025 Sergey Savelev <medovi@altlinux.org> 2.2.0-alt1
- Initial build for Sisyphus.
