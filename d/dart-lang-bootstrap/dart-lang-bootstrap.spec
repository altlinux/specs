%define _unpackaged_files_terminate_build 1

Name: dart-lang-bootstrap
Version: 3.8.1
Release: alt1

Summary: Dart language bootstrap
License: BSD-3-Clause
Group: Development/Other

Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3

ExclusiveArch: x86_64

%filter_from_requires s/.*dart.*//

%description
%summary.

%prep
%setup

%install
mkdir -p %buildroot%_libexecdir/dart %buildroot%_bindir %buildroot%_includedir
cp dart-sdk/* %buildroot%_libexecdir/dart -r

ln -s %_libexecdir/dart/bin/dart           %buildroot%_bindir/dart
ln -s %_libexecdir/dart/bin/dartaotruntime %buildroot%_bindir/dartaotruntime
ln -s %_libexecdir/dart/include/dart       %buildroot%_includedir/dart

%files
%_bindir/dart
%_bindir/dartaotruntime
%_includedir/dart
%_libexecdir/dart

%changelog
* Thu Jun 12 2025 David Sultaniiazov <x1z53@altlinux.org> 3.8.1-alt1
- Initial build
