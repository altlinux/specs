Name: fonts-ttf-PT-pack
Version: 2026.08
Release: alt1

Summary: ParaType TrueType font family
License: OFL-1.1-RFN
Group: System/Fonts/True type
URL: https://www.paratype.ru/collections/pt/44157
Source: PT-Public-Pack.ottt.zip
Source1: http://www.paratype.ru/public/Info_PT_SS.pdf
Source2: http://www.paratype.ru/public/Press_release_PT_SS.pdf

BuildArch: noarch
Requires(pre): fontconfig
BuildRequires: unzip rpm-build-fonts

%description
ParaType font pack

%define fontpackage() \
%global fontpackages %{?fontpackages} fonts-ttf-%1 \
%package -n fonts-ttf-%1 \
Group: System/Fonts/True type \
Summary: %1 familly from ParaType font pack \
%description -n fonts-ttf-%1 \
%1 familly from ParaType font pack \
%files -n fonts-ttf-%1 -f %1.files \
%{nil}

%prep
%setup -c
cp %SOURCE1 %SOURCE2 .

%build

%install
for D in PT/PT/PT-*; do (
        cd "$D"
        FONTNAME="$(basename $D)"
        %ttf_fonts_install $FONTNAME
); done
ln PT/PT/PT-*/*.files .

%fontpackage PT-Sans
%fontpackage PT-Serif
%fontpackage PT-Astra-Sans
%fontpackage PT-Astra-Serif
%fontpackage PT-Mono
%fontpackage PT-Root-UI

%package -n fonts-ttf-PT
Group: System/Fonts/True type
Summary: Allfamilies for ParaType PT
Requires: %fontpackages
Obsoletes: fonts-ttf-PTSans fonts-ttf-PTAstra
Provides: fonts-ttf-PTAstra
%description -n fonts-ttf-PT
%summary

%files -n fonts-ttf-PT
%doc *.pdf

%changelog
* Sat Aug 01 2026 Fr. Br. George <george@altlinux.org> 2026.08-alt1
- Rebuild from ParaType free OFL licensed font pack
- Also provide PTAstra famillies (included)

* Mon Aug 24 2020 Fr. Br. George <george@altlinux.ru> 2016.08-alt2
- Fix license in spec

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

