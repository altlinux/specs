Name: estrlist
Version: 0.8
Release: alt1

Summary: estrlist - string operation utility

License: MIT
Group: Development/Other
Url: http://www.altlinux.org/Etersoft-build-utils

Packager: Vitaly Lipatov <lav@altlinux.ru>

# Source-git: http://git.altlinux.org/people/lav/packages/estrlist.git
Source: %name-%version.tar
Source1: %name-development-%version.tar

BuildRequires: rpm-build-rust

Conflicts: etersoft-build-utils < 3.0.0

%description
String operation utility (Rust implementation).

%prep
%setup -a1

mkdir -p estrlist-rs/.cargo
cat >> estrlist-rs/.cargo/config.toml <<EOF
[source.crates-io]
replace-with = "vendored-sources"

[source.vendored-sources]
directory = "vendor"
EOF

%build
cd estrlist-rs
%rust_build ||:

%install
install -D bin/%name %buildroot%_bindir/%name.sh
if [ -x estrlist-rs/target/release/estrlist ]; then
    cd estrlist-rs
    %rust_install %name
else
    echo "Rust binary not found, using shell version"
    ln -s %{name}.sh %buildroot%_bindir/%name
fi

%files
%_bindir/%name.sh
%_bindir/%name

%changelog
* Fri Jan 23 2026 Vitaly Lipatov <lav@altlinux.ru> 0.8-alt1
- add Rust implementation (estrlist-rs)
- spec: build Rust version using rpm-build-rust
- change license to MIT
- pack shell estrlist as estrlist.sh
- estrlist.sh: optimize difference, containts, intersection
- estrlist.sh: filter_strip_spaces: fix reading input without trailing newline
- install estrlist-rust as estrlist (with fallback to estrlist)

* Fri Jan 09 2026 Vitaly Lipatov <lav@altlinux.ru> 0.7-alt1
- estrlist: add new verbs: first, last
- estrlist: add new verbs: firstupper, tolower
- estrlist: optimize first and last, remove forks
- estrlist: optimize count, remove fork to wc
- estrlist: fix contains to use exact word matching
- estrlist: rename strip_spaces to strip and optimize it
- estrlist: fix glob expansion in word list functions
- estrlist: optimize reg_exclude, reg_wordexclude, reg_include
- estrlist: add reg_wordinclude, fix reg_include to match ^pattern$
- estrlist: fix contains to handle tabs and newlines
- estrlist: has_space now checks all whitespace

* Mon Apr 08 2024 Vitaly Lipatov <lav@altlinux.ru> 0.6-alt1
- estrlist: print out only to stderr if error
- estrlist: add contains

* Wed May 04 2022 Vitaly Lipatov <lav@altlinux.ru> 0.5-alt1
- egrep -> grep -E

* Sun Sep 05 2021 Vitaly Lipatov <lav@altlinux.ru> 0.4-alt1
- turn off wildcard expansion

* Mon Aug 30 2021 Vitaly Lipatov <lav@altlinux.ru> 0.3-alt1
- estrlist: add is_empty alias
- estrlist: add has_space
- estrlist: add -- support

* Sat Oct 10 2020 Vitaly Lipatov <lav@altlinux.ru> 0.2-alt1
- estrlist: fix exclude, fix exclude tests

* Wed Oct 07 2020 Vitaly Lipatov <lav@altlinux.ru> 0.1-alt1
- initial build for ALT Sisyphus (separated from etersoft-build-utils)
