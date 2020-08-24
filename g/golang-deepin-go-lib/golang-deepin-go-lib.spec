%global _unpackaged_files_terminate_build 1
%set_verify_elf_method unresolved=no

%global project pkg.deepin.io
%global repo lib
%global provider_prefix %project/%repo
%global import_path %provider_prefix

# %%ifnarch s390x
%def_without check
# %%endif

Name: golang-deepin-go-lib
Version: 5.5.0.1
Release: alt2
Summary: Go bindings for Deepin Desktop Environment development

License: GPL-3.0-only and BSD-2-Clause and BSD-3-Clause
Group: Development/Other
Url: https://github.com/linuxdeepin/go-lib
Packager: Leontiy Volodin <lvol@altlinux.org>

Source: %url/archive/%version/go-lib-%version.tar.gz
# Fix Warning/Info calls with formatting directives
Patch: 0001-fix-format-calls.patch

BuildRequires: rpm-build-golang
BuildRequires: deepin-gir-generator dbus-tools-gui iso-codes mobile-broadband-provider-info
#BuildRequires: golang(github.com/cryptix/wav) golang(github.com/linuxdeepin/go-x11-client) golang(golang.org/x/image/bmp) golang(golang.org/x/image/tiff) golang(golang.org/x/net/context) golang(gopkg.in/alecthomas/kingpin.v2) golang(github.com/godbus/dbus)
BuildRequires: libgio-devel libgtk+3-devel libgdk-pixbuf-devel libpulseaudio-devel
BuildRequires: golang-github-cryptix-wav-devel golang-deepin-go-x11-client-devel golang-x-image-devel golang-golang-x-net-devel golang-gopkg-alecthomas-kingpin-2-devel
Requires: golang-github-go-dbus-devel

%if_with check
# Tests
BuildRequires: golang(github.com/smartystreets/goconvey/convey)
BuildRequires: golang(github.com/stretchr/testify/assert)
BuildRequires: golang(gopkg.in/check.v1)
%endif

#Requires: deepin-gir-generator dbus-tools-gui iso-codes mobile-broadband-provider-info
#Requires: libgio-devel libgtk+3-devel libgdk-pixbuf-devel libpulseaudio-devel

%description
Deepin Golang library is a library containing many useful go routines for things
such as glib, gettext, archive, graphic,etc.

%package devel
Summary: Go bindings for Deepin Desktop Environment development
Group: Development/Other
BuildArch: noarch

%description devel
Deepin Golang library is a library containing many useful go routines for things
such as glib, gettext, archive, graphic,etc.

%prep
%setup -n go-lib-%version
# %%patch -p1

%build
export BUILDDIR="$PWD/.build"
export IMPORT_PATH="%import_path"
export GOPATH="%go_path"
export CGO_ENABLED=1

%golang_prepare

cd .build/src/%import_path
%golang_build

%install
export BUILDDIR="$PWD/.build"
export GOPATH="%go_path"
%golang_install

%if_with check
%check
%gotest -d log -d procfs -d pulse -d shell -t users -d iso
%endif

%files devel
%go_path/src/%import_path

%changelog
* Mon Aug 24 2020 Leontiy Volodin <lvol@altlinux.org> 5.5.0.1-alt2
- Added golang(github.com/godbus/dbus) to requires.

* Tue Jul 28 2020 Leontiy Volodin <lvol@altlinux.org> 5.5.0.1-alt1
- Initial build for ALT Sisyphus (thanks fedora for this spec).

