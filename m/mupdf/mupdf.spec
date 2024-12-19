%define soname 25
Name: mupdf
Version: 1.25.2
Release: alt1
Summary:  MuPDF is a lightweight open source software framework for viewing and converting PDF, XPS, and E-book documents.
Group: Office
URL: https://github.com/ArtifexSoftware/mupdf
License: AGPL-3.0

Source:  %name-%version.tar
Source1: %name-%version-thirdparty-extract.tar
Source2: %name-%version-thirdparty-lcms2.tar
Source3: %name-%version-thirdparty-mujs.tar

Patch0: disable_strip.patch

BuildRequires: make gcc-c++
BuildRequires: zlib-devel libopenjpeg2.0-devel libjbig2dec-devel libgumbo-devel
BuildRequires: libfreeglut-devel libfreetype-devel libharfbuzz-devel gdcm-devel libjpeg-devel
BuildRequires: libX11-devel libXext-devel

Requires: lib%name%soname = %EVR

%package -n lib%name%soname
Summary: MuPDF library for PDF render
Group: System/Libraries

%package -n lib%name-devel
Summary: Development files for MuPDF library
Group: Development/C
Requires: lib%name%soname = %EVR

%description
MuPDF is a lightweight open source software framework for viewing and converting PDF, XPS, and E-book documents.
%description -n lib%name%soname
MuPDF shared library
%description -n lib%name-devel
Header files for the MuPDF shared library

%prep
%setup -a1 -a2 -a3
%patch0 -p1

%build

%make_build shared-release USE_SYSTEM_LIBS=yes  FZ_ENABLE_PDF=1 \
	XCFLAGS="-I/usr/include/freetype2/ -I/usr/include/harfbuzz/ \
	-I/usr/include/gdcm/gdcmjpeg/ -I/usr/include/gdcm/gdcmjpeg/8/ \
	-I/usr/include/openjpeg-2.5/" \
	XLDFLAGS="-g -L/usr/lib64"  XLIBS="-lgdcmjpeg8" --trace

%install
#%%define _makeinstall_target install-shared-c install-apps install-docs
make INSTALL="/bin/install -p" \
	 USE_SYSTEM_LIBS=yes \
	 DESTDIR=%buildroot \
	 bindir=%_bindir \
	 libdir=%_libdir \
	 incdir=%_includedir \
	 mandir=%_mandir \
	 prefix=%_prefix \
	 install-shared-c install-apps install-docs

%files
%_bindir/mupdf-gl
%_bindir/mupdf-x11
%_bindir/muraster
%_bindir/mutool
%_mandir/man1/*

%files -n lib%name%soname
%_libdir/libmupdf.so.%{soname}*
%doc %_defaultdocdir/%name/CHANGES
%doc %_defaultdocdir/%name/COPYING
%doc %_defaultdocdir/%name/README

%files -n lib%name-devel
%_includedir/mupdf/*.h
%_includedir/mupdf/fitz/*.h
%_includedir/mupdf/pdf/*.h

%_libdir/libmupdf.so
%doc %_defaultdocdir/%name/examples/*

%changelog
* Wed Dec 18 2024 Oleg Proskurin <proskur@altlinux.org> 1.25.2-alt1
- Build new version

* Wed Dec 09 2020 Aleksei Nikiforov <darktemplar@altlinux.org> 1.18.0-alt1
- Updated to upstream version 1.18.0 (Fixes: CVE-2017-5991, CVE-2018-10289,
  CVE-2018-16647, CVE-2018-16648, CVE-2019-14975, CVE-2020-26519).

* Thu Oct 18 2018 Fr. Br. George <george@altlinux.ru> 1.13.0-alt3
- Rebuilt with libfreeglut

* Wed Oct 17 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 1.13.0-alt2
- NMU: rebuilt with libfreeglut.

* Tue Oct 02 2018 Fr. Br. George <george@altlinux.ru> 1.13.0-alt1
- Autobuild version bump to 1.13.0

* Wed Nov 18 2015 Fr. Br. George <george@altlinux.ru> 1.8-alt1
- Autobuild version bump to 1.8

* Sun Apr 19 2015 Fr. Br. George <george@altlinux.ru> 1.7-alt1
- Autobuild version bump to 1.7

* Wed Oct 22 2014 Fr. Br. George <george@altlinux.ru> 1.6-alt1
- Autobuild version bump to 1.6

* Mon Aug 25 2014 Fr. Br. George <george@altlinux.ru> 1.5-alt1
- Autobuild version bump to 1.5
- Partly resurrect debian platform files

* Tue Jun 03 2014 Fr. Br. George <george@altlinux.ru> 1.4-alt1
- Autobuild version bump to 1.4

* Thu Aug 22 2013 Fr. Br. George <george@altlinux.ru> 1.3-alt1
- Autobuild version bump to 1.3
- Fix build
- Keep builtin static openjpeg-2.0 until it arrives in distro

* Wed May 29 2013 Fr. Br. George <george@altlinux.ru> 1.1-alt1
- Initial build from FC

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Mon Jan 21 2013 Adam Tkac <atkac redhat com> - 1.1-2
- rebuild due to "jpeg8-ABI" feature drop

* Wed Jan 09 2013 Pavel Zhukov <landgraf@fedoraproject.org> - 1.1-1
- New release

* Sun May 20 2012  Pavel Zhukov <landgraf@fedoraproject.org> - 1.0-1
- New release

* Wed Mar 14 2012  Pavel Zhukov <landgraf@fedoraproject.org> - 0.9-2
- Fix buffer overflow (#752388)

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Thu Oct 27 2011 Pavel Zhukov <landgraf@fedoraproject.org> - 0.9-1
- New release

* Tue May 03 2011 Pavel Zhukov <landgraf@fedoraproject.org> - 0.8.165-2
- New upstream release
- Fix *.a and *.h permissions

* Sun Mar 27 2011 Pavel Zhukov <landgraf@fedoraproject.org> - 0.8.15-1
- New upstream release

* Wed Feb 09 2011 Pavel Zhukov <landgraf@fedoraproject.org> - 0.7-7
- Fix dependency for F13

* Mon Feb 07 2011 Pavel Zhukov <landgraf@fedoraproject.org> - 0.7-6
- roll back to static libraries  patch for shared libs has been rejected
- Fix spec errors

* Fri Jan 14 2011 Pavel Zhukov <landgraf@fedoraproject.org> - 0.7-4
- replac poitless macros to command names

* Fri Jan 14 2011 Pavel Zhukov <landgraf@fedoraproject.org> - 0.7-3
- Create patch for optflags
- Change Summary
- Fix Require for devel package

* Thu Jan 13 2011 Pavel Zhukov <landgraf@fedoraproject.org> -0.7-2
- add Fedora CFLAGS
- create patch for use shared library

* Wed Jan 12 2011 Pavel Zhukov <landgraf@fedoraproject.org>  - 0.7-1
- Initial package
