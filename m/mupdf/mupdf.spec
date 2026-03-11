%define _unpackaged_files_terminate_build 1
%define abiversion 27
%define sominor 2
%define soname %abiversion.%sominor
%define python3_name python3-module-mupdf

Name: mupdf
Version: 1.27.2
Release: alt1

Summary: MuPDF is a lightweight open source software framework for viewing and converting PDF, XPS, and E-book documents
License: AGPL-3.0-or-later
Group: Office

Url: https://github.com/ArtifexSoftware/mupdf

Source0: %name-%version.tar
Source1: %name-%version-thirdparty-extract.tar
Source2: %name-%version-thirdparty-lcms2.tar
Source3: %name-%version-thirdparty-mujs.tar

Patch0: mupdf-1.25.2-alt1-disable_strip.patch
Patch1: mupdf-1.25.6-alt1-do-not-require-libclang-and-swig.patch
Patch2: mupdf-1.25.6-alt1-no-venv.patch
Patch3: mupdf-1.26.10-alt1-disable-auto-rpath.patch

BuildRequires: make gcc-c++
BuildRequires: zlib-devel libopenjpeg2.0-devel libjbig2dec-devel libgumbo-devel
BuildRequires: libfreeglut-devel libfreetype-devel libharfbuzz-devel gdcm-devel libjpeg-devel
BuildRequires: libX11-devel libXext-devel
BuildRequires: python3-module-clang
BuildRequires: clang-devel
BuildRequires: swig
BuildRequires: python3-dev
BuildRequires: tesseract-devel
BuildRequires: libbrotli-devel
BuildRequires: libXrandr-devel

Requires: libmupdf%abiversion = %EVR

%package -n libmupdf%abiversion
Summary: MuPDF library for PDF render
Group: System/Libraries

%package -n libmupdf-devel
Summary: Development files for MuPDF library
Group: Development/C
Requires: libmupdf%abiversion = %EVR

%package -n libmupdfcpp%abiversion
Summary: C++ bindings for MuPDF
Group: System/Libraries

%package -n %python3_name
Summary: Python bindings for MuPDF
Group: System/Libraries

%package tools
Summary: Command line tools for MuPDF
Group: Office
Conflicts: mupdf < 1.27.1

%description
MuPDF is a lightweight open source software framework for viewing
and converting PDF, XPS, and E-book documents.

%description -n libmupdf%abiversion
MuPDF shared library

%description -n libmupdf-devel
Header files for the MuPDF shared library

%description -n libmupdfcpp%abiversion
The mupdf package contains the mupdf C++ library files.

%description -n %python3_name
The python3 package contains low level mupdf python bindings.

%description tools
The mupdf-tools package contains the mutool command line tool for
manipulating PDF, XPS, and E-book documents without graphical interface.
Ideal for server environments where graphical libraries are not required.

%prep
%setup -a1 -a2 -a3
%autopatch -p1

%build
# NB: lcms2-art is a fork, mujs is also special to mupdf
# (cf. debian/opensuse build files)
make_mupdf() {
	%make_build --trace \
	USE_SYSTEM_LIBS=yes \
	USE_TESSERACT=yes \
	FZ_ENABLE_PDF=1 \
	XCFLAGS="-I%_includedir/freetype2 \
		 -I%_includedir/harfbuzz \
		 -I%_includedir/gdcm/gdcmjpeg \
		 -I%_includedir/gdcm/gdcmjpeg/8 \
		 -I%_includedir/openjpeg-2.5" \
	XLDFLAGS="-g -L%_libdir" \
	XLIBS="-lgdcmjpeg8" \
	"$@"
}

# Lack of proper deps makes separate builds neccessary
make_mupdf shared-release
make_mupdf libs python apps

%install
# Not %%makeinstall as DESTDIR would get doubled then
%make_install \
	 USE_SYSTEM_LIBS=yes \
	 DESTDIR=%buildroot \
	 bindir=%_bindir \
	 libdir=%_libdir \
	 incdir=%_includedir \
	 mandir=%_mandir \
	 prefix=%prefix \
	 install-shared-c \
	 install-shared-python \
	 install-apps \
	 install-docs \
	 pydir=%python3_sitelibdir

rm -f %buildroot%_libdir/libmupdf-third.a \
      %buildroot%_libdir/libmupdf.a

# Deleting installed from makefile upstream documentation(install-docs)
rm -r %buildroot%_defaultdocdir/mupdf

# Installing examples for later packaging
install -Dm644 docs/examples/* -t %buildroot%_defaultdocdir/mupdf/examples

%files
%doc CHANGES COPYING README
%_bindir/mupdf-gl
%_bindir/mupdf-x11
%_man1dir/mupdf.1*

%files -n libmupdf%abiversion
%_libdir/libmupdf.so.%abiversion
%_libdir/libmupdf.so.%soname

%files -n libmupdfcpp%abiversion
%_libdir/libmupdfcpp.so.%abiversion
%_libdir/libmupdfcpp.so.%soname

%files -n libmupdf-devel
%_includedir/%name/
%_libdir/libmupdf.so
%_libdir/libmupdfcpp.so
%dir %_defaultdocdir/mupdf/examples
%doc %_defaultdocdir/mupdf/examples/*

%files -n %python3_name
%dir %python3_sitelibdir/mupdf
%python3_sitelibdir/mupdf/__init__.py
%python3_sitelibdir/mupdf/__pycache__/
%python3_sitelibdir/mupdf/_mupdf.so

%files tools
%_bindir/mutool
%_man1dir/mutool.1*

%changelog
* Tue Mar 10 2026 Evgeniy Martynenko <enimalojd@altlinux.org> 1.27.2-alt1
- New version (1.27.2).

* Wed Feb 25 2026 Michael Shigorin <mike@altlinux.org> 1.27.1-alt2
- Less fragile BR: (fixes build for sisyphus_e2k).
- Build before installation, not during it.
- Spec cleanup.

* Thu Feb 12 2026 Martynenko Evgeniy <enimalojd@altlinux.org> 1.27.1-alt1
- New version (1.27.1).
- Splited mutool into separate mupdf-tools subpackage.
- Switched MuPDF library packages to ABI-based naming.

* Tue Sep 30 2025 Martynenko Evgeniy <enimalojd@altlinux.org> 1.26.10-alt1
- New version (1.26.10).

* Mon May 12 2025 Martynenko Evgeniy <enimalojd@altlinux.org> 1.25.6-alt2
- Built with tesseract ocr.

* Mon Apr 14 2025 Martynenko Evgeniy <enimalojd@altlinux.org> 1.25.6-alt1
- New version 1.25.6.
- Build C++/Python bindings.

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
