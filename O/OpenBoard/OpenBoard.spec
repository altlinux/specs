%define dest_dir %_libdir/OpenBoard
Name: OpenBoard
Version: 1.3.6
Release: alt2%ubt
Summary: Interactive whiteboard for schools and universities
License: GPL-3.0+
Group: Education
Url: https://github.com/OpenBoard-org/OpenBoard
Packager: Anton Midyukov <antohami@altlinux.org>

Source: %name-%version.tar
# use system libs as dependencies
Patch0: %name-no_Third-Party.patch
# use poppler instead of xpdf to handle pdf
Patch1: %name-XPDFRenderer_with_poppler.patch
# PATCH-FEATURE-UPSTREAM OpenBoard-1.3.6-add-openssl-1.1-compat.patch -- Add compatibility with OpenSSL 1.1 API
Patch2: OpenBoard-1.3.6-add-openssl-1.1-compat.patch
Patch4: single_application.patch

Buildrequires(pre): rpm-build-ubt
BuildRequires: gcc-c++ libgomp-devel
BuildRequires: desktop-file-utils
BuildRequires: libpaper-devel
BuildRequires: libssl-devel
BuildRequires: libquazip-qt5-devel
BuildRequires: t1lib-devel
BuildRequires: pkgconfig(Qt5Core)
BuildRequires: pkgconfig(Qt5Multimedia)
BuildRequires: pkgconfig(Qt5MultimediaWidgets)
BuildRequires: pkgconfig(Qt5Network)
BuildRequires: pkgconfig(Qt5PrintSupport)
BuildRequires: pkgconfig(Qt5Script)
BuildRequires: pkgconfig(Qt5Svg)
BuildRequires: pkgconfig(Qt5UiTools)
BuildRequires: pkgconfig(Qt5WebKit)
BuildRequires: pkgconfig(Qt5WebKitWidgets)
BuildRequires: pkgconfig(Qt5Xml)
BuildRequires: pkgconfig(Qt5XmlPatterns)
BuildRequires: pkgconfig(libpulse-mainloop-glib)
BuildRequires: pkgconfig(libpulse)
BuildRequires: pkgconfig(hunspell)
BuildRequires: pkgconfig(poppler)
BuildRequires: pkgconfig(poppler-cpp)

%description
Interactive whiteboard for schools and universities.

%prep
%setup
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch4 -p1

%build
%qmake_qt5 INCLUDEPATH+=%_includedir/quazip5 INCLUDEPATH+=%_includedir/poppler %name.pro
%make_build

%install
%makeinstall_std
install -D -m 0644 resources/images/OpenBoard.png %buildroot%_pixmapsdir/OpenBoard.png

# missing desktop file, creating one
mkdir -p %buildroot%_desktopdir/
cat > %buildroot%_desktopdir/%name.desktop <<EOF
[Desktop Entry]
Encoding=UTF-8
Name=%name
GenericName=%name
Comment=Interactive whiteboard for schools and universities
Exec=%dest_dir/run.sh "%f"
Icon=%name
StartupNotify=true
Terminal=false
Type=Application
MimeType=application/x-%name;
Categories=Qt;KDE;Education;Engineering;
X-SuSE-translate=false
EOF

install -D -m 0755 build/linux/release/product/%name %buildroot%dest_dir/%name
cp -r build/linux/release/product/* %buildroot%dest_dir/

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

env QT_PLUGIN_PATH=\$QT_PLUGIN_PATH:%dest_dir/%name/plugins LD_LIBRARY_PATH=\$LD_LIBRARY_PATH:%dest_dir/plugins/cffadaptor %dest_dir/%name "\$@"
EOF
chmod 0755 %buildroot%dest_dir/run.sh
mkdir -p %buildroot/%_bindir/
ln -s -T %dest_dir/run.sh %buildroot/%_bindir/%name

# clean some exe bits
find %buildroot -executable -type f -name *.js -exec chmod -x '{}' \+
find %buildroot -executable -type f -name *.svg -exec chmod -x '{}' \+
find %buildroot -executable -type f -name *.css -exec chmod -x '{}' \+
find %buildroot -executable -type f -name *.xml -exec chmod -x '{}' \+
find %buildroot -executable -type f -name *.html -exec chmod -x '{}' \+

# internalization
lrelease-qt5 -removeidentical %name.pro
mkdir -p %buildroot%dest_dir/i18n/
cp -R resources/i18n/%{name}*.qm %buildroot%dest_dir/i18n/

# customizations
cp -R resources/customizations %buildroot%dest_dir/

%files
%doc COPYRIGHT LICENSE
%_desktopdir/%name.desktop
%_pixmapsdir/%name.png
%_libdir/OpenBoard
%_bindir/%name

%changelog
* Wed Jan 31 2018 Anton Midyukov <antohami@altlinux.org> 1.3.6-alt2%ubt
- Fix build for ALT Sisyphus.

* Mon Nov 13 2017 Anton Midyukov <antohami@altlinux.org> 1.3.6-alt1%ubt
- Initial build for ALT Sisyphus.
