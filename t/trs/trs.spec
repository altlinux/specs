%global _unpackaged_files_terminate_build 1
%global commit_hash 8809230

Name: trs
Version: 0.7.0
Release: alt1
Summary: Secure CLI utility for moving files to trash using the XDG Trash specification
License: MIT
Group: File tools
Url: https://altlinux.space/amakeenk/trs
VCS: https://altlinux.space/amakeenk/trs

Source: %name-%version.tar
Source1: vendor.tar

BuildRequires(pre): rpm-macros-golang
BuildRequires: rpm-build-golang

%description
trs (from TRaSh) - a secure CLI utility for moving files to trash using the XDG Trash specification.
- Safe by default - Files go to trash, not /dev/null
- XDG compliant - Works with GNOME, KDE, and other desktop environments
- Security-focused - Protected against symlink attacks, path traversal, and DoS
- No dependencies - Pure Go, no external utilities needed
- Cross-device - Handles files on different filesystems automatically

This project was entirely implemented with AI assistance.

%prep
%setup -a 1

%build
export VERSION=%version
export GIT_COMMIT=%commit_hash
%make build

# create completion files
./trs completion bash > trs.bash
./trs completion fish > trs.fish
./trs completion zsh > _trs

%install
mkdir -p %buildroot%_bindir \
         %buildroot%_man1dir \
         %buildroot%_datadir/bash-completion/completions \
         %buildroot/%_datadir/zsh/site-functions \
         %buildroot%_datadir/fish/vendor_completions.d

install -m 0755 trs %buildroot%_bindir
install -m 0644 man/trs.1 %buildroot%_man1dir
install -m 0644 trs.bash %buildroot%_datadir/bash-completion/completions
install -m 0644 trs.fish %buildroot%_datadir/fish/vendor_completions.d
install -m 0644 _trs %buildroot/%_datadir/zsh/site-functions

%check
%make test

%files
%_bindir/trs
%_man1dir/trs.1.*
%_datadir/bash-completion/completions/trs.bash
%_datadir/fish/vendor_completions.d/trs.fish
%_datadir/zsh/site-functions/_trs

%changelog
* Wed Mar 18 2026 Alexander Makeenkov <amakeenk@altlinux.org> 0.7.0-alt1
- Updated to version 0.7.0.

* Mon Mar 16 2026 Alexander Makeenkov <amakeenk@altlinux.org> 0.6.0-alt1
- Updated to version 0.6.0.

* Sun Mar 08 2026 Alexander Makeenkov <amakeenk@altlinux.org> 0.5.0-alt1
- Updated to version 0.5.0.

* Sat Mar 07 2026 Alexander Makeenkov <amakeenk@altlinux.org> 0.4.2-alt1
- Updated to version 0.4.2.

* Sat Mar 07 2026 Alexander Makeenkov <amakeenk@altlinux.org> 0.4.1-alt1
- Initial build for ALT.
