%define _unpackaged_files_terminate_build 1

Name:           presenterm
Version:        0.16.1
Release:        alt1

Summary:        A markdown terminal slideshow tool
License:        BSD-2-Clause
Group:          Office
URL:            https://mfontanini.github.io/presenterm/
VCS:            https://github.com/mfontanini/presenterm.git

Source:         %name-%version.tar
Source1:        vendor.tar

Patch:          %name-%version-%release.patch

BuildRequires(pre): rpm-build-rust

%description
Presenterm lets you create presentations in markdown format and run
them from your terminal, with support for image and animated gifs,
highly customizable themes, code highlighting, exporting
presentations into PDF format, and plenty of other features.

%prep
%setup -a 1 -q
%patch -p1
%rust_prep

%build
%rust_build

%install
%rust_install

%check
%rust_test

%files
%_bindir/*
%doc README.md CHANGELOG.md LICENSE

%changelog
* Fri Feb 20 2026 Sergey Savelev <medovi@altlinux.org> 0.16.1-alt1
- New version 0.16.1.

* Mon Feb 16 2026 Sergey Savelev <medovi@altlinux.org> 0.16.0-alt1
- New version 0.16.0.

* Fri Nov 21 2025 Sergey Savelev <medovi@altlinux.org> 0.15.1-alt1
- Initial build for Sisyphus.
