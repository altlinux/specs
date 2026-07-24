%define _unpackaged_files_terminate_build 1
%set_verify_elf_method strict,lint=relaxed


Name: lmsasm
Version: 1.5.0
Release: alt1
Summary: Assembler for LEGO MINDSTORMS EV3
License: BSD-3-Clause
Group: Development/Tools
Url: https://github.com/ev3dev/lmsasm
ExclusiveArch: %go_arches

Source: %name-%version.tar

BuildRequires(pre): rpm-build-golang

%description
lmsasm compiles LEGO MINDSTORMS EV3 bytecode files (*.lms) into
VM executable files (*.rbf). Includes lmsgen for code generation
from bytecode definitions.

%prep
%setup

%build
export BUILDDIR="$PWD"
export GOPATH="%go_path"
%golang_build ./lmsasm
%golang_build ./lmsgen

%install
export BUILDDIR="$PWD"
export IGNORE_SOURCES=1
%golang_install

%check
%gotest ./...

%files
%_bindir/lmsasm
%_bindir/lmsgen
%doc LICENSE.txt README.md lmsasm/lmsasm.md lmsgen/lmsgen.md

%changelog
* Fri Jul 24 2026 Valentin Sokolov <sova@altlinux.org> 1.5.0-alt1
- Initial build for Sisyphus.

