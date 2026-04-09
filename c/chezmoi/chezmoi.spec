%define _unpackaged_files_terminate_build 1
%def_with check

Name: chezmoi
Version: 2.70.1
Release: alt1

Summary: Manage your dotfiles across multiple diverse machines, securely
License: MIT
Group: System/Configuration/Other
VCS: https://github.com/twpayne/chezmoi
Url: https://www.chezmoi.io/

Source0: %name-%version.tar
Source1: %name-%version-vendor.tar

BuildRequires(pre): rpm-build-golang

%description
chezmoi helps you manage your personal configuration files (dotfiles,
like ~/.gitconfig) across multiple machines.

chezmoi provides many features beyond symlinking or using a bare git
repo including:
- templates (to handle small differences between machines)
- password manager support (to store your secrets securely)
- importing files from archives (great for shell and editor plugins)
- full file encryption (using gpg or age)
- running scripts (to handle everything else)

%prep
%setup -a1

%build
export LDFLAGS="-compressdwarf=false \
                -X main.version=%version-%release \
                -X main.date=$(date -u +'%%Y-%%m-%%dT%%H:%%M:%%SZ' --date=@$SOURCE_DATE_EPOCH)"
%gobuild

%install
install -vDm 755 ./chezmoi \
        %buildroot/%_bindir/chezmoi

install -vDm 644 completions/chezmoi-completion.bash \
        %buildroot/%_datadir/bash-completion/completions/chezmoi

install -vDm 644 completions/chezmoi.zsh \
        %buildroot/%_datadir/zsh/site-functions/_chezmoi

install -vDm 644 completions/chezmoi.fish \
        %buildroot/%_datadir/fish/vendor_completions.d/chezmoi.fish

%check
%gotest

%files
%doc LICENSE
%_bindir/chezmoi
%_datadir/bash-completion/completions/chezmoi
%_datadir/zsh/site-functions/_chezmoi
%_datadir/fish/vendor_completions.d/chezmoi.fish

%changelog
* Thu Apr 09 2026 Egor Ignatov <egori@altlinux.org> 2.70.1-alt1
- New version 2.70.1.

* Tue Mar 10 2026 Egor Ignatov <egori@altlinux.org> 2.70.0-alt1
- New version 2.70.0.

* Tue Feb 17 2026 Egor Ignatov <egori@altlinux.org> 2.69.4-alt1
- New version 2.69.4.

* Thu Jan 29 2026 Egor Ignatov <egori@altlinux.org> 2.69.3-alt1
- New version 2.69.3.

* Wed Jan 14 2026 Egor Ignatov <egori@altlinux.org> 2.69.1-alt1
- New version 2.69.1.

* Wed Dec 10 2025 Egor Ignatov <egori@altlinux.org> 2.68.1-alt1
- New version 2.68.1.

* Thu Dec 04 2025 Egor Ignatov <egori@altlinux.org> 2.68.0-alt1
- New version 2.68.0.

* Thu Nov 27 2025 Egor Ignatov <egori@altlinux.org> 2.67.1-alt1
- New version 2.67.1.

* Wed Nov 05 2025 Egor Ignatov <egori@altlinux.org> 2.67.0-alt1
- New version 2.67.0.

* Mon Oct 27 2025 Egor Ignatov <egori@altlinux.org> 2.66.2-alt1
- New version 2.66.2.

* Wed Oct 08 2025 Egor Ignatov <egori@altlinux.org> 2.66.0-alt1
- New version 2.66.0.

* Wed Sep 24 2025 Egor Ignatov <egori@altlinux.org> 2.65.2-alt1
- New version 2.65.2.

* Wed Sep 10 2025 Egor Ignatov <egori@altlinux.org> 2.65.1-alt1
- New version 2.65.1.

* Wed Aug 27 2025 Egor Ignatov <egori@altlinux.org> 2.65.0-alt1
- New version 2.65.0.

* Mon Aug 25 2025 Egor Ignatov <egori@altlinux.org> 2.64.0-alt1
- New version 2.64.0.

* Wed Jul 30 2025 Egor Ignatov <egori@altlinux.org> 2.63.1-alt1
- New version 2.63.1.

* Tue Jul 15 2025 Egor Ignatov <egori@altlinux.org> 2.63.0-alt1
- New version 2.63.0.

* Mon Jun 23 2025 Egor Ignatov <egori@altlinux.org> 2.62.7-alt1
- New version 2.62.7.

* Fri May 23 2025 Egor Ignatov <egori@altlinux.org> 2.62.5-alt1
- New version 2.62.5.

* Tue May 13 2025 Egor Ignatov <egori@altlinux.org> 2.62.4-alt1
- New version 2.62.4.

* Tue May 06 2025 Egor Ignatov <egori@altlinux.org> 2.62.2-alt1
- New version 2.62.2.

* Mon Apr 14 2025 Egor Ignatov <egori@altlinux.org> 2.62.1-alt1
- First build for ALT.
