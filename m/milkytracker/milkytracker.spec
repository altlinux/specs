# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-fedora-compat
BuildRequires: /usr/bin/desktop-file-install gcc-c++ libalsa-devel libglvnd-devel
# END SourceDeps(oneline)
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
Name:           milkytracker
Version:        1.0.0
Release:        alt1_3
Summary:        Module tracker software for creating music

Group:          Sound
License:        GPLv3+
URL:            http://www.milkytracker.org/
Source0:        https://github.com/milkytracker/MilkyTracker/archive/v%{version}.tar.gz
Patch0:         milkytracker-1.0.0-rtmidi-name.patch
Patch1:         milkytracker-1.0.0-sdlmain.patch

BuildRequires:  libSDL2-devel
BuildRequires:  ctest cmake
BuildRequires:  desktop-file-utils
BuildRequires:  librtmidi-devel
BuildRequires:  zlib-devel
BuildRequires:  zziplib-devel
BuildRequires:  libjack-devel
Source44: import.info

%description
MilkyTracker is an application for creating music in the .MOD and .XM formats.
Its goal is to be free replacement for the popular Fasttracker II software.

%prep
%setup -q -n MilkyTracker-%{version}

find . -regex '.*\.\(cpp\|h\|inl\)' -print0 | xargs -0 chmod 644

%patch0 -p1
%patch1 -p1

%build
mkdir build
cd build
%{fedora_cmake} -DBUILD_SHARED_LIBS:BOOL=OFF ..
%make_build

%install
cd build
make install DESTDIR=%{buildroot}
cd ..

# copy the icon
mkdir -p %{buildroot}%{_datadir}/pixmaps
cp -p resources/pictures/carton.png %{buildroot}%{_datadir}/pixmaps/milkytracker.png

# copy the desktop file
desktop-file-install \
  --dir=%{buildroot}%{_datadir}/applications/ resources/milkytracker.desktop


%files
%{_bindir}/milkytracker
%{_datadir}/applications/%{name}.desktop
%{_datadir}/pixmaps/milkytracker.png
%{_datadir}/%{name}
%{_docdir}/%{name}

%changelog
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

