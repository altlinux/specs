Name: localai
Version: 4.3.6
Release: alt1

Summary: LocalAI is the open-source AI engine. Run any model - LLMs, vision, voice, image, video - on any hardware.
Group: Sciences/Computer science
License: MIT
URL: https://localai.io/
VCS: https://github.com/mudler/LocalAI

ExcludeArch: %ix86

Source0: %name-%version.tar
Source1: localai.desktop
Source2: launcher.png

Patch0: %name-%version.patch
Patch1: localai-4.3.6-alt1-prepare-for-alt.patch
Patch2: localai-4.3.6-alt1-fix-makefile-to-use-vendors.patch

BuildRequires(pre): rpm-build-golang
BuildRequires: golang 
BuildRequires: libXrandr-devel libXcursor-devel libXinerama-devel
BuildRequires: libXi-devel libXxf86vm-devel libglvnd-devel npm 

%description
The free, OpenAI, Anthropic alternative. Your All-in-One Complete AI
Stack - Run powerful language models, autonomous agents, and document
intelligence locally on your hardware.

%prep
%setup
%autopatch -p1

%build
make build-all VERSION=%version-%release \
    GOROOT=%_libexecdir/golang \
    GOPATH=%_builddir/%buildsubdir/vendor \
    BINARYPATH=%_bindir

%install
%__install -D -m 755 local-ai %buildroot%_bindir/local-ai
%__install -D -m 755 local-ai-launcher %buildroot%_bindir/local-ai-launcher
%__install -D -m 644 %SOURCE1 %buildroot/%_datadir/applications/localai.desktop
%__install -D -m 644 %SOURCE2  %buildroot/%_datadir/pixmaps/launcher.png

%check
# Network access is required to run tests.

%files
%_bindir/local-ai
%_bindir/local-ai-launcher
%_datadir/applications/localai.desktop
%_datadir/pixmaps/launcher.png


%changelog
* Tue Jun 03 2026 Evgeniy Gorbanyov <esgor@altlinux.org> 4.3.6-alt1
- Initial build for Sisyphus.
