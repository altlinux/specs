Name: qt-at-spi
Version: 0.1.1
Release: alt4

Summary: Qt plugin that bridges Qt's accessibility API to AT-SPI2
Url: git://gitorious.org/qt-at-spi/qt-at-spi.git
License: LGPL v2.1+
Group: Accessibility

Source: %name-%version.tar
Patch0: fix-undefined.patch

BuildRequires: libqt4-devel libat-spi2-core-devel gcc-c++

%description
This is a Qt plugin that bridges Qt's accessibility API to AT-SPI2.
With recent versions of AT-SPI2 this should make Qt applications accessible
with the help of tools such as Gnome's Orca screen-reader.

This package contains example and test programs.

%package -n libqspiaccessiblebridge
Summary: Qt plugin that bridges Qt's accessibility API to AT-SPI2
Group: Accessibility

%description -n libqspiaccessiblebridge
This is a Qt plugin that bridges Qt's accessibility API to AT-SPI2.
With recent versions of AT-SPI2 this should make Qt applications accessible
with the help of tools such as Gnome's Orca screen-reader.
 
This package contains the library.

%package doc
Summary: Qt plugin that bridges Qt's accessibility API to AT-SPI2
Group: Accessibility
BuildArch: noarch

%description doc
This is a Qt plugin that bridges Qt's accessibility API to AT-SPI2.
With recent versions of AT-SPI2 this should make Qt applications accessible
with the help of tools such as Gnome's Orca screen-reader.

This package contains the documentation.

%package profile
Summary: Qt plugin that bridges Qt's accessibility API to AT-SPI2
Group: Accessibility
BuildArch: noarch

%description profile
This is a Qt plugin that bridges Qt's accessibility API to AT-SPI2.
With recent versions of AT-SPI2 this should make Qt applications accessible
with the help of tools such as Gnome's Orca screen-reader.

This package contains the user session profile setting the environment
variables in order the bridge to work.

%prep
%setup
%patch0 -p2
find . -type f -name '*.pro' | while read FILE; do \
    echo "QMAKE_CXXFLAGS_RELEASE = %optflags" >> "$FILE"; \
    echo "QMAKE_CFLAGS_RELEASE = %optflags" >> "$FILE"; \
done

%build
qmake-qt4
%make

#cd doc
#qdoc3-qt4 qatspi.qdocconf

%install
%make_install INSTALL_ROOT=%buildroot install

install -D -m0755 examples/calculator/calculator %buildroot%_bindir/calculator
install -D -m0755 tests/tst_qt-atspi %buildroot%_bindir/tst_qt-atspi

mkdir -p -m0755 %buildroot%_sysconfdir/profile.d
echo "export QT_ACCESSIBILITY=1" >%buildroot%_sysconfdir/profile.d/%name.sh
echo "setenv QT_ACCESSIBILITY 1" >%buildroot%_sysconfdir/profile.d/%name.csh

%files -n libqspiaccessiblebridge
%_libdir/qt4/plugins/accessiblebridge
%_libdir/qt4/plugins/accessiblebridge/*.so
%doc README

%files
%_bindir/*

%files doc
#%doc doc/html
%doc doc/README.markdown
%doc doc/*.png

%files profile
%attr(0755,root,root) %_sysconfdir/profile.d/*.sh
%attr(0755,root,root) %_sysconfdir/profile.d/*.csh

%changelog
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

