%def_disable server
%def_disable online_editor

Name: hygg
Version: 0.1.21
Release: alt1

Summary: Simplifying the way you read
License: AGPL-3.0-only
Group: Text tools

Url: https://github.com/kruserr/hygg
VCS: https://github.com/kruserr/hygg

ExcludeArch: i586

Source0: %name-%version.tar
Source1: vendor.tar

BuildRequires(pre): rpm-build-rust
BuildRequires: /proc pkgconfig(openssl)

%description
%summary

%prep
%setup -a1

mkdir -p .cargo
cat >> .cargo/config.toml <<EOF

[source.crates-io]
replace-with = "vendored-sources"

[source.vendored-sources]
directory = "vendor"
EOF

%if_enabled server
%package -n %name-server
Group:   Text tools
Summary: %name-server - A less like CLI text reader
%description -n %name-server
%name-server - A less like CLI text reader
%endif

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

%if_enabled server
install -D target/release/%name-server %buildroot%_bindir/%name-server
%endif

install -D target/release/cli-epub-to-text %buildroot%_bindir/cli-epub-to-text
install -D target/release/cli-pdf-to-text %buildroot%_bindir/cli-pdf-to-text
install -D target/release/cli-text-reader %buildroot%_bindir/cli-text-reader

%if_enabled online_editor
install -D target/release/cli-text-reader-online %buildroot%_bindir/cli-text-reader-online
%endif

install -D target/release/cli-justify %buildroot%_bindir/cli-justify

%files
%doc *.md LICENSE
%_bindir/%name

%if_enabled server
%files -n %name-server
%_bindir/%name-server
%endif

%files -n cli-epub-to-text
%_bindir/cli-epub-to-text

%files -n cli-pdf-to-text
%_bindir/cli-pdf-to-text

%files -n cli-text-reader
%_bindir/cli-text-reader
%if_enabled online_editor
%_bindir/cli-text-reader-online
%endif

%files -n cli-justify
%_bindir/cli-justify

%changelog
* Mon Jun 08 2026 Aleksandr Shamaraev <shad@altlinux.org> 0.1.21-alt1
- 0.1.19 -> 0.1.21

* Sat Sep 27 2025 Aleksandr Shamaraev <shad@altlinux.org> 0.1.19-alt1
- 0.1.18 -> 0.1.19

* Fri Sep 26 2025 Aleksandr Shamaraev <shad@altlinux.org> 0.1.18-alt1
- 0.1.17 -> 0.1.18

* Thu Jul 24 2025 Aleksandr Shamaraev <shad@altlinux.org> 0.1.17-alt1
- 0.1.16 -> 0.1.17

* Fri Jul 18 2025 Aleksandr Shamaraev <shad@altlinux.org> 0.1.16-alt1
- 0.1.15 -> 0.1.16

* Mon May 26 2025 Aleksandr Shamaraev <shad@altlinux.org> 0.1.15-alt1
- 0.1.14 -> 0.1.15

* Wed Apr 09 2025 Aleksandr Shamaraev <shad@altlinux.org> 0.1.14-alt1
- Initial build for ALT Linux.
