%def_without check

Name:	 newsboat
Version: 2.43
Release: alt1

Summary: An RSS/Atom feed reader for the text console

License: MIT
Group:	 Networking/News
Url:	 https://newsboat.org
Vcs:	 https://github.com/newsboat/newsboat.git

Source0: %name-%version.tar
Source1: vendor.tar
Source2: %name.watch
Source3: Cargo.lock

Provides:  newsbeuter = %EVR
Obsoletes: newsbeuter < %EVR

BuildRequires(pre): rpm-build-rust
BuildRequires:	/proc
BuildRequires:	asciidoctor
BuildRequires:	gcc-c++
BuildRequires:	pkgconfig(libcurl)
BuildRequires:	pkgconfig(json-c)
BuildRequires:	pkgconfig(ncursesw)
BuildRequires:	pkgconfig(sqlite3)
BuildRequires:	pkgconfig(libssl)
BuildRequires:	pkgconfig(stfl)
BuildRequires:	pkgconfig(libxml-2.0)
BuildRequires:	rust-cargo
BuildRequires:	pkgconfig(zlib)

%description
Newsboat is an RSS/Atom feed reader for the text console. It's an actively
maintained fork of Newsbeuter.

%prep
%setup -a1
mkdir -p .cargo
cat >> .cargo/config.toml <<EOF
[source.crates-io]
replace-with = "vendored-sources"

[source.vendored-sources]
directory = "vendor"

[term]
verbose = true
quiet = false

[install]
root = "%buildroot%_prefix"

[build]
rustflags = ["-Copt-level=3", "-Cdebuginfo=1"]

[profile.release]
strip = false
EOF
cp -fv %SOURCE3 .

%build
./config.sh
%make_build prefix=%_prefix

%install
%makeinstall_std prefix=%_prefix
%find_lang %name

%check
# workaround for test compilaton: remove me in the next release
%add_optflags -Wno-error=maybe-uninitialized
export CFLAGS="%optflags"
export CXXFLAGS="$CFLAGS"

%make test
%rust_test --workspace

%files -f %name.lang
%doc LICENSE
%_bindir/newsboat
%_bindir/podboat
%_defaultdocdir/newsboat
%_man1dir/newsboat.1*
%_man1dir/podboat.1*
%dir %_iconsdir/hicolor/scalable
%dir %_iconsdir/hicolor/scalable/apps
%_iconsdir/hicolor/scalable/apps/newsboat.svg
%_datadir/fish/vendor_completions.d/%name.fish
%_datadir/zsh/site-functions/_%name

%changelog
* Tue Mar 24 2026 Sergey Gvozdetskiy <serjigva@altlinux.org> 2.43-alt1
- Updated to r2.43.

* Mon Dec 29 2025 Sergey Gvozdetskiy <serjigva@altlinux.org> 2.42-alt1
- Updated to r2.42.

* Tue Sep 23 2025 Sergey Gvozdetskiy <serjigva@altlinux.org> 2.41-alt1
- Updated to r2.41.

* Tue Jun 24 2025 Sergey Gvozdetskiy <serjigva@altlinux.org> 2.40-alt1
- Updated to r2.40.

* Thu May 15 2025 Sergey Gvozdetskiy <serjigva@altlinux.org> 2.38-alt1
- Updated to r2.38.

* Wed May 17 2023 Vladimir D. Seleznev <vseleznv@altlinux.org> 2.31-alt1
- Updated to r2.31.

* Mon Dec 26 2022 Vladimir D. Seleznev <vseleznv@altlinux.org> 2.30-alt1
- Updated to 2.30.

* Mon Sep 26 2022 Vladimir D. Seleznev <vseleznv@altlinux.org> 2.29-alt1
- Updated to 2.29.

* Mon Jun 27 2022 Vladimir D. Seleznev <vseleznv@altlinux.org> 2.28-alt1
- Updated to 2.28.

* Sun Jun 26 2022 Vladimir D. Seleznev <vseleznv@altlinux.org> 2.27-alt1
- Updated to 2.27.

* Wed Sep 29 2021 Vladimir D. Seleznev <vseleznv@altlinux.org> 2.25-alt1
- Updated to 2.25.

* Sat Aug 28 2021 Vladimir D. Seleznev <vseleznv@altlinux.org> 2.24-alt2
- Fixed FTBFS: built fat LTO objects.

* Mon Jul 26 2021 Vladimir D. Seleznev <vseleznv@altlinux.org> 2.24-alt1
- Updated to 2.24.

* Tue Mar 23 2021 Vladimir D. Seleznev <vseleznv@altlinux.org> 2.23-alt1
- Updated to 2.23.

* Wed Feb 03 2021 Vladimir D. Seleznev <vseleznv@altlinux.org> 2.22.1-alt1
- Updated to 2.22.1.

* Thu Sep 24 2020 Vladimir D. Seleznev <vseleznv@altlinux.org> 2.21-alt1
- Updated to 2.21.

* Fri Aug 14 2020 Vladimir D. Seleznev <vseleznv@altlinux.org> 2.20.1.0.308.git49794d07-alt1
- Initial build for ALT Sisyphus.

