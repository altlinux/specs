Summary: Library to access different kinds of (video) capture devices
Name: libunicap
Version: 0.9.8
Release: alt3.1
License: GPLv2+
Group: Development/C
Url: http://www.unicap-imaging.org/
Packager: Vitaly Kuznetsov <vitty@altlinux.ru>

Source: libunicap-%version.tar.gz
Source1: unicap-filter.sh
Patch: libunicap-0.9.8-alt-v4l.patch

BuildRequires: gtk-doc intltool libraw1394-devel libv4l-devel

%description
Unicap provides a uniform interface to video capture devices. It allows
applications to use any supported video capture device via a single API.
The included ucil library provides easy to use functions to render text
and graphic overlays onto video images.

%package devel
Summary: Development files for the unicap library
Group: Development/C
Requires: %name = %version-%release

%description devel
The libunicap-devel package includes header files and libraries necessary for
for developing programs which use the unicap, unicapgtk and ucil library. It
contains the API documentation of the library, too.

%prep
%setup -q
%patch -p2
%autoreconf

%build
%configure --enable-libv4l
%make_build

%install
%makeinstall_std

# Don't install any static .a and libtool .la files
rm -f %buildroot%_libdir/{,unicap2/cpi/}*.{a,la}

%find_lang unicap

%files -f unicap.lang
%doc AUTHORS ChangeLog COPYING README
%_libdir/*.so.*
%_libdir/unicap2

%files devel
%_libdir/*.so
%_pkgconfigdir/*.pc
%_includedir/unicap
%_datadir/gtk-doc/html/*

%changelog
* Thu Jul 12 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.9.8-alt3.1
- Fixed build

* Mon Mar 21 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.9.8-alt3
- rebuild for debuginfo

* Tue Dec 14 2010 Vitaly Kuznetsov <vitty@altlinux.ru> 0.9.8-alt2
- rebuild for soname set-version

* Wed May 26 2010 Vitaly Kuznetsov <vitty@altlinux.ru> 0.9.8-alt1
- 0.9.8

* Mon Jan 11 2010 Vitaly Kuznetsov <vitty@altlinux.ru> 0.9.6-alt2
- %%autoreconf added to repair build

* Sun Aug 16 2009 Vitaly Kuznetsov <vitty@altlinux.ru> 0.9.6-alt1
- 0.9.6

* Tue Jun 23 2009 Vitaly Kuznetsov <vitty@altlinux.ru> 0.9.5-alt2
- rebuild with new libpng

* Tue Apr 21 2009 Vitaly Kuznetsov <vitty@altlinux.ru> 0.9.5-alt1
- 0.9.5
- resurrected old changelog

* Wed Mar 11 2009 Vitaly Kuznetsov <vitty@altlinux.ru> 0.9.3-alt1
- 0.9.3

* Mon Jul 21 2008 Yury Aliaev <mutabor@altlinux.org> 0.2.24-alt1
- Upgrade to 0.2.24
- Russian translation updated

* Wed Jun 19 2008 Yury Aliaev <mutabor@altlinux.org> 0.2.23-alt1
- initial build for ALT Linux Sisyphus (based on FC spec)
- Russian translation added

* Mon May 19 2008 Robert Scheck <robert@fedoraproject.org> 0.2.23-1
- Upgrade to 0.2.23
- Corrected packaging of cpi/*.so files (thanks to Arne Caspari)

* Sat May 17 2008 Robert Scheck <robert@fedoraproject.org> 0.2.22-1
- Upgrade to 0.2.22 (#446021)

* Sat Feb 16 2008 Robert Scheck <robert@fedoraproject.org> 0.2.19-3
- Added patch to correct libdir paths (thanks to Ralf Corsepius)

* Mon Feb 04 2008 Robert Scheck <robert@fedoraproject.org> 0.2.19-2
- Changes to match with Fedora Packaging Guidelines (#431381)

* Mon Feb 04 2008 Robert Scheck <robert@fedoraproject.org> 0.2.19-1
- Upgrade to 0.2.19
- Initial spec file for Fedora and Red Hat Enterprise Linux
