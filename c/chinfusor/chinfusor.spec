%define _unpackaged_files_terminate_build 1

Name:    chinfusor
Version: 1.2
Release: alt1

Summary: A speech dispatcher module allowing to correctly read texts written in multiple alphabets.
License: MIT
Group:   Sound
Url:     https://github.com/RastislavKish/Chinfusor
VCS:     https://github.com/RastislavKish/Chinfusor

Source: %name-%version.tar
Patch0: lib64.patch

Requires: speech-dispatcher

BuildRequires(pre): rpm-build-rust
BuildRequires: /proc
BuildRequires: libspeechd-devel
BuildRequires: clang-devel
BuildRequires: llvm-devel

%description
When one wants to learn a new language, or simply use a language other than his native, the very basic ability required in order to do so is to be able to read text written in the particular language. And while this is quite easy for latin-based languages, which can be read simply as they are, the situation gets much more complicated, when trying to read texts written in other alphabets.


%prep
%setup

pushd src
pushd sd_chinfusor
mkdir -p .cargo
cat >> .cargo/config <<EOF
[source.crates-io]
replace-with = "vendored-sources"

[source.vendored-sources]
directory = "vendor"
EOF
popd
popd

%if "%_lib" == "lib64"
%patch0 -p1
%endif

%build
pushd src
pushd sd_chinfusor
%rust_build
popd
popd

%install
pushd src
pushd sd_chinfusor
install -D -m 755 target/release/sd_%name %buildroot%_libdir/speech-dispatcher-modules/sd_%name
popd
popd

%check
pushd src
pushd sd_chinfusor
%rust_test
popd
popd

%files
%doc *.md LICENSE
%_libdir/speech-dispatcher-modules/sd_%name

%changelog
* Thu Jan 16 2025 Artem Semenov <savoptik@altlinux.org> 1.2-alt1
- Initial build for Sisyphus (Closes: #52270)
