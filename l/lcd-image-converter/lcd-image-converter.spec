# BEGIN SourceDeps(oneline):
BuildRequires: gcc-c++ qt5-base-devel qt5-declarative-devel qt5-script-devel qt5-svg-devel qt5-xmlpatterns-devel qt5-tools
# END SourceDeps(oneline)
%define _unpackaged_files_terminate_build 1

Name: lcd-image-converter
# NOTE: run .gear/update-revision.h.sh after git pull!
# NOTE: timestamp is from last git commit
Version: 2.1.0.20200816
Release: alt1
Summary: Tool to create bitmaps and fonts for embedded applications
Group: Other
License: GPL-3
URL: http://www.riuson.com/lcd-image-converter

# git: https://github.com/riuson/lcd-image-converter
Source0: %name-%version.tar
Source1: revision.h
Source2: %name.png
Patch: lcd-image-converter.pro-manual-revision.h.patch

%description
Allows you to create bitmaps and fonts, and transform them to "C" source format for embedded applications.

- Supported display controllers
  - Monochrome, grayscale, color
  - With vertical and horizontal orientation of bytes
  - 8, 16, 24, 32-bit data
  - 1...32 bits per pixel
  - and other, not limited by some particular models
- Output format
  - Can be changed by templates
  - Text (source code) or binary
- Create a single image
  - With RLE compression
- Create fonts (set of images - characters)
  - Including unicode charset
  - Required characters only, not full range
- Command-line mode

%prep
%setup -q
%patch -p0
install -m644 %{SOURCE1} resources/revision.h

%build
%_qt5_bindir/lrelease %name.pro
%qmake_qt5
%make_build

%install
%install_qt5

install -m755 -D release/linux/output/%name  %buildroot%_bindir/%name
install -m644 -D %{SOURCE2} %buildroot%_liconsdir/%name.png

# missing desktop file, creating one
mkdir -p %buildroot%_desktopdir/
cat > %buildroot%_desktopdir/%name.desktop <<EOF
[Desktop Entry]
Encoding=UTF-8
Name=%name
GenericName=%name
Comment=Tool to create bitmaps and fonts for embedded applications
Exec=%name
Icon=%name
StartupNotify=true
Terminal=false
Type=Application
Categories=Education;Engineering;
EOF

%files
%doc readme.md license
%_bindir/%name
%_liconsdir/%name.png
%_desktopdir/%name.desktop

%changelog
* Wed Sep 09 2020 Igor Vlasenko <viy@altlinux.ru> 2.1.0.20200816-alt1
- git update

* Thu Oct 17 2019 Igor Vlasenko <viy@altlinux.ru> 2.1.0.20190317-alt1
- initial import by package builder

