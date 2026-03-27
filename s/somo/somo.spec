%define _unpackaged_files_terminate_build 1

Name: somo
Version: 1.3.2
Release: alt1
Summary: A human-friendly alternative to netstat for socket and port monitoring
License: MIT
Group: System/Configuration/Networking
Url: https://github.com/theopfr/somo

Source0: %name-%version.tar
Source1: vendor.tar
Patch: %name-%version-%release.patch

BuildRequires(pre): rpm-macros-rust
BuildRequires: rpm-build-rust
BuildRequires: rust-cargo
BuildRequires: zstd
BuildRequires: help2man
BuildRequires: pigz

%description
%summary

%prep
%setup -a 1
%patch -p1
mkdir -p .cargo
cat >> .cargo/config.toml <<EOF

[source.crates-io]
replace-with = "vendored-sources"

[source.vendored-sources]
directory = "vendor"
EOF

%build
%rust_build
for sh in 'bash' 'fish' 'zsh'; do
	./target/release/%name generate-completions "$sh" > target/%name."$sh"
done

help2man -N -n "Socket and port monitoring tool" ./target/release/%name > target/%name.1
pigz --best target/%name.1

%install
mkdir -p %buildroot%_man1dir
install -Dm 0755 target/release/%name %buildroot%_bindir/%name
install -Dm 0644 target/%name.bash %buildroot%_datadir/bash-completion/completions/%name
install -Dm 0644 target/%name.fish %buildroot%_datadir/fish/vendor_completions.d/%name.fish
install -Dm 0644 target/%name.zsh %buildroot%_datadir/zsh/site-functions/_%name
install -Dm 0644 target/%name.1.* %buildroot%_man1dir/

%files
%doc README.md images/*
%_bindir/%name
%_man1dir/%name.1.*
%_datadir/bash-completion/completions/%name
%_datadir/fish/vendor_completions.d/%name.fish
%_datadir/zsh/site-functions/_%name

%changelog
* Fri Mar 27 2026 Pavel Shilov <zerospirit@altlinux.org> 1.3.2-alt1
- 1.3.1 -> 1.3.2

* Tue Dec 23 2025 Pavel Shilov <zerospirit@altlinux.org> 1.3.1-alt1
- 1.3.0 -> 1.3.1

* Tue Oct 21 2025 Pavel Shilov <zerospirit@altlinux.org> 1.3.0-alt1
- 1.2.0 -> 1.3.0

* Wed Sep 03 2025 Pavel Shilov <zerospirit@altlinux.org> 1.2.0-alt1
- 1.1.0 -> 1.2.0

* Wed Jul 16 2025 Pavel Shilov <zerospirit@altlinux.org> 1.1.0-alt1
- Initial build for Sisyphus.
