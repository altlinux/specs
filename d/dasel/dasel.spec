%define _unpackaged_files_terminate_build 1
%global import_path github.com/tomwright/dasel/v2

Name: dasel
Version: 3.8.1
Release: alt1
Summary: Select, put and delete data from JSON, TOML, YAML, XML and CSV files with a single tool.
License: MIT
Group: Development/Other
Url: https://github.com/TomWright/dasel

Source0: %name-%version.tar
Source1: vendor.tar
Patch: %name-%version-%release.patch

BuildRequires(pre): rpm-build-golang
BuildRequires: golang

%description
%summary

%prep
%setup -a 1
%patch -p1

%build
export BUILDDIR="$PWD/.gopath"
export IMPORT_PATH="%import_path"
export GOPATH="$BUILDDIR:%go_path"
export GOFLAGS="-mod=vendor"

%golang_prepare

%golang_build cmd/%name/

%install
export BUILDDIR="$PWD/.gopath"
export IMPORT_PATH="%import_path"
export GOPATH="$BUILDDIR:%go_path"
export IGNORE_SOURCES=1
%golang_install

%files
%doc README.md
%_bindir/%name

%changelog
* Mon May 04 2026 Pavel Shilov <zerospirit@altlinux.org> 3.8.1-alt1
- New version 3.8.1.

* Fri Mar 27 2026 Pavel Shilov <zerospirit@altlinux.org> 3.4.0-alt1
- New version 3.4.0.

* Thu Mar 12 2026 Pavel Shilov <zerospirit@altlinux.org> 3.3.1-alt1
- New version 3.3.1.

* Thu Feb 26 2026 Pavel Shilov <zerospirit@altlinux.org> 3.3.0-alt1
- New version 3.3.0.

* Wed Feb 04 2026 Pavel Shilov <zerospirit@altlinux.org> 3.2.1-alt1
- New version 3.2.1.

* Tue Dec 23 2025 Pavel Shilov <zerospirit@altlinux.org> 3.1.4-alt1
- New version 3.1.4.

* Wed Oct 16 2024 Pavel Shilov <zerospirit@altlinux.org> 2.8.1-alt1
- Initial build for Sisyphus.

