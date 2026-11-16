Name: wordtsar
Version: 0.5.1850
Release: alt1

Summary: A WordStar 7.0D Document mode clone
License: AGPL-3.0-or-later
Group: Editors
URL: https://wordtsar.ca/
Vcs: https://downloads.sourceforge.net/sourceforge/wordtsar/wordtsar-0.5.1850-src.zip

Source: %name-%version.tar
Source1: vendor.tar
Source2: WordTsar.desktop
Source3: %name.png

BuildRequires(pre): rpm-macros-cmake
BuildRequires(pre): rpm-macros-qt6
BuildRequires: cmake
BuildRequires: fontconfig-devel
BuildRequires: hunspell-en
BuildRequires: libhunspell-devel
BuildRequires: libfreetype-devel
BuildRequires: libharfbuzz-devel
BuildRequires: libpugixml-devel
BuildRequires: qt6-base-devel
BuildRequires: /proc
# upstream is not ready for GCC16:
%set_gcc_version 15
BuildRequires: gcc%_gcc_version-c++

%description
A WordStar 7.0D Document mode clone. It loads WordStar 4, WordStar 7, DOCX
and RTF files, and saves in WordStar 7 and RTF format.

%prep
%setup
tar -xf %SOURCE1 -C 'third-party'
sed -i -e '/typedef long ssize_t;/d' src/core/include/config.h
%ifarch %ix86
sed -i -e 's/-Wsign-conversion/-Wno-sign-conversion/' \
       -e 's/-Werror=sign-conversion/-Wno-error=sign-conversion/' \
       cmake/sources.cmake
%endif

%build
export LC_ALL=C.UTF-8
export CC=%__cc
export CXX=%__cxx
%cmake -DUPDATE_DEPENDENCIES=OFF \
       -Wno-author \
       %nil
%cmake_build

%install
install -D -m755 %_arch-alt-linux/WordTsar %buildroot%_bindir/%name
install -D -m755 %_arch-alt-linux/ws %buildroot%_bindir/ws
install -D -m644 %SOURCE2 %buildroot%_datadir/applications/%name.desktop
install -D -m644 %SOURCE3 %buildroot%_datadir/pixmaps/%name.png

%files
%doc LICENSE.md
%_bindir/%name
%_bindir/ws
%_datadir/applications/%name.desktop
%_datadir/pixmaps/%name.png

%changelog
* Mon Nov 16 2026 Andrew A. Vasilyev <andy@altlinux.org> 0.5.1850-alt1
- 0.5.1850
- move to Qt6 and cmake

* Tue Sep 23 2025 Andrew A. Vasilyev <andy@altlinux.org> 0.3.719-alt1
- Initial build for ALT.

