%def_with check

Name: bottom
Version: 0.14.3
Release: alt1
Summary: Yet another cross-platform graphical process/system monitor
License: MIT
Group: Monitoring
Url: https://clementtsang.github.io/bottom
Vcs: https://github.com/ClementTsang/bottom

Source: %name-%version.tar
Source1: vendor.tar

BuildRequires(pre): rpm-macros-rust
BuildRequires: rpm-build-rust

%if_with check
BuildRequires: /proc /dev/pts
%endif

%description
A customizable cross-platform graphical process/system monitor for the terminal.

%prep
%setup -a 1
%rust_prep

%build
export CFLAGS="-O3 -DPIC -fPIC"
export RUSTFLAGS="-Clink-args=-fPIC -Cdebuginfo=1 --cfg rustix_use_libc"
export RUST_BACKTRACE=1
export BTM_GENERATE=true
%rust_build

%install
%rust_install btm
install -D -m 644 target/tmp/bottom/manpage/btm.1 %buildroot%_man1dir/btm.1
install -D -m 644 target/tmp/bottom/completion/btm.bash %buildroot%_datadir/bash-completion/completions/btm
install -D -m 644 target/tmp/bottom/completion/btm.fish %buildroot%_datadir/fish/vendor_completions.d/btm.fish
install -D -m 644 target/tmp/bottom/completion/_btm %buildroot%_datadir/zsh/site-functions/_btm

%check
export RUST_BACKTRACE=full
%rust_test -- --skip test_data_collection

%files
%doc LICENSE CHANGELOG.md README.md sample_configs
%_bindir/btm
%_man1dir/*
%_datadir/bash-completion/completions/btm
%_datadir/fish/vendor_completions.d/btm.fish
%_datadir/zsh/site-functions/_btm

%changelog
* Sun Jul 05 2026 Alexander Makeenkov <amakeenk@altlinux.org> 0.14.3-alt1
- Updated to version 0.14.3.

* Mon Jun 22 2026 Alexander Makeenkov <amakeenk@altlinux.org> 0.14.1-alt1
- Updated to version 0.14.1.

* Sun Jun 21 2026 Alexander Makeenkov <amakeenk@altlinux.org> 0.14.0-alt1
- Updated to version 0.14.0.

* Sat Jan 17 2026 Alexander Makeenkov <amakeenk@altlinux.org> 0.12.3-alt1
- Updated to version 0.12.3.

* Sat Dec 27 2025 Alexander Makeenkov <amakeenk@altlinux.org> 0.12.1-alt1
- Updated to version 0.12.1.

* Sat Nov 22 2025 Alexander Makeenkov <amakeenk@altlinux.org> 0.11.4-alt1
- Updated to version 0.11.4.

* Sat Nov 08 2025 Alexander Makeenkov <amakeenk@altlinux.org> 0.11.3-alt1
- Updated to version 0.11.3.

* Sat Oct 11 2025 Alexander Makeenkov <amakeenk@altlinux.org> 0.11.2-alt1
- Updated to version 0.11.2.

* Sat Aug 16 2025 Alexander Makeenkov <amakeenk@altlinux.org> 0.11.1-alt1
- Updated to version 0.11.1.

* Sat Aug 09 2025 Alexander Makeenkov <amakeenk@altlinux.org> 0.11.0-alt1
- Updated to version 0.11.0.

* Fri Aug 23 2024 Alexey Shabalin <shaba@altlinux.org> 0.10.2-alt1
- New version 0.10.2.

* Wed May 22 2024 Alexey Shabalin <shaba@altlinux.org> 0.9.6-alt2
- Add completions to package.
- Add docs and sample_configs to package.

* Sun Oct 22 2023 Alexander Makeenkov <amakeenk@altlinux.org> 0.9.6-alt1
- Updated to version 0.9.6.

* Thu Jan 26 2023 Alexander Makeenkov <amakeenk@altlinux.org> 0.8.0-alt1
- Initial build for ALT
