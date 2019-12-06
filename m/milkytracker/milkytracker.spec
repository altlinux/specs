Group: Sound
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-fedora-compat
BuildRequires: /usr/bin/desktop-file-install /usr/bin/xmlto libalsa-devel libglvnd-devel
# END SourceDeps(oneline)
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
Name:           milkytracker
Version:        1.02.00
Release:        alt3_5
Summary:        Module tracker software for creating music

License:        GPLv3+
URL:            http://www.milkytracker.org/
Source0:        https://github.com/milkytracker/MilkyTracker/archive/v%{version}.tar.gz
Patch0:         milkytracker-1.0.0-sdlmain.patch
Patch1:         milkytracker-1.02.00-buffer-overflows.patch
Patch2:         milkytracker-1.02.00-cve-2019-14464.patch

BuildRequires:  libSDL2-devel
BuildRequires:  ctest cmake
BuildRequires:  desktop-file-utils
BuildRequires:  gcc-c++
BuildRequires:  libappstream-glib
BuildRequires:  librtmidi-devel
BuildRequires:  zlib-devel
BuildRequires:  zziplib-devel
BuildRequires:  libjack-devel
Source44: import.info
Patch33: milkytracker-1.02.00-gcc8-fix.patch

%description
MilkyTracker is an application for creating music in the .MOD and .XM formats.
Its goal is to be free replacement for the popular Fasttracker II software.

%prep
%setup -q -n MilkyTracker-%{version}

find . -regex '.*\.\(cpp\|h\|inl\)' -print0 | xargs -0 chmod 644

%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch33 -p1

%build
mkdir build
cd build
%{fedora_cmake} -DBUILD_SHARED_LIBS:BOOL=OFF ..
%make_build

%install
cd build
make install DESTDIR=%{buildroot}
cd ..

# move the documentation directory (version 1.01.00 started installing
# it as MilkyTracker instead of milkytracker and we want to keep the
# name in sync with the package name)
mv -v %{buildroot}%{_docdir}/MilkyTracker %{buildroot}%{_docdir}/%{name}

# copy the icon
mkdir -p %{buildroot}%{_datadir}/pixmaps
cp -p resources/pictures/carton.png %{buildroot}%{_datadir}/pixmaps/milkytracker.png

# copy the desktop file
desktop-file-install \
  --dir=%{buildroot}%{_datadir}/applications/ resources/milkytracker.desktop

# copy the appdata file
install -v -D -m 644 resources/milkytracker.appdata %{buildroot}%{_datadir}/metainfo/%{name}.appdata.xml
appstream-util validate-relax --nonet %{buildroot}%{_datadir}/metainfo/*.appdata.xml


%files
%{_bindir}/milkytracker
%{_datadir}/applications/%{name}.desktop
%{_datadir}/metainfo/%{name}.appdata.xml
%{_datadir}/pixmaps/milkytracker.png
%{_datadir}/%{name}
%{_docdir}/%{name}

%changelog
* Thu Dec 05 2019 Igor Vlasenko <viy@altlinux.ru> 1.02.00-alt3_5
- update to new release by fcimport

* Thu Feb 14 2019 Ivan Razzhivin <underwit@altlinux.org> 1.02.00-alt3_1
- GCC8 fix

* Thu Jun 21 2018 Igor Vlasenko <viy@altlinux.ru> 1.02.00-alt2_1
- rebuild with new librtmidi

* Mon May 07 2018 Igor Vlasenko <viy@altlinux.ru> 1.02.00-alt1_1
- update to new release by fcimport

* Fri Oct 20 2017 Igor Vlasenko <viy@altlinux.ru> 1.0.0-alt1_3
- update to new release by fcimport

* Sun Sep 20 2015 Igor Vlasenko <viy@altlinux.ru> 0.90.85-alt2_11
- update to new release by fcimport

* Wed Aug 27 2014 Igor Vlasenko <viy@altlinux.ru> 0.90.85-alt2_9
- update to new release by fcimport

* Wed Jul 09 2014 Igor Vlasenko <viy@altlinux.ru> 0.90.85-alt2_8
- moved to Sisyphus by mike@ request

* Thu Jun 26 2014 Igor Vlasenko <viy@altlinux.ru> 0.90.85-alt1_8
- update to new release by fcimport

* Tue Aug 27 2013 Igor Vlasenko <viy@altlinux.ru> 0.90.85-alt1_7
- update to new release by fcimport

* Wed May 01 2013 Igor Vlasenko <viy@altlinux.ru> 0.90.85-alt1_6
- initial fc import

