%define _name libxml++
%define ver_major 3.0
%define api_ver 3.0

Name: %{_name}3
Version: %ver_major.1
Release: alt1

Summary: C++ wrapper for the libxml2 XML parser library
Group: System/Libraries
License: LGPLv2+
Url: http://libxmlplusplus.sourceforge.net/

Source: ftp://ftp.gnome.org/pub/gnome/sources/%_name/%ver_major/%_name-%version.tar.xz

BuildPreReq: mm-common
BuildRequires: libxml2-devel >= 2.7.7
BuildRequires: doxygen gcc-c++ libglibmm-devel >= 2.46.0

%description
libxml++ is a C++ wrapper for the libxml2 XML parser library.
It has SAX and DOM-like APIs, but does not attempt to conform exactly to
the DOM specification. Its API is simpler than the underlying libxml2 C API.

%package devel
Summary: Development files for %name
Group: Development/C++
Requires: %name = %version-%release

%description devel
This package contains the headers and libraries for libxml++ development.

%package devel-doc
Summary: Development documentation for %name
Group: Development/C++
BuildArch: noarch
Conflicts: %name-devel < %version

%description devel-doc
This package contains the development documentation for libxml++ library.

%prep
%setup -n %_name-%version

#sed -i 's|\(doctooldir\)\ glibmm\-2\.4|\1 mm-common-util|' configure

%build
%configure --disable-static
%make_build

%install
%makeinstall_std

%files
%_libdir/%_name-%api_ver.so.*
%doc AUTHORS NEWS README

%files devel
%_includedir/%_name-%api_ver/
%_libdir/%_name-%api_ver.so
%_libdir/%_name-%api_ver/
%_pkgconfigdir/%_name-%api_ver.pc

%files devel-doc
%_datadir/devhelp/books/%_name-%api_ver/*.devhelp2
%_docdir/%_name-%api_ver/*

%changelog
* Mon Nov 14 2016 Yuri N. Sedunov <aris@altlinux.org> 3.0.1-alt1
- 3.0.1

* Tue Feb 02 2016 Yuri N. Sedunov <aris@altlinux.org> 3.0.0-alt1
- 3.0.0

* Wed Oct 28 2015 Yuri N. Sedunov <aris@altlinux.org> 2.40.1-alt1
- 2.40.1

* Wed Sep 30 2015 Yuri N. Sedunov <aris@altlinux.org> 2.40.0-alt1
- 2.40.0

* Fri Jun 12 2015 Gleb F-Malinovskiy <glebfm@altlinux.org> 2.37.1-alt1.1
- Rebuilt for gcc5 C++11 ABI.

* Thu Nov 14 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.37.1-alt1
- Version 2.37.1

* Wed Feb 06 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.36.0-alt1
- Version 2.36.0

* Thu Jan 26 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.34.2-alt1
- Version 2.34.2

* Thu Apr 28 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.34.1-alt1
- Version 2.34.1

* Sun Mar 20 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.30.1-alt3
- Fixed build

* Sat Mar 12 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.30.1-alt2
- Rebuilt for debuginfo

* Wed Nov 03 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.30.1-alt1.1
- Rebuilt for soname set-versions

* Tue May 04 2010 Yuri N. Sedunov <aris@altlinux.org> 2.30.1-alt1
- 2.30.1
- new devel-doc noarch subpackage
- spec cleanup

* Wed Jun 10 2009 Pavlov Konstantin <thresh@altlinux.ru> 2.26.0-alt1
- 2.26.0 release.
- Remove unneeded %%post calls.

* Thu Aug 14 2008 Pavlov Konstantin <thresh@altlinux.ru> 2.23.2-alt1
- 2.23.2 release.

* Fri Sep 21 2007 Pavlov Konstantin <thresh@altlinux.ru> 2.20.0-alt1
- 2.20.0 release.

* Wed Aug 22 2007 Pavlov Konstantin <thresh@altlinux.ru> 2.19.1-alt1
- 2.19.1 release.
- Some spec cleanup.

* Wed Jun 27 2007 Pavlov Konstantin <thresh@altlinux.ru> 2.18.1-alt1
- 2.18.1 release.

* Mon Mar 12 2007 Pavlov Konstantin <thresh@altlinux.ru> 2.18.0-alt1
- 2.18.0 release.

* Fri Jan 05 2007 Pavlov Konstantin <thresh@altlinux.ru> 2.17.2-alt1
- 2.17.2 release.

* Fri Dec 15 2006 Pavlov Konstantin <thresh@altlinux.ru> 2.17.1-alt2
- Pack unpackaged file.

* Thu Dec 14 2006 Pavlov Konstantin <thresh@altlinux.ru> 2.17.1-alt1
- 2.17.1 release.

* Fri Nov 03 2006 Pavlov Konstantin <thresh@altlinux.ru> 2.14.0-alt1
- ALTLinuxized.

* Sun Sep 03 2006 Konstantin Ryabitsev <icon@fedoraproject.org> - 2.14.0-1.1
- FC6 rebuild

* Tue May 02 2006 Konstantin Ryabitsev <icon@fedoraproject.org> - 2.14.0-1
- Version 2.14.0

* Mon Feb 13 2006 Konstantin Ryabitsev <icon@fedoraproject.org> - 2.12.0-2.1
- FC5 Rebuild

* Thu Jan 26 2006 Konstantin Ryabitsev <icon@fedoraproject.org> - 2.12.0-2
- Rebuilt to address RH #178592

* Thu Sep 08 2005 Konstantin Ryabitsev <icon@linux.duke.edu> - 2.12.0-1
- Version 2.12.0
- Use --disable-static for configure.

* Thu Jul 21 2005 Konstantin Ryabitsev <icon@linux.duke.edu> - 2.10.0-1
- Version 2.10.0
- Rearrange and conform to new FE standards
- Buildrequire glibmm24-devel
- Add devel requires to -devel

* Sun May 22 2005 Jeremy Katz <katzj@redhat.com> - 0.26.0-5
- rebuild on all arches

* Fri Apr  7 2005 Michael Schwendt <mschwendt[AT]users.sf.net>
- rebuilt

* Tue Nov 04 2003 Panu Matilainen <pmatilai@welho.com> - 0:0:26.0-0.fdr.3
- remove empty .libs directories

* Mon Nov  3 2003 Michael Schwendt <mschwendt[AT]users.sf.net> - 0:0.26.0-0.fdr.2
- buildrequires graphviz
- devel package requires main package and pkgconfig
- own %%_includedir/libxml++-1.0
- clean up examples tree

* Tue Oct 21 2003 Panu Matilainen <pmatilai@welho.com>
- Initial Fedora packaging

