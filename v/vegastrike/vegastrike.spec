# BEGIN SourceDeps(oneline):
BuildRequires: /usr/bin/desktop-file-install gcc-c++ perl(English.pm) zlib-devel
# END SourceDeps(oneline)
BuildRequires: boost-python-devel
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
Name:           vegastrike
Version:        0.5.1
Release:        alt6_31.r1
Summary:        3D OpenGL spaceflight simulator
Group:          Games/Other
License:        GPLv2+
URL:            http://vegastrike.sourceforge.net/
#Source0:        http://downloads.sourceforge.net/%{name}/%{name}-src-%{version}.tar.bz2
Source0:        http://downloads.sourceforge.net/%{name}/%{name}-src-%{version}.r1.tar.bz2
# Found in the mandriva srpm, origin Debian ?
Source1:        %{name}-manpages.tar.bz2
Source2:        %{name}-wrapper.sh
Source3:        %{name}.desktop
Source4:        %{name}.appdata.xml
Patch0:         vegastrike-0.5.1-char-fix.patch
Patch1:         vegastrike-0.5.1-paths-fix.patch
Patch2:         vegastrike-0.4.2-posh-fix.patch
Patch3:         vegastrike-0.4.2-vssetup-fix.patch
Patch4:         vegastrike-0.4.3-64-bit.patch
Patch5:         vegastrike-0.5.1-openal.patch
Patch6:         vegastrike-0.5.1-sys-python.patch
Patch8:         vegastrike-0.5.1-gcc44.patch
Patch9:         vegastrike-0.5.0-glext.patch
Patch14:        vegastrike-0.5.1-gcc47.patch
Patch15:        vegastrike-0.5.1-music.patch
Patch16:        vegastrike-0.5.1-gcc48.patch
Patch17:        vegastrike-0.5.1-boost154.patch
Patch18:        vegastrike-aarch64.patch
Patch19:        vegastrike-0.5.1-gcc6.patch
# https://sourceforge.net/p/vegastrike/patches/70/
Patch20:        vegastrike-0.5.1-gcc7.patch
BuildRequires:  libGLU-devel libfreeglut-devel libXi-devel libXmu-devel gtk-builder-convert gtk-demo libgail-devel libgtk+2-devel libgtk+2-gir-devel
BuildRequires:  libjpeg-devel libpng-devel boost-asio-devel boost-context-devel boost-coroutine-devel boost-devel boost-devel-headers boost-filesystem-devel boost-flyweight-devel boost-geometry-devel boost-graph-parallel-devel boost-interprocess-devel boost-locale-devel boost-lockfree-devel boost-log-devel boost-math-devel boost-mpi-devel boost-msm-devel boost-multiprecision-devel boost-polygon-devel boost-program_options-devel boost-python-devel boost-python-headers boost-signals-devel boost-wave-devel libexpat-devel python-devel
BuildRequires:  libSDL_mixer-devel libopenal-devel libopenal1 libalut-devel
BuildRequires:  libvorbis-devel libogre-devel cegui cegui-devel desktop-file-utils
BuildRequires:  libappstream-glib
Requires:       %{name}-data = %{version}, xdg-utils, opengl-games-utils
Source44: import.info
Patch33: vegastrike-0.5.1-alt-SharedPool.patch
Patch34: vegastrike-0.5.1.r1-alt-perl522.patch
Patch35: vegastrike-0.5.1-alt-flags.patch

%description
Vega Strike is a GPL 3D OpenGL Action RPG space sim that allows a player to
trade and bounty hunt. You start in an old beat up Wayfarer cargo ship, with
endless possibility before you and just enough cash to scrape together a life.
Yet danger lurks in the space beyond.


%prep
%setup -q -a 1 -n %{name}-src-%{version}.r1
%patch0 -p0
%patch1 -p0
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p0
%patch6 -p0
%patch8 -p0
%patch9 -p1
%patch14 -p1
%patch15 -p3
%patch16 -p0
%patch17 -p1
%patch18 -p1
%patch19 -p1
%patch20 -p1
iconv -f ISO-8859-1 -t UTF-8 README > README.tmp
touch -r README README.tmp
mv README.tmp README
sed -i 's/-lboost_python-st/-lboost_python/g' Makefile.in
# we want to use the system version of expat.h
rm objconv/mesher/expat.h
%patch33 -p2
%patch34 -p1
%patch35 -p2


%build
export LDFLAGS="$LDFLAGS -Wl,--no-as-needed"
export CXXFLAGS="$RPM_OPT_FLAGS -fsigned-char"
%autoreconf
%configure --with-data-dir=%{_datadir}/%{name} --with-boost=system \
  --enable-release --enable-flags="-DBOOST_PYTHON_NO_PY_SIGNATURES $RPM_OPT_FLAGS -fsigned-char" --disable-ffmpeg \
  --enable-stencil-buffer
%make_build


%install
#make install PREFIX=$RPM_BUILD_ROOT doesn't work
%makeinstall
install -p -m 755 %{SOURCE2} $RPM_BUILD_ROOT%{_bindir}

