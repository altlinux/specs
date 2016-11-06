BuildRequires(pre): 	rpm-macros-trinity
BuildRequires(pre):	rpm-macros-suse-compat
BuildRequires(pre):	rpm-macros-cmake
#
# spec file for package trinity-filesystem (version R14)
#
# Copyright (c) 2014 Trinity Desktop Environment
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.
#
# Please submit bugfixes or comments via http://www.trinitydesktop.org/
#

# TDE variables
%if "%{?tde_version}" == ""
%define tde_version 14.0.3
%endif

Name: trinity-filesystem
Version: 14.0.3
Release: alt1_2
Summary: Trinity Directory Layout
Group: System/Base
Url: http://www.trinitydesktop.org/

License: GPL-2.0+

#Vendor:		Trinity Desktop
#Packager:	Francois Andriot <francois.andriot@free.fr>

Packager: Hihin Ruslan <ruslandh@altlinux.ru>

Source44: import.info

%description
This package installs the Trinity directory structure.

%files
%dir %tde_datadir
%dir %tde_confdir
%dir %tde_confdir/magic

%dir %tde_docdir

%dir %tde_includedir
%dir %tde_tdeincludedir

%dir %tde_libdir
%dir %tde_libdir/java
%dir %tde_libdir/jni
%dir %tde_libdir/pkgconfig
%dir %tde_tdelibdir

