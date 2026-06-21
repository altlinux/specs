%define _unpackaged_files_terminate_build 1
%define import_path github.com/ramonvermeulen/whosthere

Name:       whosthere
Version:    0.8.2
Release:    alt1

License:    Apache-2.0
Group:      Monitoring
Summary:    Local Area Network discovery tool with a TUI

Url:        https://github.com/ramonvermeulen/whosthere
Vcs:        https://github.com/ramonvermeulen/whosthere
Source:     %name-%version.tar
Source1:    vendor.tar

Patch:      %name-%version-%release.patch

BuildRequires(pre): rpm-build-golang

ExclusiveArch: %go_arches

%description
Local Area Network discovery tool with a interactive
Terminal User Interface (TUI). Discover, explore,
and understand your LAN in an intuitive way.

%prep
%setup -a 1 -q
%patch -p1

%build
export BUILDDIR="$PWD/.build"
export IMPORT_PATH="%import_path"
export GOPATH="$BUILDDIR:%go_path"

%golang_prepare

%golang_build .

%install
export BUILDDIR="$PWD/.build"
export IGNORE_SOURCES=1

%golang_install

%files
%doc LICENSE README.*
%_bindir/%name

%changelog
* Wed Jun 17 2026 Sergey Savelev <medovi@altlinux.org> 0.8.2-alt1
- New version 0.8.2.

* Mon Mar 02 2026 Sergey Savelev <medovi@altlinux.org> 0.6.1-alt1
- Initial build for Sisyphus.
