%def_disable pskc
%def_enable pam

Name: oath-toolkit
Version: 2.6.2
Release: alt1%ubt
Summary: Toolkit for one-time password authentication systems
License: %gpl3plus
Group: Security/Networking
Url: http://www.nongnu.org/oath-toolkit/
# git-vcs: https://gitlab.com/oath-toolkit/oath-toolkit.git
Source: %name-%version.tar
Patch1: %name-%version.patch

BuildRequires(pre): rpm-build-ubt rpm-build-licenses
BuildRequires: libgcrypt-devel
BuildRequires: pkgconfig(gtk-doc)
BuildRequires: pkgconfig(libxml-2.0)
BuildRequires: help2man gengetopt
%{?_enable_pskc:BuildRequires: pkgconfig(xmlsec1)}
%{?_enable_pam:BuildRequires: libpam-devel}

%description
The OATH Toolkit makes it possible to build one-time password
authentication systems. It contains shared libraries, command line
tools and a PAM module. Supported technologies include the
event-based HOTP algorithm (RFC4226) and the time-based TOTP algorithm
(RFC6238). OATH stands for Open AuTHentication, which is the
organization that specify the algorithms. For managing secret key
files, the Portable Symmetric Key Container (PSKC) format described in
RFC6030 is supported.

%package -n oathtool
Summary: OATH one-time password tool 
License: %gpl3plus
Group: Security/Networking

%description -n oathtool
The OATH Toolkit makes it possible to build one-time password
authentication systems. Supported technologies include the
event-based HOTP algorithm (RFC4226) and the time-based TOTP algorithm
(RFC6238).

This subpackage contains OATH one-time password tool.

%package -n pskctool
Summary: Manipulate Portable Symmetric Key Container (PSKC) data.
License: %gpl3plus
Group: Security/Networking

%description -n pskctool
The OATH Toolkit makes it possible to build one-time password
authentication systems. Supported technologies include the
event-based HOTP algorithm (RFC4226) and the time-based TOTP algorithm
(RFC6238).

This subpackage contains tool allows you to parse, print, validate,
sign and verify PSKC data.

%package -n pam_oath
Summary: PAM module for pluggable login authentication for OATH
License: %gpl3plus
Group: System/Base

%description -n pam_oath
The OATH Toolkit makes it possible to build one-time password
authentication systems.

This subpackage contains a module to integrate OATH into PAM.

%package -n liboath
Summary: Library for Open AuTHentication (OATH) HOTP support
License: %lgpl21plus
Group: System/Libraries

%description -n liboath
The OATH Toolkit makes it possible to build one-time password
authentication systems. Supported technologies include the
event-based HOTP algorithm (RFC4226) and the time-based TOTP algorithm
(RFC6238).

%package -n liboath-devel
Summary: Development files for the Open AuTHentication (OATH) HOTP support library
License: %lgpl21plus
Group: Development/C
Requires: liboath = %EVR

%description -n liboath-devel
The OATH Toolkit makes it possible to build one-time password
authentication systems.

This subpackage contains the header files for the HOTP/TOTP library.

%package -n libpskc
Summary: Library for Portable Symmetric Key Container
License: %lgpl21plus
Group: System/Libraries

%description -n libpskc
The OATH Toolkit makes it possible to build one-time password
authentication systems.

For managing secret key files, the Portable Symmetric Key Container
(PSKC) format described in RFC6030 is supported.

%package -n libpskc-devel
Summary: Development files for the Portable Symmetric Key Container library
License: %lgpl21plus
Group: Development/C
Requires: libpskc = %EVR

%description -n libpskc-devel
The OATH Toolkit makes it possible to build one-time password
authentication systems.

For managing secret key files, the Portable Symmetric Key Container
(PSKC) format described in RFC6030 is supported.

This subpackage contains the headers for this library.

%prep
%setup
%patch1 -p1
echo %version > .tarball-version
printf "gdoc_MANS =\ngdoc_TEXINFOS =\n" > liboath/man/Makefile.gdoc
printf "gdoc_MANS =\ngdoc_TEXINFOS =\n" > libpskc/man/Makefile.gdoc
touch ChangeLog

%build
%autoreconf
%configure  \
  --with-pam-dir=/%_lib/security \
  %{subst_enable pam} \
  %{subst_enable pskc} \
  --disable-static

# parallel build error
%make

%install
%makeinstall_std

%files -n oathtool
%_bindir/oathtool
%_man1dir/oathtool.*

%files -n pam_oath
%doc pam_oath/README
%doc pam_oath/COPYING
/%_lib/security/pam_oath.so

%files -n liboath
%doc liboath/COPYING
%_libdir/liboath.so.*

%files -n liboath-devel
%_libdir/liboath.so
%_includedir/liboath
%_pkgconfigdir/liboath.pc
#%doc %_datadir/gtk-doc/html/liboath
%_man3dir/oath_*

%if_enabled pskc
%files -n pskctool
%_bindir/pskctool
%_man1dir/pskctool.*
%_datadir/xml/pskc/

%files -n libpskc
%doc libpskc/README
%doc liboath/COPYING
%_libdir/libpskc.so.*

%files -n libpskc-devel
%_libdir/libpskc.so
%_includedir/pskc
%_pkgconfigdir/libpskc.pc
#%doc %_datadir/gtk-doc/html/libpskc
%_mani3dir/pskc_*
%endif

%changelog
* Wed Jun 06 2018 Alexey Shabalin <shaba@altlinux.ru> 2.6.2-alt1%ubt
- initial build

