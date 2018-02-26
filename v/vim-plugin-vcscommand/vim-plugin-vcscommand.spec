%define plugname vcscommand
%define plugver  1.99.40

Name: vim-plugin-%plugname
Version: %plugver
Release: alt1
Epoch: 1

Summary: CVS/SVN/SVK/git/bzr/hg integration plugin
Group: Editors
License: Distributable
Url: %vim_script_url 90

Packager: VIm Plugins Development Team <vim-plugins@packages.altlinux.org>

BuildArch: noarch

Source: %name-%version.tar
Patch: %name-%version-%release.patch

PreReq: vim-common >= 4:7.0

BuildRequires(pre): vim-devel

Obsoletes: vim-plugin-cvscommand
Provides: vim-plugin-cvscommand
Obsoletes: vim-plugin-svncommand
Provides: vim-plugin-svncommand

%description
VIM 7 plugin useful for manipulating files controlled by CVS, SVN, SVK,
git, bzr, and hg within VIM, including committing changes and performing
diffs using the vimdiff system.

To enable this plugin define "use_vcscommand" variable somewhere
in your .vimrc file.

%prep
%setup
%patch -p1

%install
mkdir -p %buildroot{%vim_doc_dir,%vim_syntax_dir,%vim_plugin_dir}
install -p -m644 doc/* %buildroot%vim_doc_dir/
install -p -m644 plugin/* %buildroot%vim_plugin_dir/
install -p -m644 syntax/* %buildroot%vim_syntax_dir/

%files
%vim_doc_dir/*
%vim_plugin_dir/*
%vim_syntax_dir/*

%changelog
* Mon Jun 21 2010 Andrey Rahmatullin <wrar@altlinux.ru> 1:1.99.40-alt1
- 1.99.40

* Wed Mar 31 2010 Andrey Rahmatullin <wrar@altlinux.ru> 1:1.99.39-alt1
- 1.99.39

* Thu Aug 20 2009 Andrey Rahmatullin <wrar@altlinux.ru> 1:1.99.31-alt1
- 1.99.31

* Thu Feb 26 2009 Andrey Rahmatullin <wrar@altlinux.ru> beta29-alt1
- beta29
- remove obsolete macros

* Wed Oct 08 2008 Andrey Rahmatullin <wrar@altlinux.ru> beta28-alt1
- beta28

* Mon Sep 01 2008 Andrey Rahmatullin <wrar@altlinux.ru> beta27-alt1
- beta27

* Sat Jul 19 2008 Andrey Rahmatullin <wrar@altlinux.ru> beta26-alt1
- beta26

* Tue Jun 03 2008 Andrey Rahmatullin <wrar@altlinux.ru> beta25-alt1
- beta25

* Tue May 27 2008 Andrey Rahmatullin <wrar@altlinux.ru> beta24-alt1
- beta24

* Sat May 03 2008 Andrey Rahmatullin <wrar@altlinux.ru> beta22-alt1
- initial build
