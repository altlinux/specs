%define gimpdatadir %(gimptool-2.0 --gimpdatadir)

Name: gimp-script-colortemp
Version: 2.1
Release: alt1

Summary: Gimp script for changing the color temperature of images
License: GPLv2+
Group: Graphics

Url: http://www.dealfaro.com/home/code/colortemp.html
Source: http://www.dealfaro.com/home/code/2.4/colortemp.scm

BuildArch: noarch
Requires: gimp >= 2.2

# Automatically added by buildreq on Sat Mar 29 2008
BuildRequires: libgimp-devel

%description
Gimp script for changing the color temperature of images.

%prep
%setup -c -T
cp -a %_sourcedir/colortemp.scm .

%build

%install
install -pD -m644 colortemp.scm %buildroot%gimpdatadir/scripts/colortemp.scm

%files
%gimpdatadir/scripts/*

%changelog
* Fri Mar 28 2008 Victor Forsyuk <force@altlinux.org> 2.1-alt1
- 2.1

* Fri Sep 14 2007 Victor Forsyuk <force@altlinux.org> 1.6-alt1
- Initial build.
