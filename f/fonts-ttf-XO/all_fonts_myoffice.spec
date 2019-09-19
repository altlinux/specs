Name: fonts-ttf-XO
Version: 20190919
Release: alt1

Summary: MyOffice fonts
License: XO Fonts
Group: System/Fonts/True type
Url: https://fonts.myoffice.ru/
Source: https://fonts.myoffice.ru/wp-content/themes/template/fonts_page/files/all_fonts_myoffice.zip
# elinks -dump https://fonts.myoffice.ru/license/ > LICENSE.txt  
Source1: LICENSE.txt

BuildArch: noarch
PreReq: fontconfig

BuildRequires: unzip rpm-build-fonts

%description
%summary

%prep
%setup -c
cp %SOURCE1 .

%build
ln */*.ttf .
%install
%ttf_fonts_install XO

%files -f XO.files
%doc LICENSE.txt

%changelog
* Thu Sep 19 2019 Fr. Br. George <george@altlinux.ru> 20190919-alt1
- Version update

* Thu Dec 22 2016 Fr. Br. George <george@altlinux.ru> 20161222-alt1
- Initial build for ALT

