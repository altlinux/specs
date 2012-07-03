%define plugname loremipsum
%define plugver  0.2

Name: vim-plugin-%plugname
Version: %plugver
Release: alt1.git20090922

Summary: A dummy text generator
Group: Editors
License: GPL
Url: %vim_script_url 2289
BuildArch: noarch

# git://github.com/tomtom/vimtlib.git
Source: %name-%version-%release.tar

BuildRequires(pre): rpm-build-vim

Packager: VIm Plugins Development Team <vim-plugins@packages.altlinux.org>

%description
Insert a dummy text of a certain length. Actually, the text isn't
generated but selected from some text. By default, the following text is
used, which is included in the archive:
http://www.lorem-ipsum-dolor-sit-amet.com/lorem-ipsum-dolor-sit-amet.html

To enable this plugin define "use_loremipsum" variable somewhere
in your .vimrc file

%prep
%setup -n %name-%version-%release

%install
mkdir -p %buildroot{%vim_doc_dir,%vim_plugin_dir,%vim_autoload_dir}
install -p -m644 doc/loremipsum.txt %buildroot%vim_doc_dir/
install -p -m644 plugin/loremipsum.vim %buildroot%vim_plugin_dir/
install -p -m644 autoload/loremipsum.{vim,txt} %buildroot%vim_autoload_dir/

%files
%vim_doc_dir/*
%vim_plugin_dir/*
%vim_autoload_dir/*

%changelog
* Tue Sep 22 2009 Artem Zolochevskiy <azol@altlinux.ru> 0.2-alt1.git20090922
- initial build for Sisyphus
