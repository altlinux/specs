# Unpackaged files in buildroot should terminate build
%define _unpackaged_files_terminate_build 1

Name: qucsator_rf
Version: 1.0.2
Release: alt1

Summary: RF circuit simulation kernel for Qucs-S
License: GPL-2.0-or-later
Group: Education
Url: https://github.com/ra3xdh/qucsator_rf

Source: %name-%version.tar
Patch: %name-%version-%release.patch

Buildrequires(pre): rpm-macros-cmake
BuildRequires: cmake
BuildRequires: gcc-c++
BuildRequires: flex
BuildRequires: gperf
BuildRequires: dos2unix

%description
QucsatorRF is a command line driven circuit simulator targeted for RF and
microwave circuits.
It takes a network list in a certain format as input and outputs a Qucs XML
dataset. This repository also contians a QucsconvRF tool for data file formats
conversion.

%prep
%setup
%patch -p1

%build
%cmake -DCMAKE_BUILD_TYPE=Release -DWITH_ADMS=OFF
%cmake_build

%install
%cmake_install

%files
%_bindir/qucsator_rf
%_bindir/qucsconv_rf
%_man1dir/qucsator_rf.1.*
%_man1dir/qucsconv_rf.1.*

%changelog
* Tue Sep 10 2024 Anton Midyukov <antohami@altlinux.org> 1.0.2-alt1
- new version 1.0.2

* Wed Jul 24 2024 Anton Midyukov <antohami@altlinux.org> 1.0.1-alt1
- Initial build
