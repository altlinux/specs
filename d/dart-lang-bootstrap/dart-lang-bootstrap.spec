%define _unpackaged_files_terminate_build 1

Name: dart-lang-bootstrap
Version: 3.10.1
Release: alt1

Summary: Dart language bootstrap
License: BSD-3-Clause
Group: Development/Other

%ifarch x86_64
%define dart_arch x64
%endif
%ifarch aarch64
%define dart_arch arm64
%endif

Url: https://dart.dev/get-dart/archive
# https://storage.googleapis.com/dart-archive/channels/stable/release/%version/sdk/dartsdk-linux-%dart_arch-release.zip
Source: dartsdk-linux-%dart_arch-release.zip

BuildRequires: rpm-build-python3
BuildRequires: musl-libc
BuildRequires: unzip

%filter_from_requires s/.*dart.*//

ExclusiveArch: x86_64 aarch64

Provides: dart-lang-sdk

Conflicts: dart-lang

%description
%summary.

%prep
%setup -c
%setup -DTn %name-%version

%install
mkdir -p %buildroot%_libexecdir %buildroot%_bindir %buildroot%_includedir
cp dart-sdk %buildroot%_libexecdir/dart -r

ln -s %_libexecdir/dart/bin/dart           %buildroot%_bindir/dart
ln -s %_libexecdir/dart/bin/dartaotruntime %buildroot%_bindir/dartaotruntime
ln -s %_libexecdir/dart/include/dart       %buildroot%_includedir/dart

%files
%_bindir/dart
%_bindir/dartaotruntime
%_includedir/dart
%_libexecdir/dart

%changelog
* Thu Mar 26 2026 David Sultaniiazov <x1z53@altlinux.org> 3.10.1-alt1
- Boostrap for 3.10.1.

* Fri Jun 13 2025 David Sultaniiazov <x1z53@altlinux.org> 3.8.1-alt2
- Get source from https://dart.dev/get-dart/archive
- Unzip on build
- Add aarch64

* Thu Jun 12 2025 David Sultaniiazov <x1z53@altlinux.org> 3.8.1-alt1
- Initial build
