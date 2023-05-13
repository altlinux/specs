# SPDX-License-Identifier: GPL-2.0-only
%define _unpackaged_files_terminate_build 1
%define _stripped_files_terminate_build 1
%set_verify_elf_method strict

Name: llama.cpp
Version: 20230513
Release: alt1
Summary: Inference of LLaMA model in pure C/C++
License: MIT
Group: Sciences/Computer science
Url: https://github.com/ggerganov/llama.cpp

ExclusiveArch: aarch64 x86_64 %e2k
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
dependencies. AVX2 support for x86 architectures. Mixed F16 / F32
precision. 4-bit quantization support. Runs on the CPU.

Note 1: You will need to:

  pip3 install -r /usr/share/llama.cpp/requirements.txt

for data format conversion scripts to work.

Note 2:
  MODELS ARE NOT PROVIDED. You need to download them from original
  sites and place them into local model/ directory.

  For example, LLaMA downloaded via public torrent link is 220 GB.

Overall this is all raw and experimental, no warranty, no support.

%prep
%setup

%build
%cmake
%cmake_build

%install
mkdir -p %buildroot%_bindir
echo "#!%__python3" > %buildroot%_bindir/llama-convert
cat convert.py >> %buildroot%_bindir/llama-convert
chmod a+rx %buildroot%_bindir/llama-convert

mkdir -p %buildroot%_datadir/%name
install -pm644 requirements.txt -t %buildroot%_datadir/%name
cp -rp prompts -t %buildroot%_datadir/%name

mkdir -p %buildroot%_datadir/%name/examples
cp -p examples/*.sh -t %buildroot%_datadir/%name/examples

cd %_cmake__builddir/bin
install -p main       %buildroot%_bindir/llama-main
install -p embedding  %buildroot%_bindir/llama-embedding
install -p perplexity %buildroot%_bindir/llama-perplexity
install -p quantize   %buildroot%_bindir/llama-quantize

%define _customdocdir %_docdir/%name

%check
%cmake_build --target test

%files
%doc LICENSE README.md
%_bindir/llama-*
%_datadir/%name

%changelog
* Sun May 14 2023 Vitaly Chikunov <vt@altlinux.org> 20230513-alt1
- Build master-bda4d7c (2023-05-13).

* Wed Apr 19 2023 Vitaly Chikunov <vt@altlinux.org> 20230419-alt1
- Build master-6667401 (2023-04-19).
