%define rname	colorfultabs
%define cid 	\{0545b830-f0aa-4d7e-8820-50a4629a56fe\}
%define ciddir  %firefox_noarch_extensionsdir/%cid

Name: firefox-%rname
Version: 23.8
Release: alt1

Summary: ColorfulTabs extension for Firefox
License: Creative Commons Attribution-Noncommercial-No Derivative Works 3.0 United States
Group: Networking/WWW

Url: http://www.binaryturf.com/free-software/colorfultabs-for-firefox/
# repackaged due to "mismatch between local and central GPF bit 11"
Source: https://www.binaryturf.com/files/extensions/colorfultabs/%rname%version.zip
Packager: Michael Shigorin <mike@altlinux.org>

BuildArch: noarch
BuildRequires(pre): rpm-build-firefox
BuildRequires: unzip

# these are ELF binaries for Mozilla Weave
%define _verify_elf_method skip
%brp_strip_none %ciddir
AutoReq: yes, nolib, noshell

%description
ColorfulTabs is an add-on for the popular browser Firefox.
Firefox is known for its tabbed-browsing feature(s). ColorfulTabs
takes the experience to the next level. ColorfulTabs colors every
tab in a unique color and makes them easy to distinguish while
enhancing the appeal of the Firefox interface. ColorfulTabs is
the favorite of the Firefox users. In the words of one of the
million users...

    "Just wanted to let you know I absolutely love your
    Colourful Tabs add on for Firefox! It's one of the best
    and my personal favourite of all add-ons available.
    Thank you so much for this!"

%prep
%setup -c

%install
mkdir -p %buildroot/%ciddir
cp -pr * %buildroot/%ciddir

%postun
if [ "$1" = 0 ]; then [ ! -d "%ciddir" ] || rm -rf "%ciddir"; fi

%files
%ciddir

%changelog
* Mon May 12 2014 Michael Shigorin <mike@altlinux.org> 23.8-alt1
- built for ALT Linux