%dir %tde_datadir/applications
%dir %tde_datadir/applications/tde
%dir %tde_datadir/applnk
%dir %tde_datadir/applnk/.hidden
%dir %tde_datadir/applnk/*
%dir %tde_datadir/applnk/*/*
%dir %tde_datadir/apps
%dir %tde_datadir/apps/*
%dir %tde_datadir/cmake
%dir %tde_datadir/config.kcfg
%dir %tde_datadir/autostart
%dir %tde_datadir/emoticons
%dir %tde_datadir/icons
%dir %tde_datadir/icons/crystalsvg
%dir %tde_datadir/icons/crystalsvg/*
%dir %tde_datadir/icons/crystalsvg/*/*
%dir %tde_datadir/icons/hicolor
%dir %tde_datadir/icons/hicolor/*
%dir %tde_datadir/icons/hicolor/*/*
%dir %tde_datadir/icons/locolor
%dir %tde_datadir/icons/locolor/*
%dir %tde_datadir/icons/locolor/*/*
%dir %tde_datadir/locale
%dir %tde_datadir/locale/*
%dir %tde_datadir/locale/*/*
%dir %tde_datadir/man
%dir %tde_datadir/man/*
%dir %tde_datadir/mimelnk
%dir %tde_datadir/mimelnk/*
%dir %tde_datadir/services
%dir %tde_datadir/services/*
%dir %tde_datadir/servicetypes
%dir %tde_datadir/wallpapers

%dir %_sysconfdir/trinity
%dir %_libexecdir/tde

##########

%prep
%build
%install
install -d -m 755 %{?buildroot}%tde_prefix

install -d -m 755 %{?buildroot}%tde_bindir

install -d -m 755 %{?buildroot}%tde_datadir
install -d -m 755 %{?buildroot}%tde_datadir/applications
install -d -m 755 %{?buildroot}%tde_datadir/applications/tde
install -d -m 755 %{?buildroot}%tde_datadir/applnk
install -d -m 755 %{?buildroot}%tde_datadir/applnk/.hidden
install -d -m 755 %{?buildroot}%tde_datadir/applnk/Applications
install -d -m 755 %{?buildroot}%tde_datadir/applnk/Development
install -d -m 755 %{?buildroot}%tde_datadir/applnk/Edutainment
install -d -m 755 %{?buildroot}%tde_datadir/applnk/Edutainment/Languages
install -d -m 755 %{?buildroot}%tde_datadir/applnk/Edutainment/Mathematics
install -d -m 755 %{?buildroot}%tde_datadir/applnk/Edutainment/Miscellaneous
install -d -m 755 %{?buildroot}%tde_datadir/applnk/Edutainment/Science
install -d -m 755 %{?buildroot}%tde_datadir/applnk/Edutainment/Tools
install -d -m 755 %{?buildroot}%tde_datadir/applnk/Games
install -d -m 755 %{?buildroot}%tde_datadir/applnk/Games/Board
install -d -m 755 %{?buildroot}%tde_datadir/applnk/Graphics
install -d -m 755 %{?buildroot}%tde_datadir/applnk/Internet
install -d -m 755 %{?buildroot}%tde_datadir/applnk/Multimedia
install -d -m 755 %{?buildroot}%tde_datadir/applnk/Office
install -d -m 755 %{?buildroot}%tde_datadir/applnk/Settings
install -d -m 755 %{?buildroot}%tde_datadir/applnk/Settings/LookNFeel
install -d -m 755 %{?buildroot}%tde_datadir/applnk/Settings/WebBrowsing
install -d -m 755 %{?buildroot}%tde_datadir/applnk/System
install -d -m 755 %{?buildroot}%tde_datadir/applnk/System/ScreenSavers
install -d -m 755 %{?buildroot}%tde_datadir/applnk/Toys
install -d -m 755 %{?buildroot}%tde_datadir/applnk/Utilities
install -d -m 755 %{?buildroot}%tde_datadir/apps
install -d -m 755 %{?buildroot}%tde_datadir/apps/plugin
install -d -m 755 %{?buildroot}%tde_datadir/apps/profiles
install -d -m 755 %{?buildroot}%tde_datadir/apps/remotes
install -d -m 755 %{?buildroot}%tde_datadir/apps/remoteview
install -d -m 755 %{?buildroot}%tde_datadir/apps/videothumbnail
install -d -m 755 %{?buildroot}%tde_datadir/apps/zeroconf
install -d -m 755 %{?buildroot}%tde_datadir/autostart
install -d -m 755 %{?buildroot}%tde_datadir/cmake
install -d -m 755 %{?buildroot}%tde_confdir
install -d -m 755 %{?buildroot}%tde_confdir/magic
install -d -m 755 %{?buildroot}%tde_datadir/config.kcfg
install -d -m 755 %{?buildroot}%tde_datadir/emoticons
install -d -m 755 %{?buildroot}%tde_datadir/locale
install -d -m 755 %{?buildroot}%tde_datadir/man
install -d -m 755 %{?buildroot}%tde_datadir/man/man1
install -d -m 755 %{?buildroot}%tde_datadir/man/man2
install -d -m 755 %{?buildroot}%tde_datadir/man/man3
install -d -m 755 %{?buildroot}%tde_datadir/man/man4
install -d -m 755 %{?buildroot}%tde_datadir/man/man5
install -d -m 755 %{?buildroot}%tde_datadir/man/man6
install -d -m 755 %{?buildroot}%tde_datadir/man/man7
install -d -m 755 %{?buildroot}%tde_datadir/man/man8
install -d -m 755 %{?buildroot}%tde_datadir/man/man9
install -d -m 755 %{?buildroot}%tde_datadir/mimelnk
install -d -m 755 %{?buildroot}%tde_datadir/mimelnk/all
install -d -m 755 %{?buildroot}%tde_datadir/mimelnk/application
install -d -m 755 %{?buildroot}%tde_datadir/mimelnk/audio
install -d -m 755 %{?buildroot}%tde_datadir/mimelnk/fonts
install -d -m 755 %{?buildroot}%tde_datadir/mimelnk/image
install -d -m 755 %{?buildroot}%tde_datadir/mimelnk/interface
install -d -m 755 %{?buildroot}%tde_datadir/mimelnk/inode
install -d -m 755 %{?buildroot}%tde_datadir/mimelnk/media
install -d -m 755 %{?buildroot}%tde_datadir/mimelnk/message
install -d -m 755 %{?buildroot}%tde_datadir/mimelnk/model
install -d -m 755 %{?buildroot}%tde_datadir/mimelnk/multipart
install -d -m 755 %{?buildroot}%tde_datadir/mimelnk/print
install -d -m 755 %{?buildroot}%tde_datadir/mimelnk/text
install -d -m 755 %{?buildroot}%tde_datadir/mimelnk/uri
install -d -m 755 %{?buildroot}%tde_datadir/mimelnk/video
install -d -m 755 %{?buildroot}%tde_datadir/services
install -d -m 755 %{?buildroot}%tde_datadir/services/tdeconfiguredialog
install -d -m 755 %{?buildroot}%tde_datadir/servicetypes

install -d -m 755 %{?buildroot}%tde_datadir/wallpapers

# Create icons directories
install -d -m 755 %{?buildroot}%tde_datadir/icons
for t in crystalsvg hicolor locolor ; do
  install -d -m 755 "%{?buildroot}%tde_datadir/icons/${t}"
  install -d -m 755 "%{?buildroot}%tde_datadir/icons/${t}/scalable"
  for i in {16,22,32,48,64,128,256} ; do
    install -d -m 755 "%{?buildroot}%tde_datadir/icons/${t}/${i}x${i}"
  done

  # Create subdirectories
  for r in actions apps categories devices mimetypes places ; do
    install -d -m 755 "%{?buildroot}%tde_datadir/icons/${t}/scalable/${r}"
    for i in {16,22,32,48,64,128} ; do
      install -d -m 755 "%{?buildroot}%tde_datadir/icons/${t}/${i}x${i}/${r}"
    done
  done
done

install -d -m 755 %{?buildroot}%tde_docdir
install -d -m 755 %{?buildroot}%tde_tdedocdir

# HTML directories
install -d -m 755 %{?buildroot}%tde_tdedocdir/HTML
install -d -m 755 %{?buildroot}%tde_tdedocdir/HTML/ca/common
install -d -m 755 %{?buildroot}%tde_tdedocdir/HTML/cs/common
install -d -m 755 %{?buildroot}%tde_tdedocdir/HTML/da/common
install -d -m 755 %{?buildroot}%tde_tdedocdir/HTML/de/common
install -d -m 755 %{?buildroot}%tde_tdedocdir/HTML/en/common
install -d -m 755 %{?buildroot}%tde_tdedocdir/HTML/en_GB/common
install -d -m 755 %{?buildroot}%tde_tdedocdir/HTML/es/common
install -d -m 755 %{?buildroot}%tde_tdedocdir/HTML/et/common
install -d -m 755 %{?buildroot}%tde_tdedocdir/HTML/fi/common
install -d -m 755 %{?buildroot}%tde_tdedocdir/HTML/fr/common
install -d -m 755 %{?buildroot}%tde_tdedocdir/HTML/he/common
install -d -m 755 %{?buildroot}%tde_tdedocdir/HTML/hu/common
install -d -m 755 %{?buildroot}%tde_tdedocdir/HTML/it/common
install -d -m 755 %{?buildroot}%tde_tdedocdir/HTML/ja/common
install -d -m 755 %{?buildroot}%tde_tdedocdir/HTML/nl/common
install -d -m 755 %{?buildroot}%tde_tdedocdir/HTML/pl/common
install -d -m 755 %{?buildroot}%tde_tdedocdir/HTML/pt_BR/common
install -d -m 755 %{?buildroot}%tde_tdedocdir/HTML/pt/common
install -d -m 755 %{?buildroot}%tde_tdedocdir/HTML/ro/common
install -d -m 755 %{?buildroot}%tde_tdedocdir/HTML/ru/common
install -d -m 755 %{?buildroot}%tde_tdedocdir/HTML/sk/common
install -d -m 755 %{?buildroot}%tde_tdedocdir/HTML/sl/common
install -d -m 755 %{?buildroot}%tde_tdedocdir/HTML/sr/common
install -d -m 755 %{?buildroot}%tde_tdedocdir/HTML/sv/common
install -d -m 755 %{?buildroot}%tde_tdedocdir/HTML/tr/common
install -d -m 755 %{?buildroot}%tde_tdedocdir/HTML/uk/common
install -d -m 755 %{?buildroot}%tde_tdedocdir/HTML/zh_CN/common
install -d -m 755 %{?buildroot}%tde_tdedocdir/HTML/zh_TW/common

install -d -m 755 %{?buildroot}%tde_includedir
install -d -m 755 %{?buildroot}%tde_tdeincludedir

install -d -m 755 %{?buildroot}%tde_libdir
install -d -m 755 %{?buildroot}%tde_libdir/java
install -d -m 755 %{?buildroot}%tde_libdir/jni
install -d -m 755 %{?buildroot}%tde_libdir/pkgconfig
install -d -m 755 %{?buildroot}%tde_tdelibdir

install -d -m 755 %{?buildroot}%_sysconfdir/trinity
install -d -m 755 %{?buildroot}%_sysconfdir/xdg/menus

# Locales directories
install -d -m 755 %{?buildroot}%tde_datadir/locale/en_US
install -d -m 755 %{?buildroot}%tde_datadir/locale/l10n
install -d -m 755 %{?buildroot}%tde_datadir/locale/l10n/C
install -d -m 755 %{?buildroot}%tde_datadir/locale/l10n/ad
install -d -m 755 %{?buildroot}%tde_datadir/locale/l10n/ae
install -d -m 755 %{?buildroot}%tde_datadir/locale/l10n/af
install -d -m 755 %{?buildroot}%tde_datadir/locale/l10n/ag
install -d -m 755 %{?buildroot}%tde_datadir/locale/l10n/ai
install -d -m 755 %{?buildroot}%tde_datadir/locale/l10n/al
install -d -m 755 %{?buildroot}%tde_datadir/locale/l10n/am
install -d -m 755 %{?buildroot}%tde_datadir/locale/l10n/an
install -d -m 755 %{?buildroot}%tde_datadir/locale/l10n/ao
install -d -m 755 %{?buildroot}%tde_datadir/locale/l10n/ar
install -d -m 755 %{?buildroot}%tde_datadir/locale/l10n/as
install -d -m 755 %{?buildroot}%tde_datadir/locale/l10n/at
install -d -m 755 %{?buildroot}%tde_datadir/locale/l10n/au
install -d -m 755 %{?buildroot}%tde_datadir/locale/l10n/aw
install -d -m 755 %{?buildroot}%tde_datadir/locale/l10n/ax
install -d -m 755 %{?buildroot}%tde_datadir/locale/l10n/az
install -d -m 755 %{?buildroot}%tde_datadir/locale/l10n/ba
install -d -m 755 %{?buildroot}%tde_datadir/locale/l10n/bb
install -d -m 755 %{?buildroot}%tde_datadir/locale/l10n/bd
install -d -m 755 %{?buildroot}%tde_datadir/locale/l10n/be
install -d -m 755 %{?buildroot}%tde_datadir/locale/l10n/bf
install -d -m 755 %{?buildroot}%tde_datadir/locale/l10n/bg
install -d -m 755 %{?buildroot}%tde_datadir/locale/l10n/bh
install -d -m 755 %{?buildroot}%tde_datadir/locale/l10n/bi
install -d -m 755 %{?buildroot}%tde_datadir/locale/l10n/bj
install -d -m 755 %{?buildroot}%tde_datadir/locale/l10n/bm
install -d -m 755 %{?buildroot}%tde_datadir/locale/l10n/bn
install -d -m 755 %{?buildroot}%tde_datadir/locale/l10n/bo
install -d -m 755 %{?buildroot}%tde_datadir/locale/l10n/br
install -d -m 755 %{?buildroot}%tde_datadir/locale/l10n/bs
install -d -m 755 %{?buildroot}%tde_datadir/locale/l10n/bt
install -d -m 755 %{?buildroot}%tde_datadir/locale/l10n/bw
install -d -m 755 %{?buildroot}%tde_datadir/locale/l10n/by
install -d -m 755 %{?buildroot}%tde_datadir/locale/l10n/bz
install -d -m 755 %{?buildroot}%tde_datadir/locale/l10n/ca
install -d -m 755 %{?buildroot}%tde_datadir/locale/l10n/cc
install -d -m 755 %{?buildroot}%tde_datadir/locale/l10n/cd
install -d -m 755 %{?buildroot}%tde_datadir/locale/l10n/cf
install -d -m 755 %{?buildroot}%tde_datadir/locale/l10n/cg
install -d -m 755 %{?buildroot}%tde_datadir/locale/l10n/ch
install -d -m 755 %{?buildroot}%tde_datadir/locale/l10n/ci
install -d -m 755 %{?buildroot}%tde_datadir/locale/l10n/ck
install -d -m 755 %{?buildroot}%tde_datadir/locale/l10n/cl
install -d -m 755 %{?buildroot}%tde_datadir/locale/l10n/cm
install -d -m 755 %{?buildroot}%tde_datadir/locale/l10n/cn
install -d -m 755 %{?buildroot}%tde_datadir/locale/l10n/co
install -d -m 755 %{?buildroot}%tde_datadir/locale/l10n/cr
install -d -m 755 %{?buildroot}%tde_datadir/locale/l10n/cu
install -d -m 755 %{?buildroot}%tde_datadir/locale/l10n/cv
install -d -m 755 %{?buildroot}%tde_datadir/locale/l10n/cx
install -d -m 755 %{?buildroot}%tde_datadir/locale/l10n/cy
install -d -m 755 %{?buildroot}%tde_datadir/locale/l10n/cz
install -d -m 755 %{?buildroot}%tde_datadir/locale/l10n/de
install -d -m 755 %{?buildroot}%tde_datadir/locale/l10n/dj
install -d -m 755 %{?buildroot}%tde_datadir/locale/l10n/dk
install -d -m 755 %{?buildroot}%tde_datadir/locale/l10n/dm
install -d -m 755 %{?buildroot}%tde_datadir/locale/l10n/do
install -d -m 755 %{?buildroot}%tde_datadir/locale/l10n/dz
install -d -m 755 %{?buildroot}%tde_datadir/locale/l10n/ec
install -d -m 755 %{?buildroot}%tde_datadir/locale/l10n/ee
install -d -m 755 %{?buildroot}%tde_datadir/locale/l10n/eg
install -d -m 755 %{?buildroot}%tde_datadir/locale/l10n/eh
install -d -m 755 %{?buildroot}%tde_datadir/locale/l10n/er
install -d -m 755 %{?buildroot}%tde_datadir/locale/l10n/es
install -d -m 755 %{?buildroot}%tde_datadir/locale/l10n/et
install -d -m 755 %{?buildroot}%tde_datadir/locale/l10n/fi
install -d -m 755 %{?buildroot}%tde_datadir/locale/l10n/fj
install -d -m 755 %{?buildroot}%tde_datadir/locale/l10n/fk
install -d -m 755 %{?buildroot}%tde_datadir/locale/l10n/fm
install -d -m 755 %{?buildroot}%tde_datadir/locale/l10n/fo
install -d -m 755 %{?buildroot}%tde_datadir/locale/l10n/fr
install -d -m 755 %{?buildroot}%tde_datadir/locale/l10n/ga
install -d -m 755 %{?buildroot}%tde_datadir/locale/l10n/gb
install -d -m 755 %{?buildroot}%tde_datadir/locale/l10n/gd
install -d -m 755 %{?buildroot}%tde_datadir/locale/l10n/ge
install -d -m 755 %{?buildroot}%tde_datadir/locale/l10n/gh
install -d -m 755 %{?buildroot}%tde_datadir/locale/l10n/gi
install -d -m 755 %{?buildroot}%tde_datadir/locale/l10n/gl
install -d -m 755 %{?buildroot}%tde_datadir/locale/l10n/gm
install -d -m 755 %{?buildroot}%tde_datadir/locale/l10n/gn
install -d -m 755 %{?buildroot}%tde_datadir/locale/l10n/gp
install -d -m 755 %{?buildroot}%tde_datadir/locale/l10n/gq
install -d -m 755 %{?buildroot}%tde_datadir/locale/l10n/gr
install -d -m 755 %{?buildroot}%tde_datadir/locale/l10n/gt
install -d -m 755 %{?buildroot}%tde_datadir/locale/l10n/gu
install -d -m 755 %{?buildroot}%tde_datadir/locale/l10n/gw
install -d -m 755 %{?buildroot}%tde_datadir/locale/l10n/gy
install -d -m 755 %{?buildroot}%tde_datadir/locale/l10n/hk
install -d -m 755 %{?buildroot}%tde_datadir/locale/l10n/hn
install -d -m 755 %{?buildroot}%tde_datadir/locale/l10n/hr
install -d -m 755 %{?buildroot}%tde_datadir/locale/l10n/ht
install -d -m 755 %{?buildroot}%tde_datadir/locale/l10n/hu
install -d -m 755 %{?buildroot}%tde_datadir/locale/l10n/id
install -d -m 755 %{?buildroot}%tde_datadir/locale/l10n/ie
install -d -m 755 %{?buildroot}%tde_datadir/locale/l10n/il
install -d -m 755 %{?buildroot}%tde_datadir/locale/l10n/in
install -d -m 755 %{?buildroot}%tde_datadir/locale/l10n/iq
install -d -m 755 %{?buildroot}%tde_datadir/locale/l10n/ir
install -d -m 755 %{?buildroot}%tde_datadir/locale/l10n/is
install -d -m 755 %{?buildroot}%tde_datadir/locale/l10n/it
install -d -m 755 %{?buildroot}%tde_datadir/locale/l10n/jm
install -d -m 755 %{?buildroot}%tde_datadir/locale/l10n/jo
install -d -m 755 %{?buildroot}%tde_datadir/locale/l10n/jp
install -d -m 755 %{?buildroot}%tde_datadir/locale/l10n/ke
install -d -m 755 %{?buildroot}%tde_datadir/locale/l10n/kg
install -d -m 755 %{?buildroot}%tde_datadir/locale/l10n/kh
install -d -m 755 %{?buildroot}%tde_datadir/locale/l10n/ki
install -d -m 755 %{?buildroot}%tde_datadir/locale/l10n/km
install -d -m 755 %{?buildroot}%tde_datadir/locale/l10n/kn
install -d -m 755 %{?buildroot}%tde_datadir/locale/l10n/kp
install -d -m 755 %{?buildroot}%tde_datadir/locale/l10n/kr
install -d -m 755 %{?buildroot}%tde_datadir/locale/l10n/kw
install -d -m 755 %{?buildroot}%tde_datadir/locale/l10n/ky
install -d -m 755 %{?buildroot}%tde_datadir/locale/l10n/kz
install -d -m 755 %{?buildroot}%tde_datadir/locale/l10n/la
install -d -m 755 %{?buildroot}%tde_datadir/locale/l10n/lb
install -d -m 755 %{?buildroot}%tde_datadir/locale/l10n/lc
install -d -m 755 %{?buildroot}%tde_datadir/locale/l10n/li
install -d -m 755 %{?buildroot}%tde_datadir/locale/l10n/lk
install -d -m 755 %{?buildroot}%tde_datadir/locale/l10n/lr
install -d -m 755 %{?buildroot}%tde_datadir/locale/l10n/ls
install -d -m 755 %{?buildroot}%tde_datadir/locale/l10n/lt
install -d -m 755 %{?buildroot}%tde_datadir/locale/l10n/lu
install -d -m 755 %{?buildroot}%tde_datadir/locale/l10n/lv
install -d -m 755 %{?buildroot}%tde_datadir/locale/l10n/ly
install -d -m 755 %{?buildroot}%tde_datadir/locale/l10n/ma
install -d -m 755 %{?buildroot}%tde_datadir/locale/l10n/mc
install -d -m 755 %{?buildroot}%tde_datadir/locale/l10n/md
install -d -m 755 %{?buildroot}%tde_datadir/locale/l10n/me
install -d -m 755 %{?buildroot}%tde_datadir/locale/l10n/mg
install -d -m 755 %{?buildroot}%tde_datadir/locale/l10n/mh
install -d -m 755 %{?buildroot}%tde_datadir/locale/l10n/mk
install -d -m 755 %{?buildroot}%tde_datadir/locale/l10n/ml
install -d -m 755 %{?buildroot}%tde_datadir/locale/l10n/mm
install -d -m 755 %{?buildroot}%tde_datadir/locale/l10n/mn
install -d -m 755 %{?buildroot}%tde_datadir/locale/l10n/mo
install -d -m 755 %{?buildroot}%tde_datadir/locale/l10n/mq
install -d -m 755 %{?buildroot}%tde_datadir/locale/l10n/mr
install -d -m 755 %{?buildroot}%tde_datadir/locale/l10n/ms
install -d -m 755 %{?buildroot}%tde_datadir/locale/l10n/mt
install -d -m 755 %{?buildroot}%tde_datadir/locale/l10n/mu
install -d -m 755 %{?buildroot}%tde_datadir/locale/l10n/mv
install -d -m 755 %{?buildroot}%tde_datadir/locale/l10n/mw
install -d -m 755 %{?buildroot}%tde_datadir/locale/l10n/mx
install -d -m 755 %{?buildroot}%tde_datadir/locale/l10n/my
install -d -m 755 %{?buildroot}%tde_datadir/locale/l10n/mz
install -d -m 755 %{?buildroot}%tde_datadir/locale/l10n/na
install -d -m 755 %{?buildroot}%tde_datadir/locale/l10n/nc
install -d -m 755 %{?buildroot}%tde_datadir/locale/l10n/ne
install -d -m 755 %{?buildroot}%tde_datadir/locale/l10n/nf
install -d -m 755 %{?buildroot}%tde_datadir/locale/l10n/ng
install -d -m 755 %{?buildroot}%tde_datadir/locale/l10n/ni
install -d -m 755 %{?buildroot}%tde_datadir/locale/l10n/nl
install -d -m 755 %{?buildroot}%tde_datadir/locale/l10n/no
install -d -m 755 %{?buildroot}%tde_datadir/locale/l10n/np
install -d -m 755 %{?buildroot}%tde_datadir/locale/l10n/nr
install -d -m 755 %{?buildroot}%tde_datadir/locale/l10n/nu
install -d -m 755 %{?buildroot}%tde_datadir/locale/l10n/nz
install -d -m 755 %{?buildroot}%tde_datadir/locale/l10n/om
install -d -m 755 %{?buildroot}%tde_datadir/locale/l10n/pa
install -d -m 755 %{?buildroot}%tde_datadir/locale/l10n/pe
install -d -m 755 %{?buildroot}%tde_datadir/locale/l10n/pf
install -d -m 755 %{?buildroot}%tde_datadir/locale/l10n/pg
install -d -m 755 %{?buildroot}%tde_datadir/locale/l10n/ph
install -d -m 755 %{?buildroot}%tde_datadir/locale/l10n/pk
install -d -m 755 %{?buildroot}%tde_datadir/locale/l10n/pl
install -d -m 755 %{?buildroot}%tde_datadir/locale/l10n/pm
install -d -m 755 %{?buildroot}%tde_datadir/locale/l10n/pn
install -d -m 755 %{?buildroot}%tde_datadir/locale/l10n/pr
install -d -m 755 %{?buildroot}%tde_datadir/locale/l10n/ps
install -d -m 755 %{?buildroot}%tde_datadir/locale/l10n/pt
install -d -m 755 %{?buildroot}%tde_datadir/locale/l10n/pw
install -d -m 755 %{?buildroot}%tde_datadir/locale/l10n/py
install -d -m 755 %{?buildroot}%tde_datadir/locale/l10n/qa
install -d -m 755 %{?buildroot}%tde_datadir/locale/l10n/ro
install -d -m 755 %{?buildroot}%tde_datadir/locale/l10n/rs
install -d -m 755 %{?buildroot}%tde_datadir/locale/l10n/ru
install -d -m 755 %{?buildroot}%tde_datadir/locale/l10n/rw
install -d -m 755 %{?buildroot}%tde_datadir/locale/l10n/sa
install -d -m 755 %{?buildroot}%tde_datadir/locale/l10n/sb
install -d -m 755 %{?buildroot}%tde_datadir/locale/l10n/sc
install -d -m 755 %{?buildroot}%tde_datadir/locale/l10n/sd
install -d -m 755 %{?buildroot}%tde_datadir/locale/l10n/se
install -d -m 755 %{?buildroot}%tde_datadir/locale/l10n/sg
install -d -m 755 %{?buildroot}%tde_datadir/locale/l10n/sh
install -d -m 755 %{?buildroot}%tde_datadir/locale/l10n/si
install -d -m 755 %{?buildroot}%tde_datadir/locale/l10n/sk
install -d -m 755 %{?buildroot}%tde_datadir/locale/l10n/sm
install -d -m 755 %{?buildroot}%tde_datadir/locale/l10n/sn
install -d -m 755 %{?buildroot}%tde_datadir/locale/l10n/so
install -d -m 755 %{?buildroot}%tde_datadir/locale/l10n/sr
install -d -m 755 %{?buildroot}%tde_datadir/locale/l10n/st
install -d -m 755 %{?buildroot}%tde_datadir/locale/l10n/sv
install -d -m 755 %{?buildroot}%tde_datadir/locale/l10n/sy
install -d -m 755 %{?buildroot}%tde_datadir/locale/l10n/sz
install -d -m 755 %{?buildroot}%tde_datadir/locale/l10n/tc
install -d -m 755 %{?buildroot}%tde_datadir/locale/l10n/td
install -d -m 755 %{?buildroot}%tde_datadir/locale/l10n/tg
install -d -m 755 %{?buildroot}%tde_datadir/locale/l10n/th
install -d -m 755 %{?buildroot}%tde_datadir/locale/l10n/tj
install -d -m 755 %{?buildroot}%tde_datadir/locale/l10n/tk
install -d -m 755 %{?buildroot}%tde_datadir/locale/l10n/tm
install -d -m 755 %{?buildroot}%tde_datadir/locale/l10n/tn
install -d -m 755 %{?buildroot}%tde_datadir/locale/l10n/to
install -d -m 755 %{?buildroot}%tde_datadir/locale/l10n/tp
install -d -m 755 %{?buildroot}%tde_datadir/locale/l10n/tr
install -d -m 755 %{?buildroot}%tde_datadir/locale/l10n/tt
install -d -m 755 %{?buildroot}%tde_datadir/locale/l10n/tv
install -d -m 755 %{?buildroot}%tde_datadir/locale/l10n/tw
install -d -m 755 %{?buildroot}%tde_datadir/locale/l10n/tz
install -d -m 755 %{?buildroot}%tde_datadir/locale/l10n/ua
install -d -m 755 %{?buildroot}%tde_datadir/locale/l10n/ug
install -d -m 755 %{?buildroot}%tde_datadir/locale/l10n/us
install -d -m 755 %{?buildroot}%tde_datadir/locale/l10n/uy
install -d -m 755 %{?buildroot}%tde_datadir/locale/l10n/uz
install -d -m 755 %{?buildroot}%tde_datadir/locale/l10n/va
install -d -m 755 %{?buildroot}%tde_datadir/locale/l10n/vc
install -d -m 755 %{?buildroot}%tde_datadir/locale/l10n/ve
install -d -m 755 %{?buildroot}%tde_datadir/locale/l10n/vg
install -d -m 755 %{?buildroot}%tde_datadir/locale/l10n/vi
install -d -m 755 %{?buildroot}%tde_datadir/locale/l10n/vn
install -d -m 755 %{?buildroot}%tde_datadir/locale/l10n/vu
install -d -m 755 %{?buildroot}%tde_datadir/locale/l10n/wf
install -d -m 755 %{?buildroot}%tde_datadir/locale/l10n/ws
install -d -m 755 %{?buildroot}%tde_datadir/locale/l10n/ye
install -d -m 755 %{?buildroot}%tde_datadir/locale/l10n/za
install -d -m 755 %{?buildroot}%tde_datadir/locale/l10n/zm
install -d -m 755 %{?buildroot}%tde_datadir/locale/l10n/zw

# Directories for LC_MESSAGES (from *-i18n packages)
install -d -m 755 %{?buildroot}%tde_datadir/locale/af/LC_MESSAGES/
install -d -m 755 %{?buildroot}%tde_datadir/locale/ar/LC_MESSAGES/
install -d -m 755 %{?buildroot}%tde_datadir/locale/az/LC_MESSAGES/
install -d -m 755 %{?buildroot}%tde_datadir/locale/be/LC_MESSAGES/
install -d -m 755 %{?buildroot}%tde_datadir/locale/bg/LC_MESSAGES/
install -d -m 755 %{?buildroot}%tde_datadir/locale/bn/LC_MESSAGES/
install -d -m 755 %{?buildroot}%tde_datadir/locale/br/LC_MESSAGES/
install -d -m 755 %{?buildroot}%tde_datadir/locale/bs/LC_MESSAGES/
install -d -m 755 %{?buildroot}%tde_datadir/locale/ca/LC_MESSAGES/
install -d -m 755 %{?buildroot}%tde_datadir/locale/cs/LC_MESSAGES/
install -d -m 755 %{?buildroot}%tde_datadir/locale/csb/LC_MESSAGES/
install -d -m 755 %{?buildroot}%tde_datadir/locale/cy/LC_MESSAGES/
install -d -m 755 %{?buildroot}%tde_datadir/locale/da/LC_MESSAGES/
install -d -m 755 %{?buildroot}%tde_datadir/locale/de/LC_MESSAGES/
install -d -m 755 %{?buildroot}%tde_datadir/locale/du/LC_MESSAGES/
install -d -m 755 %{?buildroot}%tde_datadir/locale/ee/LC_MESSAGES/
install -d -m 755 %{?buildroot}%tde_datadir/locale/el/LC_MESSAGES/
install -d -m 755 %{?buildroot}%tde_datadir/locale/en/LC_MESSAGES/
install -d -m 755 %{?buildroot}%tde_datadir/locale/en_GB/LC_MESSAGES/
install -d -m 755 %{?buildroot}%tde_datadir/locale/en_US/LC_MESSAGES/
install -d -m 755 %{?buildroot}%tde_datadir/locale/eo/LC_MESSAGES/
install -d -m 755 %{?buildroot}%tde_datadir/locale/es/LC_MESSAGES/
install -d -m 755 %{?buildroot}%tde_datadir/locale/es_AR/LC_MESSAGES/
install -d -m 755 %{?buildroot}%tde_datadir/locale/et/LC_MESSAGES/
install -d -m 755 %{?buildroot}%tde_datadir/locale/eu/LC_MESSAGES/
install -d -m 755 %{?buildroot}%tde_datadir/locale/fa/LC_MESSAGES/
install -d -m 755 %{?buildroot}%tde_datadir/locale/fi/LC_MESSAGES/
install -d -m 755 %{?buildroot}%tde_datadir/locale/fo/LC_MESSAGES/
install -d -m 755 %{?buildroot}%tde_datadir/locale/fr/LC_MESSAGES/
install -d -m 755 %{?buildroot}%tde_datadir/locale/ga/LC_MESSAGES/
install -d -m 755 %{?buildroot}%tde_datadir/locale/gl/LC_MESSAGES/
install -d -m 755 %{?buildroot}%tde_datadir/locale/he/LC_MESSAGES/
install -d -m 755 %{?buildroot}%tde_datadir/locale/hi/LC_MESSAGES/
install -d -m 755 %{?buildroot}%tde_datadir/locale/hr/LC_MESSAGES/
install -d -m 755 %{?buildroot}%tde_datadir/locale/hu/LC_MESSAGES/
install -d -m 755 %{?buildroot}%tde_datadir/locale/id/LC_MESSAGES/
install -d -m 755 %{?buildroot}%tde_datadir/locale/is/LC_MESSAGES/
install -d -m 755 %{?buildroot}%tde_datadir/locale/it/LC_MESSAGES/
install -d -m 755 %{?buildroot}%tde_datadir/locale/ja/LC_MESSAGES/
install -d -m 755 %{?buildroot}%tde_datadir/locale/ka/LC_MESSAGES/
install -d -m 755 %{?buildroot}%tde_datadir/locale/km/LC_MESSAGES/
install -d -m 755 %{?buildroot}%tde_datadir/locale/ko/LC_MESSAGES/
install -d -m 755 %{?buildroot}%tde_datadir/locale/ku/LC_MESSAGES/
install -d -m 755 %{?buildroot}%tde_datadir/locale/lo/LC_MESSAGES/
install -d -m 755 %{?buildroot}%tde_datadir/locale/lt/LC_MESSAGES/
install -d -m 755 %{?buildroot}%tde_datadir/locale/mk/LC_MESSAGES/
install -d -m 755 %{?buildroot}%tde_datadir/locale/ms/LC_MESSAGES/
install -d -m 755 %{?buildroot}%tde_datadir/locale/mt/LC_MESSAGES/
install -d -m 755 %{?buildroot}%tde_datadir/locale/nb/LC_MESSAGES/
install -d -m 755 %{?buildroot}%tde_datadir/locale/nds/LC_MESSAGES/
install -d -m 755 %{?buildroot}%tde_datadir/locale/ne/LC_MESSAGES/
install -d -m 755 %{?buildroot}%tde_datadir/locale/nl/LC_MESSAGES/
install -d -m 755 %{?buildroot}%tde_datadir/locale/nn/LC_MESSAGES/
install -d -m 755 %{?buildroot}%tde_datadir/locale/nso/LC_MESSAGES/
install -d -m 755 %{?buildroot}%tde_datadir/locale/pa/LC_MESSAGES/
install -d -m 755 %{?buildroot}%tde_datadir/locale/pl/LC_MESSAGES/
install -d -m 755 %{?buildroot}%tde_datadir/locale/pl_PL/LC_MESSAGES/
install -d -m 755 %{?buildroot}%tde_datadir/locale/pl-utf/LC_MESSAGES/
install -d -m 755 %{?buildroot}%tde_datadir/locale/pt/LC_MESSAGES/
install -d -m 755 %{?buildroot}%tde_datadir/locale/pt_PT/LC_MESSAGES/
install -d -m 755 %{?buildroot}%tde_datadir/locale/pt_BR/LC_MESSAGES/
install -d -m 755 %{?buildroot}%tde_datadir/locale/ro/LC_MESSAGES/
install -d -m 755 %{?buildroot}%tde_datadir/locale/ru/LC_MESSAGES/
install -d -m 755 %{?buildroot}%tde_datadir/locale/rw/LC_MESSAGES/
install -d -m 755 %{?buildroot}%tde_datadir/locale/se/LC_MESSAGES/
install -d -m 755 %{?buildroot}%tde_datadir/locale/sk/LC_MESSAGES/
install -d -m 755 %{?buildroot}%tde_datadir/locale/sl/LC_MESSAGES/
install -d -m 755 %{?buildroot}%tde_datadir/locale/sl_SI/LC_MESSAGES/
install -d -m 755 %{?buildroot}%tde_datadir/locale/sq/LC_MESSAGES/
install -d -m 755 %{?buildroot}%tde_datadir/locale/sr/LC_MESSAGES/
install -d -m 755 %{?buildroot}%tde_datadir/locale/sr@latin/LC_MESSAGES/
install -d -m 755 %{?buildroot}%tde_datadir/locale/sr@Latn/LC_MESSAGES/
install -d -m 755 %{?buildroot}%tde_datadir/locale/ss/LC_MESSAGES/
install -d -m 755 %{?buildroot}%tde_datadir/locale/sv/LC_MESSAGES/
install -d -m 755 %{?buildroot}%tde_datadir/locale/ta/LC_MESSAGES/
install -d -m 755 %{?buildroot}%tde_datadir/locale/tg/LC_MESSAGES/
install -d -m 755 %{?buildroot}%tde_datadir/locale/th/LC_MESSAGES/
install -d -m 755 %{?buildroot}%tde_datadir/locale/tr/LC_MESSAGES/
install -d -m 755 %{?buildroot}%tde_datadir/locale/uk/LC_MESSAGES/
install -d -m 755 %{?buildroot}%tde_datadir/locale/uk@cyrillic/LC_MESSAGES/
install -d -m 755 %{?buildroot}%tde_datadir/locale/uz/LC_MESSAGES/
install -d -m 755 %{?buildroot}%tde_datadir/locale/uz@cyrillic/LC_MESSAGES/
install -d -m 755 %{?buildroot}%tde_datadir/locale/ven/LC_MESSAGES/
install -d -m 755 %{?buildroot}%tde_datadir/locale/vi/LC_MESSAGES/
install -d -m 755 %{?buildroot}%tde_datadir/locale/xh/LC_MESSAGES/
install -d -m 755 %{?buildroot}%tde_datadir/locale/xx/LC_MESSAGES/
install -d -m 755 %{?buildroot}%tde_datadir/locale/zh_CN.GB2312/LC_MESSAGES/
install -d -m 755 %{?buildroot}%tde_datadir/locale/zh_CN/LC_MESSAGES/
install -d -m 755 %{?buildroot}%tde_datadir/locale/zh_TW.Big5/LC_MESSAGES/
install -d -m 755 %{?buildroot}%tde_datadir/locale/zh_TW/LC_MESSAGES/
install -d -m 755 %{?buildroot}%tde_datadir/locale/zu/LC_MESSAGES/
install -d -m 755 %buildroot%_libexecdir/tde

%post
for b in kcheckpass kgrantpty kpac_dhcp_helper kppp start_tdeinit tdmtsak tdekbdledsync ; do
  if ! grep -q "^%tde_bindir/${b}" "/etc/permissions.local"; then
    echo "%tde_bindir/${b}          root:root       4711" >>/etc/permissions.local
  fi
done

%changelog
* Sun Nov 06 2016 Hihin Ruslan <ruslandh@altlinux.ru> 14.0.3-alt1_2
- converted rpmcs

* Sun Nov 06 2016 Hihin Ruslan <ruslandh@altlinux.ru> 14.0.3-alt1_1
- converted for ALT Linux by srpmconvert tools

