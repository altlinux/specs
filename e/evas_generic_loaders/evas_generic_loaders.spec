%define ver_major 1.17
%define beta %nil

Name: evas_generic_loaders
Version: %ver_major.0
Release: alt1

Summary: A set of loaders for Evas
License: LGPLv2.1+
Group: System/Libraries
Url: http://www.enlightenment.org/

Source: http://download.enlightenment.org/rel/libs/%name/%name-%version%beta.tar.xz

Obsoletes: %{name}1.8 < %version
Provides:  %{name}1.8 = %version-%release

# to skip libreoffice dependency
%add_findreq_skiplist %_libdir/evas/utils/evas_generic_pdf_loader.libreoffice
#Requires: libreoffice

BuildRequires: gcc-c++ efl-libs-devel >= %ver_major
BuildRequires: libpoppler-devel
BuildRequires: libspectre-devel
BuildRequires: librsvg-devel
BuildRequires: gst-plugins1.0-devel
BuildRequires: zlib-devel
BuildRequires: libraw-devel libgomp-devel

%description
These are additional "generic" loaders for Evas that are stand-alone
executables that evas may run from its generic loader module. This means
that if they crash, the application loading the image does not crash
also. In addition the licensing of these binaries will not affect the
license of any application that uses Evas as this uses a completely
generic execution system that allows anything to be plugged in as a
loader.


%prep
%setup -n %name-%version%beta
# hardcoded path to soffice.bin
subst 's@/usr/lib@%_libdir@' src/bin/pdf/evas_generic_pdf_loader.libreoffice

%build
%configure --enable-gstreamer1
%make_build

%check
%make check

%install
%makeinstall_std

%files
%_libdir/evas/utils/*
%doc AUTHORS COPYING README

%changelog
* Tue Feb 02 2016 Yuri N. Sedunov <aris@altlinux.org> 1.17.0-alt1
- 1.17.0

* Mon Nov 09 2015 Yuri N. Sedunov <aris@altlinux.org> 1.16.0-alt1
- 1.16.0 release

* Mon Oct 26 2015 Yuri N. Sedunov <aris@altlinux.org> 1.16.0-alt0.1
- 1.16.0-beta3

* Tue Sep 15 2015 Yuri N. Sedunov <aris@altlinux.org> 1.15.0-alt2
- rebuilt against libraw.so.15

* Wed Aug 05 2015 Yuri N. Sedunov <aris@altlinux.org> 1.15.0-alt1
- 1.15.0 release

* Tue Jul 21 2015 Yuri N. Sedunov <aris@altlinux.org> 1.15.0-alt0.2
- 1.15.0 beta2

* Thu May 07 2015 Yuri N. Sedunov <aris@altlinux.org> 1.14.0-alt1
- 1.14.0 release

* Mon May 04 2015 Yuri N. Sedunov <aris@altlinux.org> 1.14.0-alt0.1
- 1.14.0-beta3

* Wed Sep 17 2014 Yuri N. Sedunov <aris@altlinux.org> 1.11.2-alt1
- 1.11.2

* Tue Feb 25 2014 Yuri N. Sedunov <aris@altlinux.org> 1.9.0-alt1
- 1.9.0

* Tue Jan 21 2014 Yuri N. Sedunov <aris@altlinux.org> 1.8.1-alt2
- rebuilt against libraw.so.10

* Tue Dec 10 2013 Yuri N. Sedunov <aris@altlinux.org> 1.8.1-alt1
- 1.8.1
- obsoletes/provides evas_generic_loaders < 1.8

* Wed Dec 04 2013 Yuri N. Sedunov <aris@altlinux.org> 1.8.0-alt1
- 1.8.0 for E18

* Fri Nov 08 2013 Yuri N. Sedunov <aris@altlinux.org> 1.7.9-alt1
- 1.7.9

* Fri Aug 23 2013 Yuri N. Sedunov <aris@altlinux.org> 1.7.8-alt1
- 1.7.8

* Wed May 15 2013 Yuri N. Sedunov <aris@altlinux.org> 1.7.7-alt1
- 1.7.7

* Tue Apr 23 2013 Yuri N. Sedunov <aris@altlinux.org> 1.7.6-alt2
- rebuilt against libpoppler.so.36

* Tue Apr 09 2013 Yuri N. Sedunov <aris@altlinux.org> 1.7.6-alt1
- 1.7.6

* Sun Apr 07 2013 Yuri N. Sedunov <aris@altlinux.org> 1.7.5-alt2
rebuilt against libpoppler.so.35

* Sat Jan 05 2013 Yuri N. Sedunov <aris@altlinux.org> 1.7.5-alt1
- 1.7.5

* Tue Dec 25 2012 Yuri N. Sedunov <aris@altlinux.org> 1.7.4-alt2
- built SVG loader

* Sat Dec 22 2012 Yuri N. Sedunov <aris@altlinux.org> 1.7.4-alt1
- 1.7.4

* Sat Dec 15 2012 Yuri N. Sedunov <aris@altlinux.org> 1.7.3-alt1
- 1.7.3

* Sat Nov 24 2012 Yuri N. Sedunov <aris@altlinux.org> 1.7.2-alt1
- 1.7.2

* Mon Oct 22 2012 Yuri N. Sedunov <aris@altlinux.org> 1.7.1-alt1
- 1.7.1

* Tue Sep 04 2012 Yuri N. Sedunov <aris@altlinux.org> 1.7.0-alt1
- 1.7.0

* Fri May 11 2012 Yuri N. Sedunov <aris@altlinux.org> 1.2.0-alt1
- 1.2.0

* Mon Dec 05 2011 Yuri N. Sedunov <aris@altlinux.org> 1.1.0-alt1
- first build for Sisyphus

