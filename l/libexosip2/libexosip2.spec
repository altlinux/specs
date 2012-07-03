Name: libexosip2
Version: 3.5.0
Release: alt1

Group: System/Libraries
Summary: The eXtended osip library
License: LGPL
Url: http://savannah.nongnu.org/projects/exosip/
Packager: Egor Glukhov <kaman@altlinux.org>
Source0: %name-%version.tar
BuildRequires: libosip2-devel >= 3.5.0
BuildRequires: libssl-devel

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
%configure --disable-static
%make_build

%install
%make DESTDIR=%buildroot install

%files
%doc AUTHORS ChangeLog NEWS README
%_libdir/*.so.*

%files devel
%_libdir/*.so
%_includedir/*

%files -n exosip-tools
%_bindir/sip_reg

%changelog
* Sat Feb 12 2011 Egor Glukhov <kaman@altlinux.org> 3.5.0-alt1
- 3.5.0

* Wed Nov 24 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.4.0-alt1.git.2d7c3bbb.1
- Rebuilt for soname set-versions

* Wed Jul 28 2010 Egor Glukhov <kaman@altlinux.org> 3.4.0-alt1.git.2d7c3bbb
- Initial build for Sisyphus

