%define gimpdatadir %(gimptool-2.0 --gimpdatadir)

Name: gimp-script-ISONoiseReduction
Version: 2.4
Release: alt1

Packager: Victor Forsyuk <force@altlinux.org>

Summary: Gimp script for reducing sensor noise at high ISO values
License: GPLv3+
Group: Graphics

Url: http://registry.gimp.org/node/104
Source: http://registry.gimp.org/files/Eg-ISONoiseReduction.scm

BuildArch: noarch
Requires: gimp >= 2.2

# Automatically added by buildreq on Thu Aug 28 2008
BuildRequires: libgimp-devel

%description
Gimp script for reducing sensor noise at high ISO values by masking the edges
and then blurring the individual color channels or the luminance channel only.

Using a plugin like Wavelet denoise or greycstoration might actually give you
better results and more options for fine tuning.

%prep
%setup -c -T
cp -a %_sourcedir/Eg-ISONoiseReduction.scm .
# Convert to Unix-style line endings and eliminate submenu named after author
%__subst 's/\r//g' Eg-ISONoiseReduction.scm
%__subst 's@Filters/Eg@Filters/Noise@' Eg-ISONoiseReduction.scm

%build

%install
install -pD -m644 Eg-ISONoiseReduction.scm %buildroot%gimpdatadir/scripts/ISONoiseReduction.scm

%files
%gimpdatadir/scripts/*

%changelog
* Thu Aug 28 2008 Victor Forsyuk <force@altlinux.org> 2.4-alt1
- 2.4

* Thu Sep 13 2007 Victor Forsyuk <force@altlinux.org> 2.1-alt1
- Initial build.
