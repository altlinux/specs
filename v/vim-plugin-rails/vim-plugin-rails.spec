# vim: set ft=spec: -*- rpm-spec -*-

%define plugname rails

Name: vim-plugin-%plugname
Version: 2.0
Release: alt1
Serial: 1

Summary: Ruby on Rails: easy file navigation, enhanced syntax highlighting, and more
Group: Editors
License: Charityware (Vim)
Url: http://rails.vim.tpope.net/

Packager: VIm Plugins Development Team <vim-plugins@packages.altlinux.org>

BuildArch: noarch

Source: %plugname-%version.tar
Patch: %name-%version-%release.patch

PreReq: vim-common >= 4:6.3.007-alt1

BuildRequires(pre): vim-devel

%description
TextMate may be the latest craze for developing Ruby on Rails applications,
but Vim is forever.  This plugin offers the following features for Ruby on
Rails application development:

* Automatically detects buffers containing files from Rails applications,
* Unintrusive.
* Provides reasonable settings for working with Rails applications.
* Easy navigation of the Rails directory structure.
* Enhanced syntax highlighting.
* Interface to script/*.
* Partial extraction and migration inversion.
* Integration with other plugins.

To enable this plugin define "use_rails_plugin" variable somewhere
in your .vimrc file.

%prep
%setup -n %plugname-%version
%patch -p1

%install
%__mkdir_p %buildroot%vim_runtime_dir
%__cp -rvp {autoload,doc,plugin} %buildroot%vim_runtime_dir

%post
%update_vimhelp

%postun
%clean_vimhelp

%files
%vim_autoload_dir/*
%vim_doc_dir/*
%vim_plugin_dir/*

%changelog
* Sun Jul 13 2008 Sir Raorn <raorn@altlinux.ru> 1:2.0-alt1
- Updated to v2.0-3-gb4f93c4 (Rails 2.1 support)

* Wed Dec 13 2006 Sir Raorn <raorn@altlinux.ru> 132-alt1
- [132]

* Mon Sep 25 2006 Sir Raorn <raorn@altlinux.ru> 128-alt2
- Removed dependencies on rails and rake

* Mon Sep 25 2006 Sir Raorn <raorn@altlinux.ru> 128-alt1
- Built for Sisyphus

