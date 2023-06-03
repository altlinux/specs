%define _unpackaged_files_terminate_build 1
%define _stripped_files_terminate_build 1
%set_verify_elf_method strict,lint=relaxed

Name: example-zig
Summary: Example of packaging Zig program
Version: 1
Release: alt1
License: GPL-2.0-only
Group: Development/Other
Url: https://ziglearn.org/

Source: %name-%version.tar

# Only these architectures have Zig compiler working.
ExclusiveArch: %zig_arches

# Following packages are required to build.
BuildRequires(pre): rpm-macros-zig
BuildRequires: /proc
BuildRequires: zig

%description
%summary.

%prep
%setup

%build
%zig_build

%install
%zig_install

%check
%zig_test

# This is not required step for normal packaging, but run executable to
# ensure it's working. Also, this ensures the example package is correct.
PATH=%buildroot%_bindir
zig-example

%files
%_bindir/zig-example

%changelog
* Sat Jun 03 2023 Vitaly Chikunov <vt@altlinux.org> 1-alt1
- Build basic Zig program example.
