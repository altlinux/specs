Name: hygg
Version: 0.1.14
Release: alt1

Summary: Simplifying the way you read
License: AGPL-3.0-only
Group: Text tools

Url: https://github.com/kruserr/hygg
VCS: https://github.com/kruserr/hygg

Source0: %name-%version.tar
Source1: vendor.tar

BuildRequires(pre): rpm-build-rust
BuildRequires: /proc pkgconfig(openssl)

%description
%summary

%prep
%setup -a1

mkdir -p .cargo
cat >> .cargo/config <<EOF
[source.crates-io]
replace-with = "vendored-sources"

[source.vendored-sources]
directory = "vendor"
EOF


%package -n %name-server
Group:   Text tools
Summary: %name-server - A less like CLI text reader
%description -n %name-server
%name-server - A less like CLI text reader

%package -n cli-epub-to-text
Group:   Text tools
Summary: A CLI epub to plain text converter
%description -n cli-epub-to-text
A CLI epub to plain text converter

%package -n cli-pdf-to-text
Group:   Text tools
Summary: A CLI pdf to plain text converter
%description -n cli-pdf-to-text
A CLI pdf to plain text converter

%package -n cli-text-reader
Group:   Text tools
Summary: cli-text-reader - A less like CLI text reader
%description -n cli-text-reader
cli-text-reader - A less like CLI text reader

%package -n cli-justify
Group:   Text tools
Summary: A CLI text justify tool
%description -n cli-justify
A CLI text justify tool

%build
%rust_build

%install
%rust_install

install -D target/release/%name-server %buildroot%_bindir/%name-server
install -D target/release/cli-epub-to-text %buildroot%_bindir/cli-epub-to-text
install -D target/release/cli-pdf-to-text %buildroot%_bindir/cli-pdf-to-text
install -D target/release/cli-text-reader %buildroot%_bindir/cli-text-reader
install -D target/release/cli-text-reader-online %buildroot%_bindir/cli-text-reader-online
install -D target/release/cli-justify %buildroot%_bindir/cli-justify

%check
%rust_test

%files
%doc *.md LICENSE
%_bindir/%name

%files -n %name-server
%_bindir/%name-server

%files -n cli-epub-to-text
%_bindir/cli-epub-to-text

%files -n cli-pdf-to-text
%_bindir/cli-pdf-to-text

%files -n cli-text-reader
%_bindir/cli-text-reader
%_bindir/cli-text-reader-online

%files -n cli-justify
%_bindir/cli-justify

%changelog
* Wed Apr 09 2025 Aleksandr Shamaraev <shad@altlinux.org> 0.1.14-alt1
- Initial build for ALT Linux.
