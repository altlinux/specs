%global _unpackaged_files_terminate_build 1
%def_with check

Name: elio
Version: 1.11.2
Release: alt1
Summary: Snappy, batteries-included terminal file manager
License: MIT
Group: File tools
URL: https://elio-fm.github.io
VCS: https://github.com/elio-fm/elio

Source: %name-%version.tar
Source1: vendor.tar

ExcludeArch: %ix86

BuildRequires(pre): rpm-macros-rust
BuildRequires: rpm-build-rust

%if_with check
BuildRequires: 7-zip
BuildRequires: xz
%endif

Requires: 7-zip
Requires: ffmpeg
Requires: ffprobe

%description
Snappy, batteries-included terminal file manager with rich previews,
inline images, bulk actions, and trash support.

%prep
%setup -a 1
%rust_prep

%build
%rust_build

%install
%rust_install

%check
export RUST_TEST_THREADS=1
# skip failing test in hasher
%rust_test -- \
	--skip chooser_stdout_pipe_receives_only_selection \
	--skip nearby_audio_preview_prefetch_warms_adjacent_file_preview

%files
%_bindir/elio

%changelog
* Tue Aug 11 2026 Alexander Makeenkov <amakeenk@altlinux.org> 1.11.2-alt1
- Updated to version 1.11.2.

* Wed Jun 17 2026 Alexander Makeenkov <amakeenk@altlinux.org> 1.9.0-alt1
- Updated to version 1.9.0.

* Thu Jun 11 2026 Alexander Makeenkov <amakeenk@altlinux.org> 1.8.0-alt1
- Initial build for ALT.
