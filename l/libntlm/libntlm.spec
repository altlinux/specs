Name: libntlm
Version: 1.5
Release: alt1

Summary: NTLMv1 authentication library
License: LGPL-2.1-or-later
Group: System/Libraries
Url: https://nongnu.org/libntlm/
# https://nongnu.org/libntlm/releases/%name-%version.tar.gz
Source: %name-%version.tar

%description
%name is a library for authenticating with Microsoft NTLMv1
challenge-response, derived from Samba sources.

Warning: NTLMv1 is not a secure authentication protocol -- it uses MD4
and single-DES.  MD4 has been broken, and single-DES have a too small
key size to be considered secure against brute-force attacks.  One
should consider using libntlm for interoperability purposes only,
not to achieve any kind of security.

%package devel
Summary: Files for development of %name-based applications
Group: Development/C
Requires: %name = %version-%release

%description devel
This package contains files for development of %name-based applications.

%prep
%setup

%build
%configure --disable-static
%make_build

%install
%makeinstall_std

%check
%make_build -k check

%set_verify_elf_method strict
%define _unpackaged_files_terminate_build 1

%files
%_libdir/*.so.*
%doc AUTHORS NEWS README THANKS

%files devel
%_libdir/*.so
%_includedir/*.h
%_pkgconfigdir/*.pc

%changelog
* Fri Aug 24 2018 Dmitry V. Levin <ldv@altlinux.org> 1.5-alt1
- 1.3 -> 1.5.

* Fri Dec 09 2011 Dmitry V. Levin <ldv@altlinux.org> 1.3-alt1
- Updated to 1.3.

* Mon Dec 06 2010 Sergey V Turchin <zerg@altlinux.org> 1.2-alt2
- rebuilt

* Thu Aug 26 2010 Sergey V Turchin <zerg@altlinux.org> 1.2-alt1
- new version

* Mon Dec 21 2009 Sergey V Turchin <zerg@altlinux.org> 1.0-alt2
- remove ldconfig from %%post

* Wed Apr 30 2008 Sergey V Turchin <zerg at altlinux dot org> 1.0-alt1
- new version

* Wed Apr 30 2008 Sergey V Turchin <zerg at altlinux dot org> 0.4.2-alt1
- new version

* Wed Jan 09 2008 Sergey V Turchin <zerg at altlinux dot org> 0.4.1-alt1
- new version

* Mon Jan 29 2007 Sergey V Turchin <zerg at altlinux dot org> 0.3.12-alt1
- new version

* Fri Jun 02 2006 Sergey V Turchin <zerg at altlinux dot org> 0.3.9-alt1
- new version

* Wed Aug 17 2005 Sergey V Turchin <zerg at altlinux dot org> 0.3.7-alt1
- new version

* Wed Feb 09 2005 Sergey V Turchin <zerg at altlinux dot org> 0.3.6-alt1
- initial spec

