Name: FlightCrew
Version: 0.7.2
Release: alt1
Summary: EPUB validation tool

Group: File tools
License: LGPLv3+
URL: http://code.google.com/p/flightcrew/
Source0: %name-%version.tar

Patch1: %name-0.7.2-fc18-soname.patch
Patch2: %name-0.7.2-fc18-as_shared.patch
Patch3: %name-0.7.2-fc18-use_system_zlib.patch
Patch4: %name-0.7.2-fc18-use_system_boost.patch
Patch5: %name-0.7.2-fc18-boost_1.48.patch
Patch6: %name-0.7.2-fc18-use_system_xerces-c.patch
Patch7: %name-0.7.2-fc18-headers.patch
Patch8: %name-0.7.2-fc18-without_googlemock.patch
Patch9: %name-0.7.2-fc18-FindFlightCrew.cmake.patch
Patch10: %name-0.7.2-fc18-shared_XercesExtensions.patch
Patch11: %name-0.7.2-fc18-shared_zipios.patch

BuildPreReq: rpm-macros-cmake
BuildRequires: cmake gcc-c++
BuildRequires: zlib-devel
BuildRequires: boost-devel boost-filesystem-devel boost-program_options-devel boost-datetime-devel boost-regex-devel boost-thread-devel boost-system-devel
BuildRequires: xerces-c-devel >= 3.1
BuildRequires: libqt4-devel
Requires: lib%name = %version

%description
FlightCrew is a C++, cross-platform, native code epub validator.

%package -n lib%name
Summary: EPUB validation library
Group: File tools

%description -n lib%name
FlightCrew is a C++, cross-platform, native code epub validator library.

%package gui
Summary: EPUB validation tool with gui
Group: File tools
Requires: lib%name = %version

%description gui
FlightCrew is a C++, cross-platform, native code epub validator.

%package -n lib%name-devel
Summary: Development files for %name
Group: Development/C++
Requires: lib%name = %version-%release

%description -n lib%name-devel
The %name-devel package contains libraries and header files for
developing applications that use %name.

%prep
%setup -q
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1
%patch6 -p1
%patch7 -p1
%patch8 -p1
%patch9 -p1
%patch10 -p1
#%patch11 -p1

# Fix EOL encoding for %%doc
for i in INSTALL.txt README.txt ChangeLog.txt; do
    sed -i.old 's/\r//' "$i"
    touch -r "$i.old" "$i"
done

# remove unbundled stuff
rm -rf src/BoostParts src/zlib src/Xerces
# remove test framework
rm -rf src/googlemock

# fix permissions
chmod a-x src/utf8-cpp/utf8/*.h


%build
%cmake -DBUILD_SHARED_LIBS:BOOL=OFF -DBUILD_SHARED_FC=1 -DBUILD_SHARED_XE=1 -DNO_TEST_EXE=1 -DINCLUDE_INSTALL_DIR=%_includedir
cd BUILD
%make_build


%install
cd BUILD
%makeinstall_std

%files
%doc INSTALL.txt README.txt ChangeLog.txt
%_bindir/*-cli

%files gui
%_bindir/*-gui

%files -n lib%name
%_libdir/*.so.*

%files -n lib%name-devel
%_includedir/%name/
%_includedir/XercesExtensions/
%_libdir/*.so
%_libdir/cmake/*


%changelog
* Mon Dec 03 2012 Dmitriy Kulik <lnkvisitor@altlinux.org> 0.7.2-alt1
- Port to ALT Linux

* Sun Aug 12 2012 Kevin Fenzi <kevin@scrye.com> - 0.7.2-5
- Rebuild for new boost

* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Tue Feb 28 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7.2-3
- Rebuilt for c++ ABI breakage

* Thu Jan 12 2012 Hans de Goede <hdegoede@redhat.com> - 0.7.2-2
- Make -devel package Requires on main package include isa
- Drop buildroot and defattr boilerplate (no longer needed with recent rpm)
- Split the use-system-libs patch into its sub patches
- Add a FindFlightCrew cmake module
- Build XercesExtensions as a shared lib (including a Find... cmake module)

* Sat Dec 24 2011 Dan Horák <dan[at]danny.cz> - 0.7.2-1
- initial Fedora version
