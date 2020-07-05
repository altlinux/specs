# SPDX-License-Identifier: GPL-2.0-only
%define _unpackaged_files_terminate_build 1

Name: git-extras
Version: 6.0.0
Release: alt2

Summary: Little git extras
License: MIT
Group: Development/Other
Url: https://github.com/tj/git-extras
Vcs: https://github.com/tj/git-extras.git
# Video: https://vimeo.com/45506445

BuildArch: noarch
Source: %name-%version.tar

# Avoid require gnustep-Backbone, xdg-utils
%add_findreq_skiplist %_bindir/git-browse
# Avoid require rsync, php
%add_findreq_skiplist %_bindir/git-scp
%add_findreq_skiplist %_bindir/git-rscp
%add_findreq_skiplist %_sysconfdir/bash_completion.d/git-extras
# Avoid pastebinit
%add_findreq_skiplist %_bindir/git-paste

%description
GIT utilities -- repo summary, repl, changelog population, author commit
percentages and more.

%prep
%setup

%build

%install
%make_install PREFIX=%buildroot%_prefix SYSCONFDIR=%buildroot%_sysconfdir install
install -D etc/git-extras-completion.zsh \
	%buildroot%_datadir/zsh/Completion/Unix/_git-extras

%check
./check_integrity.sh $(find bin | cut -b 5- | xargs)

%files
%doc LICENSE AUTHORS Readme.md Commands.md History.md
%_bindir/git-*
%_man1dir/*.1*
%_sysconfdir/bash_completion.d/git-extras
%_datadir/zsh/Completion/Unix/_git-extras

%changelog
* Sun Jul 05 2020 Vitaly Chikunov <vt@altlinux.org> 6.0.0-alt2
- Fix git brv.

* Sun Jul 05 2020 Vitaly Chikunov <vt@altlinux.org> 6.0.0-alt1
- Initial import of v6.0.0.
