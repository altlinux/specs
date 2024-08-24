%define _unpackaged_files_terminate_build 1
%define import_path github.com/charmbracelet/glow/v1.5.1

Name: glow
Version: 2.0.0
Release: alt1

Summary: Render markdown on the CLI, with pizzazz!
License: MIT
Group: Text tools
Url: https://github.com/charmbracelet/glow
ExclusiveArch: %go_arches

Source0: %name-%version.tar
Source1: %name-%version-vendor.tar

BuildRequires(pre): rpm-build-golang

%description
Glow is a terminal based markdown reader designed from
the ground up to bring out the beauty and power of the CLI.

%prep
%setup -a1
# This is necessary for the --version flag to work correctly.
sed -i 's/Version = ""/Version = "%version"/' main.go

%build
export BUILDDIR="$PWD/.build"
export IMPORT_PATH="%import_path"
export GOPATH="$BUILDDIR:%go_path"
%golang_prepare

pushd $BUILDDIR/src/$IMPORT_PATH
export LDFLAGS="-X '%import_path/config.Vendor=%vendor'"
%golang_build  .
popd

%install
export BUILDDIR="$PWD/.build"
export IGNORE_SOURCES=1
%golang_install

%files
%doc README.md LICENSE
%_bindir/%name

%changelog
* Sat Aug 24 2024 Ajrat Makhmutov <rauty@altlinux.org> 2.0.0-alt1
- New version.
- Fix the unknown version output with the --version flag.

* Tue Mar 05 2024 Ajrat Makhmutov <rauty@altlinux.org> 1.5.1.20.gcece137-alt1
- First build for ALT.
