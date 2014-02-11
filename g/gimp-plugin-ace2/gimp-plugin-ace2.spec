%define gimpver 2.0

Name: gimp-plugin-ace2
Version: 0.6.7
Release: alt2

Summary: Adaptive Contrast Enhancement plugin for Gimp
License: GPLv2+
Group: Graphics

Url: http://registry.gimp.org/node/20
Source: gimp-ace-%version.tar.gz
Patch: gimp-ace-0.6.7-alt-link.patch

Requires: gimp >= 2.2

# Automatically added by buildreq on Fri Sep 07 2007
BuildRequires: libgimp-devel intltool perl-XML-Parser

%description
The basic "Stretch Contrast" operation takes in the whole image at once, and
if there is a white pixel anywhere in the image and a black pixel anywhere in
the image, it figures the contrast is already as good as can be. But Adaptive
Contrast Enhancement works to increase the contrast locally, and brings out
details that most wide-sweeping contrast-enhancements pass over.

%prep
%setup -n gimp-ace-%version
%patch

%build
%autoreconf
%configure
%make_build

%install
%make DESTDIR=%buildroot install

%files
%_libdir/gimp/%gimpver/plug-ins/*
# NB: There are no real help files, only templates:
%_datadir/gimp-ace

%changelog
* Tue Feb 11 2014 Yuri N. Sedunov <aris@altlinux.org> 0.6.7-alt2
- explicitly link against libm

* Mon Apr 15 2013 Dmitry V. Levin (QA) <qa_ldv@altlinux.org> 0.6.7-alt1.qa1
- NMU: rebuilt for debuginfo.

* Fri Sep 07 2007 Victor Forsyuk <force@altlinux.org> 0.6.7-alt1
- Initial build.
