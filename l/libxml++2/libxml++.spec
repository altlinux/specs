%def_enable snapshot

%define _name libxml++
%define git_name libxmlplusplus
%define ver_major 2.42
%define api_ver 2.6

%def_disable doc
%def_enable check

Name: %{_name}2
Version: %ver_major.2
Release: alt1.1

Summary: C++ wrapper for the libxml2 XML parser library
Group: System/Libraries
License: LGPLv2+
Url: http://libxmlplusplus.sourceforge.net/

%if_disabled snapshot
Source: ftp://ftp.gnome.org/pub/gnome/sources/%_name/%ver_major/%_name-%version.tar.xz
%else
Vcs: https://github.com/libxmlplusplus/libxmlplusplus.git
Source: %git_name-%version.tar
%endif

BuildRequires(pre): rpm-macros-meson >= 0.55
BuildRequires: meson mm-common >= 1.0.4 gcc-c++
BuildRequires: libxml2-devel >= 2.7.7 libglibmm-devel >= 2.32.0
%{?_enable_doc:BuildRequires: doxygen graphviz docbook-style-xsl xsltproc}

%description
libxml++ is a C++ wrapper for the libxml2 XML parser library.
It has SAX and DOM-like APIs, but does not attempt to conform exactly to
the DOM specification. Its API is simpler than the underlying libxml2 C API.

%package devel
Summary: Development files for %name
Group: Development/C++
Requires: %name = %EVR

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
%setup -n %{?_disable_snapshot:%_name}%{?_enable_snapshot:%git_name}-%version

%build
%ifarch %e2k
%add_optflags -std=gnu++11
%endif
%{?_enable_snapshot:mm-common-prepare --force --copy}
%meson \
    %{?_enable_snapshot:-Dmaintainer-mode=true \
    %{?_disable_doc:-Dbuild-documentation=false}}
    %{?_enable_doc:-Dbuild-documentation=true}
%nil
%meson_build

%install
%meson_install

%check
%__meson_test

%files
%_libdir/*.so.*
%doc NEWS README*

%files devel
%_includedir/*
%_libdir/*.so
%_libdir/%_name-%api_ver
%_pkgconfigdir/*

%if_enabled doc
%files devel-doc
%_datadir/devhelp/books/%_name-%api_ver/*.devhelp2
%_docdir/%_name-%api_ver/*
%endif

%changelog
* Sun Dec 17 2023 Yuri N. Sedunov <aris@altlinux.org> 2.42.2-alt1.1
- updated to 2.42.2-14-g468bc74 (fixed build with libxml2-2.12.x)

* Fri Sep 09 2022 Yuri N. Sedunov <aris@altlinux.org> 2.42.2-alt1
- 2.42.2

* Thu May 27 2021 Yuri N. Sedunov <aris@altlinux.org> 2.42.1-alt1
- 2.42.1

* Fri Oct 02 2020 Yuri N. Sedunov <aris@altlinux.org> 2.42.0-alt1
- 2.42.0 (ported to Meson build system)

* Sat May 25 2019 Michael Shigorin <mike@altlinux.org> 2.40.1-alt4
- fix doc knob (and rename it from docs for consistency)
- E2K: explicit -std=gnu++11

* Tue May 15 2018 Yuri N. Sedunov <aris@altlinux.org> 2.40.1-alt3
- reverted broken
  "Replace (deprecated) Glib::Threads::Mutex with std::mutex."
  (ALT #34908)

* Thu Apr 05 2018 Yuri N. Sedunov <aris@altlinux.org> 2.40.1-alt2
- updated to 2.40.1-8-g174481a

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

