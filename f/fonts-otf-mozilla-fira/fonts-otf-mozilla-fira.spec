%define oname fira
%define fname mozilla-fira

Name: fonts-otf-%fname
Version: 3.108
Release: alt1
Serial: 1

Summary: Mozilla's Fira fonts
License: OFL
Group: System/Fonts/True type

Url: https://github.com/mozilla/Fira
Source0: %name-%version.tar
Source1: LICENSE

BuildArch: noarch
BuildRequires: rpm-build-fonts >= 0.4
PreReq: fontconfig >= 2.4.2

%description
Originally designed to integrate with the character of Firefox OS,
Fira is a new set of sans-serif fonts which focuses on legibility.

%prep
%setup
cp -a %SOURCE1 .

%install
%otf_fonts_install %fname

%files -f %fname.files
%doc LICENSE

%changelog
* Thu Jun 05 2014 Michael Shigorin <mike@altlinux.org> 1:3.108-alt1
- 3.108 built from upstream git
  + fixes https://github.com/mozilla/Fira/issues/39
- reworked build appropriately

* Fri May 30 2014 Michael Shigorin <mike@altlinux.org> 20130925-alt1
- built for ALT Linux (description from fedora spec)

