# vim: set ft=spec: -*- rpm-spec -*-

%define plugname mail
%define plugtype after-ftplugin

Name: vim-plugin-%plugname-%plugtype
Version: 1.9
Release: alt2

Summary: FtPlugin for helping writing mail
Group: Editors
License: Distributable

Url: http://www.vim.org/scripts/script.php?script_id=99

Packager: VIm Plugins Development Team <vim-plugins@packages.altlinux.org>

BuildArch: noarch

Source: %plugname.tgz
Patch: %plugname-%version-%release.patch

BuildRequires(pre): rpm-build-vim

%description
This plugin's purpose is helping with mail editing.  It has two
major roles.  The first is email address retrievel and the second is
added functionality while editing.

To enable this plugin define "use_mail_after_ftplugin" variable somewhere
in your .vimrc file.

%prep
%setup -q -c
%patch -p1

%install
%__mkdir_p %buildroot%vim_doc_dir
%__mkdir_p %buildroot%vim_after_ftplugin_dir

%__install -m644 after/ftplugin/mail.vim %buildroot%vim_after_ftplugin_dir
%__install -m644 after/ftplugin/mail*.mod %buildroot%vim_after_ftplugin_dir
%__install -m644 doc/mail.txt %buildroot%vim_doc_dir

%files
%doc %vim_doc_dir/mail.txt
%vim_after_ftplugin_dir/mail.vim
%vim_after_ftplugin_dir/mail*.mod

%changelog
* Mon Nov 17 2008 Sir Raorn <raorn@altlinux.ru> 1.9-alt2
- Rebuilt with new rpm-build-vim
- Fixed function separator in module list (closes: #12899)

* Sat Jun 26 2004 Sir Raorn <raorn@altlinux.ru> 1.9-alt1.1
- Fixed buildarch

* Sat Jun 26 2004 Sir Raorn <raorn@altlinux.ru> 1.9-alt1
- Built for Sisyphus

