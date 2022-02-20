Name: uefitool
Version: 0.28.0
Release: alt1
Summary: UEFI firmware image viewer and editor
License: BSD-2-Clause
Group: Development/Tools
Url: https://github.com/LongSoft/UEFITool
Source0: %name-%version.tar
Source1: %name.desktop
BuildRequires: pkgconfig(Qt5Core)
BuildRequires: pkgconfig(Qt5Gui)
BuildRequires: pkgconfig(Qt5Widgets)
BuildRequires: /usr/bin/icns2png

%description
UEFITool is a cross-platform C++/Qt program for parsing, extracting and
modifying UEFI firmware images.

It supports parsing of full BIOS images starting with the flash descriptor or
any binary files containing UEFI volumes.

This package contains the GUI utility, UEFITool.
For the CLI versions, see uefitool-cli.

%package cli
Group: Development/Tools
Summary: UEFI firmware image viewer and editor - cli version

%description cli
UEFITool is a cross-platform C++/Qt program for parsing, extracting and
modifying UEFI firmware images.
 It supports parsing of full BIOS images starting with the flash descriptor or
any binary files containing UEFI volumes.

This package contains the CLI utilities, UEFIPatch and UEFIReplace.
For the GUI version, see uefitool.

%prep
%setup

%build
%qmake_qt5
%make_build
for i in UEFIPatch UEFIReplace; do
  pushd $i
    %qmake_qt5
    %make_build
  popd
done

%install
install -Dpm 0755 UEFITool %buildroot/%_bindir/UEFITool
install -Dpm 0755 UEFIPatch/UEFIPatch %buildroot/%_bindir/UEFIPatch
install -Dpm 0755 UEFIReplace/UEFIReplace %buildroot/%_bindir/UEFIReplace
install -Dpm 0644 %SOURCE1 %buildroot/%_desktopdir/%name.desktop
icns2png -x %name.icns; \
for px in 16 32 128 256 512; do \
	size=${px}x${px}; \
	fn=%{name}_${size}x32.png; \
	if [ -f ${fn} ]; then \
		dir=%buildroot%_iconsdir/hicolor/${size}/apps/; \
		mkdir -p ${dir}; \
		mv ${fn} ${dir}/%name.png; \
	fi; \
done;

%files
%doc LICENSE.md README.rst
%_bindir/UEFITool
%_iconsdir/hicolor/*/apps/%name.png
%_desktopdir/%name.desktop

%files cli
%_bindir/UEFIPatch
%_bindir/UEFIReplace

%changelog
* Sun Feb 20 2022 Anton Farygin <rider@altlinux.ru> 0.28.0-alt1
- first build for ALT
