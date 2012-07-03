%define _unpackaged_files_terminate_build 1

%def_with doxygen

Name: rapidsvn
Version: 0.9.8
Release: alt3

Summary: wxWidgets-based Subversion client
License: %gpl3plus
Group: Development/Other
Url: http://rapidsvn.tigris.org
Packager: Ilya Mashkin <oddity@altlinux.ru>

Source: http://www.rapidsvn.org/download/release/%version/%name-%version.tar.gz
Source10: %name.desktop
Patch1: %name-0.9.4-link.patch

BuildRequires: rpm-build-licenses

# From configure.in
BuildRequires: gcc-c++
BuildRequires: libsubversion-devel >= 1.4.2
BuildRequires: wxGTK-devel  libwxGTK-devel
BuildRequires: cppunit-devel
BuildRequires: docbook-style-xsl xsltproc
%{?_with_doxygen:BuildRequires: doxygen graphviz}

BuildRequires: libpango-devel libexpat-devel

%description
RapidSVN is a cross-platform GUI front-end for the Subversion revision system 
(http://subversion.tigris.org/) written in C++ using the wxWidgets GUI 
framework.

%package -n libsvncpp
Summary: Subversion C++ API
Group: System/Libraries

%description -n libsvncpp
Subversion C++ shared library.

%package -n libsvncpp-devel
Summary: header files for libsvncpp
Group: Development/C++
Requires: libsvncpp = %version

%description -n libsvncpp-devel
Development files for libsvncpp, a C++ API for Subversion.

%prep
%setup -q
%patch1 -p0

%build
%autoreconf
%define xsldir %_datadir/xml/docbook/xsl-stylesheets/manpages/docbook.xsl
%configure --disable-static \
	--with-apr-config=%_bindir/apr-1-config \
	--with-apu-config=%_bindir/apu-1-config \
	--with-cppunit \
	--with-docbook-xsl-manpages=%xsldir \
	--with-manpage \
	%{subst_with doxygen}

%make_build

%install
%makeinstall_std
install -pD -m644 %SOURCE10 %buildroot%_desktopdir/%name.desktop

%files
%_bindir/rapidsvn
%_desktopdir/%name.desktop

%files -n libsvncpp
%_libdir/libsvncpp.so.*

%files -n libsvncpp-devel
%_libdir/libsvncpp.so
%dir %_includedir/svncpp
%_includedir/svncpp/*.hpp

%changelog
* Wed Mar 10 2010 Ilya Mashkin <oddity@altlinux.ru> 0.9.8-alt3
- rebuild with current wxGTK

* Tue May 26 2009 Alexey Rusakov <ktirf@altlinux.org> 0.9.8-alt2
- Fixed buildreqs.

* Sun Mar 22 2009 Alexey Rusakov <ktirf@altlinux.org> 0.9.8-alt1
- New version (0.9.8).
- Updated the version to %gpl3plus.
- Use %%autoreconf macro.
- Updated buildreqs.
- A workaround for RapidSVN Bug 511 went upstream.
- Use SMP-aware build command.
- Added .desktop file (ALT Bug 19268).

* Fri May 18 2007 Alexey Rusakov <ktirf@altlinux.org> 0.9.4-alt3
- Another way to fix building on x86_64.

* Tue Apr 17 2007 Alexey Rusakov <ktirf@altlinux.org> 0.9.4-alt2
- Fixed building on x86_64.

* Fri Apr 06 2007 Alexey Rusakov <ktirf@altlinux.org> 0.9.4-alt1
- New version (0.9.4).
- Spec cleanup.
- Added 'with doxygen' switch, enabled by default.

* Sun Nov 19 2006 Alex V. Myltsev <avm@altlinux.ru> 0.9.3-alt1
- Initial build for Sisyphus.

