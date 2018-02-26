%define fname droid

Name: fonts-ttf-droid
Version: 1.0
Release: alt1

Summary: TrueType fonts of droid fonts

License: Apache 2
Group: System/Fonts/True type
Url: http://www.droidfonts.com/droidfonts/

Packager: Mikhail Yakshin <greycat@altlinux.org>

Source: %name-%version.tar.bz2

BuildArch: noarch

BuildRequires: rpm-build-fonts >= 0.3
PreReq: fontconfig >= 2.4.2

%description
The Droid family of fonts was designed by Ascender's Steve Matteson
beginning in the fall of 2006. The goal was to provide optimal quality
and reading comfort on a mobile handset. The Droid fonts were optimized
for use in application menus, web browsers and for other screen text.

Ascender Corporation worked closely with Google and the Open Handset
Alliance to develop these system fonts for Android, a free, open source,
and fully customizable mobile platform.

%prep
%setup -q -n fonts

%install
%ttf_fonts_install %fname

%post
%post_fonts

%postun
%postun_fonts

%files -f %fname.files
%doc NOTICE README.txt

%changelog
* Sun Mar 08 2009 Mikhail Yakshin <greycat@altlinux.org> 1.0-alt1
- Initial build for ALT Linux
