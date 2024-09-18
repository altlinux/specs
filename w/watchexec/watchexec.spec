Name:    watchexec
Version: 2.1.2
Release: alt1

Summary: Executes commands in response to file modifications
License: Apache-2.0
Group:   Other
Url:     https://github.com/watchexec/watchexec

Packager: Mikhail Gordeev <obirvalger@altlinux.org>

Source:   %name-%version.tar

BuildRequires(pre): rpm-build-rust
BuildRequires: /proc

ExcludeArch: %ix86

%description
Software development often involves running the same commands over and over.
Boring!

watchexec is a simple, standalone tool that watches a path and runs a command
whenever it detects modifications.

%prep
%setup
mkdir -p .cargo
cat > .cargo/config <<EOF
[source.crates-io]
replace-with = "vendored-sources"

[source.vendored-sources]
directory = "vendor"
EOF

%build
%rust_build

%install
%rust_install
install -Dm 644 completions/zsh %buildroot/%_datadir/zsh/site-functions/_%name
install -Dm 644 doc/%name.1 %buildroot/%_man1dir/%name.1

%check
%rust_test

%files
%_bindir/%name
%_man1dir/%name.1.*
%_datadir/zsh/site-functions/_%name
%doc *.md

%changelog
* Wed Sep 18 2024 Mikhail Gordeev <obirvalger@altlinux.org> 2.1.2-alt1
- new version 2.1.2

* Mon May 15 2023 Mikhail Gordeev <obirvalger@altlinux.org> 1.22.3-alt1
- new version 1.22.3

* Mon Mar 27 2023 Mikhail Gordeev <obirvalger@altlinux.org> 1.22.2-alt1
- new version 1.22.2

* Wed Mar 15 2023 Mikhail Gordeev <obirvalger@altlinux.org> 1.21.1-alt1
- new version 1.21.1

* Thu Jan 19 2023 Mikhail Gordeev <obirvalger@altlinux.org> 1.21.0-alt1
- new version 1.21.0

* Sun Nov 06 2022 Mikhail Gordeev <obirvalger@altlinux.org> 1.20.6-alt1
- new version 1.20.6

* Sun Sep 12 2021 Mikhail Gordeev <obirvalger@altlinux.org> 1.17.1-alt1
- Initial build for Sisyphus
