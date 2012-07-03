# vim: set ft=spec: -*- rpm-spec -*-

%define plugname matchit
#define plugtype plugin

Name: vim-plugin-%plugname
Version: 1.13.2
Release: alt1

Summary: Extended "%%" matching
Group: Editors
License: Distributable
Url: http://www.vim.org/scripts/script.php?script_id=39

Packager: VIm Plugins Development Team <vim-plugins@packages.altlinux.org>

BuildArch: noarch

Source: %plugname.zip

Patch: %name-%version-%release.patch

PreReq: vim-common >= 4:6.3.007-alt1

BuildRequires(pre): vim-devel

# Automatically added by buildreq on Thu Jun 24 2004 (-bi)
BuildRequires: unzip

%description
In Vim, as in plain vi, the percent key, |%%|, jumps the cursor from
a brace, bracket, or paren to its match.  This can be configured
with the 'matchpairs' option.  The matchit plugin extends this in
several ways.

To enable this plugin define "use_matchit" variable somewhere
in your .vimrc file.

%prep
%setup -T -c
%__unzip -Lqa %SOURCE0
%patch -p1

%install
mkdir -p %buildroot{%vim_plugin_dir,%vim_doc_dir}
install -m644 doc/%plugname.txt %buildroot%vim_doc_dir
install -m644 plugin/%plugname.vim %buildroot%vim_plugin_dir

%post
%update_vimhelp

%postun
%clean_vimhelp

%files
%doc %vim_doc_dir/%plugname.txt
%vim_plugin_dir/%plugname.vim

%changelog
* Fri Feb 22 2008 Andrey Rahmatullin <wrar@altlinux.ru> 1.13.2-alt1
- 1.13.2
- spec cleanup

* Wed Dec 13 2006 Sir Raorn <raorn@altlinux.ru> 1.12-alt1
- [1.12]
- Added packager tag

* Sat Jun 26 2004 Sir Raorn <raorn@altlinux.ru> 1.9-alt1.1
- Fixed buildarch

* Fri Jun 25 2004 Sir Raorn <raorn@altlinux.ru> 1.9-alt1
- Built for Sisyphus

