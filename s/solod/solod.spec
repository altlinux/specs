%define _unpackaged_files_terminate_build 1
%define _stripped_files_terminate_build 1

%global import_path github.com/solod-dev/solod

Name: solod
Version: 0.4
Release: alt1

Summary: A subset of Go that translates to C11

License: BSD-3-Clause
Group: Development/Other
URL: https://solod.dev
VCS: https://github.com/solod-dev/solod

### ExclusiveArch: %go_arches
# We exclude the 386 goarch; the upstream test suite
# assumes int can fit 64-bit integer values throughout
# many of the tests. For the test suite to be ready
# for 32-bit architectures, notably different test
# implementations have to be maintained.
ExclusiveArch: x86_64 aarch64

BuildRequires(pre): rpm-macros-golang
BuildRequires: rpm-build-golang
BuildRequires: make

Source: %name-%version-%release.tar

%description
Solod is a strict subset of Go that translates to regular C.

Highlights:

    Go in, C out. You write regular Go code and get readable C11 as output.
    Zero runtime. No garbage collection, no reference counting, no hidden allocations.
    Rich standard library. Use familiar types and functions ported from Go's stdlib.
    Native C interop. Call C from Solod and Solod from C; no CGO, no overhead.
    Go tooling works out of the box. Syntax highlighting, LSP, linting and modules.

Solod supports structs, methods, interfaces, slices, maps, multiple returns, and defer.
Everything is stack-allocated by default; heap is opt-in through the standard library.
There is limited support for generics, and concurrency is provided by the standard library
instead of being built into the language.

Solod is for C programmers who like Go's safety, structure, and tooling.

%prep
%setup -n %name-%version-%release

%build
export IGNORE_SOURCES=1
export BUILDDIR="$PWD/.build"
%golang_build cmd/so

%install
export IGNORE_SOURCES=1
export BUILDDIR="$PWD/.build"
%golang_install

%check
export IGNORE_SOURCES=1
export BUILDDIR="$PWD/.build"
make test

%files
%_bindir/so

%changelog
* Mon Oct 12 2026 Arseny Maslennikov <arseny@altlinux.org> 0.4-alt1
- Initial build for ALT Sisyphus.
