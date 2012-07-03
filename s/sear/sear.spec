# BEGIN SourceDeps(oneline):
BuildRequires: gcc-c++ libGL-devel libSDL-devel libX11-devel pkgconfig(avahi-client) pkgconfig(cal3d) pkgconfig(eris-1.3) pkgconfig(sage) pkgconfig(varconf-1.0)
# END SourceDeps(oneline)
Name:           sear
Version:        0.6.4
Release:        alt3_0.8.g0b70ddb
Summary:        3D WorldForge client

Group:          Games/Other
License:        GPLv2+
URL:            http://www.worldforge.org
# sear is mostly dead and out of date, but the following will retrieve a much
# more recent version than the last official release (0.6.3). The suggested
# filename for the download from github ends up being
# worldforge-sear-sear-0_6_2-291-g0b70ddb.tar.gz
# Currently adding /worldforge-sear-sear-0_6_2-291-g0b70ddb.tar.gz to the end
# of the documented url works for github and is an easy way for rpmbuild
# to grab the right name.
# In spite of the naming, this is a post 0.6.3 tarball.
Source0:        https://github.com/worldforge/sear/tarball/0b70ddb963d6bead86e3/worldforge-sear-sear-0_6_2-291-g0b70ddb.tar.gz
Patch0:         sear-0.6.3-desktop.patch
Patch1:         sear-0.6.3-erisupgrade.patch
Patch2:         sear-0.6.4-mercatorupgrade.patch
Patch3:         sear-eris-api-change.patch
Patch4:         sear-missing-includes.patch
Patch5:         sear-lua-fix.patch
Patch6:         sear-compileopts.patch

BuildRequires:  lib3ds-devel mercator-devel varconf-devel eris-devel sage-devel
BuildRequires:  cal3d-devel libguichan05-devel libmodelfile-devel libGLU-devel
BuildRequires:  libtiffxx-devel libtiff-devel libjpeg-devel libpng-devel
BuildRequires:  libSDL_image-devel libSDL_mixer-devel libXt-devel
BuildRequires:  desktop-file-utils libwfut-devel libguichan-devel liblua5-devel swig
BuildRequires:  libtool automake autoconf
Requires:       wfut sear-media
Source44: import.info

%description
Sear is a 3D client for the WorldForge roleplaying environment.  WorldForge
can be viewed as a MMORPG construction kit, providing a working 3D environment
in which quests and full games can be built.


%prep
%setup -q -n worldforge-sear-0b70ddb
%patch0 -p0 -b .desktop
%patch1 -p0 -b .erisupgrade
%patch2 -p0 -b .mercatorupgrade
%patch3 -p0 -b .erisapichange
%patch4 -p0 -b .missingincludes
%patch5 -p0 -b .luafix
%patch6 -p0 -b .compileopts
chmod a-x COPYING AUTHORS
chmod a-x */*.h
chmod a-x */*.cpp
chmod a-x */*.xpm

%build

# Since this isn't an actual release we need to do autotools stuff
./autogen.sh
%configure || cat config.log
make %{?_smp_mflags}

%install
make install DESTDIR=$RPM_BUILD_ROOT

desktop-file-install  \
    --delete-original --dir=$RPM_BUILD_ROOT%{_datadir}/applications \
    $RPM_BUILD_ROOT%{_datadir}/applications/%{name}.desktop

mkdir -p $RPM_BUILD_ROOT%{_datadir}/pixmaps
mv $RPM_BUILD_ROOT%{_datadir}/icons/worldforge/sear_icon.xpm \
    $RPM_BUILD_ROOT%{_datadir}/pixmaps/


%files
%doc AUTHORS ChangeLog COPYING NEWS README TODO
%{_bindir}/%{name}
%{_bindir}/%{name}-bin
%{_datadir}/applications/*.desktop
%{_datadir}/pixmaps/sear_icon.xpm
# datadir/%{name} is owned by sear-media
%{_datadir}/%{name}/*


%changelog
* Thu Jun 07 2012 Igor Vlasenko <viy@altlinux.ru> 0.6.4-alt3_0.8.g0b70ddb
- update to new release by fcimport

* Wed May 09 2012 Igor Vlasenko <viy@altlinux.ru> 0.6.4-alt3_0.7.g0b70ddb
- update to new release by fcimport

* Fri Mar 02 2012 Igor Vlasenko <viy@altlinux.ru> 0.6.4-alt3_0.5.g0b70ddb
- rebuild with fixed sourcedep analyser (#27020)

* Tue Feb 21 2012 Igor Vlasenko <viy@altlinux.ru> 0.6.4-alt2_0.5.g0b70ddb
- rebuild with new libwfmath

* Wed Feb 01 2012 Igor Vlasenko <viy@altlinux.ru> 0.6.4-alt1_0.5.g0b70ddb
- update to new release by fcimport

* Sat Jan 21 2012 Igor Vlasenko <viy@altlinux.ru> 0.6.4-alt1_0.4.g0b70ddb
- update to new release by fcimport

* Fri Nov 25 2011 Igor Vlasenko <viy@altlinux.ru> 0.6.4-alt1_0.2.g0b70ddb
- update to new release by fcimport

* Sat Jul 02 2011 Igor Vlasenko <viy@altlinux.ru> 0.6.4-alt1_0.1.g0b70ddb
- initial release by fcimport

