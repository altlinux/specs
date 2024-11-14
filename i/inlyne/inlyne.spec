Name:    inlyne
Version: 0.4.3
Release: alt2

Summary: Introducing Inlyne, a GPU powered yet browserless tool to help you quickly view markdown files in the blink of an eye
License: MIT
Group:   Other
Url:     https://github.com/Inlyne-Project/inlyne

Packager: Mikhail Gordeev <obirvalger@altlinux.org>

Source: %name-%version.tar

Patch: inlyne-0.4.3-alt-old-nix-loongarch64.patch

BuildRequires(pre): rpm-build-rust
BuildRequires: /proc
BuildRequires: pkgconfig(wayland-client) pkgconfig(xkbcommon)
BuildRequires: pkgconfig(fontconfig)

%description
Markdown files are a wonderful tool to get formatted, visually appealing,
information to people in a minimal way. Except 9 times out of 10 you need an
entire web browser to quickly open a file...

Introducing Inlyne, a GPU powered yet browserless tool to help you quickly view
markdown files in the blink of an eye.

%prep
%setup
mkdir -p .cargo
cat >> .cargo/config.toml <<EOF
[source.crates-io]
replace-with = "vendored-sources"

[source.vendored-sources]
directory = "vendor"
EOF

%patch -p1
sed -i -e 's/"files":{[^}]*}/"files":{}/' \
    ./vendor/nix-0.25.1/.cargo-checksum.json

%build
%rust_build

%install
%rust_install

install -Dm 644 completions/_%name %buildroot/%_datadir/zsh/site-functions/_%name
install -Dm 644 completions/%name.bash %buildroot%_datadir/bash-completion/completions/%name
install -Dm 644 completions/%name.fish %buildroot%_datadir/fish/vendor_completions.d/%name.fish

%check
%ifarch %ix86
%rust_test -- \
    --skip interpreter::tests::centered_image_with_size_align_and_link \
    --skip interpreter::tests::image_loading_fails_gracefully
%else
%rust_test
%endif

%files
%doc *.md
%_bindir/*
%_datadir/zsh/site-functions/_%name
%_datadir/bash-completion/completions/%name
%_datadir/fish/vendor_completions.d/%name.fish

%changelog
* Wed Nov 13 2024 Ilya Sorochan <k0tran@altlinux.org> 0.4.3-alt2
- Add patch for loongarch64 that fixes nix crate.

* Thu Nov 07 2024 Mikhail Gordeev <obirvalger@altlinux.org> 0.4.3-alt1
- Initial build for Sisyphus
