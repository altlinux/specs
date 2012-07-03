Name: kasablanca
Version: 0.4.0.2
Release: alt1.2.1.qa3

Summary: Kasablanca - a graphical ftp client for kde.
License: GPL
Group: Networking/File transfer
Url: http://kasablanca.berlios.de/
Packager: Ilya Mashkin <oddity at altlinux dot ru>

Source0: %name-%version.tar.gz
Source1: %name.menu
Patch0: %name-0.4.0.2-alt-DSO.patch
BuildRequires(pre): kdelibs-devel
BuildRequires: gcc-c++ libjpeg-devel libpng-devel libssl-devel xml-utils zlib-devel

%description
Kasablanca is  a graphical ftp client for kde. Among its features are support
for ssl/tls encryption (both commands and data using auth tls, not sftp), fxp
(direct ftp to ftp transfer) bookmarks, and queues.

%description -l ru_RU.KOI8-R
Kasablanca - графический клиент программы передачи файлов для kde. 
Среди его особенностей - поддержка ssl/tls шифрования, fxp 
(прямая передача файлов с ftp на ftp), закладки, и списки очередей.

%prep
%setup -q
%patch0 -p2

%__subst 's,\.la,\.so,' configure 
%__subst 's/\(-Wl,--no-undefined\)/-Wl,--warn-unresolved-symbols \1/g' configure
%__subst 's/\-lkdeui/-lkdeui -lpthread/g' configure

%build
%add_optflags -I%_includedir/tqtinterface
%K3configure --disable-rpath --disable-arts
%set_verify_elf_method textrel=relaxed
%make_build

%install
%K3install

#menu
%__mkdir_p %buildroot%_menudir
%__install -pD -m644 %SOURCE1 %buildroot%_menudir/%name

%K3find_lang %name

%files -f %name.lang
%doc AUTHORS ChangeLog README TODO
%_K3bindir/%name
%_K3apps/%name/
%_menudir/%name

%_K3applnk/Utilities/kasablanca.desktop
%_K3cfg/kbconfig.kcfg
%doc %_K3doc/en/%name
%_K3datadir/icons/*/*/apps/%name.png

%changelog
* Wed Jun 13 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.4.0.2-alt1.2.1.qa3
- Fixed build

* Thu May 05 2011 Andrey Cherepanov <cas@altlinux.org> 0.4.0.2-alt1.2.1.qa2
- Remove excessive build requires

* Tue Dec 07 2010 Igor Vlasenko <viy@altlinux.ru> 0.4.0.2-alt1.2.1.qa1.1
- rebuild with new openssl and/or boost by request of git.alt administrator

* Mon Dec 07 2009 Repocop Q. A. Robot <repocop@altlinux.org> 0.4.0.2-alt1.2.1.qa1
- NMU (by repocop): the following fixes applied:
  * update_menus for kasablanca
  * postclean-05-filetriggers for spec file

* Sat Aug 09 2008 ALT QA Team Robot <qa-robot@altlinux.org> 0.4.0.2-alt1.2.1
- Automated rebuild due to libssl.so.6 -> libssl.so.7 soname change.

* Tue May 27 2008 Ilya Mashkin <oddity at altlinux dot ru> 0.4.0.2-alt1.2
- spec cleanup

* Wed Feb 02 2005 Ilya Mashkin <oddity at altlinux dot ru> 0.4.0.2-alt1
- new version with several small improvements

* Mon Jan 10 2005 Ilya Mashkin <oddity at altlinux dot ru> 0.4.0.1-alt2
- fix Group (#5179)
- little spec cleanup

* Wed Aug 19 2004 Dmitriy Porollo <spider@altlinux.ru> 0.4.0.1-alt1
- 0.4.0.1-alt1 -changed: reduced cpu quite a bit again
- 0.4.0.1-alt1 -added: status tooltip for systray icon
- 0.4.0.1-alt1 -fixed: correct-pasv bug
- 0.4.0.1-alt1 -fixed: evil flaw in local delete method, added option to move 
- 0.4.0.1-alt1 -files into trash instead
- 0.4.0.1-alt1 -added: import gftp bookmarks [crissi] 
- 0.4.0.1-alt1 -added: polish translation [tomwal]
- 0.4.0.1-alt1 -fixed: compilation error
- 0.4.0.1-alt1 -fixed: filesize issues, files bigger than 2GB should be supported now
- 0.4.0.1-alt1 -changed: some changes to the bookmark editor
- 0.4.0.1-alt1 -changed: improved directory caching
- 0.4.0.1-alt1 -added: auto-completion in the lineedits
- 0.4.0.1-alt1 -changed: items are queued at the end of the queue list now
- 0.4.0.1-alt1 -changed: remember sorting preference when changing directories
- 0.4.0.1-alt1 -changed: report when ftp servers do not support encryption
- 0.4.0.1-alt1 -fixed: crash when trying to remove active item from queue
- 0.4.0.1-alt1 -fixed: compilation with gcc 2.95

* Fri Aug 13 2004 Dmitriy Porollo <spider@altlinux.ru> 0.4-alt1
- 0.4-alt1 -added german translation
- 0.4-alt1 -directory caching added
- 0.4-alt1 -added documentation and help buttons
- 0.4-alt1 -added bookmark current site option
- 0.4-alt1 -option to hide hidden files from view
- 0.4-alt1 -priority list functionality implemented
- 0.4-alt1 -added advanced settings to custom sites
- 0.4-alt1 -bookmarks can be re-arranged now
- 0.4-alt1 -rewrote bookmark implementation
- 0.4-alt1 -representation of sitenames in statusbar
