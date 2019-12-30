#%%define ttf_fontdir %%_datadir/fonts/truetype
%define fname roboto

Name: fonts-ttf-roboto
Version: 1.0
Release: alt2
License: Apache-2.0
Summary: Android Roboto Fonts
Url: http://code.google.com/android/
Group: System/Fonts/True type
# http://www.fontsquirrel.com/fonts/download/roboto
Source: roboto.zip
Source1: COPYING

BuildPreReq: rpm-build-licenses unzip
BuildRequires: rpm-build-fonts
PreReq: fontconfig
BuildArch: noarch

%description
Roboto is a Helvetica alike sans serif font that was introduced with
Android 4.0 (Ice Cream Sandwich).

%prep
%setup -c
cp %SOURCE1 .

%install
%ttf_fonts_install %fname

%files -f %fname.files
%doc COPYING

%changelog
* Fri Dec 27 2019 Gleb F-Malinovskiy <glebfm@altlinux.org> 1.0-alt2
- Fixed license tag.

* Fri Oct 26 2012 Gleb F-Malinovskiy <glebfm@altlinux.org> 1.0-alt1
- initial build from Suse
