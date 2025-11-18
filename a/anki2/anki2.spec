%global _unpackaged_files_terminate_build 1

%define git_commit 3890e12c9e48c028c3f12aa58cb64bd9f8895e30
%define git_commit_short %(c="%git_commit"; echo "${c:0:8}")

Name: anki2
Version: 25.09.2
Release: alt1

Summary: Flashcard program for using space repetition learning
License: AGPL-3.0+ and BSD-3-Clause and GPL-3 and MIT and 0BSD and CC-BY-4.0 and Apache-2.0
Group: Education
Url: https://apps.ankiweb.net
Vcs: https://github.com/ankitects/anki

# Build only for officially supported architectures
# see https://github.com/ankitects/anki/blob/24.06.3/build/ninja_gen/src/archives.rs#L43
ExclusiveArch: x86_64 aarch64

Source: %name-%version.tar
# Rust dependencies
Source1: vendor.tar
# Git submodules
Source2: ftl_core-repo.tar
Source3: ftl_qt-repo.tar
# JS dependencies
Source4: yarn-cache.tar

# For offline build
Patch1: anki2-25.07.5-alt-disable-git-rev-parse.patch
Patch2: anki2-25.07.5-arch-strip-formatter-deps.patch
Patch3: anki-24.06.3-arch-strip-type-checking-deps.patch
# aqt wheel contains non-python files.
# This puts files in %%python3_sitelibdir instead of %%python3_sitelibdir_noarch
# and satisfies sisyphus_check
Patch4: anki2-25.07.5-alt-mark-aqt-as-non-pure-python.patch

# For playing sound.
Requires: mpv
Requires(post,postun): desktop-file-utils

Conflicts: anki < %version-%release

BuildRequires(pre): rpm-macros-rust rpm-build-xdg
BuildPreReq: desktop-file-utils
BuildRequires: rpm-build-rust
BuildRequires: rpm-build-python3
BuildRequires: ninja-build
BuildRequires: libssl-devel
BuildRequires: protobuf-compiler
BuildRequires: node
BuildRequires: yarn
BuildRequires: python3
BuildRequires: git
BuildRequires: uv
BuildRequires: python3-module-hatchling
BuildRequires: python3-module-PyQt6
BuildRequires: python3-module-wheel
BuildRequires: python3-module-installer


%description
Anki is a program designed to help you remember facts (such as words
and phrases in a foreign language) as easily, quickly and efficiently
as possible. Anki is based on a theory called spaced repetition.

%prep
# For packaging instructions see for_maintainers.txt
%setup -a 1 -a 2 -a 3 -a 4
%patch1 -p 1
%patch2 -p 1
%patch3 -p 1
%patch4 -p 1

# Replace git rev-parse hash with alt release
sed -i 's/@BUILDHASH_STRING@/%git_commit_short/' build/runner/src/build.rs
# Build with system yarn
sed -i 's/"type": "module",/"type": "module"/' package.json
sed -i '/packageManager/d' package.json

# Needed for successful build
mkdir .git/

# Must be set up according to
# https://github.com/ankitects/anki/blob/main/docs/linux.md
mkdir -p out/pyenv/bin
ln -s "$(command -v python3)" out/pyenv/bin/python

mkdir -p .cargo
cat >> .cargo/config.toml <<EOF
[source.crates-io]
replace-with = "vendored-sources"

[source."git+https://github.com/ankitects/linkcheck.git?rev=184b2ca50ed39ca43da13f0b830a463861adb9ca"]
git = "https://github.com/ankitects/linkcheck.git"
rev = "184b2ca50ed39ca43da13f0b830a463861adb9ca"
replace-with = "vendored-sources"

[source."git+https://github.com/ankitects/rust-url.git?rev=bb930b8d089f4d30d7d19c12e54e66191de47b88"]
git = "https://github.com/ankitects/rust-url.git"
rev = "bb930b8d089f4d30d7d19c12e54e66191de47b88"
replace-with = "vendored-sources"

[source.vendored-sources]
directory = "vendor"
EOF

%build
# Do not download anything, disables git checks.
export OFFLINE_BUILD=1

