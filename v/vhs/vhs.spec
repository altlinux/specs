%define _unpackaged_files_terminate_build 1
%define _stripped_files_terminate_build 1
# eu-elflint rejects Go PIE metadata (.note.go.buildid and .gnu.version*).
# Keep the other ELF checks strict.
%set_verify_elf_method strict,lint=relaxed

Name: vhs
Version: 0.12.1
Release: alt1

%define commit 24fa225

Summary: Tool for recording terminal sessions as code
Summary(ru_RU.UTF-8): Инструмент для записи сеансов терминала в виде кода
License: MIT
Group: Video
Url: https://github.com/charmbracelet/vhs
Vcs: https://github.com/charmbracelet/vhs.git
# Chromium is available in Sisyphus only on these architectures.
ExclusiveArch: x86_64 aarch64

Source: %name-%version.tar
Source1: %name-%version-vendor.tar

Requires: bash
Requires: chromium
Requires: ffmpeg
Requires: fonts-otf-jetbrains-mono
Requires: ttyd >= 1.7.2

BuildRequires(pre): rpm-build-golang
# Preserve the minimum Go version from go.mod when regenerating BuildRequires.
BuildPreReq: golang >= 1.26.7

%description
VHS is a command-line tool for writing terminal recordings as code. It reads
.tape scripts and renders terminal sessions to GIF, MP4, WebM, screenshots, or
textual test output.

%description -l ru_RU.UTF-8
VHS — инструмент командной строки для описания записей терминала в виде кода.
Он читает сценарии .tape и сохраняет сеансы терминала в GIF, MP4, WebM, снимки
экрана или текстовые результаты тестов.

%prep
%setup -a1

%build
export CGO_ENABLED=0
export GOTOOLCHAIN=local
export GOPROXY=off

export LDFLAGS="-X main.Version=%version -X main.CommitSHA=%commit"
go build -v -buildmode=pie -mod=vendor -ldflags "$LDFLAGS" -o %name .
./%name manual > %name.1
./%name completion bash > %name.bash
./%name completion zsh > %name.zsh
./%name completion fish > %name.fish

%install
install -pDm0755 %name %buildroot%_bindir/%name
install -pDm0644 %name.1 %buildroot%_mandir/man1/%name.1
install -pDm0644 %name.bash %buildroot%_datadir/bash-completion/completions/%name
install -pDm0644 %name.zsh %buildroot%_datadir/zsh/site-functions/_%name
install -pDm0644 %name.fish %buildroot%_datadir/fish/vendor_completions.d/%name.fish

%check
export CGO_ENABLED=0
export GOTOOLCHAIN=local
export GOPROXY=off

%gotest -mod=vendor ./...

%files
%_bindir/%name
%_mandir/man1/%name.1*
%_datadir/bash-completion/completions/%name
%_datadir/zsh/site-functions/_%name
%_datadir/fish/vendor_completions.d/%name.fish
%doc LICENSE README.md THEMES.md

%changelog
* Mon Nov 02 2026 Georgij Tsarin <crystarm@altlinux.org> 0.12.1-alt1
- Initial build for Sisyphus.
