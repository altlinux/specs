# SPDX-License-Identifier: GPL-2.0-only
%define _unpackaged_files_terminate_build 1
%define _stripped_files_terminate_build 1
%set_verify_elf_method strict

Name: stgit
Version: 1.5
Release: alt1
Summary: Stacked Git
License: GPL-2.0-only
Group: Development/Tools
Url: https://stacked-git.github.io/
Vcs: https://github.com/stacked-git/stgit

Source: %name-%version.tar

BuildArch: noarch
BuildRequires: asciidoc
BuildRequires: git-core
BuildRequires: make
BuildRequires: rpm-build-python3
BuildRequires: python3-module-setuptools
BuildRequires: xmlto

%description
Stacked Git, StGit for short, is an application for managing Git commits
as a stack of patches.

With a patch stack workflow, multiple patches can be developed
concurrently and efficiently, with each patch focused on a single concern,
resulting in both a clean Git commit history and improved productivity.

%prep
%setup

%build
%make_build STGIT_VERSION=%version-%release all doc

%install
%makeinstall_std install-doc STGIT_VERSION=%version-%release \
		PYTHON=%__python3 DESTDIR=%buildroot prefix=%_prefix
install -Dpm0644 completion/stgit.bash \
		%buildroot%_datadir/bash-completion/completions/stgit
install -Dpm0644 completion/stgit.zsh \
		%buildroot%_datadir/zsh/site-functions/_stgit
install -Dpm0644 completion/stg.fish \
		%buildroot%_datadir/fish/vendor_completions.d/stg.fish

install -d %buildroot%_datadir/vim/vimfiles/{syntax,ftdetect}
install -m 644 contrib/vim/syntax/*.vim   %buildroot%_datadir/vim/vimfiles/syntax/
install -m 644 contrib/vim/ftdetect/*.vim %buildroot%_datadir/vim/vimfiles/ftdetect/

%check
%make_build test

%files
%doc COPYING README.md AUTHORS.md CHANGELOG.md contrib/stgbashprompt.sh
%_bindir/stg
%_man1dir/*.1*
%python3_sitelibdir_noarch/stgit*
%_datadir/bash-completion/completions/stgit
%_datadir/zsh/site-functions/_stgit
%_datadir/fish/vendor_completions.d/stg.fish
%_datadir/vim/vimfiles/*/*.vim

%changelog
* Thu Mar 10 2022 Vitaly Chikunov <vt@altlinux.org> 1.5-alt1
- First import v1.5 (2022-01-28).
