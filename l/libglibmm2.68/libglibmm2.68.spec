%def_disable snapshot

%define rname glibmm
%define ver_major 2.76
%define ver_base 2.68
%define api_ver %ver_base

%def_enable docs
# see %%setup section below
%def_enable check

Name: lib%rname%api_ver
Version: %ver_major.0
Release: alt1

Summary: C++ wrapper for GLib
License: LGPL-2.1 and GPL-2.0
Group: System/Libraries
Url: https://gtkmm.sourceforge.net/

%if_enabled snapshot
Source: %rname-%version.tar
%else
Source: ftp://ftp.gnome.org/pub/gnome/sources/glibmm/%ver_major/%rname-%version.tar.xz
%endif

%define glib_ver 2.76
%define sigc_ver 3.0.0

%add_perl_lib_path %_libdir/glibmm-%api_ver/proc/pm
# to avoid duplicate provides remove self-satisfied perl deps
# basename -a -s .pm tools/pm/*.pm| sed -E 's;$;\\\\|;g' |tr -d '\n'
%define pm_deps DocsParser\\|Enum\\|FunctionBase\\|Function\\|GtkDefs\\|Object\\|Output\\|Property\\|Util\\|WrapParser
%filter_from_provides /%pm_deps/d
%filter_from_requires /%pm_deps/d

BuildRequires(pre): meson
BuildRequires: mm-common gcc-c++
BuildRequires: libgio-devel >= %glib_ver libsigc++3-devel >= %sigc_ver
BuildRequires: perl-XML-Parser
%{?_enable_docs:BuildRequires: docbook-style-xsl doxygen graphviz fonts-ttf-open-sans xsltproc}

%description
A C++ interface for glib library.

This package contains the library needed to run programs dynamically
linked with glibmm.

%package devel
Summary: Headers and development files of glibmm
Group: Development/GNOME and GTK+
Requires: %name = %version-%release

%description devel
A C++ interface for glib library.

This package contains the headers and development files that are needed,
when trying to develop or compile applications which need glibmm.

%package devel-doc
Summary: glibmm documentation
Group: Development/Documentation
BuildArch: noarch

%description devel-doc
Gtkmm provides a C++ interface to the GTK+ GUI library.
glibmm originally belongs to gtkmm, but is now separated,
for use with non-GUI software written in C++.

This package contains all API documentation for glibmm.


%prep
%setup -n %rname-%version
# online tests restricted in hasher
sed -i  '/giomm_tls_client/d' tests/meson.build

%build
%{?_enable_snapshot:mm-common-prepare -f}
%meson \
    %{?_enable_docs:-Dbuild-documentation=true} \
    %{?_enable_snapshot:-Dmaintainer-mode=true
    -Dbuild-documentation=true}
%nil
%meson_build

%install
%meson_install

%check
export LD_LIBRARY_PATH=%buildroot%_libdir
%meson_test

