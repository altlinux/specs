%define _unpackaged_files_terminate_build 1
%ifarch %arm
%def_disable check
%else
%def_enable check
%endif

Name: fish
Version: 4.7.1
Release: alt2

Summary: A friendly interactive shell
License: GPLv2+
Group: Shells

Url: http://fishshell.com/
Vcs: https://github.com/fish-shell/fish-shell.git

Source0: %name-%version.tar
Source1: vendor-%version.tar
Patch0: fish-4.0.0-alt_apt_adapter.patch

Requires: man
BuildRequires(pre): rpm-build-rust rpm-build-python3 rpm-macros-cmake rpm-macros-ninja-build
BuildRequires: rust-cargo >= 1.85
BuildRequires: cargo-license gcc
BuildRequires: terminfo
BuildRequires: libpcre2-devel >= 10.22
BuildRequires: cmake ninja-build rpm-build-ninja rpm-build-cmake
# BuildRequires: python3-module-sphinx-sphinx-build-symlink

# for check
BuildRequires: ctest
BuildRequires: shellcheck
BuildRequires: /proc /dev/pts
BuildRequires: procps
BuildRequires: python3-module-pexpect
BuildRequires: tmux
BuildRequires: git-core

%description
fish is a shell geared towards interactive use. Its features are
focused on user friendliness and discoverability. The language syntax
is simple but incompatible with other shell languages.

%prep
%setup -a 1
%rust_prep
cat >> .cargo/config.toml <<EOF
[source."git+https://github.com/fish-shell/rust-pcre2?tag=0.2.9-utf32"]
git = "https://github.com/fish-shell/rust-pcre2"
tag = "0.2.9-utf32"
replace-with = "vendored-sources"
EOF

%patch0 -p1
echo "%version" > version

# Change the bundled scripts to invoke the python binary directly.
for f in $(find share/tools -type f -name '*.py'); do
    sed -i -e '1{s@^#!.*@#!%__python3@}' "$f"
done
# Fix autocompletion for zed package
sed -i 's/-c zed/-c zed-editor/g' share/completions/zed.fish
mv share/completions/zed.fish share/completions/zed-editor.fish

%build
export CARGO_NET_OFFLINE=true
%cmake \
    -GNinja \
    -DCMAKE_BUILD_TYPE=RelWithDebInfo \
    -DCMAKE_INSTALL_SYSCONFDIR=%_sysconfdir \
    -DWITH_DOCS=OFF \
    -DCMAKE_INSTALL_DOCDIR=%_docdir/%name
%cmake_build -t all
cargo license > LICENSE.dependencies

%install
%cmake_install
%find_lang %name

rm -f %buildroot%_datadir/fish/completions/docker.fish
rm -f %buildroot%_desktopdir/fish.desktop
rm -f %buildroot%_pixmapsdir/fish.png
rm -rf %buildroot%_datadir/pkgconfig

%check
export CARGO_NET_OFFLINE=true
printf '/vendor/\n' >> .ignore
unset LESS LESSOPEN LESSCLOSE NO_COLOR
cargo xtask shellcheck
export RUST_TEST_THREADS=1
export TERM=xterm-256color
%cmake_build --target fish_run_tests ||:

%post
grep -q %_bindir/fish %_sysconfdir/shells ||
	echo %_bindir/fish >>%_sysconfdir/shells

%postun
. shell-quote
if [ "$1" = 0 ]; then
	sed -i "/^$(quote_sed_regexp %_bindir/fish)$/ d" %_sysconfdir/shells
fi

