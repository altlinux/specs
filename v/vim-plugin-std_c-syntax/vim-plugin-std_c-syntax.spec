# vim: set ft=spec: -*- rpm-spec -*-
# $Id: vim-plugin-std_c-syntax,v 1.5 2005/08/13 10:05:00 raorn Exp $

%define plugname std_c
%define plugtype syntax

Name: vim-plugin-%plugname-%plugtype
Version: 12.5
Release: alt1

Summary: Standard C syntax highlight for vim
Group: Editors
License: Distributable
Url: http://www.eandem.co.uk/mrw/vim/syntax/
Packager: VIm Plugins Development Team <vim-plugins@packages.altlinux.org>

BuildArch: noarch

Source: %url/%plugname.zip

Patch: %name-%version-%release.patch

PreReq: vim-common >= 4:6.3.007-alt1

BuildRequires(pre): vim-devel

# Automatically added by buildreq on Thu Jun 24 2004 (-bi)
BuildRequires: unzip

%description
This syntax file is to highlight Standard C source code, and can be
confgured to highlight to the C89, C94, or C99 standard. This syntax
file is useful if you are developing portable Standard C code, so
that extensions that your compiler supports (such as C++ // comments
in C89) that may not be supported by another compiler are flagged as
errors. It is better to catch these problems at edit time than from
the overnight build.

To enable this plugin define "use_std_c_syntax" variable somewhere
in your .vimrc file.

%prep
%setup -T -c
%__unzip -Lqa %SOURCE0
%patch -p1

%install
%__mkdir_p %buildroot{%vim_syntax_dir,%vim_doc_dir}
%__install -m644 doc/std_c.txt %buildroot%vim_doc_dir
%__install -m644 syntax/c.vim %buildroot%vim_syntax_dir

%post
%update_vimhelp

%postun
%clean_vimhelp

%files
%doc %vim_doc_dir/std_c.txt
%vim_syntax_dir/c.vim

%changelog
* Wed Dec 13 2006 Sir Raorn <raorn@altlinux.ru> 12.5-alt1
- [12.5]

* Sat Aug 13 2005 Sir Raorn <raorn@altlinux.ru> 11.4-alt1
- [11.4]
- Added Packager: tag

* Sat Jun 26 2004 Sir Raorn <raorn@altlinux.ru> 10.8-alt1.2
- Fixed buildarch

* Fri Jun 25 2004 Sir Raorn <raorn@altlinux.ru> 10.8-alt1.1
- Fix Requires
- Mention "use_std_c_syntax" variable in description

* Thu Jun 24 2004 Sir Raorn <raorn@altlinux.ru> 10.8-alt1
- Built for Sisyphus


