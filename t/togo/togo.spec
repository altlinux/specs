Name: togo
Version: 1.0.1
Release: alt1
License: MIT

Summary: A terminal-based Todo Manager

Group: Office

Url: https://github.com/prime-run/togo
Vcs: https://github.com/prime-run/togo.git

Source: %name-%version.tar
Source1: %name-development-%version.tar

BuildRequires(pre): rpm-macros-golang
BuildRequires: rpm-build-golang

%description
A command-line todo application built in Go for developers
who need to capture ideas without breaking their workflow.

%prep
%setup -a1

%build
%gobuild -mod=vendor

%install
install -D -m 0755 ./%name %buildroot%_bindir/%name

%buildroot%_bindir/%name completion bash | \
    install -Dm644 /dev/stdin %buildroot%_datadir/bash-completion/completions/%name

%buildroot%_bindir/%name completion zsh | \
    install -Dm644 /dev/stdin  %buildroot%_datadir/zsh/site-functions/_%name

%buildroot%_bindir/%name completion fish | \
    install -Dm644 /dev/stdin %buildroot%_datadir/fish/vendor_completions.d/%name.fish

%files
%_bindir/%name
%_datadir/bash-completion/completions/%name
%_datadir/zsh/site-functions/_%name
%_datadir/fish/vendor_completions.d/%name.fish

%changelog
* Sun Apr 13 2025 Kirill Unitsaev <fiersik@altlinux.org> 1.0.1-alt1
- Initial build
