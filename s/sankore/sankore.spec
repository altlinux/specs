#
# spec file for package sankore
#
# Copyright (c) 2012 SUSE LINUX Products GmbH, Nuernberg, Germany.
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

%define dest_dir %_libdir/OpenSankore
# OR %%{_datadir}/%%{name} ?

Name: sankore
Version: 3.1.git.1386578185
Release: alt1

Summary: The open-source software suite for digital teachers
License: GPL-3.0+
Group: Education

Url: https://github.com/Sankore/
Source: %name-%version.tar.xz
Source1: %name.xml
# Source1:	%%{name}-thirdparty-1353579018.tar.xz
Patch: tutorial_it.diff
Patch1: editor_it.diff
# fix include in UBGraphicsItemAction.h
Patch2: %name-phonon_include.patch
# use libs from openSUSE
Patch3: %name-no_Third-Party.patch
# use poppler instead of xpdf to handle pdf
Patch4: %name-XPDFRenderer_with_poppler.patch
# quazip from distro for plugins, too
Patch5: %name-plugins_UBCFFAdaptor.diff
Packager: Michael Shigorin <mike@altlinux.org>

# Automatically added by buildreq on Tue Mar 22 2016
# optimized out: fontconfig libX11-devel libfreetype-devel libgpg-error libgst-plugins1.0 libjson-c libqt4-core libqt4-dbus libqt4-devel libqt4-gui libqt4-location libqt4-network libqt4-opengl libqt4-script libqt4-sensors libqt4-svg libqt4-uitools libqt4-webkit libqt4-xml libqt4-xmlpatterns libssl-devel libstdc++-devel t1lib xorg-xproto-devel xz zlib-devel
BuildRequires: gcc-c++ libgomp-devel libpaper-devel libpoppler-devel libqt4-webkit-devel libqtsingleapplication-devel libquazip-devel phonon-devel t1lib-devel

%description
%name can be considered as three integrated functions in one outstanding tool:
- uniboard universal interactive white board software
- the sankore teaching designer
- the sankore editor

Authors:
--------
http://open-sankore.org/

%prep
%setup

#Italian Tutorial
%patch0 -p1
#Italian Editor
%patch1 -p1

%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5

sed -i 's,qtsingleapplication.h,QtSolutions/&,' src/core/UBApplication.h
sed -i 's,phonon/,kde4/&,' src/*/*.h src/gui/UBVideoPlayer.cpp

%define qmake qmake-qt4
%define lrelease lrelease-qt4

%build
# plugin cffadaptor (should be redundant, since code is already included into the main program while building)
pushd plugins/cffadaptor
%qmake UBCFFAdaptor.pro QMAKE_CFLAGS+="%optflags" QMAKE_CXXFLAGS+="%optflags"
%make_build VERBOSE=1
popd

%qmake Sankore_3.1.pro QMAKE_CFLAGS+="%optflags" QMAKE_CXXFLAGS+="%optflags"
%make_build VERBOSE=1

%install
%make_install install

#missed icon, taking one
install -pDm644 resources/images/uniboard.png %buildroot%_pixmapsdir/sankore.png

#missed desktop file, writing one
mkdir -p %buildroot%_desktopdir
cat > %buildroot%_desktopdir/%name.desktop <<EOF
[Desktop Entry]
Encoding=UTF-8
Name=Open-Sankore
GenericName=Open-Sankore
Comment=Software to create presentations for interactive whiteboard (TNI)
Comment[fr]=Logiciel de création de présentations pour tableau numérique interactif (TNI)
Exec=%dest_dir/run.sh "%%f"
Icon=sankore
StartupNotify=true
Terminal=false
Type=Application
MimeType=application/x-open-sankore;
Categories=Qt;KDE;Education;Engineering;
X-SuSE-translate=false
EOF

# missing mime type file
install -pD %SOURCE1 %buildroot%_datadir/mime/packages/%name.xml

#Install files
install -pDm755 build/linux/release/product/Open-Sankore \
	%buildroot%dest_dir/Open-Sankore
cp -a build/linux/release/product/* %buildroot%dest_dir/

#run.sh (set env to avoid some possible issues)
cat > %buildroot%dest_dir/run.sh <<EOF
#!/bin/bash
# --------------------------------------------------------------------
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
# ---------------------------------------------------------------------

env QT_PLUGIN_PATH=\$QT_PLUGIN_PATH:%dest_dir/OpenSankore/plugins LD_LIBRARY_PATH=\$LD_LIBRARY_PATH:%dest_dir/plugins/cffadaptor %dest_dir/Open-Sankore "\$@"
EOF
chmod 0755 %buildroot%dest_dir/run.sh
mkdir -p %buildroot/%_bindir/
ln -s -T %dest_dir/run.sh %buildroot/%_bindir/open-%name

# clean some exe bits
find %buildroot%dest_dir/library -executable -type f -name *.js -exec chmod -x '{}' \+
find %buildroot%dest_dir/library -executable -type f -name *.svg -exec chmod -x '{}' \+
find %buildroot%dest_dir/library -executable -type f -name *.css -exec chmod -x '{}' \+
find %buildroot%dest_dir/library -executable -type f -name *.xml -exec chmod -x '{}' \+
chmod -x %buildroot%dest_dir/library/*/*/*.html

# internalization
%lrelease -removeidentical Sankore_3.1.pro
mkdir -p %buildroot%dest_dir/i18n/
cp -R resources/i18n/sankore*.qm %buildroot%dest_dir/i18n/

# Disabled, we added local_plugins to qt_plugins...
# ... otherwise we would brake icons and more (GUI/plugin translations?) and we would have
# to copy/link global qt4/plugins inside program dir
# # qt.conf
# cp -R resources/linux/qtlinux/* %%{buildroot}%%dest_dir/

# customizations
cp -a resources/customizations %buildroot%dest_dir/

# startup hints
cp -a resources/startupHints %buildroot%dest_dir/

# plugins
mkdir -p %buildroot%dest_dir/plugins/cffadaptor
install -p plugins/cffadaptor/build/linux/release/lib/libCFF_Adaptor* \
	%buildroot%dest_dir/plugins/cffadaptor/

%files
%doc README.txt LICENSE.txt JournalDesModifications.pdf ReleaseNotes.pdf
%_desktopdir/%name.desktop
%_datadir/mime/packages/%name.xml
%_pixmapsdir/%name.png
%dest_dir/
%_bindir/open-%name

%changelog
* Tue Mar 22 2016 Michael Shigorin <mike@altlinux.org> 3.1.git.1386578185-alt1
- initial build for ALT Linux Sisyphus (based on openSUSE package)
- spec cleanup
- buildreq
