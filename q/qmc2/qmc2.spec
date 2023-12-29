Name:           qmc2
Version:        0.243
Group: Games/Arcade
Release:        alt1
Summary:        M.A.M.E. Catalog / Launcher II

#PDF.js is ASL 2.0
#data/js/pdfjs/web/l10n.js is MIT
#everything else is GPLv2
License:        GPLv2 and ASL 2.0 and MIT
URL:            http://qmc2.batcom-it.net
Source:        %name-%version.tar.gz
#Fedora-specific configuration
Patch0:         %{name}-ini.patch
Patch1:		QWebengine.patch

BuildRequires:  desktop-file-utils
BuildRequires:  libarchive-devel
BuildRequires:  libXmu-devel
BuildRequires:  make
BuildRequires:  libminizip-ng-compat-devel
BuildRequires:  zlib-devel
BuildRequires:  qt5-multimedia-devel
BuildRequires:  qt5-svg-devel qt5-script-devel
BuildRequires:  qt5-webengine-devel
BuildRequires:  qt5-xmlpatterns-devel
BuildRequires:  rsync
BuildRequires:  libSDL2-devel
Requires: mame mame-tools mame-data mame-data-software-lists

ExclusiveArch: aarch64 x86_64

%description
A Qt based multi-platform GUI front-end for MAME.


%package -n qchdman
Summary:        Qt CHDMAN GUI
Group: Games/Arcade
License:        GPLv2
Requires:       mame-tools

%description -n qchdman
A stand-alone graphical user interface / front-end to chdman


%package arcade
Summary:        Arcade QMC2 GUI
Group: Games/Arcade
License:        GPLv2

%description arcade
A QML-based standalone graphical arcade mode binary which utilizes the cached
data of qmc2 to quickly display and launch emulators and get you "straight into
the games"


%prep
%setup
%patch0 -p1
%patch1 -p1
#ensure system minizip and zlib are used
#https://bugzilla.redhat.com/show_bug.cgi?id=1998742
rm -rf src/minizip
rm -rf src/zlib
#fix opening documentation from the menu
sed -i s@doc/html/@doc/@ src/qmc2main.cpp


%build
#https://bugzilla.redhat.com/show_bug.cgi?id=1998742
%make_build DISTCFG=1 CC_FLAGS="$RPM_OPT_FLAGS" CXX_FLAGS="$RPM_OPT_FLAGS" \
    L_FLAGS="$RPM_LD_FLAGS" \
    SYSTEM_MINIZIP=1 \
    SYSTEM_ZLIB=1 LIBARCHIVE=1 GIT_REV=0
%make_build arcade CXX_FLAGS="%{optflags}" \
    L_FLAGS="$RPM_LD_FLAGS"  \
    SYSTEM_MINIZIP=1 \
    SYSTEM_ZLIB=1
%make_build qchdman CXX_FLAGS="%{optflags}" SDL=2

%make_build doc DISTCFG=1


%install
rm -rf $RPM_BUILD_ROOT

make install DESTDIR=$RPM_BUILD_ROOT DISTCFG=1 PREFIX=%{_prefix}
make arcade-install DESTDIR=$RPM_BUILD_ROOT DISTCFG=1 PREFIX=%{_prefix}
make qchdman-install DESTDIR=$RPM_BUILD_ROOT DISTCFG=1 PREFIX=%{_prefix}
make doc-install DESTDIR=$RPM_BUILD_ROOT DISTCFG=1 MAN_DIR=%{_mandir}

#remove docs since we are installing docs in %%doc

#validate the desktop files
desktop-file-validate $RPM_BUILD_ROOT%{_datadir}/applications/qmc2-sdlmame.desktop
desktop-file-validate $RPM_BUILD_ROOT%{_datadir}/applications/qmc2-arcade.desktop
desktop-file-validate $RPM_BUILD_ROOT%{_datadir}/applications/qchdman.desktop


%files
%doc data/doc/html/*
%doc data/doc/html/us/copying.html data/js/pdfjs/LICENSE
%config(noreplace) %{_sysconfdir}/qmc2
%{_bindir}/qmc2
%{_bindir}/qmc2-sdlmame
%{_datadir}/applications/qmc2-sdlmame.desktop
%{_mandir}/man6/qmc2-main-gui.6*
%{_mandir}/man6/qmc2-sdlmame.6*
%{_mandir}/man6/qmc2.6*
%{_datadir}/qmc2

%files arcade
%doc data/doc/html/us/copying.html
%{_bindir}/qmc2-arcade
%{_datadir}/applications/qmc2-arcade.desktop
%{_mandir}/man6/qmc2-arcade.6*

%files -n qchdman
%doc data/doc/html/us/copying.html
%{_bindir}/qchdman
%{_datadir}/applications/qchdman.desktop
%{_mandir}/man6/qchdman.6*


%changelog
* Fri Dec 29 2023 Artyom Bystrov <arbars@altlinux.org> 0.243-alt1
- Initial commit for Sisyphus