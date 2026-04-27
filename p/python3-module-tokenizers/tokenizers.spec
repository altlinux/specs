%define pypi_name tokenizers
%define _unpackaged_files_terminate_build 1

%def_with check

Name:    python3-module-%pypi_name
Version: 0.22.2
Release: alt1

Summary: Fast State-of-the-Art Tokenizers for Python
License: Apache-2.0
Group:   Other
Url:     https://huggingface.co/docs/tokenizers/index
VCS:     https://github.com/huggingface/tokenizers

Source0: %name-%version.tar
Source1: %name-vendor-%version.tar
Patch0: %name-%version-alt.patch

BuildRequires(pre): rpm-build-rust
BuildRequires(pre): rpm-build-python3
BuildRequires(pre): rpm-macros-rust
BuildRequires: gcc-c++
BuildRequires: liboniguruma-devel
BuildRequires: python3-devel 
BuildRequires: python3-module-setuptools 
BuildRequires: python3-module-wheel 
BuildRequires: python3-module-maturin
%if_with check
BuildRequires: python3-module-pytest
BuildRequires: python3-module-requests
BuildRequires: python3-module-numpy
%endif

%description
Provides an implementation of today's most used tokenizers, with a focus on performance and versatility.

Main features:
- Train new vocabularies and tokenize, using today's most used tokenizers.
- Extremely fast (both training and tokenization), thanks to the Rust implementation. 
  Takes less than 20 seconds to tokenize a GB of text on a server's CPU.
- Easy to use, but also extremely versatile.
- Designed for research and production.
- Normalization comes with alignments tracking.
  It's always possible to get the part of the original sentence that corresponds to a given token.
- Does all the pre-processing: Truncate, Pad, add the special tokens your model needs.

%prep
%setup -a1
%autopatch -p1

cp -f bindings/python/vendor/Cargo.lock bindings/python/Cargo.lock
cd bindings/python
%rust_prep

%build
cd bindings/python
export CARGO_PROFILE_RELEASE_LTO=off
# Build vendored esaxx static library explicitly and link it into abi3 module.
mkdir -p build-esaxx
%__cxx $CXXFLAGS -fno-stack-protector -std=c++11 -c vendor/esaxx-rs/src/esaxx.cpp -Ivendor/esaxx-rs/src -o build-esaxx/esaxx.o
%__ar crs build-esaxx/libesaxx.a build-esaxx/esaxx.o
export RUSTFLAGS="${RUSTFLAGS:+$RUSTFLAGS } \
    -C link-arg=-Wl,--no-as-needed \
    -C link-arg=-Wl,--whole-archive \
    -C link-arg=$(pwd)/build-esaxx/libesaxx.a \
    -C link-arg=-Wl,--no-whole-archive \
    -C link-arg=-lonig \
    -C link-arg=-lstdc++"
%pyproject_build

%install
cd bindings/python
%pyproject_install

%check
cd bindings/python
%pyproject_run_pytest -q \
    tests/bindings \
    tests/implementations \
    --ignore=tests/test_serialization.py \
    --ignore=tests/documentation \
    --ignore=tests/bindings/test_encoding.py \
    --ignore=tests/bindings/test_models.py \
    --ignore=tests/bindings/test_processors.py \
    --ignore=tests/bindings/test_tokenizer.py \
    --ignore=tests/bindings/test_trainers.py \
    --ignore=tests/implementations/test_bert_wordpiece.py \
    --ignore=tests/implementations/test_byte_level_bpe.py \
    --ignore=tests/implementations/test_char_bpe.py

%files
%doc LICENSE
%doc bindings/python/README.md
%python3_sitelibdir/%pypi_name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}

%changelog
* Wed Apr 01 2026 Matvey Pyanov <sen@altlinux.org> 0.22.2-alt1
- First build for Alt.
