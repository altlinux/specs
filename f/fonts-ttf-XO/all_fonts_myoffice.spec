Name: fonts-ttf-XO
Version: 20161222
Release: alt1

Summary: MyOffice fonts
License: XO Fonts
Group: System/Fonts/True type
Url: https://fonts.myoffice.ru/
Source: https://fonts.myoffice.ru/wp-content/themes/template/fonts_page/files/all_fonts_myoffice.zip

BuildArch: noarch
PreReq: fontconfig
# Automatically added by buildreq on Wed Mar 30 2011
BuildRequires: unzip

BuildRequires: unzip rpm-build-fonts

%description
%summary

%prep
%setup -c

%build
ln */*.ttf .
%install
%ttf_fonts_install XO

%files -f XO.files
%doc XO_Caliburn/XO_Fonts_License.txt

%changelog
* Thu Dec 22 2016 Fr. Br. George <george@altlinux.ru> 20161222-alt1
- Initial build for ALT

