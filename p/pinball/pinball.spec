# BEGIN SourceDeps(oneline):
BuildRequires: cppunit-devel gcc-c++ libICE-devel libSDL-devel libSM-devel libX11-devel liballegro-devel
# END SourceDeps(oneline)
Name:           pinball
Version:        0.3.1
Release:        alt2_19
Summary:        Emilia arcade game
Group:          Games/Other
License:        GPL+
URL:            http://pinball.sourceforge.net
Source0:        http://downloads.sourceforge.net/pinball/%{name}-%{version}.tar.gz
Source1:        %{name}.desktop
Source2:        %{name}.png
Patch0:         pinball-0.3.1-sys-ltdl.patch
Patch1:         pinball-0.3.1-hiscore.patch
Patch2:		pinball-0.3.1-strictproto.patch
Patch3:		pinball-0.3.1-lacomment.patch
Patch4:		pinball-0.3.1-cstddef.patch
BuildRequires:  libXt-devel freeglut-devel libSDL_image-devel libSDL_mixer-devel
BuildRequires:  libpng-devel libvorbis-devel libltdl7-devel
BuildRequires:  desktop-file-utils
Requires:       icon-theme-hicolor opengl-games-utils
Source44: import.info

%description
The Emilia Pinball project is an open source pinball simulator for linux
and other unix systems. The current release is a stable and mature alpha.
There is only one level to play with but it is however very addictive.


%prep
%setup -q
%patch0 -p1 -z .sys-ltdl
%patch1 -p1 -z .hiscore
%patch2 -p0
%patch3 -p0
%patch4 -p0
rm -fr libltdl
# sigh stop autoxxx from rerunning because of our patches above.
touch aclocal.m4
touch configure
touch `find -name Makefile.in`
touch pinconfig.h.in
# cleanup a bit
chmod -x ChangeLog */*.h */*.cpp data/*/Module*.cpp


%build
%configure
make CXXFLAGS="$RPM_OPT_FLAGS"


%install
make DESTDIR=$RPM_BUILD_ROOT INSTALL="%{__install} -p" install
ln -s opengl-game-wrapper.sh $RPM_BUILD_ROOT%{_bindir}/%{name}-wrapper
# remove unused global higescorefiles:
rm -fr $RPM_BUILD_ROOT%{_localstatedir}
# remove unused test module
rm $RPM_BUILD_ROOT%{_libdir}/%{name}/libModuleTest.*
# .la files are needed for ltdl
rm $RPM_BUILD_ROOT%{_libdir}/%{name}/lib*.{a,so}
# remove bogus development files
rm $RPM_BUILD_ROOT%{_bindir}/%{name}-config
rm -r $RPM_BUILD_ROOT%{_includedir}/%{name}

# below is the desktop file and icon stuff.
mkdir -p $RPM_BUILD_ROOT%{_datadir}/applications
desktop-file-install             \
  --dir $RPM_BUILD_ROOT%{_datadir}/applications \
  %{SOURCE1}
mkdir -p $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/48x48/apps
install -p -m 644 %{SOURCE2} \
  $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/48x48/apps


%files
%doc README ChangeLog
%{_bindir}/%{name}*
%{_libdir}/%{name}
%{_datadir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/48x48/apps/%{name}.png


%changelog
* Wed May 09 2012 Igor Vlasenko <viy@altlinux.ru> 0.3.1-alt2_19
- update to new release by fcimport

* Fri Mar 02 2012 Igor Vlasenko <viy@altlinux.ru> 0.3.1-alt2_18
- rebuild with fixed sourcedep analyser (#27020)

* Sat Jan 21 2012 Igor Vlasenko <viy@altlinux.ru> 0.3.1-alt1_18
- update to new release by fcimport

* Sun Jul 10 2011 Igor Vlasenko <viy@altlinux.ru> 0.3.1-alt1_17
- initial release by fcimport

