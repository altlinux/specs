%define _unpackaged_files_terminate_build 1
%def_with check

%define import_path github.com/danielmiessler/fabric

Name: fabric
Version: 1.4.448
Release: alt1

Summary: Fabric is an open-source framework for augmenting humans using AI

License: MIT
Group: System/Configuration/Other
VCS: https://github.com/danielmiessler/Fabric
Url: https://github.com/danielmiessler/Fabric

Source0: %name-%version.tar
Source1: %name-%version-vendor.tar

Patch0: %name-%version-alt.patch

BuildRequires(pre): rpm-build-golang

%if_with check
BuildRequires: notify-send
%endif

%description
Fabric is an open-source framework for augmenting humans using AI. It
provides  a modular  system  for solving  specific  problems using  a
crowdsourced set of AI prompts that can be used anywhere.

%prep
%setup -a1
%patch0 -p1

# Remove large images to reduce package size
rm -f docs/images/fabric-logo-gif.gif
rm -f docs/images/svelte-preview.png

export BUILDDIR="$PWD/.build"
export IMPORT_PATH="%import_path"
export GOPATH="$BUILDDIR:%go_path"
%golang_prepare

%build
export BUILDDIR="$PWD/.build"
export IMPORT_PATH="%import_path"
export GOPATH="$BUILDDIR:%go_path"

%golang_build cmd/fabric

%install
export BUILDDIR="$PWD/.build"
export GOPATH="$BUILDDIR:%go_path"
export IGNORE_SOURCES=1

%golang_install

mkdir -pv %buildroot/%_datadir/fabric
cp -a ./data/patterns %buildroot/%_datadir/fabric/
cp -a ./data/strategies %buildroot/%_datadir/fabric/

install -vDm 644 completions/fabric.bash \
        %buildroot/%_datadir/bash-completion/completions/fabric

install -vDm 644 completions/_fabric \
        %buildroot/%_datadir/zsh/site-functions/_fabric

install -vDm 644 completions/fabric.fish \
        %buildroot/%_datadir/fish/vendor_completions.d/fabric.fish

%check
%gotest -v ./...

%files
%doc LICENSE README.md CHANGELOG.md docs
%_bindir/fabric
%_datadir/fabric
%_datadir/bash-completion/completions/fabric
%_datadir/zsh/site-functions/_fabric
%_datadir/fish/vendor_completions.d/fabric.fish

%changelog
* Wed Apr 22 2026 Egor Ignatov <egori@altlinux.org> 1.4.448-alt1
- New version 1.4.448.

* Mon Mar 30 2026 Egor Ignatov <egori@altlinux.org> 1.4.442-alt1
- New version 1.4.442.

* Tue Feb 24 2026 Egor Ignatov <egori@altlinux.org> 1.4.420-alt1
- New version 1.4.420.

* Tue Feb 17 2026 Egor Ignatov <egori@altlinux.org> 1.4.409-alt1
- New version 1.4.409.

* Tue Feb 10 2026 Egor Ignatov <egori@altlinux.org> 1.4.401-alt1
- New version 1.4.401.

* Wed Feb 04 2026 Egor Ignatov <egori@altlinux.org> 1.4.399-alt1
- New version 1.4.399.

* Wed Dec 24 2025 Egor Ignatov <egori@altlinux.org> 1.4.360-alt1
- New version 1.4.360.

* Tue Dec 23 2025 Egor Ignatov <egori@altlinux.org> 1.4.358-alt1
- New version 1.4.358.

* Wed Dec 10 2025 Egor Ignatov <egori@altlinux.org> 1.4.340-alt1
- New version 1.4.340.

* Sun Dec 07 2025 Egor Ignatov <egori@altlinux.org> 1.4.338-alt1
- New version 1.4.338.

* Fri Nov 28 2025 Egor Ignatov <egori@altlinux.org> 1.4.335-alt1
- First build for ALT.
