%global optflags_lto %optflags_lto -ffat-lto-objects
# remove me in the next release
%add_optflags -Wno-deprecated-declarations

Name:	 newsboat
Version: 2.30
Release: alt1

Summary: an RSS/Atom feed reader for the text console

License: MIT
Group:	 Networking/News
Url:	 https://github.com/newsboat/newsboat

VCS:	 https://github.com/newsboat/newsboat
Source:  newsboat-%version.tar
# cargo vendor
Source1: vendor.tar
Source2: newsboat.watch

Provides:  newsbeuter = %EVR
Obsoletes: newsbeuter < %EVR

BuildRequires:	/proc
BuildRequires:	asciidoctor >= 1.5.2
BuildRequires:	gcc-c++ >= 4.9
BuildRequires:	libcurl-devel >= 7.21.6
BuildRequires:	libjson-c-devel >= 0.11
BuildRequires:	libncursesw-devel
BuildRequires:	libsqlite3-devel >= 3.5.0
BuildRequires:	libssl-devel
BuildRequires:	libstfl0-devel
BuildRequires:	libxml2-devel
BuildRequires:	rust-cargo >= 1.42.0
BuildRequires:	zlib-devel

%description
Newsboat is an RSS/Atom feed reader for the text console. It's an actively
maintained fork of Newsbeuter.

%prep
%setup -a 1
mkdir -p .cargo
cat > .cargo/config <<EOF
[source.crates-io]
replace-with = "vendored-sources"

[source.vendored-sources]
directory = "vendor"
EOF

%build
export CFLAGS="%optflags"
export CXXFLAGS="$CFLAGS"
export CARGO_FLAGS="--offline"

./config.sh
%make_build \
	prefix=%_prefix \
	#

%install
%makeinstall_std \
	prefix=%_prefix \
	#
%find_lang %name

%check
# workaround for test compilaton: remove me in the next release
%add_optflags -Wno-error=maybe-uninitialized
export CFLAGS="%optflags"
export CXXFLAGS="$CFLAGS"

make test
cargo test

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

%changelog
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

