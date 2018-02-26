Version: 0.1
Release: alt4
Name: emacs-emhacks
License: GPL
Group: Editors
Url: http://sourceforge.net/projects/emhacks/
Packager: Emacs Maintainers Team <emacs@packages.altlinux.org>
Summary: Various hacks for Emacs, including tabbar
Requires: emacs-common 

Source: %name.tar.gz
Patch: recentf-emacs22.0-fix-1.patch
Patch1: tree-widget-images-path.patch
BuildArch: noarch

# Automatically added by buildreq on Tue Dec 24 2002
BuildRequires: emacs-common emacs-devel

#Also includes recentf.el and tree-widget.el,
#which are now part of emacs22

%description
Various hacks for Emacs including:
  gdiff.el -- Use a GUI diff tool from Emacs
  swbuff.el --- Quick switch between Emacs buffers
  tabbar.el --- Display a tab bar in the header line

%prep
%setup -n %name
%patch
%patch1

%build
rm overlay-fix.el tree-widget.el recentf.el
for i in tabbar.el swbuff.el gdiff.el ; do
  emacs -batch --eval "(progn (add-to-list 'load-path \".\") (byte-compile-file \"$i\"))"
done

%install
mkdir -p %buildroot%_emacslispdir/emhacks
install -m 644 {tabbar,swbuff,gdiff}.el* %buildroot%_emacslispdir/emhacks

#mkdir -p %buildroot%_emacs_etc_dir
#cp -r tree-widget-themes %buildroot%_emacs_etc_dir/tree-widget

mkdir -p %buildroot/etc/emacs/site-start.d
cat > %buildroot/etc/emacs/site-start.d/emhacks.el <<EOF
(add-to-list 'load-path "/usr/share/emacs/site-lisp/emhacks")
; obsolete overlay-fix removed from distribution
;(require 'overlay-fix)
; recentf and tree-widget are now part of emacs22
;(require 'recentf)
;(require 'tree-widget)
(require 'swbuff)
(require 'tabbar)
EOF

%files
%_emacslispdir/emhacks/
#%_emacs_etc_dir/tree-widget/
%config /etc/emacs/site-start.d/*
#config(noreplace) /etc/emacs/site-start.d/*

%changelog
* Thu Feb 23 2006 Igor Vlasenko <viy@altlinux.ru> 0.1-alt4
- removed recentf.el and tree-widget.el,
  which are now part of emacs22

* Wed Dec 14 2005 Igor Vlasenko <viy@altlinux.ru> 0.1-alt3
- site-start.d/emhacks.el cleanup:
  * removed (noreplace) as this can cause unworkable upgrade
  * moved to spec

* Thu Dec 08 2005 Igor Vlasenko <viy@altlinux.ru> 0.1-alt2
- spec cleanup: url, etc
- removed obsolete overlay-fix.el --- overlay bug workaround
- fixed no images bug in ecb --- installed images and added patch
- patched recentf to install menu item properly
- packager is set to Emacs Maintainers Team

* Sat Feb 21 2004 Ott Alex <ott@altlinux.ru> 0.1-alt1
- First build for ALTLinux

