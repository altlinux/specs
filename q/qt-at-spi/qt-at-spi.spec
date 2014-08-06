Name: qt-at-spi
Version: 0.3.1
Release: alt1

Summary: Qt plugin that bridges Qt's accessibility API to AT-SPI2
Url: git://anongit.kde.org/qtatspi
License: LGPL v2.1+
Group: Accessibility

Source: %name-%version.tar
Patch0: fix-undefined.patch

BuildRequires: libqt4-devel libat-spi2-core-devel gcc-c++ cmake kde4libs-devel chrpath

%description
This is a Qt plugin that bridges Qt's accessibility API to AT-SPI2.
With recent versions of AT-SPI2 this should make Qt applications accessible
with the help of tools such as Gnome's Orca screen-reader.

This package contains example and test programs.

%prep
%setup
#%patch0 -p2
#find . -type f -name '*.pro' | while read FILE; do \
#    echo "QMAKE_CXXFLAGS_RELEASE = %optflags" >> "$FILE"; \
#    echo "QMAKE_CFLAGS_RELEASE = %optflags" >> "$FILE"; \
#done

%build
mkdir build
cd build
cmake ..
%make
chrpath -r %_libdir/kde4/devel ./lib/libqspiaccessiblebridge.so
cd ..

cd doc
qdoc3-qt4 qatspi.qdocconf
cd ..

%install
%__install -d -m 755 %buildroot%_libdir/qt4/plugins/accessiblebridge
%__install -pD -m 644 build/lib/libqspiaccessiblebridge.so %buildroot%_libdir/qt4/plugins/accessiblebridge/libqspiaccessiblebridge.so

%files
%_libdir/qt4/plugins/accessiblebridge
%doc LICENSE README doc/html doc/TODO
#%doc doc/README.markdown
#%doc doc/*.png

%changelog
* Wed Aug 06 2014 Michael Pozhidaev <msp@altlinux.ru> 0.3.1-alt1
- New version
- All subpackages gathered in single package qt-at-spi (as well-recognized by users of other distros)

* Thu Mar 22 2012 Paul Wolneykien <manowar@altlinux.ru> 0.1.1-alt4
- Add C Shell profile.
- Fix suffix and permissions for the Shell profile.

* Tue Mar 20 2012 Paul Wolneykien <manowar@altlinux.ru> 0.1.1-alt3
- Make the documentation package noarch.
- Add "profile" package defining the environment variables.

* Tue Mar 06 2012 Paul Wolneykien <manowar@altlinux.ru> 0.1.1-alt2
- Fix undefined methods for Repocop.

* Mon Feb 27 2012 Paul Wolneykien <manowar@altlinux.ru> 0.1.1-alt1
- Initial build for ALT Linux.

