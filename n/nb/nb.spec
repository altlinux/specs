%define _unpackaged_files_terminate_build 1

Name:      nb
Version:   7.20.1
Release:   alt1.gitb1f81f9b

Summary:   Command line note-taking, bookmarking, and archiving with encryption, search, and Git syncing
License:   AGPL-3.0
Group:     Office
Url:       https://github.com/xwmx/nb

Source:    %name-%version.tar

BuildArch: noarch

# Too many dependencies with overlapping functionality
%add_findreq_skiplist %_bindir/%name
%add_findreq_skiplist %_bindir/bookmark
%add_findreq_skiplist %_bindir/notes

Requires: bash coreutils file gawk grep sed
Requires: curl wget netcat socat
Requires: less w3m highlight
Requires: git-core findutils procps
Requires: gnupg openssl tar
Requires: iconv pandoc ripgrep
Requires: termutils xdg-utils

%description
nb is a command line note-taking, bookmarking, archiving, and knowledge
base application with:

* Plain text data storage
* Encryption
* Filtering and search
* Pinning and #tagging
* Git-backed versioning and syncing
* Pandoc-backed conversion
* Global and local notebooks
* Customizable color themes
* Wiki-style linking
* Plugins
* And more in a single portable script

%prep
%setup -q

%install
mkdir -p %buildroot%_bindir
cp %name %buildroot%_bindir/%name
cp bin/bookmark %buildroot%_bindir/bookmark
cp bin/notes %buildroot%_bindir/notes

mkdir -p %buildroot%_datadir/bash-completion/completions
mkdir -p %buildroot%_datadir/zsh/site-functions
mkdir -p %buildroot%_datadir/fish/vendor_completions.d
cp etc/%name-completion.bash %buildroot%_datadir/bash-completion/completions/%name
cp etc/%name-completion.zsh %buildroot%_datadir/zsh/site-functions/_%name
cp etc/%name-completion.fish %buildroot%_datadir/fish/vendor_completions.d/%name.fish

%files
%doc README.md
%_bindir/%name
%_bindir/bookmark
%_bindir/notes
%_datadir/bash-completion/completions/%name
%_datadir/zsh/site-functions/_%name
%_datadir/fish/vendor_completions.d/%name.fish

%changelog
* Fri Sep 05 2025 Andrey Limachko <liannnix@altlinux.org> 7.20.1-alt1.gitb1f81f9b
- Initial build for Sisyphus.

