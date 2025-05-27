%define _unpackaged_files_terminate_build 1
%define pypi_name clipster

Name:    python3-module-%pypi_name
Version: 2.1.1
Release: alt1

Summary: clipster - python clipboard manager
License: AGPL-3.0
Group:   Development/Python3
URL:     https://github.com/mrichar1/clipster
Provides: %pypi_name = %EVR

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel python3-module-setuptools python3-module-wheel

BuildArch: noarch

Source: %pypi_name-%version.tar

%description
Clipster is a simple clipboard manager, written in `Python` (2 or 3). It aims to be lightweight, have a small set of non-core dependencies (`Gtk+`), and is designed to interact well with tiling and keyboard-based window managers. It uses selection events, rather than polling, and offers both command-line and GUI interaction with the clipboard.

%prep
%setup -n %pypi_name-%version

%build
%pyproject_build

%install
%pyproject_install

%files
%python3_sitelibdir/%pypi_name-0.0.0.dist-info/*
%doc *.md
%_bindir/%pypi_name
%_datadir/licenses/%pypi_name/*.md
%_docdir/%pypi_name/*.md

%changelog
* Mon Jan 27 2025 Artem Semenov <savoptik@altlinux.org> 2.1.1-alt1
- Initial build for Sisyphus
