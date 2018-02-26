# BEGIN SourceDeps(oneline):
BuildRequires: /usr/bin/gtk-update-icon-cache /usr/bin/update-desktop-database gcc-c++ pkgconfig(Equalizer) pkgconfig(gl) pkgconfig(libavcodec) pkgconfig(libavdevice) pkgconfig(libavformat) pkgconfig(libavutil) pkgconfig(liblircclient0) pkgconfig(libswscale)
# END SourceDeps(oneline)
Group: Emulators
Name:           wlcreator
Version:        1.0.4
Release:        alt1_1.R
BuildArch:      noarch
Summary:        Creating Linux desktop launchers for Windows programs

License:        GPLv3+
URL:            http://code.google.com/p/wine-launcher-creator/
Source0:        http://wine-launcher-creator.googlecode.com/files/wine-launcher-creator-%{version}.tar.gz
Source1:        wlcreator.desktop

BuildRequires:  desktop-file-utils
Requires:       icoutils python-module-PyQt4
Source44: import.info

%description
WLCreator is a Python program (script) that creates Linux desktop launchers 
for Windows programs (using Wine).

%prep
%setup -q -n wine-launcher-creator-%{version}

%build

%install
%{__install} -D wlcreator.py $RPM_BUILD_ROOT%{_bindir}/wlcreator
desktop-file-install --dir=$RPM_BUILD_ROOT%{_datadir}/applications/ %{SOURCE1}

%files
%doc NoInternet.txt Readme.txt gpl.txt
%{_bindir}/wlcreator
%{_datadir}/applications/wlcreator.desktop

%changelog
* Wed Feb 22 2012 Igor Vlasenko <viy@altlinux.ru> 1.0.4-alt1_1.R
- update to new release by fcimport

* Fri Dec 16 2011 Igor Vlasenko <viy@altlinux.ru> 1.0.3-alt1_2.R
- converted by srpmconvert script

