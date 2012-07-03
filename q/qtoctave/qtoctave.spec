Name: qtoctave
Version: 0.10.1
Release: alt2
Summary: Frontend for Octave

Group: Sciences/Mathematics

License: GPLv2
Url: http://qtoctave.wordpress.com/
Source0: http://forja.rediris.es/frs/download.php/1383/%name-%version.tar.gz

#BuildRequires: cmake
Requires: octave octave-devel

#Patch0: qtoctave-includes.patch
Patch: qtoctave-0.10.1-qtinfo.patch

Packager: Fr. Br. George <george@altlinux.ru>

# Automatically added by buildreq on Mon Mar 22 2010
BuildRequires: cmake gcc-c++ libSM-devel libXcursor-devel libXext-devel libXfixes-devel libXi-devel libXinerama-devel libXrandr-devel libXrender-devel libqt4-devel qt4-assistant

%description
QtOctave is a frontend for Octave based on Qt4.

%prep
%setup
#patch0 -p1 -b .includes
%patch -p0

find xmlwidget/qt4/src/ -type f -exec chmod a-x {} \;
find easy_plot/src/ -type f -exec chmod a-x {} \;
sed -i 's@share/doc/%name/@share/doc/%name-%version/@g' qtoctave/src/configure.h.in
sed -i 's@share/doc/%name@share/doc/%name-%version@g' qtoctave/src/CMakeLists.txt
#sed -i 's@share/doc/octave-html/octave_doc@share/%name/octave-html@g' qtoctave/src/configure.h.in
#sed -i 's@share/doc/octave-html@share/%name/octave-html@g' qtoctave/src/CMakeLists.txt
sed -i 's@.{CMAKE_CURRENT_BINARY_DIR}/configure.h@${CMAKE_CURRENT_SOURCE_DIR}/configure.h@g' qtoctave/src/CMakeLists.txt
sed -i 's@lrelease@lrelease-qt4@g' qtoctave/src/CMakeLists.txt
#sed -i 's@"qtinfo"@"qtoctave_qtinfo"@' qtoctave/src/main.cpp
#sed -i 's@"qtinfo@"qtoctave_qtinfo@' qtoctave/src/scripts_octave/qtinfo.m

%build
#cmake -DCMAKE_INSTALL_PREFIX=/usr -DLIB_DESTINATION=%_lib -DCMAKE_CXX_FLAGS:STRING='-pipe -Wall -O2' -DCMAKE_C_FLAGS:STRING='-pipe -Wall -O2' -DCMAKE_C_FLAGS_RELEASE:STRING="-DNDEBUG" -DCMAKE_CXX_FLAGS_RELEASE:STRING="-DQT_NO_DEBUG" -DCMAKE_SKIP_RPATH:STRING="ON"
%cmake -DCMAKE_INSTALL_PREFIX:PATH=%_prefix
cd BUILD
%make_build

%install
cd BUILD
%makeinstall DESTDIR=%buildroot
cd ..
install qtoctave/src/config_files/pkg-commands.list %buildroot%_datadir/%name/
#ln -s %_defaultdocdir/octave*/interpreter/octave.html/* %buildroot%_datadir/%name/octave-html

%files
%doc readme.txt LICENSE_GPL.txt
%doc %_defaultdocdir/%name-utils
%doc %name/src/qtoctave_doc
%_bindir/*
%dir %_datadir/%name
%_datadir/%name/*
%_desktopdir/%name.desktop
%_iconsdir/hicolor/64x64/apps/%name.png

%changelog
* Fri Aug 26 2011 Fr. Br. George <george@altlinux.ru> 0.10.1-alt2
- Fix cmake-unaware build configuration part (closes: #26149)

* Tue Apr 26 2011 Fr. Br. George <george@altlinux.ru> 0.10.1-alt1
- Autobuild version bump to 0.10.1

* Thu Jun 17 2010 Fr. Br. George <george@altlinux.ru> 0.9.1-alt1
- Version up

* Tue Mar 23 2010 Fr. Br. George <george@altlinux.ru> 0.8.2-alt1
- Initial build from FC

* Thu Jan 28 2010 Alexey Kurov <nucleo@fedoraproject.org> - 0.8.2-2
- fixed BR qt4-devel >= 4.5.0, octave-devel >= 3.2.0

* Thu Jan 28 2010 Alexey Kurov <nucleo@fedoraproject.org> - 0.8.2-1
- update to 0.8.2

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8.1-0.20080826.svn165
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Fri Mar 06 2009 Caolán McNamara <caolanm@redhat.com> - 0.8.1-0.20080825.svn165
- add stdio.h for printf

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8.1-0.20080824.svn165
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Thu Aug 14 2008 Claudio Tomasoni <claudio@claudiotomasoni.it> 0.8.1-0.20080823.svn165
- bump to svn version pre 0.8.1
- fixes on icon and desktop file

* Sat May 24 2008 Claudio Tomasoni <claudio@claudiotomasoni.it> 0.7.4-3
- fixed SOURCE1 setup

* Mon May 12 2008 Claudio Tomasoni <claudio@claudiotomasoni.it> 0.7.4-2
- new GPLv2 icon

* Thu May 01 2008 Claudio Tomasoni <claudio@claudiotomasoni.it> 0.7.4-1
- update to 0.7.4
- removed autodetected qt4 requirement
- changed cmake options to avoid rpaths
- fixed wrong permissions in the source tree

* Mon Apr 07 2008 Claudio Tomasoni <claudio@claudiotomasoni.it> 0.7.3-3.fc8
- deleted useless post and postun scripts
- fixed issues in install section
- fixed wrong compilation flags
- license is GPLv2

* Sun Mar 30 2008 Claudio Tomasoni <claudio@claudiotomasoni.it> 0.7.3-2.fc8
- sync with 0.7.3 package released on official blog
- fixed silly errors with cmake macro

* Tue Mar 25 2008 Claudio Tomasoni <claudio@claudiotomasoni.it> 0.7.3-1.139.20080425svn.fc8
- Update to svn version 0.7.3
- Bump to cmake

* Sun Mar 23 2008 Claudio Tomasoni <claudio@claudiotomasoni.it> 0.7.1-1.fc8
- First release
