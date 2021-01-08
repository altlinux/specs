%define _unpackaged_files_terminate_build 1

%def_with tests

Name: bear
Version: 3.0.7
Release: alt1

Summary: Tool that generates a compilation database for clang tooling

License: GPLv3
Group: Development/Tools
Url: https://github.com/rizsotto/Bear.git

Packager: Maxim Knyazev <mattaku@altlinux.org>

Source: %name-%version.tar

# Fedora ppl have submitted the patch to upstream:
# https://github.com/rizsotto/Bear/pull/348
# Good for them!
Patch1: fedora-bear.libexec-subdir.patch

BuildRequires(pre): rpm-macros-cmake
BuildRequires: cmake
%if_with tests
BuildRequires: ctest
%endif
BuildRequires: gcc-c++
#BuildRequires: clang
BuildRequires: libprotobuf-devel
BuildRequires: protobuf-compiler
BuildRequires: libgrpc++-devel
BuildRequires: grpc-plugins
BuildRequires: libsqlite3-devel
BuildRequires: libfmt-devel
BuildRequires: libspdlog-devel
BuildRequires: nlohmann-json-devel

%description
Build ear records the CLI flags passed to compilers for each translation unit
during the build and stores them in JSON format. The resulting database
describes how single compilation unit should be processed and can be used by
Clang tooling and other various tools.

Some build systems (e. g. Meson, CMake) can produce the command database by
themselves and do not require this tool. Others, including plain Make, do not.

%prep
%setup
%patch1 -p1

%build
%define _cmake_builddir %_target_platform
mkdir -p "%_cmake_builddir"
srcdir=.. # %%cmake does "pushd BUILD"
%cmake -S $srcdir -B "$srcdir/%_cmake_builddir"
cmake --build "%_cmake_builddir" --verbose -j%__nprocs

%install
DESTDIR=%buildroot cmake --install "%_cmake_builddir" --verbose

for i in CODE_OF_CONDUCT.md CONTRIBUTING.md COPYING INSTALL.md README.md; do
    rm -f %buildroot%_docdir/Bear/$i
done

%files
%define _libexecdir %_prefix/libexec
%_bindir/*
%_man1dir/*.1*
%_libexecdir/bear
%doc COPYING README.md

%changelog
* Wed Jan 27 2021 Arseny Maslennikov <arseny@altlinux.org> 3.0.7-alt1
- 2.4.3 -> 3.0.7.

* Fri Apr 10 2020 Maxim Knyazev <mattaku@altlinux.org> 2.4.3-alt1
- Initial build to Sisyphus
