%define oname extract_dtb

Name: python3-module-%oname
Version: 1.2.3
Release: alt1

Summary: Tool to split a kernel image
License: GPLv3
Group: Development/Python3
Url: https://github.com/PabloCastellano/extract-dtb
VCS: https://github.com/PabloCastellano/extract-dtb

Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3
BuildRequires: python3(setuptools)
BuildRequires: python3(wheel)

BuildArch: noarch

%description
Tool to split a kernel image with appended dtbs
into separated kernel and dtb files.

This tool is similar to split-appended-dtb but it is written
in Python and its code is simpler and almost 3x shorter.
Moreover, it doesn't require any external Python library.

%prep
%setup

%build
%pyproject_build

%install
%pyproject_install

%files
%doc README.md  CHANGES.md LICENSE
%_bindir/*
%python3_sitelibdir/%oname/
%python3_sitelibdir/*.dist-info
%exclude %_usr/LICENSE
%exclude %_usr/CHANGES.md

%changelog
* Wed Jan 21 2026 Danila Skachedubov <skachedubov@altlinux.org> 1.2.3-alt1
- Initial build for ALT.
