Name:    peel-cli
Version: 0.8.0
Release: alt1

Summary: Parallel file downloader with streaming archive extraction
License: Apache-2.0
Group:   Networking/File transfer
URL:     https://agouin.github.io/peel/
VCS:     https://github.com/agouin/peel

Source0: %name-%version.tar
Source1: vendor.tar

Patch0:  peel-i586-fallocate.patch

BuildRequires(pre): rpm-macros-rust
BuildRequires: rpm-build-rust

%description
Peel is a command-line tool for downloading files and extracting archives. It
downloads multiple byte ranges in parallel and can extract an archive while the
download is still in progress.

Peel can resume downloads after a connection drops or the process is killed.
During streaming extraction, it reclaims disk space occupied by archive data it
has already processed. It can also keep the original archive or download it
without extracting it.

Supported formats include tar, ZIP, 7z, and RAR, as well as compression formats
such as Zstandard, XZ, LZ4, gzip, and bzip2.

%prep
%setup -a1
%autopatch -p1
%rust_prep

%build
%rust_build

%install
%rust_install peel

%check
%rust_test

%files
%_bindir/peel

%changelog
* Fri Nov 13 2026 Evgeniy Serov <scala@altlinux.org> 0.8.0-alt1
- Initial build for Sisyphus (Closes: #60607).
