Group: Games/Arcade
# BEGIN SourceDeps(oneline):
BuildRequires: /usr/bin/desktop-file-install gcc-c++ libGL-devel zlib-devel
# END SourceDeps(oneline)
%define _libexecdir %_prefix/libexec
%global commit a7ef3bfa0c32df4852bf057fab969c1a080edf4d
%global shortcommit %(c=%{commit}; echo ${c:0:7})

Name:           frogatto
Version:        1.3.3
Release:        alt1_6
Summary:        An old-school 2D platform game

# Artwork and music not released under an open license
License:        GPLv3+ and proprietary
URL:            http://www.frogatto.com/
Source0:        https://github.com/frogatto/frogatto/archive/%{commit}/%{name}-%{version}-%{shortcommit}.tar.gz
Source1:        %{name}.sh
Source2:        %{name}.desktop
Source3:        %{name}.pod
# Patch Makefile not to link lSDLmain
Patch0:         %{name}-1.2-Makefile.patch
# Boost no longer has separate non mt and -mt variants of its libs
Patch1:         %{name}-1.3-no-boost-mt.patch
# Use FreeFont instead of the Ubuntu Font Family
Patch2:         %{name}-1.3-fonts.patch
# Fix gcc6 build only fixes some of the narrowing conversion warnings, there
# are too many, so we add -Wno-narrowing to the CXXFLAGS as a workaround
Patch3:         %{name}-1.3-narrowing-conversion-fixes.patch

BuildRequires:  libSDL-devel >= 1.2.7
BuildRequires:  libSDL_image-devel
BuildRequires:  libSDL_mixer-devel
BuildRequires:  libSDL_ttf-devel >= 2.0.8
BuildRequires:  libGLU-devel
BuildRequires:  libGLEW-devel
BuildRequires:  libpng-devel
BuildRequires:  ccache
BuildRequires: boost-asio-devel boost-context-devel boost-coroutine-devel boost-devel boost-devel-headers boost-filesystem-devel boost-flyweight-devel boost-geometry-devel boost-graph-parallel-devel boost-interprocess-devel boost-locale-devel boost-lockfree-devel boost-log-devel boost-math-devel boost-mpi-devel boost-msm-devel boost-multiprecision-devel boost-polygon-devel boost-program_options-devel boost-python-devel boost-python-headers boost-signals-devel boost-wave-devel
BuildRequires:  perl-podlators
BuildRequires:  libicns-utils
BuildRequires:  desktop-file-utils 
Requires:       icon-theme-hicolor
Requires:       fonts-ttf-gnu-freefont-mono
Source44: import.info
Requires: %name-gamedata = %version-%release


%description
An old-school 2D platform game, starring a certain quixotic frog. Frogatto
has gorgeous, high-end pixel art, pumping arcade tunes, and all the gameplay 
nuance of a classic console title. Run and jump over pits and enemies. Grab 
enemies with your tongue, swallow them, and then spit them out at other enemies 
as projectiles! Fight dangerous bosses, and solve vexing puzzles. Collect coins 
and use them to buy upgrades and new abilities in the store. Talk to characters 
in game, and work to unravel Big Bad Milgram's plot against the townsfolk! 

%package gamedata
Summary: Game data for frogatto
License: distributable
Group: Games/Arcade
# We split game data to separate package to make it noarch and thus save
# bandwidth and space on distribution media.
BuildArch: noarch

%description gamedata
Game data for frogatto.



%prep
%setup -qn %{name}-%{commit}
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1

# Fix locale file path
sed -i 's!"./locale/"!"%{_datadir}/locale/"!' src/i18n.cpp


%build
make %{?_smp_mflags} \
  BASE_CXXFLAGS="$RPM_OPT_FLAGS -fno-inline-functions -fthreadsafe-statics -Wno-narrowing"


%install
# Install wrapper script
install -d %{buildroot}%{_bindir}
install -m 755 -p %{SOURCE1} %{buildroot}%{_bindir}/%{name}

