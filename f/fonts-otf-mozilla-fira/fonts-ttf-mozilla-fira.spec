%define oname fira
%define fname mozilla-fira

Name: fonts-otf-%fname
Version: 20130925
Release: alt1

Summary: Mozilla's Fira fonts
License: OFL
Group: System/Fonts/True type

Url: https://www.mozilla.org/en-US/styleguide/products/firefox-os/typeface/
# Upstream tarball is not versioned. See the "Downloads" section of %%{url}.
# Upstream does not provide a direct download link.
Source0: %oname-%version.zip
# The license file was obtained from here:
# https://raw.github.com/mozilla/Fira/master/LICENSE
# It is the standard OFL.
Source1: fira-LICENSE

BuildArch: noarch
BuildRequires: unzip, rpm-build-fonts >= 0.4
PreReq: fontconfig >= 2.4.2

%description
Originally designed to integrate with the character of Firefox OS,
Fira is a new set of sans-serif fonts which focuses on legibility.

%prep
%setup -c
mv */*.otf .
cp -p %SOURCE1 LICENSE

%install
%otf_fonts_install %fname

%files -f %fname.files
%doc LICENSE

%changelog
* Fri May 30 2014 Michael Shigorin <mike@altlinux.org> 20130925-alt1
- built for ALT Linux (description from fedora spec)

