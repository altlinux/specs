%define _unpackaged_files_terminate_build 1

%def_with tests

%define optflags_lto %{nil}

Name: bear
Version: 4.1.5
Release: alt1

Summary: Tool that generates a compilation database for clang tooling

License: GPLv3
Group: Development/Tools
Url: https://github.com/rizsotto/Bear.git

Packager: Maxim Knyazev <mattaku@altlinux.org>

Source: %name-%version.tar

BuildRequires: rust rust-cargo
BuildRequires: lld

%description
Build ear records the CLI flags passed to compilers for each translation unit
during the build and stores them in JSON format. The resulting database
describes how single compilation unit should be processed and can be used by
Clang tooling and other various tools.

Some build systems (e. g. Meson, CMake) can produce the command database by
themselves and do not require this tool. Others, including plain Make, do not.

%prep
%setup

mkdir -p .cargo
cat >> .cargo/config.toml <<EOF
[source.crates-io]
replace-with = "vendored-sources"

[source.vendored-sources]
directory = "vendor"
EOF

%build

cargo build --frozen --release

# generate shell completions
./target/release/generate-completions target/release/completions

%install
DESTDIR="%buildroot" PREFIX=%_prefix ./scripts/install.sh

%files
%_bindir/*
%_prefix/libexec/%name
%{_datadir}/elvish/lib/%name.elv
%{_datadir}/bash-completion/completions/%name
%{_datadir}/fish/vendor_completions.d/bear.fish
%{_datadir}/zsh/site-functions/_bear
%_man1dir/*.1*
%{_datadir}/doc/%name

%changelog
* Mon Jul 13 2026 Vladimir Didenko <cow@altlinux.org> 4.1.5-alt1
- New version

* Sat Oct 19 2024 Nazarov Denis <nenderus@altlinux.org> 3.1.5-alt1
- New version

* Sat Oct 14 2023 Nazarov Denis <nenderus@altlinux.org> 3.1.3-alt1
- New version

* Fri Aug 4 2023 Vladimir Didenko <cow@altlinux.org> 3.1.2-alt1
- New version

* Wed Jun 21 2023 Ilya Kurdyukov <ilyakurdyukov@altlinux.org> 3.0.19-alt1.git67d5a34.1
- Fixed build for Elbrus (GTest is required but not specified)

* Tue Jul 19 2022 Vladimir Didenko <cow@altlinux.org> 3.0.19-alt1.git67d5a34
- Update to the latest master to fix build with libfmt 9.0

* Tue Sep 28 2021 Vladimir Didenko <cow@altlinux.org> 3.0.16-alt1
- New version.

* Mon Aug 30 2021 Vladimir Didenko <cow@altlinux.org> 3.0.13-alt1
- New version.
- Disable lto build flag.

* Wed Jun 23 2021 Arseny Maslennikov <arseny@altlinux.org> 3.0.12-alt1
- 3.0.11-alt1.gitdfa9e262 -> 3.0.12.

* Thu May 13 2021 Vladimir Didenko <cow@altlinux.org> 3.0.11-alt1.gitdfa9e262
- New version.

* Wed Jan 27 2021 Arseny Maslennikov <arseny@altlinux.org> 3.0.7-alt1
- 2.4.3 -> 3.0.7.

* Fri Apr 10 2020 Maxim Knyazev <mattaku@altlinux.org> 2.4.3-alt1
- Initial build to Sisyphus
