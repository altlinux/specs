Name:    nfpm
Version: 2.46.3
Release: alt1

Summary: Simple deb, rpm, apk and arch linux packager written in Go
License: MIT
Group:   Other
Url:     https://github.com/goreleaser/nfpm

Source: %name-%version.tar
Source1: %name-development-%version.tar

BuildRequires(pre): rpm-macros-golang
BuildRequires: rpm-build-golang

%description
nFPM is a simple and 0-dependencies deb, rpm, apk and arch linux packager
written in Go

%package -n %name-bash-completion
Summary: Bash Completion for %name
Group:   Shells
Requires: %name = %EVR
Requires: bash-completion
# Supplements: (%name and bash-completion)
BuildArch: noarch

%description -n %name-bash-completion
Bash command line completion support for %name.

%package -n %name-fish-completion
Summary: Fish Completion for %name
Group:   Shells
Requires: %name = %EVR
# Supplements: (%name and fish)
BuildArch: noarch

%description -n %name-fish-completion
Fish command line completion support for %name.

%package -n %name-zsh-completion
Summary: Zsh Completion for %{name}
Group:   Shells
Requires: %name = %EVR
# Supplements: (%name and zsh)
BuildArch: noarch

%description -n %name-zsh-completion
zsh command line completion support for %name.

%prep
%setup -a1

%build
DATE_FMT="+%%Y-%%m-%%dT%%H:%%M:%%SZ"
BUILD_DATE=$(date -u -d "@${SOURCE_DATE_EPOCH}" "${DATE_FMT}" 2>/dev/null || date -u -r "${SOURCE_DATE_EPOCH}" "${DATE_FMT}" 2>/dev/null || date -u "${DATE_FMT}")
go build \
	-mod=vendor \
	-buildmode=pie \
	-ldflags=" \
	-X main.date=${BUILD_DATE} \
	-X main.version=%version \
	-X main.builtBy=OBS \
	-X main.treeState=false" \
	-o bin/%name ./cmd/%name

%install
# Install the binary.
install -D -m 0755 bin/%name %buildroot/%_bindir/%name

# create the bash completion file
mkdir -p %buildroot%_datadir/bash-completion/completions/
%buildroot/%_bindir/%name completion bash > %buildroot%_datadir/bash-completion/completions/%name

# create the fish completion file
mkdir -p %buildroot%_datadir/fish/vendor_completions.d/
%buildroot/%_bindir/%name completion fish > %buildroot%_datadir/fish/vendor_completions.d/%name.fish

# create the zsh completion file
mkdir -p %buildroot%_datadir/zsh_completion.d/
%buildroot/%_bindir/%name completion zsh > %buildroot%_datadir/zsh_completion.d/_%name

%files
%doc LICENSE.md README.md
%_bindir/%name

%files -n %name-bash-completion
%dir %_datadir/bash-completion/completions/
%_datadir/bash-completion/completions/%name

%files -n %name-fish-completion
%dir %_datadir/fish
%dir %_datadir/fish/vendor_completions.d
%_datadir/fish/vendor_completions.d/%name.fish

%files -n %name-zsh-completion
%dir %_datadir/zsh_completion.d/
%_datadir/zsh_completion.d/_%name

%changelog
* Fri Jun 12 2026 Sergey Palcheh <minergenon@altlinux.org> 2.46.3-alt1
- new version 2.46.3

* Fri Feb 21 2025 Sergey Palcheh <minergenon@altlinux.org> 2.41.2-alt1
- Initial build for Sisyphus
