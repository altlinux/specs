Name:           hut
Version:        0.3.0
Release:        alt1
Source:         %name-v%version.tar.gz
Source1:        vendor.tar
Group:          Other
Summary:        A CLI tool for sr.ht
License:        AGPL-3.0-only
URL:            https://sr.ht/~emersion/hut/

# Automatically added by buildreq on Tue May 17 2022
# optimized out: golang-src libgpg-error python3-base sh4
BuildRequires: golang python3 scdoc

%description
A CLI tool for sr.ht.

Run hut init to get started. Read the man page to learn about all commands.

%prep
%setup -n %name-v%version -a1

%build
%make_build PREFIX=%_prefix

%install
%makeinstall_std PREFIX=%_prefix

%files
%doc README.md
%_bindir/*
%_datadir/bash-completion/completions/hut
%_datadir/fish/vendor_completions.d/hut.fish
%_datadir/zsh/site-functions/_hut
%_man1dir/*

%changelog
* Mon Jun 05 2023 Fr. Br. George <george@altlinux.ru> 0.3.0-alt1
- Version up; update vendor tree

* Tue May 17 2022 Fr. Br. George <george@altlinux.org> 0.1.0-alt1
- Initial build for ALT
