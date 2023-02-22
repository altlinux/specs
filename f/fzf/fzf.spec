%global __find_debuginfo_files %nil
%global _unpackaged_files_terminate_build 1

%set_verify_elf_method unresolved=no
%add_debuginfo_skiplist %_bindir
%brp_strip_none %_bindir/*

%define fzf_revision 2023012

Name:		fzf
Version:	0.38.0
Release:	alt1
Summary:	A general-purpose command-line fuzzy finder.

Group:		Development/Tools
License:	MIT
URL:		https://github.com/junegunn/fzf

Packager:	Vladimir Didenko <cow@altlinux.org>

Source0: %name-%version.tar

ExclusiveArch: %go_arches

BuildRequires(pre): rpm-build-golang
BuildRequires(pre): rpm-build-vim
BuildRequires: golang

Provides: bash-completion-%name = %version-%release
Obsoletes: bash-completion-%name < 0.28.0

Provides: zsh-completion-%name = %version-%release
Obsoletes: zsh-completion-%name < 0.28.0

%description
fzf is an interactive Unix filter for command-line that can be used with any
list; files, command history, processes, hostnames, bookmarks, git commits, etc.

%package tmux
Summary: script for launching fzf in a tmux pane
Group: Development/Tools
BuildArch: noarch

%description tmux
Script for launching fzf in a tmux pane

%package -n vim-plugin-%name
Summary: Vim plugin for %name
Group: Editors
BuildArch: noarch
Requires: %_bindir/vim
Requires: %name = %EVR

%description -n vim-plugin-%name
Vim plugin for %name

%prep
%setup -q

%build
export FZF_VERSION=%version
export FZF_REVISION=%fzf_revision
go build -a -ldflags "-s -w -X main.version=${FZF_VERSION} -X main.revision=${FZF_REVISION}" -tags "" -o bin/%name

%install
mkdir -p %buildroot%_bindir

#install main binary
install -Dpm0755 bin/%name %{buildroot}%{_bindir}/

#install tmux support
install -Dpm0755 bin/%name-tmux %{buildroot}%{_bindir}/

#install man pages
install -d -p %{buildroot}%{_mandir}/man1
install -Dpm0644 man/man1/*.1 %{buildroot}%{_mandir}/man1/

install -d %{buildroot}%{_datadir}/%name/shell
install -Dpm0644 shell/key-bindings.* %{buildroot}%{_datadir}/%name/shell/

# Install shell completion
install -d %{buildroot}%{_datadir}/bash-completion/completions
install -Dpm0644 shell/completion.bash %{buildroot}%{_datadir}/bash-completion/completions/fzf
install -d %{buildroot}%{_datadir}/zsh/site-functions
install -Dpm0644 shell/completion.zsh %{buildroot}%{_datadir}/zsh/site-functions/fzf

# Install vim plugin
install -d %buildroot%vim_runtime_dir/plugin
install -Dpm0644 plugin/fzf.vim %buildroot%vim_runtime_dir/plugin/

%files
%_bindir/%name
%_mandir/man1/%name.1*
%dir %_datadir/%name
%_datadir/%name/shell
%_datadir/bash-completion/completions/*
%_datadir/zsh/site-functions/*

%files tmux
%_bindir/%name-tmux
%{_mandir}/man1/%name-tmux.1*

%files -n vim-plugin-%name
%vim_runtime_dir/plugin/*

%changelog
* Wed Feb 22 2023 Vladimir Didenko <cow@altlinux.org> 0.38.0-alt1
- New version

* Tue Jan 31 2023 Vladimir Didenko <cow@altlinux.org> 0.37.0-alt1
- New version

* Fri Jan 20 2023 Vladimir Didenko <cow@altlinux.org> 0.36.0-alt1
- New version

* Thu Dec 1 2022 Vladimir Didenko <cow@altlinux.org> 0.35.1-alt1
- New version

* Tue Nov 15 2022 Vladimir Didenko <cow@altlinux.org> 0.35.0-alt1
- New version

* Wed Oct 5 2022 Vladimir Didenko <cow@altlinux.org> 0.34.0-alt1
- New version

* Mon Sep 5 2022 Vladimir Didenko <cow@altlinux.org> 0.33.0-alt2
- Fix build on armh platform

* Mon Sep 5 2022 Vladimir Didenko <cow@altlinux.org> 0.33.0-alt1
- New version

* Tue Aug 9 2022 Vladimir Didenko <cow@altlinux.org> 0.32.1-alt1
- New version

* Tue Jul 26 2022 Vladimir Didenko <cow@altlinux.org> 0.31.0-alt1
- New version

* Wed Apr 6 2022 Vladimir Didenko <cow@altlinux.org> 0.30.0-alt1
- New version

* Tue Jan 11 2022 Vladimir Didenko <cow@altlinux.org> 0.29.0-alt1
- New version

* Thu Dec 2 2021 Vladimir Didenko <cow@altlinux.org> 0.28.0-alt1
- New version
- Modify spec to comply with new shell completions policy

* Wed Oct 27 2021 Vladimir Didenko <cow@altlinux.org> 0.27.3-alt1
- New version

* Tue Jun 8 2021 Vladimir Didenko <cow@altlinux.org> 0.27.2-alt1
- New version

* Wed May 26 2021 Vladimir Didenko <cow@altlinux.org> 0.27.1-alt1
- New version

* Mon Apr 12 2021 Vladimir Didenko <cow@altlinux.org> 0.27.0-alt1
- New version

* Wed Mar 17 2021 Vladimir Didenko <cow@altlinux.org> 0.26.0-alt1
- New version

* Sat Feb 20 2021 Vladimir Didenko <cow@altlinux.org> 0.25.1-alt2
- Fix build with golang 1.16

* Mon Feb 8 2021 Vladimir Didenko <cow@altlinux.org> 0.25.1-alt1
- New version

* Wed Jan 13 2021 Vladimir Didenko <cow@altlinux.org> 0.25.0-alt1
- New version

* Mon Dec 21 2020 Vladimir Didenko <cow@altlinux.org> 0.24.4-alt1
- New version

* Tue Nov 19 2020 Vladimir Didenko <cow@altlinux.org> 0.24.3-alt1
- New version

* Tue Nov 10 2020 Vladimir Didenko <cow@altlinux.org> 0.24.2-alt1
- New version

* Mon Oct 19 2020 Vladimir Didenko <cow@altlinux.org> 0.23.1-alt1
- New version

* Fri Aug 14 2020 Vladimir Didenko <cow@altlinux.org> 0.22.0-alt1
- New version

* Fri Apr 10 2020 Vladimir Didenko <cow@altlinux.org> 0.21.1-alt1
- New version

* Thu Mar 19 2020 Vladimir Didenko <cow@altlinux.org> 0.21.0-alt1
- New version

* Wed Jan 8 2020 Vladimir Didenko <cow@altlinux.org> 0.20.0-alt1
- New version

* Thu Nov 28 2019 Vladimir Didenko <cow@altlinux.org> 0.19.0-alt1
- New version

* Fri Sep 6 2019 Vladimir Didenko <cow@altlinux.org> 0.18.0-alt2
- Fix build with golang 1.13

* Mon Apr 8 2019 Vladimir Didenko <cow@altlinux.org> 0.18.0-alt1
- New version

* Fri Mar 1 2019 Vladimir Didenko <cow@altlinux.org> 0.17.5-alt2
- vendor dependencies to fix build (closes: #36205)

* Wed Oct 24 2018 Vladimir Didenko <cow@altlinux.org> 0.17.5-alt1
- New version

* Fri Jul 27 2018 Vladimir Didenko <cow@altlinux.org> 0.17.4-alt1
- Initial build for Sisyphus
