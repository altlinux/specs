# vim: set ft=spec: -*- rpm-spec -*-

%define plugname xmledit
%define plugtype ftplugin
%define plugver  65

Name: vim-plugin-%plugname-%plugtype
Version: %plugver
Release: alt1

Summary: A filetype plugin to help edit XML and SGML documents
Group: Editors
License: Distributable

Url: %vim_script_url 301

Packager: VIm Plugins Development Team <vim-plugins@packages.altlinux.org>

BuildArch: noarch

Source: xml.vim

PreReq: vim-common >= 4:6.3.007-alt1

BuildRequires(pre): vim-devel
BuildRequires: vim-console

%description
This script provides some convenience when editing XML (and some SGML
including HTML) formated documents. It allows you to jump to the
beginning or end of the tag block your cursor is in. '%' will jump
between '<' and '>' within the tag your cursor is in. When in insert
mode and you finish a tag (pressing '>') the tag will be completed. If
you press '>' twice it will complete the tag and place the cursor in
the middle of the tags on it's own line (helps with nested tags).

To enable this plugin define "use_xmledit_ftplugin" variable somewhere
in your .vimrc file.

%prep
%setup -q -c -T
%__mkdir_p {ftplugin,doc}
%__cp -p %_sourcedir/xml.vim ftplugin/

%build
%__cat <<EOS | /usr/bin/vim -E -s -X -N -n -i NONE -u NONE -U NONE
let use_xmledit_ftplugin = 1
edit ftplugin/xml.vim
normal zRgg
source %%
/^" Section: Doc installation/,/^" Mappings and Settings./-1 d
/^" Section: Documentation content/-1,/^=\{3,}\s\+END_DOC\C/+2 d
write!
quit!
EOS
# "

%install
%__mkdir_p %buildroot%vim_doc_dir
%__mkdir_p %buildroot%vim_ftplugin_dir

%__install -m644 ftplugin/xml.vim %buildroot%vim_ftplugin_dir
%__install -m644 doc/xml-plugin.txt %buildroot%vim_doc_dir

%post
%update_vimhelp

%postun
%clean_vimhelp

%files
%doc %vim_doc_dir/xml-plugin.txt
%vim_ftplugin_dir/xml.vim

%changelog
* Mon Mar 31 2008 Sir Raorn <raorn@altlinux.ru> 65-alt1
- [r65]
- Fixed url

* Tue Jul 19 2005 Sir Raorn <raorn@altlinux.ru> 1.29-alt1
- [1.29]

* Wed Aug 25 2004 Sir Raorn <raorn@altlinux.ru> 1.20-alt1
- Built for Sisyphus

