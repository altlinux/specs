Name: libexosip2
Version: 4.1.0
Release: alt1

Group: System/Libraries
Summary: The eXtended osip library
License: LGPL
Url: http://savannah.nongnu.org/projects/exosip/
# git://git.sv.gnu.org/exosip
Source0: %name-%version.tar
BuildRequires: libosip2-devel >= 3.5.0
BuildRequires: libssl-devel libcares-devel

%description
eXosip is a GPL library that  extend  the  capability  of
the oSIP library. It aims  to  implement  a  simple  high
layer API to control the SIP for sessions establishements
and common extensions.

%package devel
Summary: Headers, libraries and docs for the eXosip library
Group: Development/C
Requires: %name = %version-%release

%description devel
eXosip is a GPL library that  extend  the  capability  of
the oSIP library. It aims  to  implement  a  simple  high
layer API to control the SIP for sessions establishements
and common extensions.

This package contains header files and development libraries needed to
develop programs using the eXosip library.

%package -n exosip-tools
Summary: Headers, libraries and docs for the eXosip library
Group: Development/C
Requires: %name = %version-%release

%description -n exosip-tools
eXosip is a GPL library that  extend  the  capability  of
the oSIP library. It aims  to  implement  a  simple  high
layer API to control the SIP for sessions establishements
and common extensions.

This package contains tools related to eXosip library.

%prep
%setup
./autogen.sh

%build
%configure \
	--disable-static \
	--enable-semaphore \
	--enable-sysv \
	--enable-openssl
%make_build

%install
%makeinstall_std

%files
%doc AUTHORS ChangeLog NEWS README
%_libdir/*.so.*

%files devel
%_libdir/*.so
%_includedir/*

%files -n exosip-tools
%_bindir/sip_reg

%changelog
* Wed Sep 10 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.1.0-alt1
- Version 4.1.0

* Fri Apr 19 2013 Dmitry V. Levin (QA) <qa_ldv@altlinux.org> 3.5.0-alt1.qa1
- NMU: rebuilt for updated dependencies.

* Sat Feb 12 2011 Egor Glukhov <kaman@altlinux.org> 3.5.0-alt1
- 3.5.0

* Wed Nov 24 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.4.0-alt1.git.2d7c3bbb.1
- Rebuilt for soname set-versions

* Wed Jul 28 2010 Egor Glukhov <kaman@altlinux.org> 3.4.0-alt1.git.2d7c3bbb
- Initial build for Sisyphus

