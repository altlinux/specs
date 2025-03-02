%define _unpackaged_files_terminate_build 1

Name:    svn2git
Version: 1.0.18
Release: alt2

Summary: :octopus: A fast-import based converter for an svn repo to git repos
License: GPL-3.0
Group:   Other
Url:     https://github.com/svn-all-fast-export/svn2git

Source: %name-%version.tar
Patch: %name-%version-alt.patch

BuildRequires: qt5-base-devel
#BuildRequires: qtchooser
BuildRequires: git subversion bats bats-file bats-assert bats-support
BuildRequires: libapr1-devel
BuildRequires: libsubversion-devel
BuildRequires: /proc

%description
This project contains all the tools required to do a conversion of an svn repository (server side, not a checkout) to one or more git repositories.

%prep
%setup
%patch -p1
sed -i 's|/usr/local|%buildroot%prefix|g' src/src.pro

%build
%qmake_qt5 -o Makefile src/src.pro
%make_build

%install
%makeinstall_std

%check
sed -i 's|qmake|/usr/share/qt5/bin/qmake|g' test.sh
sed -i 's|libs|%_datadir|g' test/common.bash
sed -i 's|test/libs/bats-core/bin/bats|/usr/bin/bats|g' test.sh
./test.sh

%files
%_bindir/*
%doc *.md

%changelog
* Sun Mar 02 2025 Artem Semenov <savoptik@altlinux.org> 1.0.18-alt2
- enabled tests (thx Paul Wolneykien)

* Wed Feb 05 2025 Artem Semenov <savoptik@altlinux.org> 1.0.18-alt1
- Initial build for Sisyphus
