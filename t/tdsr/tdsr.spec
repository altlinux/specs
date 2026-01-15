%define _unpackaged_files_terminate_build 1

Name:    tdsr
Version: 20250830
Release: alt1

Summary: A console screen reader for macOS and Linux
License: GPL-3.0
Group:   Accessibility
URL:     https://github.com/tspivey/tdsr
Source: %name-%version.tar

# Ignome macos requires
%add_python3_req_skip PyObjCTools
%add_python3_req_skip objc
%add_python3_req_skip Foundation
%add_python3_req_skip AVFoundation

BuildRequires(pre): rpm-macros-python3
BuildRequires: rpm-build-python3
BuildRequires: python3-devel
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-wheel
BuildRequires: python3-module-flit-core

BuildArch: noarch

%description
This is a console-based screen reader.
It has been tested under macOS, Linux and FreeBSD.
It might also run on other \*nix systems, but this hasn't been tested.

What works
* Reading output
* Reading by line, word and character
* cursor keys (waits some amount of time and speaks)

%package -n python3-module-%name
Summary: Python3 module fore %name
Group: Development/Python3

%description -n python3-module-%name
%summary

%prep
%setup

%build
%pyproject_build

%install
%pyproject_install

mkdir -p %buildroot%_sysconfdir/%name
ln -s %python3_sitelibdir/%name/tdsr.cfg.dist %buildroot%_sysconfdir/%name/%name.cfg

%files
%doc readme.md COPYING.txt
%config(noreplace) %_sysconfdir/%name/%name.cfg
%_bindir/%name

%files -n python3-module-%name
%python3_sitelibdir/%name
%python3_sitelibdir/%name-0.0.dist-info

%changelog
* Wed Jan 14 2026 Artem Semenov <savoptik@altlinux.org> 20250830-alt1
- Updated to latest pip version 20250830

* Fri Mar 21 2025 Artem Semenov <savoptik@altlinux.org> 20240602-alt2
- Cleaned-up the spec

* Fri Nov 01 2024 Artem Semenov <savoptik@altlinux.org> 20240602-alt1
- Initial build for Sisyphus (ALT bug: 51706)
