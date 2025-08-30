# SPDX-License-Identifier: GPL-2.0-only
%define _unpackaged_files_terminate_build 1

%define neovim_runtime_dir %_datadir/nvim/runtime

%define plugname llama
Name: llama.vim
Version: 20250829
Release: alt1
Summary: Vim plugin for LLM-assisted code/text completion
License: MIT
Group: Other
Url: https://github.com/ggml-org/llama.vim
Packager: VIm Plugins Development Team <vim-plugins@packages.altlinux.org>
BuildArch: noarch

Source: %name-%version.tar
BuildRequires(pre): rpm-build-vim
%{?!_without_check:%{?!_disable_check:
BuildRequires: neovim-runtime
BuildRequires: vim-common
}}

%define descr_text \
%summary.\
The plugin requires FIM-compatible models, such as Qwen Coder model family.\
Currently recommended model is: Qwen 3 Coder 30B A3B Instruct\
\
The plugin could be enabled in .vimrc with:\
  let g:llama_config = { 'enable_at_startup': v:true }\
or interactively with :LlamaEnable command.\
See README.md for configuration details.

%description
%descr_text

%package -n vim-plugin-%plugname
Summary: %summary
Group: Editors
Requires(pre): vim-common >= 9.0.1
Requires: curl

%description -n vim-plugin-%plugname
%descr_text

%package -n neovim-plugin-%plugname
Summary: Neo%summary
Group: Editors
Requires(pre): neovim-runtime
Requires: curl

%description -n neovim-plugin-%plugname
%descr_text

%prep
%setup

%build
# Non the plugin-specific auto-generated file.
rm doc/tags

# It activates and interferes with the terminal even if there is no connection
# to the server, for example de-selecting the current line.
sed -i '/enable_at_startup/s/v:true/v:false/' autoload/llama.vim

%install
for t in %buildroot%vim_runtime_dir %buildroot%neovim_runtime_dir; do
	mkdir -pv $t
	cp -av autoload doc plugin -t $t
done

%check
set -o pipefail
# Experimental syntax check for .vim
! view -S autoload/%plugname.vim +:q </dev/null | sed -E 's/\x1b\[[^[:alpha:]]*[[:alpha:]]//g' | grep -99 Error || exit 1
! nvim -S autoload/%plugname.vim +:q </dev/null | sed -E 's/\x1b\[[^[:alpha:]]*[[:alpha:]]//g' | grep -99 Error || exit 1

%files -n vim-plugin-%plugname
%doc LICENSE README.md
%vim_runtime_dir/*/*

%files -n neovim-plugin-%plugname
%doc LICENSE README.md
%neovim_runtime_dir/*/*

%changelog
* Sat Aug 30 2025 Vitaly Chikunov <vt@altlinux.org> 20250829-alt1
- Experimental first import of commit 6aff02a (2025-08-29).
