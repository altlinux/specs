%def_enable static

Name: libnes
Version: 1.1.0
Release: alt1
Summary: NetEffect RNIC Userspace Library
Group: System/Libraries
License: %gpl2only
Url: http://www.openfabrics.org
Source: %name-%version.tar
Requires: libibverbs
Packager: Repocop Q. A. Robot <repocop@altlinux.org>

BuildRequires(pre): rpm-build-licenses
BuildRequires: libibverbs-devel

%description
%name provides a device-specific userspace driver for NetEffect RNICs
for use with the libibverbs library.


%if_enabled static
%package devel-static
Summary: Static %name driver
Group: Development/C

%description devel-static
Static version of %name that may be linked directly to an application,
which may be useful for debugging.
%endif


%prep
%setup


%build
./autogen.sh
%configure %{subst_enable static}
%make_build


%install
%make_install DESTDIR=%buildroot install


%files
%doc AUTHORS COPYING
%_libdir/*.so
%_sysconfdir/libibverbs.d/*


%if_enabled static
%files devel-static
%_libdir/*.a
%endif


%changelog
* Wed Dec 15 2010 Timur Aitov <timonbl4@altlinux.org> 1.1.0-alt1
- New version

* Thu Aug 19 2010 Andriy Stepanov <stanv@altlinux.ru> 1.0.1-alt1
- New version (OFED 1.5.1)

* Wed Nov 04 2009 Igor Vlasenko <viy@altlinux.ru> 0.5-alt1.1
- NMU (by repocop): the following fixes applied:
  * post_ldconfig for libnes
  * postun_ldconfig for libnes

* Tue Oct 28 2008 Led <led@altlinux.ru> 0.5-alt1
- initial build for ALTLinux

* Wed Aug 29 2007 Glenn Grundstrom <ggrundstrom@neteffect.com> - 0.5
- Updated for OFED-1.3

* Fri Feb 16 2007 Glenn Grundstrom <ggrundstrom@neteffect.com> - 0.3
- Updated for OFED-1.2

* Wed May 10 2006 Glenn Grundstrom <ggrundstrom@neteffect.com> - 0.1
- First development effort