mkdir -p $RPM_BUILD_ROOT%{_libexecdir}/%{name}
chmod +x $RPM_BUILD_ROOT%{_prefix}/objconv/*
mv $RPM_BUILD_ROOT%{_prefix}/objconv/* \
  $RPM_BUILD_ROOT%{_libexecdir}/%{name}
for i in asteroidgen base_maker mesh_xml mesher replace tempgen trisort \
         vsrextract vsrmake; do
  mv $RPM_BUILD_ROOT%{_bindir}/$i $RPM_BUILD_ROOT%{_libexecdir}/%{name}
done

mkdir -p $RPM_BUILD_ROOT%{_mandir}/man6
install -p -m 644 *.6 $RPM_BUILD_ROOT%{_mandir}/man6

# below is the desktop file and icon stuff.
mkdir -p $RPM_BUILD_ROOT%{_datadir}/applications
desktop-file-install --dir $RPM_BUILD_ROOT%{_datadir}/applications %{SOURCE3}
mkdir -p $RPM_BUILD_ROOT%{_datadir}/appdata
install -p -m 644 %{SOURCE4} $RPM_BUILD_ROOT%{_datadir}/appdata
appstream-util validate-relax --nonet \
  $RPM_BUILD_ROOT%{_datadir}/appdata/%{name}.appdata.xml


%files
%doc AUTHORS DOCUMENTATION README ToDo.txt
%doc COPYING
%{_bindir}/vega*
%{_bindir}/vs*
%{_libexecdir}/%{name}
%{_mandir}/man6/*
%{_datadir}/appdata/%{name}.appdata.xml
%{_datadir}/applications/%{name}.desktop


%changelog
* Wed Jan 31 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 0.5.1-alt6_31.r1
- Fixed build with new compiler flags.

* Wed Sep 27 2017 Igor Vlasenko <viy@altlinux.ru> 0.5.1-alt5_31.r1
- update to new release by fcimport

* Thu Mar 16 2017 Igor Vlasenko <viy@altlinux.ru> 0.5.1-alt5_28.r1
- update to new release by fcimport

* Tue Mar 29 2016 Igor Vlasenko <viy@altlinux.ru> 0.5.1-alt5_27.r1
- update to new release by fcimport

* Wed Feb 17 2016 Igor Vlasenko <viy@altlinux.ru> 0.5.1-alt5_25.r1
- fixed build

* Sun Sep 20 2015 Igor Vlasenko <viy@altlinux.ru> 0.5.1-alt4_25.r1
- update to new release by fcimport

* Tue Apr 07 2015 Igor Vlasenko <viy@altlinux.ru> 0.5.1-alt4_20.r1
- update to new release by fcimport

* Fri Jan 16 2015 Igor Vlasenko <viy@altlinux.ru> 0.5.1-alt4_19.r1
- rebuild with new boost

* Mon Oct 27 2014 Igor Vlasenko <viy@altlinux.ru> 0.5.1-alt3_19.r1
- update to new release by fcimport

* Thu Sep 18 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.5.1-alt3_13.r1.1
- Rebuilt with new libogre

* Mon Aug 12 2013 Igor Vlasenko <viy@altlinux.ru> 0.5.1-alt3_13.r1
- update to new release by fcimport

* Fri Jul 26 2013 Slava Dubrovskiy <dubrsl@altlinux.org> 0.5.1-alt3_10.r1.1
- Rebuilt with ogre 1.8.1

* Tue Feb 26 2013 Igor Vlasenko <viy@altlinux.ru> 0.5.1-alt3_10.r1
- update to new release by fcimport

* Wed Feb 06 2013 Igor Vlasenko <viy@altlinux.ru> 0.5.1-alt3_6.r1
- update to new release by fcimport

* Sat Dec 01 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.5.1-alt3_4.r1.2
- Rebuilt with Boost 1.52.0

* Mon Oct 08 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.5.1-alt3_4.r1.1
- Rebuilt with libpng15

* Wed Sep 05 2012 Igor Vlasenko <viy@altlinux.ru> 0.5.1-alt3_4.r1
- update to new release by fcimport

* Tue Jun 26 2012 Igor Vlasenko <viy@altlinux.ru> 0.5.1-alt3_2.r1
- fixed build

* Thu Jun 07 2012 Igor Vlasenko <viy@altlinux.ru> 0.5.1-alt2_2.r1
- update to new fc release

* Mon May 28 2012 Slava Dubrovskiy <dubrsl@altlinux.org> 0.5.1-alt2_0.6.beta1.4
- Rebuilt with ogre 1.8.0

* Thu Apr 05 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.5.1-alt2_0.6.beta1.3
- Rebuilt with Boost 1.49.0

* Fri Mar 02 2012 Igor Vlasenko <viy@altlinux.ru> 0.5.1-alt2_0.6.beta1.2
- rebuild with fixed sourcedep analyser (#27020)

* Wed Feb 01 2012 Igor Vlasenko <viy@altlinux.ru> 0.5.1-alt1_0.6.beta1.2
- update to new release by fcimport

* Sun Dec 11 2011 Igor Vlasenko <viy@altlinux.ru> 0.5.1-alt1_0.4.beta1.2
- updated by fcimport

* Mon Dec 05 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.5.1-alt1_0.2.beta1.2.2
- Rebuilt with Boost 1.48.0

* Wed Oct 26 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.5.1-alt1_0.2.beta1.2.1
- Rebuild with Python-2.7

* Tue Aug 09 2011 Igor Vlasenko <viy@altlinux.ru> 0.5.1-alt1_0.2.beta1.2
- update to new release by fcimport

* Mon Aug 01 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.5.0-alt1_23.1
- Rebuilt with Boost 1.47.0

* Thu Jul 07 2011 Igor Vlasenko <viy@altlinux.ru> 0.5.0-alt1_23
- update to new release by fcimport

* Fri May 13 2011 Slava Dubrovskiy <dubrsl@altlinux.org> 0.5.0-alt1_21.2
- Rebuild with new ogre

* Fri Mar 25 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.5.0-alt1_21.1
- Rebuilt with Boost 1.46.1

* Wed Feb 16 2011 Igor Vlasenko <viy@altlinux.ru> 0.5.0-alt1_21
- converted from Fedora by srpmconvert script

