Name: libzen
Version: 0.4.40
Release: alt1

Group: System/Libraries
Summary: %name - Shared library for libmediainfo and medianfo-related programs
License: Zlib
Url: http://mediainfo.sourceforge.net

Source: https://mediaarea.net/download/source/%name/%version/%{name}_%{version}.tar.xz

BuildRequires: gcc-c++

%package devel
Group: System/Libraries
Summary: Devel package for %name
Requires: %name = %version-%release
Provides: %name.so

%description
Base shared library for libmediainfo and medianfo-related programs

%description devel
This package contains files for development with libzen.

%prep
%setup -q -T -b 0 -n ZenLib

%build
pushd Project/GNU/Library
%add_optflags %(getconf LFS_CFLAGS)
%autoreconf
%configure --enable-shared --enable-static=no
%make
popd

%install
pushd Project/GNU/Library
%makeinstall_std
popd

%files
%doc ReadMe.txt
%_libdir/*.so.*

%files devel
%_includedir/ZenLib
%_pkgconfigdir/libzen.pc
%_libdir/*.so

%changelog
* Fri Dec 23 2022 Yuri N. Sedunov <aris@altlinux.org> 0.4.40-alt1
- 0.4.40

* Sat Mar 27 2021 Yuri N. Sedunov <aris@altlinux.org> 0.4.39-alt1
- 0.4.39

* Fri Apr 03 2020 Yuri N. Sedunov <aris@altlinux.org> 0.4.38-alt1
- 0.4.38
- fixed License tag

* Fri Aug 25 2017 Yuri N. Sedunov <aris@altlinux.org> 0.4.37-alt1
- 0.4.37

* Tue Apr 04 2017 Yuri N. Sedunov <aris@altlinux.org> 0.4.35-alt1
- 0.4.35

* Tue Aug 25 2015 Motsyo Gennadi <drool@altlinux.ru> 0.4.31-alt1
- 0.4.31

* Wed Oct 01 2014 Motsyo Gennadi <drool@altlinux.ru> 0.4.29-alt1
- 0.4.29

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
