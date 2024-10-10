%define _unpackaged_files_terminate_build 1

Name: hsh-svace
Version: 1.0
Release: alt1

Summary: Run SVACE in hasher
License: GPL-3.0
Group: Development/Other
Url: https://github.com/Blarse/hsh-svace

BuildArch: noarch

Source0: %name-%version.tar

# These scripts are run in hasher
%add_findreq_skiplist %_libexecdir/hsh-svace/hsh-svace-build.sh
%add_findreq_skiplist %_libexecdir/hsh-svace/hsh-svace-analyze.sh

%description
%summary.

This package requires special hasher configuration, please refer to README.md.

%prep
%setup

%install
mkdir -pv %buildroot%_libexecdir/hsh-svace/
mkdir -pv %buildroot%_bindir
ln -svf %_libexecdir/hsh-svace/hsh-svace %buildroot%_bindir/hsh-svace
install -Dm755 ./hsh-svace -t %buildroot%_libexecdir/hsh-svace/
install -Dm644 ./hsh-svace-build.sh -t %buildroot%_libexecdir/hsh-svace/
install -Dm644 ./hsh-svace-analyze.sh -t %buildroot%_libexecdir/hsh-svace/

%files
%doc README.md LICENSE
%_bindir/hsh-svace
%dir %_libexecdir/hsh-svace
%_libexecdir/hsh-svace/*

%changelog
* Wed Oct 09 2024 Egor Ignatov <egori@altlinux.org> 1.0-alt1
- First build for ALT.
