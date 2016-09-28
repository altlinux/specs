Name: fonts-ttf-PTAstra
Version: 1001
Release: alt1

Summary: Free Times New Roman full metric analog
License: SIL open font license 1.1
Group: System/Fonts/True type
Url: http://astralinux.com/fonts.html
Source: PTAstra-%version.zip
Source1: README.txt

BuildArch: noarch
PreReq: fontconfig
# Automatically added by buildreq on Wed Mar 30 2011
BuildRequires: unzip

BuildRequires: unzip rpm-build-fonts

%description
Free Times New Roman full metric analog

%prep
%setup -c
cp %SOURCE1 .

%build
%install
%ttf_fonts_install PTAstra

%files -f PTAstra.files
%doc *.txt

%changelog
* Wed Sep 28 2016 Fr. Br. George <george@altlinux.ru> 1001-alt1
- Autobuild version bump to 1001

* Sun Aug 21 2016 Fr. Br. George <george@altlinux.ru> 2016.08-alt1
- Update to actual state (copyright 2014)

* Sun May 06 2012 Fr. Br. George <george@altlinux.ru> 2012.05-alt1
- Add monospace typeface

* Wed Mar 30 2011 Fr. Br. George <george@altlinux.ru> 2011.03-alt1
- Switch back to Paratype licensed recent source
- Add Serif fontset
- change package name

* Sat Nov 06 2010 Fr. Br. George <george@altlinux.ru> 2010.11-alt1
- Version up
- (Closes #22780)

* Mon Apr 05 2010 Fr. Br. George <george@altlinux.ru> 2010.04-alt1
- Version up
- Switch to Ofen Font License

* Mon Dec 28 2009 Fr. Br. George <george@altlinux.ru> 2009.12-alt1
- Initial build from scratch

