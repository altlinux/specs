%define gimpver 2.0

Name: gimp-plugin-ace2
Version: 0.6.7
Release: alt1

Summary: Adaptive Contrast Enhancement plugin for Gimp
License: GPLv2+
Group: Graphics

Url: http://registry.gimp.org/plugin?id=5221
Source: gimp-ace-%version.tar.gz

Requires: gimp >= 2.2

# Automatically added by buildreq on Fri Sep 07 2007
BuildRequires: libgimp-devel perl-XML-Parser

%description
The basic "Stretch Contrast" operation takes in the whole image at once, and
if there is a white pixel anywhere in the image and a black pixel anywhere in
the image, it figures the contrast is already as good as can be. But Adaptive
Contrast Enhancement works to increase the contrast locally, and brings out
details that most wide-sweeping contrast-enhancements pass over.

%prep
%setup -n gimp-ace-%version

%build
%configure
%make_build

%install
%make DESTDIR=%buildroot install

%files
%_libdir/gimp/%gimpver/plug-ins/*
# NB: There are no real help files, only templates:
%_datadir/gimp-ace

%changelog
* Fri Sep 07 2007 Victor Forsyuk <force@altlinux.org> 0.6.7-alt1
- Initial build.
