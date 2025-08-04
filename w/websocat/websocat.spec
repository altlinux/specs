Name: websocat
Version: 1.14.0
Release: alt1

Summary: Netcat, curl and socat for WebSockets

License: MIT
Group: Networking/Other
Url: https://github.com/vi/websocat

VCS: https://github.com/vi/websocat.git
Source: %name-%version.tar
Source1: vendor.tar
Source99: websocat.watch

BuildRequires(pre): rpm-build-rust /proc
BuildRequires: libssl-devel
BuildRequires: perl-Pod-Usage

%description
%summary.

%prep
%setup -a1
mkdir .cargo
cat <<EOF >.cargo/config.toml
[source.crates-io]
replace-with = "vendored-sources"

[source.vendored-sources]
directory = "vendor"
EOF
unlink ./Cargo.lock
subst 's+PATH=target/debug:$PATH+PATH=target/release:$PATH+g' ./test.sh

%build
%rust_build \
	--features=seqpacket,signal_handler,ssl,unix_stdio

%install
%rust_install

%check
%rust_test --workspace
./test.sh

%files
%_bindir/%name
%doc *.md

%changelog
* Mon Aug 04 2025 Sergey Gvozdetskiy <serjigva@altlinux.org> 1.14.0-alt1
- Updated to v1.14.0.

* Sun Sep 25 2022 Vladimir D. Seleznev <vseleznv@altlinux.org> 1.11.0-alt1
- Updated to v1.11.0.

* Wed May 18 2022 Vladimir D. Seleznev <vseleznv@altlinux.org> 1.10.0-alt1
- Updated to v1.10.1.

* Thu Dec 09 2021 Vladimir D. Seleznev <vseleznv@altlinux.org> 1.9.0-alt1
- Updated to v1.9.0.

* Wed May 12 2021 Vladimir D. Seleznev <vseleznv@altlinux.org> 1.8.1-alt1
- Updated to v1.8.1.
- Built against OpenSSL libs.
- Built with the following features: seqpacket, signal_handler, ssl and
  unix_stdio.
- Fixed %%check.

* Sat Apr 17 2021 Vladimir D. Seleznev <vseleznv@altlinux.org> 1.8.0-alt1
- Updated to v1.8.0.

* Thu Apr 08 2021 Vladimir D. Seleznev <vseleznv@altlinux.org> 1.7.0-alt1
- Initial build for ALT Sisyphus.

