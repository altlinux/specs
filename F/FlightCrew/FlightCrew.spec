Name: FlightCrew
Version: 0.9.2
Release: alt1
Summary: EPUB validation tool

Group: File tools
License: LGPLv3+
URL: https://github.com/Sigil-Ebook/flightcrew

# https://github.com/Sigil-Ebook/flightcrew.git
Source: %name-%version.tar

Patch1: %name-%version-fedora-system-zlib.patch
Patch2: %name-%version-fedora-system-boost.patch
Patch3: %name-%version-fedora-system-xercec-c.patch
Patch4: %name-%version-fedora-dont-build-gmock.patch
Patch5: %name-%version-fedora-move-zipextraction.patch
Patch6: %name-%version-fedora-system-zipios.patch
Patch7: %name-%version-fedora-fix-installed-plugins.patch
Patch8: %name-%version-fedora-use-random-tmp-path.patch
Patch9: %name-%version-alt-build.patch

BuildPreReq: rpm-macros-cmake
BuildRequires: cmake gcc-c++
BuildRequires: zlib-devel
BuildRequires: boost-devel boost-filesystem-devel boost-program_options-devel boost-datetime-devel boost-regex-devel boost-thread-devel boost-system-devel
BuildRequires: xerces-c-devel >= 3.1
BuildRequires: python3-dev
BuildRequires: qt5-base-devel

Requires: lib%name = %version-%release

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
Requires: lib%name = %version-%release

%description gui
FlightCrew is a C++, cross-platform, native code epub validator.

%package sigil-plugin
Summary: Sigil FlightCrew epub validator plugin
Group: File tools
Requires: sigil

%description sigil-plugin
Sigil FlightCrew epub validator plugin.

%prep
%setup
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1
%patch6 -p1
%patch7 -p1
%patch8 -p1
%patch9 -p1

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
%cmake -DBUILD_SHARED_FC:BOOL=ON -DNO_TEST_EXE=1

pushd BUILD
%make_build
popd

%install
pushd BUILD
%makeinstall_std
popd

mkdir -p %buildroot%_datadir/sigil/plugins/%name
install -p -m 755 src/FlightCrew-plugin/plugin.py  %buildroot%_datadir/sigil/plugins/%name
install -p -m 644 src/FlightCrew-plugin/plugin.xml %buildroot%_datadir/sigil/plugins/%name

%files
%doc INSTALL.txt README.txt ChangeLog.txt
%_bindir/*-cli

%files gui
%_bindir/*-gui

%files -n lib%name
%_libdir/*.so

%files sigil-plugin
%_bindir/*-plugin
%_datadir/sigil/plugins/%name

%changelog
* Fri Sep 29 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 0.9.2-alt1
- Updated to upstream version 0.9.2.

* Thu Apr 07 2016 Dmitry V. Levin (QA) <qa_ldv@altlinux.org> 0.7.2-alt2.qa3
- NMU: rebuilt with boost 1.57.0 -> 1.58.0.

* Sat Jan 03 2015 Ivan A. Melnikov <iv@altlinux.org> 0.7.2-alt2.1
- rebuild with boost 1.57.0

* Mon Feb 18 2013 Dmitriy Kulik <lnkvisitor@altlinux.org> 0.7.2-alt2
- Rebuild with boost1.53.0

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
