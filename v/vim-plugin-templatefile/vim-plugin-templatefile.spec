%define plugname templatefile
Name: vim-plugin-%plugname
Version: 1.5
Release: alt4

Summary: loads template file when you edit new files
License: Distributable
Group: Editors
Url: %vim_script_url 198
BuildArch: noarch

Source: %plugname-%version.tar
Source1: skel.spec
Patch: templatefile-1.5-alt-disable-default.patch

BuildRequires(pre): vim-devel

Packager: VIm Plugins Development Team <vim-plugins at packages.altlinux.org>

%description
This plugin is for loading template files when editing new files.
A template file will be loaded if found, keywords in that template are
expanded, and/or a customized function for that type of files is called.

To enable this plugin define the "load_templates" variable
somewhere in your .vimrc file.

%prep
%setup -n %plugname-%version
%patch -p1

%install
%__mkdir_p %buildroot%vim_runtime_dir
%__cp -a vim/plugin %buildroot%vim_runtime_dir
%__cp -a vim/templates %buildroot%vim_dir
%__cp %SOURCE1 %buildroot%vim_dir/templates/

%files
%vim_dir/templates
%vim_plugin_dir/*

%changelog
* Thu Aug 02 2007 Alex V. Myltsev <avm@altlinux.ru> 1.5-alt4
- fixes for the spec template:
- - try to guess Name from filename
- - remove translated Summary/%description headers
- - default to .tar instead of .tar.bz2

* Mon Aug 29 2005 Alex V. Myltsev <avm@altlinux.ru> 1.5-alt3
- Added a template for RPM spec files.

* Sat May 07 2005 Alex V. Myltsev <avm@altlinux.ru> 1.5-alt2
- Moved the default templates so the plugin can find them.

* Fri May 06 2005 Alex V. Myltsev <avm@altlinux.ru> 1.5-alt1
- Initial build for ALT Linux.
