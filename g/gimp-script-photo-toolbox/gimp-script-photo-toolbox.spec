%define gimpver 2.0

Name: gimp-script-photo-toolbox
Version: 1.00
Release: alt1

Summary: Gimp plugin to perform several actions on a photo in one time
License: GPLv2+
Group: Graphics

Url: http://registry.gimp.org/plugin?id=9072
Source: photo-toolbox.scm

BuildArch: noarch
Requires: gimp >= 2.2

%description
Perform several actions on a photo in one time such as defocus, desaturate
(several papers emulations), toning, add grain.

%prep
%setup -c -T
cp -a %_sourcedir/photo-toolbox.scm .

%build

%install
install -d %buildroot%_datadir/gimp/%gimpver/scripts/
install -p -m644 photo-toolbox.scm %buildroot%_datadir/gimp/%gimpver/scripts/

%files
%_datadir/gimp/%gimpver/scripts/*

%changelog
* Fri Sep 14 2007 Victor Forsyuk <force@altlinux.org> 1.00-alt1
- Initial build.
