Name: sdcv
Version: 0.5.4
Release: alt1

Summary: A console version of StarDict the international dictionary

Group: System/Internationalization
License: GPLv2
Url: https://dushistov.github.io/sdcv/

Source: %name-%version.tar
Patch0: %name-t_interactive.patch
Patch1: %name-t_list.patch

BuildPreReq: rpm-macros-cmake
BuildRequires: gcc-c++
BuildRequires: cmake >= 3.5
BuildRequires: ctest >= 3.5
BuildRequires: jq
BuildRequires: zlib-devel
BuildRequires: libreadline-devel
BuildRequires: glib2-devel >= 2.36

%description
The console version of StarDict the cross-platform and international
dictionary.

%prep
%setup -q
# fix tests to run in isolated environment
%patch0 -p1
%patch1 -p1
# make output readable on dark terminals
sed -i 's/;34m/;36m/' src/libwrapper.cpp

%build
%cmake \
    -DENABLE_NLS=YES \
    -DWITH_READLINE=YES \
    -DBUILD_TESTS=YES

%cmake_build
%cmake_build --target lang

%install
%cmake_install
%find_lang %name

%check
pushd %_cmake__builddir
ctest
popd

%files -f %name.lang
%_bindir/*
%_man1dir/*
%_mandir/uk/man1/*

%changelog
* Fri Oct 28 2022 Andrew Savchenko <bircoph@altlinux.org> 0.5.4-alt1
- Version bump.

* Mon May 31 2021 Arseny Maslennikov <arseny@altlinux.org> 0.5.3-alt1.1
- NMU: spec: adapted to new cmake macros.

* Sat Apr 03 2021 Andrew Savchenko <bircoph@altlinux.org> 0.5.3-alt1
- Version bump.
- Use upstream patch for synonyms binsearch speedup.

* Sat Jan 5 2019 Andrew Savchenko <bircoph@altlinux.org> 0.5.2-alt2
- Run tests sequentially to avoid random failures due to race
  conditions between tests.

* Fri Aug 31 2018 Andrew Savchenko <bircoph@altlinux.org> 0.5.2-alt1
- Version bump, upstream relocated.
- Enable tests.

* Thu Dec 12 2013 Paul Wolneykien <manowar@altlinux.org> 0.5.0-alt1
- Freshed up to v0.5.0 with the help of cronbuild and update-source-functions.

* Thu Dec 12 2013 Paul Wolneykien <manowar@altlinux.org> 0.4.2-alt1
- Freshed up to v0.4.2 with the help of cronbuild and update-source-functions.

