%define _unpackaged_files_terminate_build 1

Name: hsh-svace
Version: 1.3
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
install -Dm755 ./hsh-svace-svacer-import -t %buildroot%_bindir

%files
%doc README.md LICENSE
%_bindir/hsh-svace
%_bindir/hsh-svace-svacer-import
%dir %_libexecdir/hsh-svace
%_libexecdir/hsh-svace/*

%changelog
* Tue Oct 15 2024 Egor Ignatov <egori@altlinux.org> 1.3-alt1
- Add --apt-config option.

* Tue Oct 15 2024 Egor Ignatov <egori@altlinux.org> 1.2-alt1
- Add hsh-svace-svacer-import script.

* Tue Oct 15 2024 Egor Ignatov <egori@altlinux.org> 1.1-alt1
- Output the results as a tar archive.
- Use required mountpoints for build and analysis.

* Wed Oct 09 2024 Egor Ignatov <egori@altlinux.org> 1.0-alt1
- First build for ALT.
