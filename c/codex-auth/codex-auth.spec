%define _unpackaged_files_terminate_build 1
%define _stripped_files_terminate_build 1
%set_verify_elf_method strict,lint=relaxed

# codex-auth has no external Zig dependencies.
# Without this override rpm-macros-zig expects a zig-pkg directory.
%global _zig_system_integration %nil

Name: codex-auth
Version: 0.3.0
Release: alt1

Summary: Command-line tool for switching Codex accounts
License: MIT
Group: Development/Other
URL: https://github.com/Loongphy/codex-auth
VCS: https://github.com/Loongphy/codex-auth

Source: %name-%version.tar

# Build only on architectures supported by the Zig toolchain in ALT.
ExclusiveArch: %zig_arches

BuildRequires(pre): rpm-macros-zig
BuildRequires: zig >= 0.16.0
BuildRequires: glibc-devel

Requires: curl

# Disable API requests in remove tests when the isolated build
# environment has no network access.
Patch0: %name-%version-alt-offline-tests.patch

# Preserve UTF-8 boundaries when measuring and truncating table cells.
Patch1: %name-%version-alt-fix-unicode.patch

%description
codex-auth is a command-line tool for managing and switching
between Codex accounts.

%prep
%setup
%autopatch -p1

%build
%zig_build

%install
%zig_install

%check
%zig_test

%files
%_bindir/%name
%doc LICENSE README.md CHANGELOG.md

%changelog
* Thu Sep 24 2026 Pavel Khromov <hromovpi@altlinux.org> 0.3.0-alt1
- Initial build for ALT Sisyphus. 

