Name: fonts-ttf-droid
Version: 2
Release: alt1

Summary: Server-side component of google-droid fonts
License: BSD
Group: System/Fonts/True type

BuildArch: noarch
Requires(pre): fontconfig

BuildRequires: rpm-build-fonts

BuildRequires: fonts-ttf-google-droid-sans fonts-ttf-google-droid-serif fonts-ttf-google-droid-sans-mono

Requires: fonts-ttf-google-droid-sans fonts-ttf-google-droid-serif fonts-ttf-google-droid-sans-mono

%description
%summary

%prep
%build
rm -rf %name && mkdir %name
cd %name
ln -s %_datadir/fonts/ttf/google-droid/* .

%install
cd %name
%ttf_fonts_install google-droid

%files -f %name/google-droid.files
%dir %_datadir/fonts/ttf/google-droid
%exclude %_datadir/fonts/ttf/google-droid/*ttf

%changelog
* Mon Feb 18 2019 Fr. Br. George <george@altlinux.ru> 2-alt1
- Initial build for ALT

