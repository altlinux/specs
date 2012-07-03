Name: fonts-ttf-PT
Version: 2012.05
Release: alt1

Summary: ParaType TrueType font family
License: distributable
Group: System/Fonts/True type
Url: http://fonts.ru/public/
Source0: http://www.fontstock.com/public/PTSans.zip
Source1: http://www.fontstock.com/public/PTSerif.zip
Source4: http://www.fontstock.com/public/PTMono.zip
Source2: http://www.paratype.ru/public/Info_PT_SS.pdf
Source3: http://www.paratype.ru/public/Press_release_PT_SS.pdf

BuildArch: noarch
PreReq: fontconfig
# Automatically added by buildreq on Wed Mar 30 2011
BuildRequires: unzip

BuildRequires: unzip rpm-build-fonts
Obsoletes: fonts-ttf-PTSans

%description
ParaType font family

%prep
%setup -qc
unzip -o %SOURCE1
unzip -o %SOURCE4
cp %SOURCE2 %SOURCE3 .

%build

%install
%ttf_fonts_install PT

%files -f PT.files
%doc *.pdf *.txt

%changelog
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

