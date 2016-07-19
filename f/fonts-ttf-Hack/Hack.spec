Name: fonts-ttf-Hack
Version: 2.020
Release: alt1

Summary: A hand groomed and optically balanced font familly to be your go-to code face
License: Modified OFL
Group: System/Fonts/True type
Url: http://sourcefoundry.org/hack
Source: Hack-v%version-ttf.zip

BuildArch: noarch
PreReq: fontconfig

# Automatically added by buildreq on Tue Sep 01 2015
BuildRequires: unzip

BuildRequires: rpm-build-fonts

%description
A Family of Four Faces. Hack includes monospaced regular, bold, oblique,
and bold oblique sets to cover all of your syntax highlighting needs.
Multilingual. Over 1500 glyphs that include lovingly tuned expanded
Latin, modern Greek, and Cyrillic character sets. Powerline Support.
Powerline glyphs are included in the regular set. Patching is not
necessary. Install and go.

%prep
%setup -c

%build
%install
%ttf_fonts_install Hack

%files -f Hack.files
%changelog
* Thu Jul 14 2016 Fr. Br. George <george@altlinux.ru> 2.020-alt1
- Autobuild version bump to 2.020

* Wed Nov 18 2015 Fr. Br. George <george@altlinux.ru> 2.018-alt1
- Autobuild version bump to 2.018

* Tue Sep 01 2015 Fr. Br. George <george@altlinux.ru> 2.010-alt1
- Autobuild version bump to 2.010

* Tue Sep 01 2015 Fr. Br. George <george@altlinux.ru> 2.009-alt1
- Initial build

