Name: libxcbutil-proto
Version: 1.12
Release: alt1
Summary: XCB protocol descriptions
License: MIT
Group: System/Libraries
Url: http://xcb.freedesktop.org
Packager: Evgenii Terechkov <evg@altlinux.org>
BuildArch: noarch

Source: %name-%version.tar
Patch: %name-%version-%release.patch

BuildRequires: rpm-build-python

%description
XCB is a project to enable efficient language bindings to the X11 protocol.
This package contains the protocol descriptions themselves.  Language
bindings use these protocol descriptions to generate code for marshalling
the protocol.

%prep
%setup

%build
%autoreconf
# Bit of a hack to get the pc file in /usr/share, so we can be noarch.
%configure --libdir=%{_datadir}
%make_build

%install
%make DESTDIR=%buildroot pkgpythondir=%python_sitelibdir/xcbgen install

%files
%_datadir/pkgconfig/xcb-proto.pc
%dir %_datadir/xcb/
%_datadir/xcb/*.xsd
%_datadir/xcb/*.xml
%python_sitelibdir/xcbgen
%doc COPYING NEWS README TODO HACKING doc/xml-xcb.txt

%changelog
* Fri Jul 15 2016 Sergey V Turchin <zerg@altlinux.org> 1.12-alt1
- 1.12

* Fri Oct 30 2015 Sergey V Turchin <zerg@altlinux.org> 1.11-alt1
- 1.11 (ALT #31415)

* Sun Mar 30 2014 Terechkov Evgenii <evg@altlinux.org> 1.10-alt1
- 1.10 (ALT #29918)

* Wed Sep  5 2012 Terechkov Evgenii <evg@altlinux.org> 1.7.1-alt1
- Initial build for ALT Linux Sisyphus
