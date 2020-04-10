Name: bear
Version: 2.4.3
Release: alt1

Summary: Tool that generates a compilation database for clang tooling

License: GPLv3
Group: Databases
Url: https://github.com/rizsotto/Bear.git

Packager: Maxim Knyazev <mattaku@altlinux.org>

Source: %name-%version.tar

BuildRequires(pre): rpm-macros-cmake
BuildRequires: cmake
BuildRequires: gcc-c++
BuildRequires: clang
BuildRequires: bash-completion-cmake
BuildRequires: bash-completion

%description
Build ear produces compilation database in JSON format. This database describes
how single compilation unit should be processed and can be used by Clang
tooling.

%prep
%setup

%build
%cmake_insource
%make_build

%install
%makeinstall_std

%files
%_bindir/bear
%_datadir/bash-completion/
%_man1dir/bear.1*
%_libdir/bear/
%_datadir/doc/bear
%doc COPYING ChangeLog.md README.md

%changelog
* Fri Apr 10 2020 Maxim Knyazev <mattaku@altlinux.org> 2.4.3-alt1
- Initial build to Sisyphus
