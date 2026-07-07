%define _unpackaged_file_terminate_build 1

Name: caligula
Version: 0.5.0
Release: alt1

Summary: A user-friendly, lightweight TUI for disk imaging
License: GPL-3.0
Group: Other
URL: https://github.com/ifd3f/caligula
VCS: https://github.com/ifd3f/caligula

Source: %name-%version.tar
Source1: vendor.tar

ExcludeArch: i586

BuildRequires(pre): rpm-macros-rust
BuildRequires: rpm-build-rust

%description
Features:
- Cool graphs that show you how fast you're writing
- Listing attached disks, and telling you their size and hardware
model information
- Decompressing your input file for a variety of formats, including
gz, bz2, and xz
- Validating your input file against a hash before burning, with 
support for md5, sha1, sha256, and more!
- Running sudo/doas/su if you forgot to run as root earlier (it 
happens)
- Rich confirmation dialogs so you don't accidentally nuke your 
filesystem
- Verifying your disk after writing to make sure it was written 
correctly
- Small binary size of <5 megabytes, even when statically linked

%prep
%setup -a 1
%rust_prep

%build
%rust_build

%check
%rust_test

%install
%rust_install

%files
%_bindir/%name
%doc LICENSE

%changelog
* Mon Jul 06 2026 Vladislav Eliseev <general@altlinux.org> 0.5.0-alt1
- Initial build for Sisyphus.
