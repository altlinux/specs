%def_disable debug
%def_with gui

%define githash ca0f365
%define Name Factor
Name: factor
Version: 0.92
Release: alt0.9.1
Summary: A general purpose, dynamically typed, stack-based programming language
License: %bsd
Group: Development/Other
URL: http://%{name}code.org
# http://gitweb.factorcode.org/gitweb.cgi?p=factor/.git;a=summary
# git clone git://factorcode.org/git/factor.git
%ifdef githash
Source0: %name-git-%githash.tar
%else
Source0: %name-%version.tar
%endif
Source1: %url/images/latest/boot.x86.32.image
Source2: %url/images/latest/boot.unix-x86.64.image
Source3: %url/images/latest/boot.linux-ppc.image
Source4: %url/images/latest.darcs/boot.arm.image
Source10: %name-faq.html
Patch: %name-%version-%release.patch
Provides: %Name = %version-%release
%{?_with_gui:Requires: fonts-ttf-vera}
Packager: Led <led@altlinux.ru>

BuildRequires(pre): rpm-build-licenses
BuildRequires: vim-devel %_bindir/emacs /proc
%{?_with_gui:BuildRequires: libX11-devel libfreetype-devel ImageMagick libGL-devel libGLU-devel}

%description
%Name is a general purpose, dynamically typed, stack-based programming
language.


%package -n vim-plugin-%name-syntax
Summary: VIm syntax for %Name
Group: Development/Other
BuildArch: noarch
Requires: vim-common

%description -n vim-plugin-%name-syntax
This package contains VIm syntax for %Name.


%package -n emacs-mode-%name
Summary: %Name mode for GNU Emacs
Group: Editors
BuildArch: noarch
Requires: emacs-base

%description -n emacs-mode-%name
%Name mode for GNU Emacs.


%package -n emacs-mode-%name-el
Summary: The Emacs Lisp sources for bytecode included in emacs-mode-%name
Group: Editors
BuildArch: noarch
Requires: emacs-base

%description -n emacs-mode-%name-el
The Emacs Lisp sources for bytecode included in emacs-mode-%name.


%prep
%setup %{?githash:-n %name-git-%githash}
%patch -p1
install %SOURCE10 ./faq.html
%ifarch %ix86
install -m 0644 %SOURCE1 ./boot.%_arch.image
%endif
%ifarch x86_64 k8 opteron nocona
install -m 0644 %SOURCE2 ./boot.%_arch.image
%endif
%ifarch ppc
install -m 0644 %SOURCE3 ./boot.%_arch.image
%endif
%ifarch arm
install -m 0644 %SOURCE4 ./boot.%_arch.image
%endif


%build
%define _optlevel 3
%make_build \
    SITE_CFLAGS="%optflags" \
    %{?_without_ui:NO_UI=1} \
    %{?_enable_debug:DEBUG=1} \
    LDFLAGS="-Wl,--no-as-needed"
./%name -i=boot.%_arch.image
%if_with gui
cat > %Name.desktop <<__MENU__
[Desktop Entry]
GenericName=%Name
Name=%Name
Exec=%Name
Icon=%Name
Type=Application
Terminal=false
Categories=Development;IDE;
__MENU__
for s in 96 72 64 36 24 22; do
    convert misc/icons/%{Name}_128x128.png -resize ${s}x$s -depth 8 misc/icons/%{Name}_${s}x$s.png
done
%endif
emacs -q --no-site-file -batch -f batch-byte-compile misc/%name.el


%install
install -D -m 0755 %name %buildroot%_bindir/%Name
install -D -m 0644 {,%buildroot%_libdir/%name/}%name.image
install -D -m 0644 {misc,%buildroot%vim_syntax_dir}/%name.vim
%if_with gui
install -D -m 0755 {,%buildroot%_desktopdir/}%Name.desktop
for s in 128 96 72 64 48 36 32 24 22 16; do
    install -D -m 0644 {misc/icons/%{Name}_${s}x$s,%buildroot%_iconsdir/hicolor/${s}x$s/apps/%Name}.png
done
ln -sf %_datadir/fonts/ttf/TrueType-vera %buildroot%_libdir/%name/fonts
%endif
install -d -m 0755 %buildroot%_emacslispdir
install -m 0644 misc/%name.el* %buildroot%_emacslispdir/

%add_findreq_skiplist %_libdir/%name/fonts


%files
%doc faq.html
%_libdir/%name
%_bindir/*
%if_with gui
%_desktopdir/*
%_iconsdir/hicolor/*/apps/*
%endif


%files -n vim-plugin-%name-syntax
%vim_syntax_dir/*


%files -n emacs-mode-%name
%_emacslispdir/*.elc


%files -n emacs-mode-%name-el
%_emacslispdir/*.el


%changelog
* Tue Apr 19 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.92-alt0.9.1
- fix build

* Mon Dec 29 2008 Led <led@altlinux.ru> 0.92-alt0.9
- new git snapshot

* Thu Sep 04 2008 Led <led@altlinux.ru> 0.92-alt0.8
- git snapshot at 20080904

* Fri Aug 29 2008 Led <led@altlinux.ru> 0.92-alt0.7
- git snapshot at 20080829

* Wed Aug 20 2008 Led <led@altlinux.ru> 0.92-alt0.6
- git snapshot at 20080819

* Thu Aug 14 2008 Led <led@altlinux.ru> 0.92-alt0.5
- git snapshot at 20080813

* Sat Aug 09 2008 Led <led@altlinux.ru> 0.92-alt0.4
- git snapshot at 20080808
- fixed %name.desktop

* Mon Aug 04 2008 Led <led@altlinux.ru> 0.92-alt0.3
- git snapshot at 20080804
- fixed Requires

* Mon Aug 04 2008 Led <led@altlinux.ru> 0.92-alt0.2
- git snapshot at 20080803
- added emacs-mode-%{name}* packages

* Sun Aug 03 2008 Led <led@altlinux.ru> 0.92-alt0.1
- initial build (git snapshot at 20080802)