%files
%doc AUTHORS NEWS
%_libdir/*.so.*

%files devel
%_includedir/glibmm-%api_ver/
%_includedir/giomm-%api_ver/
%_libdir/*.so
%_libdir/glibmm-%api_ver/
%_libdir/giomm-%api_ver/
%_pkgconfigdir/*-%api_ver.pc

%if_enabled docs
%files devel-doc
%_docdir/%rname-%api_ver/
%_datadir/devhelp/books/%rname-%api_ver
%endif

%changelog
* Sun Mar 12 2023 Yuri N. Sedunov <aris@altlinux.org> 2.76.0-alt1
- 2.76.0

* Mon Sep 26 2022 Yuri N. Sedunov <aris@altlinux.org> 2.74.0-alt1
- 2.74.0

* Thu May 05 2022 Yuri N. Sedunov <aris@altlinux.org> 2.72.1-alt1
- 2.72.1

* Fri Apr 08 2022 Yuri N. Sedunov <aris@altlinux.org> 2.72.0-alt1
- 2.72.0

* Wed Oct 06 2021 Yuri N. Sedunov <aris@altlinux.org> 2.70.0-alt1
- 2.70.0

* Wed Oct 06 2021 Yuri N. Sedunov <aris@altlinux.org> 2.68.2-alt1
- 2.68.2

* Thu May 20 2021 Yuri N. Sedunov <aris@altlinux.org> 2.68.1-alt1
- 2.68.1

* Fri Dec 18 2020 Yuri N. Sedunov <aris@altlinux.org> 2.68.0-alt1
- 2.68.0 (new glibmm-2.68 library)
- -- end of glibmm-2.4 --

* Sun Dec 13 2020 Yuri N. Sedunov <aris@altlinux.org> 2.64.5-alt1
- 2.64.5

* Sat Nov 21 2020 Yuri N. Sedunov <aris@altlinux.org> 2.64.4-alt1
- 2.64.4 (ported to Meson build system)
- enabled %%check

* Sun Mar 22 2020 Yuri N. Sedunov <aris@altlinux.org> 2.64.2-alt1
- 2.64.2

* Thu Mar 19 2020 Yuri N. Sedunov <aris@altlinux.org> 2.64.1-alt1
- 2.64.1

* Sun Sep 22 2019 Yuri N. Sedunov <aris@altlinux.org> 2.62.0-alt1
- 2.62.0

* Tue Mar 19 2019 Yuri N. Sedunov <aris@altlinux.org> 2.60.0-alt1
- 2.60.0

* Sun Mar 17 2019 Yuri N. Sedunov <aris@altlinux.org> 2.58.1-alt1
- 2.58.1

* Wed Oct 31 2018 Yuri N. Sedunov <aris@altlinux.org> 2.58.0-alt1
- 2.58.0

* Sat Mar 31 2018 Yuri N. Sedunov <aris@altlinux.org> 2.56.0-alt1
- 2.56.0

* Tue Sep 19 2017 Yuri N. Sedunov <aris@altlinux.org> 2.54.1-alt1
- 2.54.1

* Wed Sep 13 2017 Yuri N. Sedunov <aris@altlinux.org> 2.54.0-alt1
- 2.54.0

* Mon Sep 04 2017 Yuri N. Sedunov <aris@altlinux.org> 2.52.1-alt1
- 2.52.1

* Fri Jun 23 2017 Yuri N. Sedunov <aris@altlinux.org> 2.52.0-alt1
- 2.52.0

* Tue Apr 04 2017 Yuri N. Sedunov <aris@altlinux.org> 2.50.1-alt1
- 2.50.1

* Tue Sep 20 2016 Yuri N. Sedunov <aris@altlinux.org> 2.50.0-alt1
- 2.50.0

* Thu Mar 31 2016 Yuri N. Sedunov <aris@altlinux.org> 2.48.1-alt1
- 2.48.1

* Mon Mar 28 2016 Yuri N. Sedunov <aris@altlinux.org> 2.48.0-alt1
- 2.48.0

* Fri Mar 18 2016 Yuri N. Sedunov <aris@altlinux.org> 2.47.92-alt1
- 2.47.92

* Wed Dec 16 2015 Yuri N. Sedunov <aris@altlinux.org> 2.46.3-alt1
- 2.46.3

* Fri Nov 20 2015 Yuri N. Sedunov <aris@altlinux.org> 2.46.2-alt1
- 2.46.2

* Tue Sep 22 2015 Yuri N. Sedunov <aris@altlinux.org> 2.46.1-alt1
- 2.46.1

* Fri May 29 2015 Anton Farygin <rider@altlinux.ru> 2.44.0-alt2
- rebuild in new environment

* Wed Mar 25 2015 Yuri N. Sedunov <aris@altlinux.org> 2.44.0-alt1
- 2.44.0

* Tue Sep 23 2014 Yuri N. Sedunov <aris@altlinux.org> 2.42.0-alt1
- 2.42.0

* Mon Apr 14 2014 Yuri N. Sedunov <aris@altlinux.org> 2.40.0-alt1
- 2.40.0

* Tue Mar 04 2014 Yuri N. Sedunov <aris@altlinux.org> 2.39.91-alt1
- 2.39.91

* Mon Nov 18 2013 Yuri N. Sedunov <aris@altlinux.org> 2.38.1-alt1
- 2.38.1

* Fri Oct 11 2013 Yuri N. Sedunov <aris@altlinux.org> 2.38.0-alt1
- 2.38.0

* Fri Sep 20 2013 Yuri N. Sedunov <aris@altlinux.org> 2.37.93-alt1
- 2.37.93

* Thu May 02 2013 Yuri N. Sedunov <aris@altlinux.org> 2.36.2-alt1
- 2.36.2

* Tue Apr 16 2013 Yuri N. Sedunov <aris@altlinux.org> 2.36.0-alt1
- 2.36.0

* Tue Mar 19 2013 Yuri N. Sedunov <aris@altlinux.org> 2.35.9-alt1
- 2.35.9

* Mon Nov 05 2012 Yuri N. Sedunov <aris@altlinux.org> 2.34.1-alt1
- 2.34.1

* Sun Oct 21 2012 Yuri N. Sedunov <aris@altlinux.org> 2.34.0-alt1
- 2.34.0

* Mon Oct 15 2012 Yuri N. Sedunov <aris@altlinux.org> 2.33.14-alt1
- 2.33.14

* Sat Sep 08 2012 Yuri N. Sedunov <aris@altlinux.org> 2.33.12-alt1
- 2.33.12

* Wed Jul 11 2012 Yuri N. Sedunov <aris@altlinux.org> 2.32.1-alt1
- 2.32.1

* Tue Apr 10 2012 Yuri N. Sedunov <aris@altlinux.org> 2.32.0-alt1
- 2.32.0

* Wed Mar 28 2012 Yuri N. Sedunov <aris@altlinux.org> 2.31.22-alt1
- 2.31.22

* Mon Jan 16 2012 Yuri N. Sedunov <aris@altlinux.org> 2.30.1-alt1
- 2.30.1

* Tue Sep 27 2011 Yuri N. Sedunov <aris@altlinux.org> 2.30.0-alt1
- 2.30.0

* Tue Jun 14 2011 Yuri N. Sedunov <aris@altlinux.org> 2.28.2-alt1
- 2.28.2

* Thu May 12 2011 Yuri N. Sedunov <aris@altlinux.org> 2.28.1-alt1
- 2.28.1

* Wed Apr 06 2011 Yuri N. Sedunov <aris@altlinux.org> 2.28.0-alt1
- 2.28.0

* Thu Mar 31 2011 Yuri N. Sedunov <aris@altlinux.org> 2.27.99.2-alt1
- 2.27.99.2

* Wed Mar 23 2011 Yuri N. Sedunov <aris@altlinux.org> 2.27.98-alt1
- 2.27.98

* Tue Mar 15 2011 Yuri N. Sedunov <aris@altlinux.org> 2.27.97-alt1
- 2.27.97

* Mon Feb 28 2011 Yuri N. Sedunov <aris@altlinux.org> 2.27.95-alt1
- 2.27.95

* Mon Feb 21 2011 Yuri N. Sedunov <aris@altlinux.org> 2.27.94-alt1
- 2.27.94

* Wed Feb 09 2011 Yuri N. Sedunov <aris@altlinux.org> 2.27.93-alt1
- 2.27.93

* Sun Oct 03 2010 Yuri N. Sedunov <aris@altlinux.org> 2.25.5-alt1
- 2.25.5

* Tue May 04 2010 Yuri N. Sedunov <aris@altlinux.org> 2.24.2-alt1
- 2.24.2

* Fri Apr 16 2010 Yuri N. Sedunov <aris@altlinux.org> 2.24.1-alt1
- 2.24.1

* Wed Apr 07 2010 Yuri N. Sedunov <aris@altlinux.org> 2.24.0-alt1
- 2.24.0

* Mon Jan 11 2010 Yuri N. Sedunov <aris@altlinux.org> 2.23.1-alt1
- 2.23.1

* Fri Oct 02 2009 Valery Inozemtsev <shrek@altlinux.ru> 2.22.1-alt1
- 2.22.1

* Mon Sep 21 2009 Valery Inozemtsev <shrek@altlinux.ru> 2.20.2-alt1
- 2.20.2

* Tue Nov 04 2008 Vitaly Lipatov <lav@altlinux.ru> 2.18.1-alt1
- new version 2.18.1 (with rpmrb script)

* Sat Apr 12 2008 Vitaly Lipatov <lav@altlinux.ru> 2.16.1-alt1
- new version 2.16.1 (with rpmrb script)

* Sun Jan 13 2008 Vitaly Lipatov <lav@altlinux.ru> 2.14.2-alt1
- new version (2.14.2)
- rename source package to libglibmm
- cleanup spec

* Sun Apr 29 2007 Vitaly Lipatov <lav@altlinux.ru> 2.13.4-alt1
- new version 2.13.4 (with rpmrb script)

* Sat Apr 07 2007 Vitaly Lipatov <lav@altlinux.ru> 2.13.3-alt1
- new version 2.13.3 (with rpmrb script)

* Sun Nov 12 2006 Vitaly Lipatov <lav@altlinux.ru> 2.13.2-alt0.1
- new version 2.13.2 (with rpmrb script)

* Sat Sep 02 2006 Vitaly Lipatov <lav@altlinux.ru> 2.12.0-alt0.1
- new version 2.12.0 (with rpmrb script)

* Fri Jul 21 2006 Vitaly Lipatov <lav@altlinux.ru> 2.11.2-alt0.1
- new version 2.11.2 (with rpmrb script)
- use major in spec

* Tue Feb 21 2006 Vitaly Lipatov <lav@altlinux.ru> 2.9.1-alt0.1
- new version 2.9.1 (with rpmrb script)

* Sun Sep 11 2005 Vitaly Lipatov <lav@altlinux.ru> 2.8.0-alt1
- new version

* Thu Mar 17 2005 Vitaly Lipatov <lav@altlinux.ru> 2.6.1-alt1
- new version

* Thu Jan 20 2005 Vitaly Lipatov <lav@altlinux.ru> 2.5.4-alt1
- new version
- build with gcc3.4

* Sat Dec 18 2004 Vitaly Lipatov <lav@altlinux.ru> 2.5.1-alt1
- new version
- fix static package
- fix descriptions

* Mon Nov 08 2004 Vitaly Lipatov <lav@altlinux.ru> 2.4.5-alt1
- new version

* Sat Sep 04 2004 Vitaly Lipatov <lav@altlinux.ru> 2.4.4-alt1
- new version

* Thu Jul 15 2004 Vitaly Lipatov <lav@altlinux.ru> 2.4.3-alt1
- new version
- use a macro for ldconfig
- remove LICENSE from doc

* Wed Jun 09 2004 Vitaly Lipatov <lav@altlinux.ru> 2.4.2-alt1
- new version

* Mon May 24 2004 Vitaly Lipatov <lav@altlinux.ru> 2.4.1-alt1
- first build for Sisyphus (thanks Mandrake)

* Tue May 04 2004 Abel Cheung <deaddog@deaddog.org> 2.4.1-1mdk
- New version

* Tue Apr 27 2004 Abel Cheung <deaddog@deaddog.org> 2.4.0-1mdk
- First Mandrake package

