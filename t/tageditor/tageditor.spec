%define _unpackaged_files_terminate_build 1

Name: tageditor
Version: 3.9.9
Release: alt1

Summary: A tag editor with a Qt GUI and a command-line interface
Group: Development/C++
License: GPL-2.0-or-later
Url: https://github.com/Martchus/tageditor
Vcs: https://github.com/Martchus/tageditor
ExclusiveArch: %qt6_qtwebengine_arches

Source: %name-%version.tar

BuildRequires(pre): rpm-macros-cmake
BuildRequires(pre): rpm-macros-qt6-webengine
BuildRequires: cmake
BuildRequires: gcc-c++
BuildRequires: libtagparser-devel
BuildRequires: libmartchus-c++utilities-devel
BuildRequires: libmartchus-qtutilities-devel
BuildRequires: qt6-declarative-devel
BuildRequires: qt6-tools-devel
BuildRequires: qt6-webengine-devel
BuildRequires: iso-codes

%description
A tag editor with a Qt GUI and a command-line interface. It supports MP4
(iTunes), ID3, Vorbis, Opus, FLAC, and Matroska. The tag editor can also
display technical information such as the ID, format, language, bitrate,
duration, size, timestamps, sampling frequency, FPS and other information
of the tracks. It also allows one to inspect and validate the element structure
of MP4 and Matroska files.

%prep
%setup

%build
%cmake \
  -DCMAKE_BUILD_TYPE=Release \
  -DBUILD_SHARED_LIBS:BOOL=ON \
  -DPACKAGE_NAMESPACE=martchus \
  -DQT_PACKAGE_PREFIX:STRING=Qt6 \
  -DKF_PACKAGE_PREFIX:STRING=KF6 \
  -DBUILTIN_TRANSLATIONS:BOOL=ON \
  -DWEBVIEW_PROVIDER:STRING=webengine \
  -DJS_PROVIDER:STRING=qml \
  -DLANGUAGE_FILE_ISO_639_2=%_datadir/iso-codes/json/iso_639-2.json
%cmake_build

%install
%cmake_install

%files
%doc LICENSE README.md LICENSE.LESSER
%_bindir/tageditor
%_datadir/applications/tageditor-renamingutility.desktop
%_datadir/applications/tageditor.desktop
%_datadir/bash-completion/completions/tageditor
%_datadir/icons/hicolor/scalable/apps/tageditor.svg
%_datadir/metainfo/io.github.martchus.tageditor.metainfo.xml

%changelog
* Mon Mar 23 2026 Arseniy Kostevich <faux@altlinux.org> 3.9.9-alt1
- Initial build for ALT.
