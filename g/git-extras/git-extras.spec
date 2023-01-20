# SPDX-License-Identifier: GPL-2.0-only
%define _unpackaged_files_terminate_build 1

Name: git-extras
Version: 6.5.0
Release: alt1

Summary: Little git extras
License: MIT
Group: Development/Other
Url: https://github.com/tj/git-extras
Vcs: https://github.com/tj/git-extras.git
# Video: https://vimeo.com/45506445

BuildArch: noarch
Source: %name-%version.tar

# Avoid require gnustep-Backbone, xdg-utils
%add_findreq_skiplist %_bindir/git-browse*
# Avoid require rsync, php
%add_findreq_skiplist %_bindir/git-scp
%add_findreq_skiplist %_bindir/git-rscp
%add_findreq_skiplist %_datadir/bash-completion/completions/%name
# Avoid pastebinit
%add_findreq_skiplist %_bindir/git-paste

%description
GIT utilities -- repo summary, repl, changelog population, author commit
percentages and more.

%prep
%setup
sed -i 's|$(SYSCONFDIR)/bash-completion|/usr/share/bash-completion|' Makefile

%build

%install
%make_install PREFIX=%_prefix SYSCONFDIR=%buildroot%_sysconfdir DESTDIR=%buildroot install
install -D etc/git-extras-completion.zsh \
	%buildroot%_datadir/zsh/Completion/Unix/_git-extras

%check
./check_integrity.sh $(find bin | cut -b 5- | xargs)

%files
%doc LICENSE AUTHORS Readme.md Commands.md History.md
%_bindir/git-*
%_man1dir/*.1*
%_datadir/bash-completion/completions/%name
%_datadir/zsh/Completion/Unix/_git-extras

%changelog
* Fri Jan 20 2023 Andrew A. Vasilyev <andy@altlinux.org> 6.5.0-alt1
- 6.5.0

* Mon Oct 04 2021 Vitaly Chikunov <vt@altlinux.org> 6.3.0-alt1
- Update to 6.3.0 (2021-10-02).

* Fri Mar 26 2021 Vitaly Chikunov <vt@altlinux.org> 6.2.0-alt1
- Update to 6.2.0 (2021-03-26).

* Sun Sep 27 2020 Vitaly Chikunov <vt@altlinux.org> 6.1.0-alt1
- Update to 6.1.0 (2020-09-26).

* Sun Jul 05 2020 Vitaly Chikunov <vt@altlinux.org> 6.0.0-alt2
- Fix git brv.

* Sun Jul 05 2020 Vitaly Chikunov <vt@altlinux.org> 6.0.0-alt1
- Initial import of v6.0.0.
