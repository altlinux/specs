# Unpackaged files in buildroot should terminate build
%define _unpackaged_files_terminate_build 1

Name: git-subrepo
Version: 0.4.9
Release: alt2

Group: Development/Other
Summary: git submodule alternative
License: MIT
Url: https://github.com/ingydotnet/git-subrepo

Source: %name-%version.tar
Patch:  git-subrepo-debian-fixed-bash-completion-integration-with-git.patch

BuildArch: noarch

BuildRequires: git-core

%description
git-subrepo command "clones" an external git repo into a subdirectory
of your repo. Later on, upstream changes can be pulled in, and local
changes can be pushed back. Simple.

%prep
%setup
%autopatch -p1

%install
%_make_bin install DESTDIR=%buildroot PREFIX=%_prefix

# completions
install -Dm0644 share/completion.bash \
    %buildroot%_datadir/bash-completion/completions/git-subrepo
install -Dm0644 share/zsh-completion/_git-subrepo \
    %buildroot%_datadir/zsh/site-functions/_git-subrepo

%files
%doc ReadMe.pod License
%_bindir/%name
%_datadir/%name
%_man1dir/%name.*
%_datadir/bash-completion/completions/git-subrepo
%_datadir/zsh/site-functions/_git-subrepo

%changelog
* Tue Jun 17 2025 Ivan A. Melnikov <iv@altlinux.org> 0.4.9-alt2
- fix and package bash and zsh completion

* Thu May 22 2025 Ivan A. Melnikov <iv@altlinux.org> 0.4.9-alt1
- 0.4.9

* Thu May 04 2023 Alexey Sheplyakov <asheplyakov@altlinux.org> 0.4.6-alt1
- Initial build for ALT Sisyphus.
