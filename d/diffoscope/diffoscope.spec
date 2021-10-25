%define _unpackaged_files_terminate_build 1
Name: diffoscope
Version: 188
Release: alt1

Summary: In-depth comparison of files, archives, and directories
Group: Development/Python3
License: GPLv3+
Url: https://diffoscope.org/

Source: %name-%version.tar

BuildArch: noarch
BuildRequires: python3-devel
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-libmagic
BuildRequires: python3-module-libarchive-c
BuildRequires: python3-module-docutils
BuildRequires: python3-modules-curses
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

%build
%python3_build
%make -C doc

%install
%python3_install
install -Dm644 doc/diffoscope.1 %buildroot%_man1dir/diffoscope.1

%files
%doc README.rst debian/changelog COPYING
%python3_sitelibdir_noarch/diffoscope*
%_bindir/diffoscope
%_man1dir/diffoscope.1*

%changelog
* Mon Oct 25 2021 Slava Aseev <ptrnine@altlinux.org> 188-alt1
- Update to upstream version 188

* Thu Mar 12 2020 Slava Aseev <ptrnine@altlinux.org> 137-alt1
- Update to upstream version 137

* Mon Dec 24 2018 Slava Aseev <ptrnine@altlinux.org> 107-alt1
- Initial build for ALT
