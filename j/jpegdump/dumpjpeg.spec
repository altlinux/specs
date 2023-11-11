# SPDX-License-Identifier: GPL-2.0-only
%define _unpackaged_files_terminate_build 1

Name: jpegdump
Version: 0.0.10
Release: alt1
Summary: JPEG file analysis tool
License: ALT-Public-Domain
Group: Graphics
Url: https://blog.didierstevens.com/my-software/#jpegdump
Vcs: https://github.com/DidierStevens/DidierStevensSuite/commits/master/jpegdump.py
BuildArch: noarch

Source: %name-%version.tar
BuildRequires: rpm-build-python3

%description
jpegdump.py is a tool that takes one or more files to analyze them for
sequences. It does this by searching for 0xFF bytes and then starts to
parse them as markers (possibly followed by data).

%prep
%setup

%build
sed -i '1c\#! %__python3' jpegdump.py
chmod a+rx jpegdump.py
./jpegdump.py --man > README

%install
install -Dp jpegdump.py %buildroot%_bindir/jpegdump.py

%check
%__python3 -m py_compile jpegdump.py
./jpegdump.py sample-red-100x75.jpg
./jpegdump.py sample-red-100x75.jpg -s2

%files
%doc README
%_bindir/jpegdump.py

%changelog
* Sat Nov 11 2023 Vitaly Chikunov <vt@altlinux.org> 0.0.10-alt1
- First import V0_0_10 (2022-09-02).
