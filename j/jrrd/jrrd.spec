Name: jrrd
Version: 1.0.5
Release: alt1
License: GPL
Group: Databases
Summary: Java interface to RRDTool
URL: http://www.opennms.org/
Source: %name-%version.tar.gz
Packager: Slava Dubrovskiy <dubrsl@altlinux.ru>

BuildRequires: /proc jpackage-1.6-compat librrd-devel gcc

%description
A Java native interface (JNI) to RRDTool

%package -n lib%name
Summary: Java interface to RRDTool
Group: Databases
Provides: %name = %version-%release

%description -n lib%name
A Java native interface (JNI) to RRDTool

%prep
%setup -n %name-%version

%build
%autoreconf
%configure
make

%install
%makeinstall

%files -n lib%name
%_libdir/libjrrd*
%_datadir/java/*.jar

%changelog
* Sat Dec 31 2011 Slava Dubrovskiy <dubrsl@altlinux.org> 1.0.5-alt1
- New version

* Mon Apr 26 2010 Slava Dubrovskiy <dubrsl@altlinux.org> 1.0.3-alt3
- Rebuild with new rrd
- Use jpackage-1.6-compat instead jpackage-1.5-compat

* Sat Nov 29 2008 Slava Dubrovskiy <dubrsl@altlinux.org> 1.0.3-alt2
- Remmove depricated ldconfig call in post

* Sun Aug 10 2008 Slava Dubrovskiy <dubrsl@altlinux.ru> 1.0.3-alt1
- Build for ALT
