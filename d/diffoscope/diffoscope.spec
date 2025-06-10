%define _unpackaged_files_terminate_build 1
Name: diffoscope
Version: 297
Release: alt1

Summary: In-depth comparison of files, archives, and directories
Group: Development/Python3
License: GPLv3+
Url: https://diffoscope.org/
Vcs: https://salsa.debian.org/reproducible-builds/diffoscope.git
BuildArch: noarch

Source: %name-%version.tar
Patch0: %name-%version-sbin.patch

BuildRequires(pre): rpm-build-pyproject
BuildRequires: /proc
BuildRequires: /dev
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-libmagic
BuildRequires: python3-module-libarchive-c
BuildRequires: python3-module-docutils
BuildRequires: python3-modules-curses
BuildRequires: python3-module-wheel
BuildRequires: /usr/bin/help2man
BuildRequires: /usr/bin/xxd
Requires: python3(tlsh)
Requires: python3(libarchive)
Requires: python3(curses)

%description
Diffoscope will try to get to the bottom of what makes files or directories different.
It will recursively unpack archives of many kinds and transform various binary formats
into more human readable form to compare them. It can compare two tarballs, ISO images,
or PDF just as easily. The differences can be shown in a text or HTML report.

%prep
%setup
%autopatch -p1

%build
%pyproject_build
%make -C doc

%install
%pyproject_install
install -Dm644 doc/diffoscope.1 %buildroot%_man1dir/diffoscope.1

%check
%pyproject_run_pytest

%files
%doc README.rst debian/changelog COPYING
%python3_sitelibdir_noarch/diffoscope*
%_bindir/diffoscope
%_man1dir/diffoscope.1*

%changelog
* Tue Jun 10 2025 Ivan Khanas <xeno@altlinux.org> 297-alt1
- New version.

* Mon Dec 25 2023 Slava Aseev <ptrnine@altlinux.org> 253-alt1
- new version

* Thu Sep 15 2022 Slava Aseev <ptrnine@altlinux.org> 220-alt1
- new version

* Mon Oct 25 2021 Slava Aseev <ptrnine@altlinux.org> 188-alt1
- Update to upstream version 188

* Thu Mar 12 2020 Slava Aseev <ptrnine@altlinux.org> 137-alt1
- Update to upstream version 137

* Mon Dec 24 2018 Slava Aseev <ptrnine@altlinux.org> 107-alt1
- Initial build for ALT
