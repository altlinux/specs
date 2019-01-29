Name: vim-plugin-wmgraphviz
%define pname wmgraphviz.vim
Version: 1.2
Release: alt1
Url: http://vim-twiki.sourceforge.net/
License: GPL
Group: Editors
Source: v%version.tar.gz
BuildRequires(pre): rpm-build-vim

BuildArch: noarch

Summary: Vim plugin for Graphviz dot
%description
Features:
    Compiling: :GraphvizCompile
    Viewing: :GraphvizShow
    Interactive viewing + editing: :GraphvizInteractive
    Omnicompletion: <C-X><C-O>
    Quickfix window for errors and warnings
    Snippet support

%prep
%setup

%build
%install
mkdir -p %buildroot%vim_runtime_dir
cp -a doc ftplugin snippets test %buildroot%vim_runtime_dir

%files
%doc README*
%vim_runtime_dir/*/*

%changelog
* Tue Jan 29 2019 Fr. Br. George <george@altlinux.ru> 1.2-alt1
- Autobuild version bump to 1.2

* Tue Jan 29 2019 Fr. Br. George <george@altlinux.ru> 1.1-alt1
- Initiasl build from scratch

