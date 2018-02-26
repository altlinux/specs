Name: libzen
Version: 0.4.24
Release: alt1

Group: System/Libraries
Summary: %name - Shared library for libmediainfo and medianfo-related programs
License: LGPL
Url: http://mediainfo.sourceforge.net
Packager: Sergei Epiphanov <serpiph@altlinux.ru>

Source0: %{name}_%{version}.tar.bz2

BuildRequires: gcc-c++
#BuildRequires: dos2unix
#BuildRequires: doxygen
BuildRequires: libwxGTK-devel

%package devel
Group: System/Libraries
Summary: Devel package for %name
Requires: %name = %version
Provides: %name.so

%description
Base shared library for libmediainfo and medianfo-related programs

%description devel
This package contains files for development with libzen.

%prep
%setup -q -T -b 0 -n ZenLib

%build
#dos2unix      *.txt Source/Doc/*.txt
#chmod 644    *.txt Source/Doc/*.txt
#pushd Source/Doc
#doxygen Doxyfile
#popd
#cp Source/Doc/*.txt ./
pushd Project/GNU/Library
%autoreconf
%configure --enable-shared --enable-static=no --with-wxwidgets=system
%make
popd

%install
pushd Project/GNU/Library
%makeinstall
popd
# Add here commands to install the package
install -dm 755 %buildroot%_includedir/ZenLib
install -m 644 Source/ZenLib/*.h %buildroot%_includedir/ZenLib
#install -dm 755 %buildroot%_includedir/ZenLib/Base64
#install -m 644 Source/ZenLib/Base64/*.h %buildroot%_includedir/ZenLib/Base64
install -dm 755 %buildroot%_includedir/ZenLib/HTTP_Client
install -m 644 Source/ZenLib/HTTP_Client/*.h %buildroot%_includedir/ZenLib/HTTP_Client
install -dm 755 %buildroot%_includedir/ZenLib/Format/Html
install -m 644 Source/ZenLib/Format/Html/*.h %buildroot%_includedir/ZenLib/Format/Html
install -dm 755 %buildroot%_includedir/ZenLib/Format/Http
install -m 644 Source/ZenLib/Format/Http/*.h %buildroot%_includedir/ZenLib/Format/Http
#install -dm 755 %buildroot%_includedir/ZenLib/TinyXml
#install -m 644 Source/ZenLib/TinyXml/*.h %buildroot%_includedir/ZenLib/TinyXml

sed -i -e 's|Version: |Version: %{version}|g' Project/GNU/Library/libzen.pc
install -dm 755 %buildroot%_libdir/pkgconfig
install -m 644 Project/GNU/Library/libzen.pc %buildroot%_pkgconfigdir

%files
%doc ReadMe.txt
%_libdir/*.so.*

%files devel
%_includedir/ZenLib
%_pkgconfigdir/libzen.pc
%_libdir/*.so

%changelog
* Sat Feb 18 2012 Sergei Epiphanov <serpiph@altlinux.ru> 0.4.24-alt1
- New version

* Sat Dec 03 2011 Sergei Epiphanov <serpiph@altlinux.ru> 0.4.23-alt1
- New version

* Thu Jul 21 2011 Sergei Epiphanov <serpiph@altlinux.ru> 0.4.21-alt1
- New version

* Sun Mar 06 2011 Sergei Epiphanov <serpiph@altlinux.ru> 0.4.18-alt2
- Update from source

* Mon Feb 28 2011 Sergei Epiphanov <serpiph@altlinux.ru> 0.4.18-alt1
- New version

* Sun Oct 24 2010 Sergei Epiphanov <serpiph@altlinux.ru> 0.4.16-alt2
- Add TinyXml

* Mon Oct 18 2010 Sergei Epiphanov <serpiph@altlinux.ru> 0.4.16-alt1
- New version

* Wed Mar 10 2010 Sergei Epiphanov <serpiph@altlinux.ru> 0.4.11-alt2
- Rebuild with libwxGTK

* Tue Mar 02 2010 Sergei Epiphanov <serpiph@altlinux.ru> 0.4.11-alt1
- New version

* Wed Feb 10 2010 Sergei Epiphanov <serpiph@altlinux.ru> 0.4.10-alt1
- New version

* Mon Nov 23 2009 Sergei Epiphanov <serpiph@altlinux.ru> 0.4.9-alt1
- New version

* Thu Nov 12 2009 Sergei Epiphanov <serpiph@altlinux.ru> 0.4.8-alt1
- New version

* Mon Nov 09 2009 Sergei Epiphanov <serpiph@altlinux.ru> 0.4.3-alt1
- initial build
