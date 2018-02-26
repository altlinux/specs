Name: vim-plugin-deldiff
Version: 0.1
Release: alt1

Summary: VIm plugin for deleting unified diff blocks
Group: Editors
License: Distributable
Url: %vim_script_url 444
BuildArch: noarch

Source0: deldiff.vim
Patch0: %name-0.1-alt-disable-default.patch

PreReq: vim-common >= 4:6.3.007-alt1
BuildPreReq: vim-devel

Packager: VIm Plugins Development Team <vim-plugins@packages.altlinux.org>

%description
This script provides "did" and "dad" which work like "dib" or "dip" but
for unified diffs.

To enable this plugin define "use_deldiff_plugin" variable somewhere
in your .vimrc file.

%prep
%setup -cT
cp %SOURCE0 .
%patch0 -p0

%install
mkdir -p %buildroot%vim_plugin_dir
install -m644 deldiff.vim %buildroot%vim_plugin_dir

%files
%vim_plugin_dir/deldiff.vim

%changelog
* Thu Feb 22 2007 Andrey Rahmatullin <wrar@altlinux.ru> 0.1-alt1
- initial build
