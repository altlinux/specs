Epoch: 1
# BEGIN SourceDeps(oneline):
BuildRequires: gcc-c++ pkgconfig(CEGUI-OPENGL) pkgconfig(sigc++-1.2)
# END SourceDeps(oneline)
# Copyright (c) 2007 oc2pus <toni@links2linux.de>
# Copyright (c) 2007 Hans de Goede <j.w.r.degoede@hhs.nl>
# This file and all modifications and additions to the pristine
# package are under the same license as the package itself.
#
# Please submit bugfixes or comments to us at the above email addresses

Name:           TnL
Version:        071111
Release:        alt3_19
Summary:        Thunder & Lightning - A futuristic action flight simulator game
Group:          Games/Other
License:        GPL+
URL:            http://tnlgame.net
Source0:        http://tnlgame.net/downloads/tnl/%{version}/%{name}-source-%{version}.tar.bz2
Source1:        %{name}.desktop
Patch0:         TnL-070909-system-boost.patch
Patch1:         TnL-070909-crash-on-exit.patch
Patch2:         TnL-source-071111-gcc43.patch
Patch3:         TnL-071111-openal-compile-fixes.patch
#Patch4:		TnL-071111-cegui.patch
BuildRequires:  libglew-devel libpng-devel libsigc++2-devel
BuildRequires:  libSDL-devel Io-language-devel boost-devel boost-filesystem-devel boost-wave-devel boost-graph-parallel-devel boost-math-devel boost-mpi-devel boost-program_options-devel boost-signals-devel boost-intrusive-devel boost-asio-devel cegui06-devel
BuildRequires:  libopenal-devel libalut-devel >= 1.1.0-10
BuildRequires:  desktop-file-utils
Requires:       TnL-data = %{version} opengl-games-utils
Source44: import.info
Patch33: TnL-071111-alt-as-needed.patch

%description
Thunder&Lightning is a futuristic action flight simulator game
that takes place in a large 3D environment. Jump into the pilot
seat of your Lightning aircraft and fight against Thunder tanks
in a fierce battle for control of the island!

In the long run, Thunder&Lightning will incorporate features from
the 80's classics Carrier Command and Midwinter. There will be
multiple Islands to conquer, each with its own defense strategy.

Thunder&Lightning will not be mission oriented, but there will be
scripted events for each island.


%prep
%setup -q -n %{name}-source-%{version}
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
#%patch4 -p0

# we want to use the system version of boost
rm -r src/boost
# stop autoxxx from rerunning because of our patches above
touch aclocal.m4
touch configure config.h.in `find -name Makefile.in`
%patch33 -p1
autoreconf -fisv


%build
sed -i s/CEGUI\-OPENGL/CEGUI\-OPENGL\-0\.6/g configure
%configure --with-io-cflags=-I/usr/include/io --with-io-libs=-liovmall \
   --enable-release
make %{?_smp_mflags}


%install
# tnl installs a useless and ugly wrapper, all we need is the binary, so DIY
mkdir -p $RPM_BUILD_ROOT%{_bindir}
install -m 755 src/tnl-bin $RPM_BUILD_ROOT%{_bindir}/%{name}
ln -s opengl-game-wrapper.sh $RPM_BUILD_ROOT%{_bindir}/%{name}-wrapper
mkdir -p $RPM_BUILD_ROOT%{_datadir}/applications
desktop-file-install             \
  --dir $RPM_BUILD_ROOT%{_datadir}/applications \
  %{SOURCE1}


%files
%doc AUTHORS COPYING README
%{_bindir}/%{name}*
%{_datadir}/applications/%{name}.desktop


%changelog
* Wed May 09 2012 Igor Vlasenko <viy@altlinux.ru> 1:071111-alt3_19
- update to new release by fcimport

* Fri Mar 02 2012 Igor Vlasenko <viy@altlinux.ru> 1:071111-alt3_18
- rebuild with fixed sourcedep analyser (#27020)

* Thu Feb 23 2012 Igor Vlasenko <viy@altlinux.ru> 1:071111-alt2_18
- new fc release

* Tue Jan 03 2012 Igor Vlasenko <viy@altlinux.ru> 1:071111-alt2_13
- dropped hook

* Thu Jul 21 2011 Igor Vlasenko <viy@altlinux.ru> 1:071111-alt1_13
- initial release by fcimport

