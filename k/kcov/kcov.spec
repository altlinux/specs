%ifarch %ix86 x86_64
%def_enable check
%else
%def_disable check
%endif

Name: kcov
Version: 38
Release: alt2
Summary: Code coverage tool without special compilation options

# Licenses of kcov itself and its bundled js libraries (see below)
License: GPLv2 and BSD and MIT
Url: https://simonkagstrom.github.io/%name
# Repacked https://github.com/SimonKagstrom/%name/archive/%version/%name-%version.tar.gz
Source: %name-%version.tar
Group: Development/Tools

# https://github.com/SimonKagstrom/kcov/blob/v35/src/solib-parser/lib.c#L87-L97
ExclusiveArch: %ix86 x86_64 %arm aarch64 ppc ppc64 ppc64le

# We do not allow use of biarch libraries in build environments.
Patch0: kcov-38-alt-drop-fork-32-test.patch

BuildRequires(pre): rpm-macros-cmake
BuildRequires(pre): rpm-macros-ninja-build
# Automatically added by buildreq on Thu May 07 2020
# optimized out: cmake-modules glibc-devel-static glibc-kernheaders-generic glibc-kernheaders-x86 libelf-devel libsasl2-3 libstdc++-devel pkg-config python2-base python3-base sh4 zlib-devel zlib-devel-static
BuildRequires: binutils-devel cmake gcc-c++ libcurl-devel libdw-devel ninja-build python3

# From fedora's specfile:
# NB: Last I tried to unbundle those dependencies I hit a first roadblock in
# the sense that all three were available in Fedora but packaged differently
# and none of the versions matched:
#
# - js-jquery.noarch (compat package js-jquery2.noarch too)
# - nodejs-handlebars.noarch
# - xstatic-jquery-tablesorter-common.noarch
#
# All three packages drop files in different locations, following different
# patterns. NodeJS modules in particular look a bit more involved.
#
# Since those dependencies are merely used to slightly improve static HTML
# reports, I'd rather not spend mindless efforts unbundling things that are
# not ultimately exposed by the package. They are embedded in the kcov(1)
# program and written by `html-writer.cc` as static strings.
#
# It would make more sense to unbundle those if they were used as libraries
# instead of just assets. Here it seems overkill. I'm registering them as
# bundled provides even though they don't appear as individual files to at
# least keep awareness of what I consider a non-issue.
#
# -- dridi

#Provides: bundled(handlebars) = 2.2.0
#Provides: bundled(jquery) = 2.1.1
#Provides: bundled(jquery-tablesorter) = 2.17.1

%description
Kcov is a code coverage tester for compiled programs, Python scripts and shell
scripts.  It allows collecting code coverage information from executables
without special command-line arguments, and continuously produces output from
long-running applications.

%prep
%setup
%patch -p1
rm -r external/ # remove LLDB headers bundled for MacOS

%build
%cmake \
	-G Ninja \
	-DKCOV_INSTALL_DOCDIR:STRING=%_docdir/%name-%version \
	#
%ninja_build -C BUILD

%if_enabled check
cmake -S tests -B build-tests -G Ninja
%ninja_build -C build-tests
%endif

cmake -S tools -B build-tools -G Ninja
%ninja_build -C build-tools

%install
%ninja_install -C BUILD

%check
tests/tools/run-tests BUILD/src/kcov /tmp $(pwd)/build-tests $(pwd) -v ||:

%files
%_bindir/*
%_mandir/man1/*
%_docdir/%name-%version

%changelog
* Thu May 07 2020 Gleb F-Malinovskiy <glebfm@altlinux.org> 38-alt2
- Initial build.
