%def_enable static

Name: libsdp
Summary: LD_PRELOAD-able library for using SDP
Version: 1.1.103
Release: alt1
License: %gpl2only
Group: System/Libraries
Url: http://www.openfabrics.org
Source: %name-%version.tar
Packager: Led <led@altlinux.ru>

BuildRequires(pre): rpm-build-licenses
BuildRequires: flex

%description
%name can be LD_PRELOAD-ed to have a sockets application use
InfiniBand Sockets Direct Protocol (SDP) instead of TCP, transparently
and without recompiling the application.


%package devel
Summary: Development files for the %name
Group: Development/C
Requires: %name = %version-%release

%description devel
Development files of %name.


%if_enabled static
%package devel-static
Summary: Static %name library
Group: Development/C
Requires: %name-devel = %version-%release

%description devel-static
Static %name library.
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
%doc README NEWS ChangeLog COPYING
%config(noreplace) %_sysconfdir/*
%_libdir/*.so.*


%files devel
%_libdir/*.so


%if_enabled static
%files devel-static
%_libdir/*.a
%endif


%changelog
* Thu Dec 16 2010 Timur Aitov <timonbl4@altlinux.org> 1.1.103-alt1
- New version

* Thu Aug 19 2010 Andriy Stepanov <stanv@altlinux.ru> 1.1.100-alt1
- New version (OFED 1.5.1)

* Mon Nov 02 2009 Igor Vlasenko <viy@altlinux.ru> 1.1.99-alt1.1
- NMU (by repocop): the following fixes applied:
  * post_ldconfig for libsdp
  * postun_ldconfig for libsdp

* Tue Oct 28 2008 Led <led@altlinux.ru> 1.1.99-alt1
- initial build for ALTLinux

* Sun Jul 22 2007 Vladimir Sokolovsky <vlad@mellanox.co.il>
- Initial packaging
