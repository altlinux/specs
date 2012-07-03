Name: fonts-ttf-PTSans
Version: 2010.11
Release: alt1

Summary: ParaType Sans TrueType font
License: OFL
Group: System/Fonts/True type
Url: http://fonts.ru/public/
Source: http://www.fontstock.com/public/PTSans_OFL.zip
# wget http://fonts.ru/public -O doc.ru.html
#Source2: doc.ru.html
#Source3: http://www.fontstock.com/public/Info_PT_Sans.pdf

BuildArch: noarch
PreReq: fontconfig
BuildRequires: unzip rpm-build-fonts

%description
ParaType Sans font familly

%prep
%setup -qc

%build

%install
%ttf_fonts_install PTSans

%post
%post_fonts

%postun
%postun_fonts

%files -f PTSans.files
%doc PTSansOFL.txt

%changelog
* Sat Nov 06 2010 Fr. Br. George <george@altlinux.ru> 2010.11-alt1
- Version up
- (Closes #22780)

* Mon Apr 05 2010 Fr. Br. George <george@altlinux.ru> 2010.04-alt1
- Version up
- Switch to Ofen Font License

* Mon Dec 28 2009 Fr. Br. George <george@altlinux.ru> 2009.12-alt1
- Initial build from scratch

