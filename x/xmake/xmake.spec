%define _unpackaged_files_terminate_build 1
%define _stripped_files_terminate_build 1

# https://xmake.io/posts/xmake-update-v2.6.1.html
%def_without luajit
%def_with check

Name: xmake
Version: 3.0.9
Release: alt1

Summary: A cross-platform build utility based on Lua
License: Apache-2.0
Group: Development/Tools
Url: https://xmake.io
VCS: https://github.com/xmake-io/xmake

Source: %name-%version.tar
Patch: xmake-3.0.8-alt-fix-sv-external-include.patch
Patch1: xmake-3.0.8-alt-fix-DESTDIR-configure.patch
Patch2: xmake-3.0.8-alt-add-relwithdebinfo-mode.patch

Requires: %name-data = %EVR

BuildRequires: pkgconfig(readline)
BuildRequires: pkgconfig(ncurses)
BuildRequires: pkgconfig(lua)
%{?_with_luajit:BuildRequires: pkgconfig(luajit)}
BuildRequires: pkgconfig(liblz4)
BuildRequires: pkgconfig(libsv)
BuildRequires: pkgconfig(tbox)

%if_with check
BuildRequires: /proc
BuildRequires: gcc-c++
%endif

%description
Xmake is a lightweight, cross-platform build utility based on Lua. It
uses a Lua script to maintain project builds, but is driven by a
dependency-free core program written in C. Compared with Makefiles or
CMake, the configuration syntax is much more concise and intuitive. As
such, it's friendly to novices while still maintaining the flexibility
required in a build system. With Xmake, you can focus on your project
instead of the build system.

Xmake can be used to directly build source code (like with Make or
Ninja), or it can generate project files like CMake or Meson. It also
has a built-in package management system to help users integrate C/C++
dependencies.

%package data
Summary: Data files for %name
Group: Development/Tools
BuildArch: noarch
AutoReqProv: no

%description data
This package contains data files for %name.

%prep
%setup
%autopatch -p1

# create stub for external build
mkdir -p core/src/tbox/tbox/src
touch core/src/tbox/tbox/src/xmake.sh

%build
%configure \
    --mode=relwithdebinfo \
    --external=yes \
%if_with luajit
    --runtime=luajit
%else
    --runtime=lua
%endif
%make_build

%install
%makeinstall_std
mkdir -p %buildroot%_man1dir
install -m 644 scripts/man/*.1 %buildroot%_man1dir
install -Dm 644 xmake/scripts/completions/register-completions.bash \
    %buildroot%_datadir/bash-completion/completions/%name
install -Dm 644 xmake/scripts/completions/register-completions.fish \
    %buildroot%_datadir/fish/vendor_completions.d/%name.fish
install -Dm 644 xmake/scripts/completions/register-completions.zsh \
    %buildroot%_datadir/zsh/site-functions/_%name

%check
export PATH="%buildroot%_bindir:$PATH"
export XMAKE_PROGRAM_DIR="%buildroot%_datadir/%name"

# remove tests that require network access
rm -r \
    tests/actions/install \
    tests/actions/package/localpkg \
    tests/apis/namespace/package \
    tests/projects

xmake l tests/run.lua

%files
%doc CHANGELOG.md CODE_OF_CONDUCT.md CONTRIBUTING.md NOTICE.md README.md
%_bindir/%name
%_bindir/xrepo
%_datadir/bash-completion/completions/%name
%_datadir/fish/vendor_completions.d/%name.fish
%_datadir/zsh/site-functions/_%name
%_man1dir/%name.1.xz
%_man1dir/xrepo.1.xz

%files data
%_datadir/%name

%changelog
* Mon Jun 22 2026 Dmitry Maksimenkov <dmaks@altlinux.org> 3.0.9-alt1
- Updated to version 3.0.9.

* Tue Apr 14 2026 Dmitry Maksimenkov <dmaks@altlinux.org> 3.0.8-alt1
- Initial build for ALT.

