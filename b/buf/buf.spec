%def_disable snapshot

%define _name buf
%define binary_name %_name
%define ver_major 1.71
%define import_path github.com/bufbuild/buf

%def_disable bootstrap

Name: %binary_name
Version: %ver_major.0
Release: alt1

Summary: The best way of working with Protocol Buffers.
License: Apache-2.0
Group: Development/Other
Url: https://github.com/bufbuild/buf

Vcs: https://github.com/bufbuild/buf.git

%if_disabled snapshot
Source: %url/archive/v%version/%_name-%version.tar.gz
%else
Source: %_name-%version.tar
%endif
%{?_disable_bootstrap:Source1: %_name-%version-vendor.tar}

ExcludeArch: %ix86

BuildRequires(pre): rpm-build-golang
BuildRequires: golang

%description
The buf CLI is the best tool for working with Protocol Buffers. It provides:

* A linter that enforces good API design choices and structure.
* A breaking change detector that enforces compatibility at the source code or wire level.
* A generator that invokes your plugins based on configuration files.
* A formatter that formats your Protobuf files in accordance with industry standards.
* Integration with the Buf Schema Registry, including full dependency management.


%prep
%setup -n %_name-%version %{?_disable_bootstrap: -a1}
%{?_enable_bootstrap:go mod vendor
tar -cf %_sourcedir/%_name-%version-vendor.tar vendor/}

%build
export BUILDDIR="$PWD/.build"
export IMPORT_PATH="%import_path"
export GOPATH="$BUILDDIR:%go_path"

export GOFLAGS="${GOFLAGS-} \
-buildvcs=false \
-buildmode=pie \
-mod=readonly \
-modcacherw"

#-ldflags '-compressdwarf=false -linkmode external -extldflags '${LDFLAGS}''"

export VERSION=%version

%golang_prepare

cd .build/src/%import_path
%golang_build cmd/%binary_name

# generate completions
for shell in bash fish zsh; do
    $BUILDDIR/bin/%binary_name completion "$shell" > "$BUILDDIR/completion.$shell"
done
# generate manpages
mkdir -p $BUILDDIR/manpages
$BUILDDIR/bin/%binary_name manpages $BUILDDIR/manpages

%install
export BUILDDIR="$PWD/.build"
export IGNORE_SOURCES=1
%golang_install

# completions
install -vDm644 $BUILDDIR/completion.bash %buildroot%_datadir/bash-completion/completions/%binary_name
install -vDm644 $BUILDDIR/completion.fish %buildroot%_datadir/fish/vendor_completions.d/%binary_name.fish
install -vDm644 $BUILDDIR/completion.zsh %buildroot%_datadir/zsh/site-functions/_%binary_name

# manpages
install -vDm644 $BUILDDIR/manpages/* -t %buildroot/%_man1dir

%files
%_bindir/%binary_name
%_datadir/bash-completion/completions/%binary_name
%_datadir/fish/vendor_completions.d/%binary_name.fish
%_datadir/zsh/site-functions/_%binary_name
%_man1dir/%{binary_name}*.1*
%doc *.md

%changelog
* Wed Jun 17 2026 Yuri N. Sedunov <aris@altlinux.org> 1.71.0-alt1
- 1.71.0

* Tue May 26 2026 Yuri N. Sedunov <aris@altlinux.org> 1.70.0-alt1
- 1.70.0

* Sat May 02 2026 Yuri N. Sedunov <aris@altlinux.org> 1.69.0-alt1
- 1.69.0

* Sat Apr 18 2026 Yuri N. Sedunov <aris@altlinux.org> 1.68.2-alt1
- 1.68.2

* Wed Apr 15 2026 Yuri N. Sedunov <aris@altlinux.org> 1.68.1-alt1
- 1.68.1

* Fri Apr 03 2026 Yuri N. Sedunov <aris@altlinux.org> 1.67.0-alt1
- 1.67.0

* Tue Mar 10 2026 Yuri N. Sedunov <aris@altlinux.org> 1.66.1-alt1
- 1.66.1

* Tue Feb 24 2026 Yuri N. Sedunov <aris@altlinux.org> 1.66.0-alt1
- 1.66.0

* Wed Feb 04 2026 Yuri N. Sedunov <aris@altlinux.org> 1.65.0-alt1
- 1.65.0

* Tue Jan 20 2026 Yuri N. Sedunov <aris@altlinux.org> 1.64.0-alt1
- 1.64.0

* Thu Dec 04 2025 Yuri N. Sedunov <aris@altlinux.org> 1.61.0-alt1
- 1.61.0

* Mon Nov 24 2025 Yuri N. Sedunov <aris@altlinux.org> 1.60.0-alt1
- 1.60.0

* Mon Aug 04 2025 Yuri N. Sedunov <aris@altlinux.org> 1.56.0-alt1
- 1.56.0

* Fri Jun 13 2025 Yuri N. Sedunov <aris@altlinux.org> 1.54.0-alt1
- first build for Sisyphus



