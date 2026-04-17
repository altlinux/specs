%def_without check

Name: miniserve
Version: 0.35.0
Release: alt1
Summary: A CLI tool to serve files and dirs over HTTP
License: MIT
Group: System/Servers
Url: https://crates.io/crates/miniserve
VCS: https://github.com/svenstaro/miniserve

Source: %name-%version.tar
Source1: vendor.tar

ExcludeArch: ppc64le

BuildRequires(pre): rpm-macros-rust
BuildRequires: rpm-build-rust
BuildRequires: libssl-devel

%description
miniserve is a small, self-contained cross-platform CLI tool
that allows you to just grab the binary and serve some file(s)
via HTTP.

%prep
%setup -a 1
%rust_prep

%build
%rust_build
./target/release/%name --print-manpage > %name.1

%install
%rust_install
mkdir -p %buildroot%_man1dir
install -m 0644 %name.1 %buildroot%_man1dir

%check
%rust_test

%files
%_bindir/%name
%_man1dir/%name.1.*
%doc LICENSE README.md

%changelog
* Thu Apr 16 2026 Dmitry Maksimenkov <dmaks@altlinux.org> 0.35.0-alt1
- Updated to version 0.35.0.

* Sun Mar 08 2026 Alexander Makeenkov <amakeenk@altlinux.org> 0.33.0-alt1
- Updated to version 0.33.0.

* Sat Nov 08 2025 Alexander Makeenkov <amakeenk@altlinux.org> 0.32.0-alt1
- Updated to version 0.32.0.

* Wed Jul 16 2025 Alexander Makeenkov <amakeenk@altlinux.org> 0.31.0-alt1
- Updated to version 0.31.0.

* Fri Sep 27 2024 Alexander Makeenkov <amakeenk@altlinux.org> 0.28.0-alt1
- Updated to version 0.28.0.

* Wed Jan 17 2024 Alexander Makeenkov <amakeenk@altlinux.org> 0.26.0-alt1
- Updated to version 0.26.0.

* Sun Jan 07 2024 Alexander Makeenkov <amakeenk@altlinux.org> 0.25.0-alt1
- Updated to version 0.25.0.

* Sun Oct 02 2022 Alexander Makeenkov <amakeenk@altlinux.org> 0.22.0-alt1
- Initial build for ALT.
