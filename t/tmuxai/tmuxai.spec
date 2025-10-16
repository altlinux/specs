%define _unpackaged_files_terminate_build 1

%global import_path github.com/alvinunreal/tmuxai
Name: tmuxai
Version: 1.1.3
Release: alt1

Summary: AI-Powered, Non-Intrusive Terminal Assistant
License: Apache-2.0
Group: Terminals
Url: https://github.com/alvinunreal/tmuxai

Source: %name-%version.tar
Source1: %name-development-%version.tar

Patch: %name-%version-%release.patch

BuildRequires(pre): rpm-build-golang
BuildRequires: golang

Requires: tmux

%description
TmuxAI is an intelligent terminal assistant that lives inside your tmux
sessions. Unlike other CLI AI tools, TmuxAI observes and understands the
content of your tmux panes, providing assistance without requiring you
to change your workflow or interrupt your terminal sessions.

Think of TmuxAI as a pair programmer that sits beside you, watching your
terminal environment exactly as you see it. It can understand what
you're working on across multiple panes, help solve problems and execute
commands on your behalf in a dedicated execution pane.

%prep
%setup -a1
%patch -p1

%build
export GOROOT="%_libexecdir/golang"
%gobuild -mod=vendor

%install
install -Dpm755 %name %buildroot%_bindir/%name

%post
echo "NOTE: TmuxAI looks for its configuration file at ~/.config/tmuxai/config.yaml"
echo "      For a sample configuration file, see /usr/share/doc/tmuxai-%version/config.example.yaml"

%files
%doc LICENSE README.md config.example.yaml
%_bindir/*

%changelog
* Thu Oct 16 2025 Nikolay Strelkov <snk@altlinux.org> 1.1.3-alt1
- New version 1.1.3.

* Tue Sep 23 2025 Nikolay Strelkov <snk@altlinux.org> 1.1.1-alt1
- Initial build for Sisyphus
