# vim: set ft=spec: -*- rpm-spec -*-

%define plugname vtreeexplorer
#define plugtype plugin

Name: vim-plugin-%plugname
Version: 1.24
Release: alt1

Summary: tree based file explorer within vim
Group: Editors
License: Distributable
Url: http://www.vim.org/scripts/script.php?script_id=184
Packager: VIm Plugins Development Team <vim-plugins@packages.altlinux.org>

BuildArch: noarch

Source: %plugname-%version.tar

Patch: %name-%version-%release.patch

PreReq: vim-common >= 4:6.3.007-alt1

BuildPreReq: vim-devel

%description
This is like the directory explorer plugin that ships with
vim, but instead of presenting just one directory at a time,
this plugin present portions of the filesystem hierarch in
a tree view.

To enable this plugin define "use_vtreeexplorer" variable somewhere
in your .vimrc file.

%prep
%setup -q -c
%patch -p1

%install
%__mkdir_p %buildroot{%vim_plugin_dir,%vim_doc_dir}
%__install -m644 doc/%plugname.txt %buildroot%vim_doc_dir
%__install -m644 plugin/%plugname.vim %buildroot%vim_plugin_dir

%post
%update_vimhelp

%postun
%clean_vimhelp

%files
%doc %vim_doc_dir/%plugname.txt
%vim_plugin_dir/%plugname.vim

%changelog
* Wed Dec 13 2006 Sir Raorn <raorn@altlinux.ru> 1.24-alt1
- [1.24]

* Sun Feb 05 2006 Sir Raorn <raorn@altlinux.ru> 1.23-alt1
- Built for Sisyphus

