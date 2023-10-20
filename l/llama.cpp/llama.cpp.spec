# SPDX-License-Identifier: GPL-2.0-only
%define _unpackaged_files_terminate_build 1
%define _stripped_files_terminate_build 1
%set_verify_elf_method strict

Name: llama.cpp
Version: 20231019
Release: alt1
Summary: Inference of LLaMA model in pure C/C++
License: MIT
Group: Sciences/Computer science
Url: https://github.com/ggerganov/llama.cpp

ExclusiveArch: aarch64 x86_64
Source: %name-%version.tar

AutoReqProv: nopython3
Requires: python3
Requires: python3(argparse)
Requires: python3(glob)
Requires: python3(os)
Requires: python3(pip)
Requires: python3(struct)

BuildRequires(pre): rpm-macros-cmake
BuildRequires: cmake
BuildRequires: ctest
BuildRequires: gcc-c++

%description
Plain C/C++ implementation (of inference of LLaMA model) without
dependencies. AVX, AVX2 and AVX512 support for x86 architectures.
Mixed F16/F32 precision. 2-bit, 3-bit, 4-bit, 5-bit, 6-bit and 8-bit
integer quantization support. Runs on the CPU. Supported models:

    LLaMA
    LLaMA 2
    Alpaca
    GPT4All
    Chinese LLaMA / Alpaca
    Vigogne (French)
    Vicuna
    Koala
    OpenBuddy (Multilingual)
    Pygmalion / Metharme
    WizardLM
    Baichuan 1 & 2 + derivations
    Aquila 1 & 2
    Starcoder models
    Mistral AI v0.1
    Refact
    Persimmon 8B
    MPT
    Bloom

NOTE 1: You will need to:

  pip3 install -r /usr/share/llama.cpp/requirements.txt

for data format conversion scripts to work.

NOTE 2:
  MODELS ARE NOT PROVIDED. You need to download them from original
  sites and place them into "./models" directory.

  For example, LLaMA downloaded via public torrent link is 220 GB.

Overall this is all raw and experimental, no warranty, no support.

%prep
%setup

%build
%cmake
%cmake_build
find -name '*.py' | xargs sed -i '1s|#!/usr/bin/env python3|#!%__python3|'
sed -i '1i\%__python3' convert-persimmon-to-gguf.py

%install
# Main format converter.
install -Dp convert.py %buildroot%_bindir/llama-convert
# Additional and experimental converters.
install -Dp convert-*.py -t %buildroot%_bindir
# Python requirements file.
install -Dpm644 requirements.txt -t %buildroot%_datadir/%name
# Additional data.
cp -rp prompts -t %buildroot%_datadir/%name
cp -rp grammars -t %buildroot%_datadir/%name
# Not all examples.
install -Dp examples/*.sh -t %buildroot%_datadir/%name/examples
# Install and rename binaries to have llama- prefix.
cd %_cmake__builddir/bin
find -maxdepth 1 -type f -executable -printf '%f\0' |
	xargs -0ti -n1 install -p {} %buildroot%_bindir/llama-{}

%check
%cmake_build --target test

%files
%define _customdocdir %_docdir/%name
%doc LICENSE README.md SHA256SUMS docs
%_bindir/llama-*
%_bindir/convert-*.py
%_datadir/%name

%changelog
* Fri Oct 20 2023 Vitaly Chikunov <vt@altlinux.org> 20231019-alt1
- Update to b1400 (2023-10-19).
- Install experimental converters (convert- prefixed tools).

* Sun Jul 30 2023 Vitaly Chikunov <vt@altlinux.org> 20230728-alt1
- Update to master-8a88e58 (2023-07-28).

* Sun May 14 2023 Vitaly Chikunov <vt@altlinux.org> 20230513-alt1
- Build master-bda4d7c (2023-05-13).

* Wed Apr 19 2023 Vitaly Chikunov <vt@altlinux.org> 20230419-alt1
- Build master-6667401 (2023-04-19).