# Install game and data
install -d %{buildroot}%{_libexecdir}/%{name}
install -m 755 -p game %{buildroot}%{_libexecdir}/%{name}
install -d %{buildroot}%{_datadir}/%{name}/modules/%{name}
cp -pr data images music *.cfg \
  %{buildroot}%{_datadir}/%{name}
pushd modules/%{name}
  cp -pr data images music sounds *.cfg \
    %{buildroot}%{_datadir}/%{name}/modules/%{name}
  # Install translations
  cp -pr locale %{buildroot}%{_datadir}
popd

# Install desktop file
install -d %{buildroot}%{_datadir}/applications
desktop-file-install \
  --dir %{buildroot}%{_datadir}/applications \
  %{SOURCE2}

# Extract Mac OS X icons
icns2png -x modules/%{name}/images/os/mac/icon.icns 

# Install icons
for i in 16 32 128 256; do
  install -d -m 755 %{buildroot}%{_datadir}/icons/hicolor/${i}x${i}/apps
  install -m 644 icon_${i}x${i}x32.png \
    %{buildroot}%{_datadir}/icons/hicolor/${i}x${i}/apps/%{name}.png
done

# Install man page
install -d %{buildroot}%{_mandir}/man6
pod2man --section=6 \
  -center="RPM Fusion contributed man pages" \
  -release="%{name} %{version}" \
  -date="July 13th, 2010" \
  %{SOURCE3} > %{buildroot}%{_mandir}/man6/%{name}.6

%find_lang %{name}


%files -f %{name}.lang
%{_bindir}/%{name}
%{_libexecdir}/%{name}

%files gamedata
%doc modules/%{name}/CHANGELOG LICENSE
%{_datadir}/%{name}
%{_datadir}/icons/hicolor/*/apps/%{name}.png
%{_datadir}/applications/%{name}.desktop
%{_mandir}/man6/%{name}.6*



%changelog
* Tue Nov 15 2016 Igor Vlasenko <viy@altlinux.ru> 1.3.3-alt1_6
- new version

* Thu Apr 07 2016 Dmitry V. Levin (QA) <qa_ldv@altlinux.org> 1.1.1-alt1.6.qa2
- NMU: rebuilt with boost 1.57.0 -> 1.58.0.

* Sat Jan 03 2015 Ivan A. Melnikov <iv@altlinux.org> 1.1.1-alt1.6.qa1.1
- rebuild with boost 1.57.0

* Sun Apr 14 2013 Dmitry V. Levin (QA) <qa_ldv@altlinux.org> 1.1.1-alt1.6.qa1
- NMU: rebuilt with libboost_*.so.1.53.0.

* Fri Nov 30 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.1.1-alt1.6
- Rebuilt with Boost 1.52.0

* Thu Oct 04 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.1.1-alt1.5
- Rebuilt with libpng15

* Thu Sep 06 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.1.1-alt1.4
- Rebuilt with Boost 1.51.0

* Thu Apr 05 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.1.1-alt1.3
- Rebuilt with Boost 1.49.0

* Sun Dec 04 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.1.1-alt1.2
- Rebuilt with Boost 1.48.0

* Sat Jul 30 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.1.1-alt1.1
- Rebuilt with Boost 1.47.0

* Sun Jul 10 2011 Victor Forsiuk <force@altlinux.org> 1.1.1-alt1
- 1.1.1

* Wed May 11 2011 Victor Forsiuk <force@altlinux.org> 1.1-alt1
- 1.1

* Fri Mar 25 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.3-alt1.2
- Rebuilt with Boost 1.46.1

* Thu Dec 16 2010 Igor Vlasenko <viy@altlinux.ru> 1.0.3-alt1.1
- rebuild with new icu44 and/or boost by request of git.alt administrator

* Thu Sep 23 2010 Victor Forsiuk <force@altlinux.org> 1.0.3-alt1
- 1.0.3
- Fix starting script error on x86_64 (closes: #24007).
- Apply %%optflags.

* Thu Aug 26 2010 Victor Forsiuk <force@altlinux.org> 1.0-alt1
- Initial build.
