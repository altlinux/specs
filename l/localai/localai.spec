%global import_path github.com/mudler/LocalAI

Name: localai
Version: 4.10.0
Release: alt1

Summary: Open-source AI engine
Group: Sciences/Computer science
License: MIT
URL: https://localai.io/
VCS: https://github.com/mudler/LocalAI

ExclusiveArch: %go_arches
ExcludeArch: %ix86

Source0: %name-%version.tar
Source1: localai.desktop
Source2: launcher.png

Patch0: %name-%version.patch
Patch1: localai-4.6.2-alt1-prepare-for-alt.patch

BuildRequires(pre): rpm-macros-golang
BuildRequires: rpm-build-golang
BuildRequires: libXrandr-devel
BuildRequires: libXcursor-devel
BuildRequires: libXinerama-devel
BuildRequires: libXxf86vm-devel
BuildRequires: libXi-devel
BuildRequires: libglvnd-devel

%description
The free, OpenAI, Anthropic alternative. Your All-in-One Complete AI
Stack - Run powerful language models, autonomous agents, and document
intelligence locally on your hardware.

%prep
%setup
%autopatch -p1

%build
export BUILDDIR="$PWD/.build"
export IMPORT_PATH="%import_path"
export GOPATH="$BUILDDIR:%go_path"
%golang_prepare
export LDFLAGS="-X github.com/mudler/LocalAI/internal.Version=%version-%release \
    -X github.com/mudler/LocalAI/internal.BinaryPathRoot=%_bindir"
%golang_build cmd/local-ai cmd/launcher
mv "$BUILDDIR/bin/launcher" "$BUILDDIR/bin/local-ai-launcher"

%install
export BUILDDIR="$PWD/.build"
export IGNORE_SOURCES=1
%golang_install
%__install -D -m 644 %SOURCE1 %buildroot/%_datadir/applications/localai.desktop
%__install -D -m 644 %SOURCE2  %buildroot/%_datadir/pixmaps/launcher.png

%check
# Tests requiring network access are skipped
%gotest $(go list ./pkg/... | grep -Ev '/pkg/(oci|downloader|huggingface-api|utils|system)($|/)') \
	./core/schema/... \
	./core/cli/... \
	./core/backend/... \
	./core/templates/... \
	./core/trace/... \
%ifarch x86_64
	./pkg/system/... \
%endif
	%nil

%files
%_bindir/local-ai
%_bindir/local-ai-launcher
%_datadir/applications/localai.desktop
%_datadir/pixmaps/launcher.png


%changelog
* Thu Oct 08 2026 Evgeniy Gorbanyov <esgor@altlinux.org> 4.10.0-alt1
- Updated to 4.10.0.
- Switched the build to golang RPM macros; dropped the makefile patch and npm.
- Added offline tests.

* Tue Aug 25 2026 Evgeniy Gorbanyov <esgor@altlinux.org> 4.9.0-alt1
- Updated from 4.8.2 to 4.9.0.

* Tue Aug 11 2026 Evgeniy Gorbanyov <esgor@altlinux.org> 4.8.2-alt1
- Updated from 4.6.2 to 4.8.2.

* Tue Jul 14 2026 Evgeniy Gorbanyov <esgor@altlinux.org> 4.6.2-alt1
- Updated from 4.4.3 to 4.6.2.

* Tue Jun 16 2026 Evgeniy Gorbanyov <esgor@altlinux.org> 4.4.3-alt1
- Updated from 4.3.6 to 4.4.3.

* Tue Jun 03 2026 Evgeniy Gorbanyov <esgor@altlinux.org> 4.3.6-alt1
- Initial build for Sisyphus.