# Use system packages instead of downloading stuff from internet.
export NODE_BINARY="$(command -v node)"
export YARN_BINARY="$(command -v yarn)"
export PROTOC_BINARY="$(command -v protoc)"
export UV_BINARY="$(command -v uv)"
export UV_PYTHON="$(command -v python3)"
export UV_OFFLINE=1
export UV_NO_BUILD_ISOLATION=1

# Use local cache instead of downloading.
export YARN_CACHE_FOLDER="$(realpath ./yarn-cache/)"

# Anki internal variable for optimization.
export RELEASE=2

./ninja wheels -v

%install
for wheel in out/wheels/*.whl; do
    python3 -m installer --destdir="%buildroot" "$wheel"
done

desktop-file-install --dir %buildroot%_desktopdir qt/launcher/lin/anki.desktop

install -Dm644 qt/launcher/lin/anki.1 %buildroot%_man1dir/anki.1
install -Dm644 qt/launcher/lin/anki.png %buildroot%_pixmapsdir/anki.png
install -Dm644 qt/launcher/lin/anki.xpm %buildroot%_pixmapsdir/anki.xpm
install -Dm644 qt/launcher/lin/anki.xml %buildroot%_xdgmimedir/packages/anki.xml

%files
%doc LICENSE README.md SECURITY.md
%_bindir/anki
%_bindir/ankiw
%python3_sitelibdir/anki
%python3_sitelibdir/aqt
%python3_sitelibdir/_aqt
# remove zeroes from version
# 25.07.5 -> 25.7.5
%python3_sitelibdir/%(dir='%{pyproject_distinfo anki}'; echo ${dir//0/})
%python3_sitelibdir/%(dir='%{pyproject_distinfo aqt}'; echo ${dir//0/})
%_desktopdir/anki.desktop
%_pixmapsdir/anki.png
%_pixmapsdir/anki.xpm
%_xdgmimedir/packages/anki.xml
%_man1dir/anki.*

%changelog
* Tue Nov 18 2025 Alexander Stepchenko <geochip@altlinux.org> 25.09.2-alt1
- 25.07.5 -> 25.09.2.

* Thu Aug 28 2025 Alexander Stepchenko <geochip@altlinux.org> 25.07.5-alt1
- Update to 25.07.5.

* Thu Aug 28 2025 Alexander Stepchenko <geochip@altlinux.org> 24.11-alt2
- Fix build with rust 1.89.

* Mon Dec 09 2024 Alexander Stepchenko <geochip@altlinux.org> 24.11-alt1
- 24.06.3 -> 24.11

* Sat Sep 21 2024 Alexander Stepchenko <geochip@altlinux.org> 24.06.3-alt2
- Fix build with rust 1.80 (force "time" crate to use version 0.3.36).

* Tue Jul 23 2024 Alexander Stepchenko <geochip@altlinux.org> 24.06.3-alt1
- 2.1.12 -> 24.06.3 (ALT #44369, #44622, #42124, #42288)

* Fri Oct 20 2023 Grigory Ustinov <grenka@altlinux.org> 2.1.12-alt3.1
- NMU: dropped dependency on distutils.

* Fri Feb 18 2022 Sergey V Turchin <zerg@altlinux.org> 2.1.12-alt3
- using not_qt5_qtwebengine_arches macro

* Thu Feb 03 2022 Sergey V Turchin <zerg@altlinux.org> 2.1.12-alt2
- build according qtwebengine arches

* Thu Apr 25 2019 Vitaly Lipatov <lav@altlinux.ru> 2.1.12-alt1
- NMU: new version (2.1.12) with rpmgs script
- switched to python3 and Qt5, add mpv require

* Sat Apr 13 2019 Dmitry V. Levin (QA) <qa_ldv@altlinux.org> 2.0.50-alt4
- NMU: really fixed build of this miserable package.

* Sat Apr 13 2019 Denis Smirnov <mithraen@altlinux.ru> 2.0.50-alt3
- fix build

* Mon Feb 25 2019 Denis Smirnov <mithraen@altlinux.ru> 2.0.50-alt2
- fix build

* Tue Apr 17 2018 Denis Smirnov <mithraen@altlinux.ru> 2.0.50-alt1
- first build for Sisyphus
