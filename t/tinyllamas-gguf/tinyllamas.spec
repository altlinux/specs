# SPDX-License-Identifier: MIT
%define _unpackaged_files_terminate_build 1

Name: tinyllamas-gguf
Version: 0
Release: alt1
Summary: Llama 2 architecture model trained on the TinyStories dataset
License: MIT
Group: Toys
Url: https://huggingface.co/ggml-org/tiny-llamas/
# Converted model from https://huggingface.co/karpathy/tinyllamas/
BuildArch: noarch

Source: %name-%version.tar

%description
This is a Llama 2 architecture model [from the series] trained on the
TinyStories dataset, intended for use in the llama2.c project, then converted
into GGUF format purely for testing and fun.

%prep
%setup

%install
install -Dpm644 stories260K.gguf* -t %buildroot%_datadir/tinyllamas

%files
%_datadir/tinyllamas

%changelog
* Mon Jun 03 2024 Vitaly Chikunov <vt@altlinux.org> 0-alt1
- Import stories260K.gguf.
