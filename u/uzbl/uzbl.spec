Name: uzbl
Version: 20111001
Release: alt1.1

Group: Networking/WWW
License: GPL
Summary: The uzbl web interface tools

Packager: Vladislav Zavjalov <slazav@altlinux.org>


URL: http://www.uzbl.org

Source0: %name-%version.tar

BuildRequires: libwebkitgtk3-devel

%description
The uzbl web interface tools

%prep
%setup

%build
%make PREFIX=/usr DESTDIR=%buildroot

%install
%makeinstall PREFIX=/usr DESTDIR=%buildroot

# Uzbl installs many various files into
# /usr/share/uzbl. Let's move something to %_docdir:

mkdir -p -- %buildroot/%_docdir
mv -- %buildroot/%_datadir/uzbl/docs   %buildroot/%_docdir/uzbl

mkdir -p -- %buildroot/%_docdir/uzbl/examples
mv -- %buildroot/%_datadir/uzbl/examples/data/bookmarks\
      %buildroot/%_datadir/uzbl/examples/data/dforms\
      %buildroot/%_datadir/uzbl/examples/data/scripts\
        %buildroot/%_docdir/uzbl/examples/
rm -f -- %buildroot/%_datadir/uzbl/examples/uzbl-cookie-manager.c

# install vim syntax:
cp -r -- extras/vim %buildroot/%_datadir/vim

# make /usr/bin/uzbl symlink
ln -s -- uzbl-tabbed %buildroot/%_bindir/uzbl

%files
%_bindir/*
%_docdir/uzbl
%_datadir/uzbl
%_datadir/vim/ftplugin/uzbl.vim
%_datadir/vim/ftdetect/uzbl.vim
%_datadir/vim/syntax/uzbl.vim

%changelog
* Mon Nov 07 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 20111001-alt1.1
- Rebuild with Python-2.7

* Mon Oct 24 2011 Alexey Shabalin <shaba@altlinux.ru> 20111001-alt1
- 2011.10.01 release
- build with libwebkitgtk3

* Sun Dec 05 2010 Vladislav Zavjalov <slazav@altlinux.org> 20101125-alt1
- 2010.11.25 release
- install vim syntax files
- add /usr/bin/uzbl (symlink to uzbl-tabbed)

* Wed Oct 20 2010 Vladislav Zavjalov <slazav@altlinux.org> 20100805-alt1
- 2010.08.05 release

* Sat May 08 2010 Vladislav Zavjalov <slazav@altlinux.org> 20100410-alt1
- current upstream snapshot

* Tue Feb 09 2010 Vladislav Zavjalov <slazav@altlinux.org> 20100202-alt1
- current upstream snapshot

* Fri Jan 15 2010 Vladislav Zavjalov <slazav@altlinux.org> 20100115-alt1
- current upstream snapshot

* Fri Dec 25 2009 Vladislav Zavjalov <slazav@altlinux.org> 20091224-alt1
- current upstream snapshot
- move some files from _datadir/uzbl/examples/ to _docdir/usbl/examples
  (closes: #22613)

* Wed Dec 16 2009 Vladislav Zavjalov <slazav@altlinux.org> 20091216-alt1
- build current version

* Tue Dec 08 2009 Vladislav Zavjalov <slazav@altlinux.org> 20091206-alt1
- first build for Altlinux

