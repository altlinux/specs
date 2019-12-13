Name: libcmis
Version: 0.5.2
Release: alt5.git.172e837

Summary: A C++ client library for the CMIS interface
License: GPLv2+ or LGPLv2+ or MPLv1.1
Group: System/Libraries

Url: https://github.com/tdf/libcmis
Source: %name-%version.tar
Patch: %name-0.4.1-alt2.1.patch
Patch2: %name-0.5.2-alt-boost-compat.patch

BuildRequires: gcc-c++
BuildRequires: pkgconfig(libcurl)
BuildRequires: pkgconfig(libxml-2.0)
BuildRequires: pkgconfig(cppunit) >= 1.12

BuildRequires: boost-devel boost-program_options-devel
BuildRequires: doxygen
BuildRequires: xmlto

%description
LibCMIS is a C++ client library for the CMIS interface. This allows C++
applications to connect to any ECM behaving as a CMIS server like
Alfresco, Nuxeo for the open source ones.

%package devel
Summary: Development files for %name
Group: Development/C++
Requires: %name = %version-%release

%description devel
The %name-devel package contains libraries and header files for
developing applications that use %name.

%package tools
Summary: Command line tool to access CMIS
Group: Publishing
Requires: %name = %version-%release

%description tools
The %name-tools package contains a tool for accessing CMIS from the
command line.

%prep
%setup
%patch -p1
%patch2 -p2

%build
touch ChangeLog
mkdir -p m4
%autoreconf
%configure --disable-static --disable-werror --disable-tests \
	DOCBOOK2MAN='xmlto man'
%make_build

%install
%makeinstall_std

%files
%doc AUTHORS COPYING.* NEWS README.md
%_libdir/*.so.*

%files devel
%_includedir/*
%_libdir/*.so
%_pkgconfigdir/*.pc

%files tools
%_bindir/*
%_man1dir/*.1*

%changelog
* Tue Dec 03 2019 Aleksei Nikiforov <darktemplar@altlinux.org> 0.5.2-alt5.git.172e837
- Rebuilt with boost-1.71.0.

* Mon Dec 17 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 0.5.2-alt4.git.172e837
- NMU: upstream master snapshot 172e83762b2b4b300073212ffd841dc90680bb86

* Wed Oct 31 2018 Michael Shigorin <mike@altlinux.org> 0.5.2-alt3.git.738528
- E2K: no more difference

* Thu May 31 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 0.5.2-alt2.git.738528
- NMU: rebuilt with boost-1.67.0

* Mon May 28 2018 Alexey Shabalin <shaba@altlinux.ru> 0.5.2-alt1.git.738528
- rebuild with new boost (ALT #34948)

* Mon Feb 12 2018 Alexey Shabalin <shaba@altlinux.ru> 0.5.2-alt0.git.738528
- upstream master snapshot 738528d790b2b1d52d9b72d673842969a852815d

* Mon Feb 12 2018 Alexey Shabalin <shaba@altlinux.ru> 0.5.1-alt1
- 0.5.1

* Sun Aug 27 2017 Michael Shigorin <mike@altlinux.org> 0.5.0-alt4
- E2K:
  + drop boost patch (only spoils things with lcc)
  + disable manpage build

* Mon Jul 31 2017 Fr. Br. George <george@altlinux.ru> 0.5.0-alt3
- Rebuild with boost 1.63.0

* Sun Jun 14 2015 Gleb F-Malinovskiy <glebfm@altlinux.org> 0.5.0-alt2.1
- Rebuilt for gcc5 C++11 ABI.

* Wed Feb 04 2015 Fr. Br. George <george@altlinux.ru> 0.5.0-alt2
- Fix incomplete source import

* Tue Feb 03 2015 Fr. Br. George <george@altlinux.ru> 0.5.0-alt1
- Autobuild version bump to 0.5.0
- Change packaging scheme

* Sat Jan 03 2015 Ivan A. Melnikov <iv@altlinux.org> 0.4.1-alt2.1
- rebuild with boost 1.57.0

* Thu Mar 20 2014 Fr. Br. George <george@altlinux.ru> 0.4.1-alt2
- fix incorrectly formed patch

* Wed Mar 19 2014 Fr. Br. George <george@altlinux.ru> 0.4.1-alt1
- new version

* Tue Aug 13 2013 Alexey Shabalin <shaba@altlinux.ru> 0.3.1-alt1
- initial build
