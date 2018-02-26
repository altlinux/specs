Name: oneko
Version: 1.2
Release: alt4.qa1

Summary: Cat chases the cursor
License: Public Domain
Group: Toys
URL: http://www.daidouji.com/oneko/
# Modified Source to remove BSD images, due to copyright.
# Source0: http://www.daidouji.com/oneko/distfiles/oneko-1.2.sakura.5.tar.gz
Source0: oneko-1.2.sakura.5.noBSD.tar.gz
Source1: oneko.desktop
Source2: oneko.png

Patch0: oneko-1.2.sakura.5-nobsd.patch

Packager: Igor Zubkov <icesik@altlinux.org>

# Automatically added by buildreq on Tue Aug 04 2009
BuildRequires: gccmakedep imake libX11-devel libXext-devel xorg-cf-files
BuildRequires: desktop-file-utils

%description
A cat (neko) chases the cursor (now a mouse) around the screen while you 
work. Alternatively, a dog chases a bone.

%prep
%setup -q -n %name-%version.sakura.5
%patch0 -p1

%build
xmkmf -a
%make_build CFLAGS="%optflags -Dlinux -D_POSIX_C_SOURCE=199309L-D_POSIX_SOURCE -D_XOPEN_SOURCE -D_BSD_SOURCE -D_SVID_SOURCE -D_LARGEFILE_SOURCE -D_FILE_OFFSET_BITS=64 -DFUNCPROTO=15 -DNARROWPROTO -DSHAPE "

%install
%make_install DESTDIR=%buildroot install

mkdir -p %buildroot%_man1dir/
mkdir -p %buildroot%_mandir/ja/man1/
install -p -m0644 oneko.man %buildroot%_man1dir/oneko.1
install -p -m0644 oneko.man.jp %buildroot%_mandir/ja/man1/oneko.1
mkdir -p %buildroot%_datadir/applications/
mkdir -p %buildroot%_datadir/pixmaps/
install -p -m0644 %SOURCE1 %buildroot%_datadir/applications/
install -p -m0644 %SOURCE2 %buildroot%_datadir/pixmaps/
mv README README.jp
mv README-SUPP README-SUPP.jp
desktop-file-install --dir %buildroot%_desktopdir \
	--add-category=Amusement \
	%buildroot%_desktopdir/oneko.desktop

%files
%doc README.jp README-NEW README-SUPP.jp sample.resource
%_bindir/oneko
%_datadir/applications/oneko.desktop
%_datadir/pixmaps/oneko.png
%_mandir/ja/man1/*
%_man1dir/*

%changelog
* Tue May 17 2011 Repocop Q. A. Robot <repocop@altlinux.org> 1.2-alt4.qa1
- NMU (by repocop): the following fixes applied:
  * freedesktop-desktop-file-proposed-patch for oneko

* Tue Aug 04 2009 Igor Zubkov <icesik@altlinux.org> 1.2-alt4
- fix desktop file

* Tue Dec 02 2008 Igor Zubkov <icesik@altlinux.org> 1.2-alt3
- buildreq

* Sat Nov 15 2008 Igor Zubkov <icesik@altlinux.org> 1.2-alt2
- apply patch from repocop

* Thu Dec 06 2007 Igor Zubkov <icesik@altlinux.org> 1.2-alt1
- build for Sisyphus

* Thu Sep 14 2006 Tom "spot" Callaway <tcallawa@redhat.com> 1.2-4
- FC-6 rebuild

* Tue Mar  7 2006 Tom "spot" Callaway <tcallawa@redhat.com> 1.2-3
- remove includedir macro, not needed
- rename japanese man page to not have .jp extension

* Thu Jan 19 2006 Tom "spot" Callaway <tcallawa@redhat.com> 1.2-2
- use _includedir macro
- remove _i386_ hardcode
- fix blatant typo in patch
- rename docs to jp
- use -p for install
- remove xorg-x11-proto-devel, unnecessary

* Wed Jan 18 2006 Tom "spot" Callaway <tcallawa@redhat.com> 1.2-1
- Initial package for Fedora Extras
