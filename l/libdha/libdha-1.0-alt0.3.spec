Packager: Repocop Q. A. Robot <repocop@altlinux.org>
%define subst_enable_to() %{expand:%%{?_enable_%{1}:--enable-%{2}}} %{expand:%%{?_disable_%{1}:--disable-%{2}}}

%def_enable static
%def_enable shared
%def_enable svgalib_helper

%define svnrev 21861

Name: libdha
Version: 1.0
Release: alt1
Summary: Library of Direct Hardware Access
License: GPL
Group: System/Libraries
URL: http://www.mplayerhq.hu
# svn checkout svn.mplayerhq.hu/mplayer/trunk/libdha
Source: %name-svn-r%svnrev.tar.bz2
Patch0: %name-1.0-configure.patch.gz
Patch1: %name-svn-r21861-bswap.patch.gz

# Automatically added by buildreq on Wed Aug 30 2006
#BuildRequires: linux-libc-headers mawk

BuildRequires: awk
%{?_enable_svgalib_helper:BuildRequires: svgalib-devel}

%description
%name - Library of Direct Hardware Access.
This library was designed for direct hardware access under different OS
and architectures.
This library is based on gfxdump utility from GATOS project.
Note: This library requires ROOT privileges or SUID'ed executable file
(same as XServer). (Or use %name kernel helper or svgalib_helper.)


%package devel
Summary: Header for library of Direct Hardware Access
Group: Development/C
Requires: %name%{?_disable_shared:-devel-static} = %version-%release

%description devel
Header for library of Direct Hardware Access.


%if_enabled static
%package devel-static
Summary: Static library of Direct Hardware Access
Group: Development/C
Requires: %name-devel = %version-%release

%description devel-static
Static library of Direct Hardware Access.
%endif


%prep
%setup -q -n %name-svn-r%svnrev
%patch0 -p1
%patch1 -p1


%build
CFLAGS="%optflags" sh ./configure --prefix=%_prefix --libdir=%_libdir \
    %{subst_enable_to svgalib_helper svgalib-helper} \
    --cc=gcc
%if_disabled shared
%if_disabled static
echo
echo "Must be enabled shared or static or both!"
exit 1
%endif
%else
%make_build
%endif
%{?_enable_static:%make_build %name.a}


%install
%{?_enable_shared:%make_install LIBDIR=%buildroot%_libdir install}
%{?_enable_static:install -pD -m 0644 %name.a %buildroot%_libdir/%name.a}
install -d -m 0755 %buildroot%_includedir/%name
install -m 0644 %name.h %buildroot%_includedir/%name.h
install -m 0644 pci_*.h %buildroot%_includedir/%name/


%if_enabled shared
%files
%doc README
%_libdir/*.so.*
%endif


%files devel
%_includedir/*
%if_enabled shared
%_libdir/*.so
%else
%doc README
%endif


%if_enabled static
%files devel-static
%_libdir/*.a
%endif


%changelog
* Mon Nov 01 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0-alt1
- Rebuilt for soname set-versions

* Wed Nov 04 2009 Igor Vlasenko <viy@altlinux.ru> 1.0-alt0.3.1
- NMU (by repocop): the following fixes applied:
  * post_ldconfig for libdha
  * postun_ldconfig for libdha

* Wed Jan 10 2007 Led <led@altlinux.ru> 1.0-alt0.3
- new SVN snapshot (revision 21861)
- updated %name-svn-r21861-bswap.patch

* Mon Oct 02 2006 Led <led@altlinux.ru> 1.0-alt0.2
- updated libdha-1.0-configure.patch for ability use svgalib_helper
- enabled svgalib_helper

* Wed Aug 30 2006 Led <led@altlinux.ru> 1.0-alt0.1
- initial separate build
