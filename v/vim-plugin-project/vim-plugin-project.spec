%define plugname project
%define plugver  1.3

Name: vim-plugin-%plugname
Version: %plugver
Release: alt1

Summary: Project plugin 
Group: Editors
License: Distributable
Url: %vim_script_url 69
BuildArch: noarch

Source: %{plugname}-%{plugver}.tar.gz

PreReq: vim-common >= 4:6.3.007-alt1
BuildPreReq: vim-devel

Packager: VIm Plugins Development Team <vim-plugins@packages.altlinux.org>

%post
%update_vimhelp

%postun
%clean_vimhelp

%description
You can use this plugin's basic functionality to set up a list of
frequently-accessed files for easy navigation. The list of files
will be displayed in a window on the left side of the Vim
window, and you can press <Return> or double-click on
filenames in the list to open the files. This is similar to how
some IDEs I've used work. I find this easier to use than
having to navigate a directory hierarchy with the file-explorer.
It also obviates the need for a buffer explorer because you
have your list of files on the left of the Vim Window.

%prep
%setup -c

%install
%__mkdir_p %buildroot%vim_runtime_dir
%__cp -a {doc,plugin} %buildroot%vim_runtime_dir

%files
%vim_doc_dir/*
%vim_plugin_dir/*

%changelog
* Wed Jul 06 2005 Kirill A. Shutemov <kas@altlinux.ru> 1.3-alt1
- inital build

