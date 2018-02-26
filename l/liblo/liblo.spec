%def_disable static

Name: liblo
Version: 0.25
Release: alt2.1

Summary: Open Source implementation of the Open Sound Control protocol
License: GPL
Group: System/Libraries
Url: http://plugin.org.uk/%name
Packager: Eugene Ostapets <eostapets@altlinux.ru>

Source: %url/%name-%version.tar.gz

# Automatically added by buildreq on Mon Dec 04 2006
BuildRequires: doxygen gcc-c++

%description
%name is a lightweight, easy to use implementation of the Open Sound
Control protocol (see http://www.cnmat.berkeley.edu/OpenSoundControl/
for details).

%package devel
Summary: Headers for developing programs that will use %name
Group: Development/C
Requires: %name = %version-%release

%description devel
This package contains the headers that programmers will need to develop
applications which will use %name.

%prep
%setup -q

%build
%configure \
    %{subst_enable static}

sed -ri 's/^(hardcode_libdir_flag_spec|runpath_var)=.*/\1=/' libtool
%make_build

%install
%makeinstall

%files
%_libdir/*.so.*
%doc AUTHORS README

%files devel
%_bindir/oscdump
%_bindir/oscsend
%_includedir/*
%_libdir/*.so
%_libdir/pkgconfig/*
%doc ChangeLog
%doc doc/html 
%doc examples/*.c

%changelog
* Sat Feb 04 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.25-alt2.1
- Removed bad RPATH

* Thu Oct 28 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.25-alt2
- Rebuilt for soname set-versions

* Mon Dec 15 2008 Yuri N. Sedunov <aris@altlinux.org> 0.25-alt1
- new version
- removed obsolete %%post{,un}_ldconfig

* Sun Jun 17 2007 Eugene Ostapets <eostapets@altlinux.ru> 0.24-alt1
- new version

* Mon Dec 04 2006 Eugene Ostapets <eostapets@altlinux.ru> 0.23-alt1
- new version for ardour 2.0beta9.

* Tue Sep 21 2004 Yuri N. Sedunov <aris@altlinux.ru> 0.9-alt1
- new version.

* Sat Jul 31 2004 Yuri N. Sedunov <aris@altlinux.ru> 0.8-alt1
- First build for Sisyphus.

