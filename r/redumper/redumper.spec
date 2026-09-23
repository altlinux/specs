%define _unpackaged_files_terminate_build 1

Name: redumper
Version: 752
Release: alt1

Summary: Low level CD dumper utility
License: GPL-3.0
Group: Archiving/Cd burning
Url: https://github.com/superg/redumper
Vcs: https://github.com/superg/redumper

Source: %name-%version.tar

BuildRequires(pre): rpm-macros-cmake
BuildRequires: cmake
BuildRequires: ninja-build
BuildRequires: ctest
BuildRequires: clang18.1 clang18.1-tools
BuildRequires: libstdc++-devel-static
BuildRequires: libgtest-devel

%description
redumper is a cross-platform command-line tool for creating accurate optical
disc dumps. It provides a low-level, byte-perfect workflow for CDs, including
incremental refinement, SCSI/C2 error recovery, raw subchannel preservation,
and automatic audio-offset detection. It also supports dumping of DVD, HD DVD,
and Blu-ray media.
redumper was originally created for the Redump disc-preservation initiative and
is now the default dumping software used for Redump optical-disc submissions.

%prep
%setup

%build
%cmake -G Ninja -DCMAKE_BUILD_TYPE=Release \
	-DREDUMPER_VERSION_BUILD=%version \
	-DCMAKE_TOOLCHAIN_FILE=cmake/toolchains/linux-x64.cmake
%cmake_build

%install
%cmake_install

%check
%ctest

%files
%_bindir/%name
%doc LICENSE README.md

%changelog
* Tue Sep 22 2026 Bogdan Boguslavskij <bogdanb@altlinux.org> 752-alt1
- Version b752.

* Fri Sep 11 2026 Bogdan Boguslavskij <bogdanb@altlinux.org> 750-alt1
- Initial build for Sisyphus.

