%define plugname python
%define plugtype after-ftplugin
%define plugver  1.13

Name: vim-plugin-%plugname-%plugtype
Version: %plugver
Release: alt1

Summary: VIm plugin for easier editing of python scripts
Group: Editors
License: Distributable
Url: %vim_script_url 30
BuildArch: noarch

Source: python_fn.vim
Patch: %name-1.13-alt-disable-default.patch

PreReq: vim-common >= 4:6.3.007-alt1
BuildPreReq: vim-devel

Packager: VIm Plugins Development Team <vim-plugins@packages.altlinux.org>

%description
This script can be useful when editing Python scripts. It provides the
following menus:

- Select a block of lines with the same indentation
- Select a function
- Select a class
- Go to previous/next class/function
- Go to the beginning/end of a block
- Comment the selection
- Uncomment the selection
- Jump to the last/next line with the same indent
- Shift a block (left/right)

To enable this plugin define "use_python_after_ftplugin" variable somewhere
in your .vimrc file.

%prep
%setup -cT
cp %SOURCE0 .
%patch -p0

%install
mkdir -p %buildroot%vim_after_ftplugin_dir
install -m644 python_fn.vim %buildroot%vim_after_ftplugin_dir

%files
%vim_after_ftplugin_dir/python_fn.vim

%changelog
* Wed Oct 08 2008 Andrey Rahmatullin <wrar@altlinux.ru> 1.13-alt1
- 1.13

* Wed Dec 13 2006 Andrey Rahmatullin <wrar@altlinux.ru> 1.11-alt1
- 1.11

* Sat Oct 22 2005 Andrey Rahmatullin <wrar@altlinux.ru> 1.7-alt1
- initial build