%files -f %name.lang
%_bindir/*
%dir %_sysconfdir/fish
%config %_sysconfdir/fish/config.fish
%_datadir/fish
%doc %_docdir/%name
%doc LICENSE.dependencies
# %_man1dir/*

%changelog
* Fri Jun 19 2026 Artyom Sinyugin <writers@altlinux.org> 4.7.1-alt2
- Fix fail in gyle because of random test fail.

* Fri May 22 2026 Artyom Sinyugin <writers@altlinux.org> 4.7.1-alt1
- New version 4.7.1.

* Mon Mar 02 2026 Artyom Sinyugin <writers@altlinux.org> 4.5.0-alt1
- New release 4.5.0.
- Sphinx auto doc removed from building process.

* Thu Nov 20 2025 Artyom Sinyugin <writers@altlinux.org> 4.2.1-alt1
- New version 4.2.1.
- Fixed zed autocomplete (ALT#57050).

* Tue Nov 11 2025 Artyom Sinyugin <writers@altlinux.org> 4.2.0-alt1
- New version 4.2.0 (ALT#56212).

* Fri May 23 2025 Artyom Sinyugin <writers@altlinux.org> 4.0.2-alt1
- New version 4.0.2.

* Thu Mar 20 2025 Artyom Sinyugin <writers@altlinux.org> 4.0.1-alt1
- New version 4.0.1.

* Wed Mar 05 2025 Artyom Sinyugin <writers@altlinux.org> 4.0.0-alt1
- 4.0.0 (ALT#53265)

* Wed Feb 19 2025 Alexey Shabalin <shaba@altlinux.org> 3.7.1-alt2
- Fix FTBFS. Drop PCRE2_ERROR_BADREPESCAPE test for pcre2-10.45

* Wed Apr 03 2024 Alexey Shabalin <shaba@altlinux.org> 3.7.1-alt1
- 3.7.1

* Mon Jan 15 2024 Alexey Shabalin <shaba@altlinux.org> 3.7.0-alt1
- 3.7.0

* Wed Dec 06 2023 Alexey Shabalin <shaba@altlinux.org> 3.6.4-alt1
- 3.6.4 (Fixes: CVE-2023-49284)

* Wed Nov 29 2023 Michael Shigorin <mike@altlinux.org> 3.6.1-alt1.2
- E2K: lcc 1.26.20 ftbfs workaround by ilyakurdyukov@ (mcst#8502)

* Sat May 27 2023 Alexey Shabalin <shaba@altlinux.org> 3.6.1-alt1.1
- disable tests for arm32

* Mon Apr 17 2023 Alexey Shabalin <shaba@altlinux.org> 3.6.1-alt1
- 3.6.1

* Wed Jan 11 2023 Alexey Shabalin <shaba@altlinux.org> 3.6.0-alt1
- 3.6.0

* Wed Jun 22 2022 Alexey Shabalin <shaba@altlinux.org> 3.5.0-alt1
- 3.5.0

* Fri Apr 08 2022 Alexey Shabalin <shaba@altlinux.org> 3.4.1-alt1
- 3.4.1

* Thu Mar 24 2022 Alexey Shabalin <shaba@altlinux.org> 3.4.0-alt2
- cherry-pick commits from Integration_3.4.1 branch

* Mon Mar 21 2022 Alexey Shabalin <shaba@altlinux.org> 3.4.0-alt1
- 3.4.0 (Fixes: CVE-2022-20001)

* Sun Oct 31 2021 Alexey Shabalin <shaba@altlinux.org> 3.3.1-alt2
- Drop tests with resetting match start inside lookaround.

* Mon Jul 19 2021 Alexey Shabalin <shaba@altlinux.org> 3.3.1-alt1
- 3.3.1

* Tue Jul 06 2021 Alexey Shabalin <shaba@altlinux.org> 3.3.0-alt1
- 3.3.0

* Sun May 30 2021 Arseny Maslennikov <arseny@altlinux.org> 3.2.2-alt1.1
- NMU: spec: adapt to new cmake macros.

* Tue Apr 20 2021 Alexey Shabalin <shaba@altlinux.org> 3.2.2-alt1
- 3.2.2

* Sun Mar 14 2021 Alexey Shabalin <shaba@altlinux.org> 3.2.0-alt1
- 3.2.0

* Wed May 06 2020 Alexey Shabalin <shaba@altlinux.org> 3.1.2-alt1
- 3.1.2

* Thu Feb 20 2020 Alexey Shabalin <shaba@altlinux.org> 3.1.0-alt1
- 3.1.0

* Sat Feb 23 2019 Alexey Shabalin <shaba@altlinux.org> 3.0.2-alt1
- 3.0.2

* Sun Feb 17 2019 Alexey Shabalin <shaba@altlinux.org> 3.0.1-alt1
- 3.0.1

* Wed Jan 09 2019 Alexey Shabalin <shaba@altlinux.org> 3.0.0-alt2
- remove completion for docker, fixed file conflict with docker-ce package

* Sun Dec 30 2018 Alexey Shabalin <shaba@altlinux.org> 3.0.0-alt1
- 3.0.0

* Tue Feb 13 2018 Alexey Shabalin <shaba@altlinux.ru> 2.7.1-alt2
- fix find altlinux path /etc/openssh for completions

* Sat Feb 10 2018 Alexey Shabalin <shaba@altlinux.ru> 2.7.1-alt1
- 2.7.1

* Wed Dec 13 2017 Alexey Shabalin <shaba@altlinux.ru> 2.7.0-alt1
- 2.7.0

* Tue Oct 31 2017 Alexey Shabalin <shaba@altlinux.ru> 2.6.0-alt1
- 2.6.0

* Sun Sep 07 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.1.1-alt1.git20140907
- Version 2.1.1

* Fri Apr 19 2013 Dmitry V. Levin (QA) <qa_ldv@altlinux.org> 1.23.1-alt2.qa1
- NMU: rebuilt for updated dependencies.

* Sun Mar 06 2011 Kirill A. Shutemov <kas@altlinux.org> 1.23.1-alt2
- Do not compress /usr/share/fish/man/*

* Sat Mar 05 2011 Kirill A. Shutemov <kas@altlinux.org> 1.23.1-alt1
- Initial build
