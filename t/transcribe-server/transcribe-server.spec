# SPDX-License-Identifier: GPL-2.0-only
%define _unpackaged_files_terminate_build 1
%define _stripped_files_terminate_build 1
%set_verify_elf_method strict,lint=relaxed,lfs=relaxed

Name: transcribe-server
Version: 0.0.4
Release: alt1

Summary: OpenAI-compatible speech-to-text server on top of transcribe.cpp
License: MIT
Group: Sound
Url: https://altlinux.space/shaba/transcribe-server
Vcs: https://altlinux.space/shaba/transcribe-server.git

# libtranscribe-devel (the link manifest this package builds against) is not
# built for i586 either.
ExcludeArch: %ix86

Source: %name-%version.tar
Source1: %name-%version-vendor.tar

# The soname dependency on libtranscribe.so.* is generated automatically, but
# the library itself is useless without an inference backend. The CPU one is
# stated explicitly here; transcribe.cpp-cuda or transcribe.cpp-vulkan are
# installed on top of it when a GPU is available.
Requires: transcribe.cpp-cpu

BuildRequires(pre): rpm-macros-rust
BuildRequires(pre): rpm-build-systemd
BuildRequires: rpm-build-rust
BuildRequires: libtranscribe-devel >= 0.2.0
# ffmpeg-sys-next generates its bindings with bindgen, which dlopens libclang;
# the "clang" metapackage does NOT pull it in, clang-devel does.
BuildRequires: clang-devel
# ffmpeg-next probes the libraries with the pkg-config crate.
BuildRequires: libavcodec-devel libavformat-devel
BuildRequires: libavutil-devel libswresample-devel

%description
transcribe-server exposes transcribe.cpp over an OpenAI-compatible HTTP API
(/v1/audio/transcriptions, /v1/models) plus a WebSocket streaming endpoint,
with optional Bearer API-key authentication and FFmpeg-based decoding of
arbitrary input containers.

Models are not provided. GGUF models can be downloaded from Hugging Face
(https://huggingface.co/handy-computer) and pointed at with -m/--model.

%prep
%setup -a1
%rust_prep

%build
export TRANSCRIBE_DIR=%prefix
# engine-transcribe is optional: the default build has only the fake engine.
%rust_build --features engine-transcribe
grep -qFx 'cargo:rerun-if-changed=%_libdir/transcribe-link.json' \
	target/release/build/transcribe-cpp-sys-*/output
! find target/release/build -name CMakeCache.txt | grep -q .

%install
%rust_install
# Parametric systemd template: one instance per /etc/transcribe/%%i.env file.
# The env files themselves are not packaged (as in llama.cpp): the admin writes
# them, and the optional per-instance %%i.api-keys, into %_sysconfdir/transcribe,
# starting from the commented example shipped as documentation (%%files).
install -Dpm644 packaging/%name@.service %buildroot%_unitdir/%name@.service
# Drop the upstream hint about putting a private install prefix on the loader
# path: here the library comes from libtranscribe0 in %_libdir.
sed -i '/^# Shared prefix /,/^#Environment=LD_LIBRARY_PATH=/d' \
	%buildroot%_unitdir/%name@.service
! grep -q LD_LIBRARY_PATH %buildroot%_unitdir/%name@.service
# An instance with no %%i.api-keys must still start (no keys configured means
# anonymous access, which matches the default 127.0.0.1 bind): SetCredential= is
# what systemd falls back to when LoadCredential= finds no file, and without it
# systemd refuses to start the instance. Its value must stay non-empty (a bare
# newline here) - systemd ignores an empty SetCredential= altogether.
grep -qxF 'SetCredential=api-keys:\n' %buildroot%_unitdir/%name@.service
install -dm755 %buildroot%_sysconfdir/transcribe
install -dm755 %buildroot%_localstatedir/transcribe/models

%check
# The integration tests need the dev-dependencies (reqwest + rustls), which are
# intentionally not vendored; run the built binary instead - that also proves it
# resolves libtranscribe.so.* from the system at run time.
%buildroot%_bindir/%name --version
%buildroot%_bindir/%name --help >/dev/null

%post
%post_systemd '%name@*.service'

%preun
%preun_systemd '%name@*.service'

%files
%define _customdocdir %_docdir/%name
%doc LICENSE README.md NEWS.md packaging/gigaam.env.example
%_bindir/%name
%_unitdir/%name@.service
%dir %_sysconfdir/transcribe
%dir %_localstatedir/transcribe
%dir %_localstatedir/transcribe/models

%changelog
* Thu Sep 03 2026 Alexey Shabalin <shaba@altlinux.org> 0.0.4-alt1
- Update to 0.0.4.

* Thu Jul 30 2026 Alexey Shabalin <shaba@altlinux.org> 0.0.1-alt1
- Initial build for ALT Sisyphus.
