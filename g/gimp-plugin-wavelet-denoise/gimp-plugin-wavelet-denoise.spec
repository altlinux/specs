%def_disable snapshot
%define _name wavelet-denoise
%define gimpplugindir %(gimptool-2.0 --gimpplugindir)

Name: gimp-plugin-%_name
Version: 0.4
Release: alt1

Summary: GIMP tool for reducing sensor noise in an image
License: GPLv2+
Group: Graphics
Url: https://github.com/mrossini-ethz/gimp-wavelet-denoise

%if_disabled snapshot
Source: %url/archive/v%version/gimp-%_name-%version.tar.gz
%else
Vcs: https://github.com/mrossini-ethz/gimp-wavelet-denoise.git
Source: gimp-%_name-%version.tar
%endif

Requires: gimp >= 2.6
BuildRequires(pre): libgimp-devel

%description
The wavelet denoise plugin is a tool to selectively reduce noise in individual
channels of an image with optional RGB<->YCbCr conversion. It has a user
inteface to adjust the amount of denoising applied. The wavelet nature of the
algorithm makes the processing quite fast.

%prep
%setup -n gimp-%_name-%version

%build
%make_build

%install
%make LOCALEDIR=%buildroot%_datadir/locale install -C po
install -pD -m755 src/%_name %buildroot%gimpplugindir/plug-ins/%_name
%find_lang --output=%_name.lang gimp20-%_name-plug-in

%files -f %_name.lang
%gimpplugindir/plug-ins/*
%doc AUTHORS ChangeLog README

%changelog
* Sat Nov 12 2022 Yuri N. Sedunov <aris@altlinux.org> 0.4-alt1
- 0.4 (new %%url)

* Sat Dec 05 2020 Yuri N. Sedunov <aris@altlinux.org> 0.3.1-alt3
fixed build with gcc10/-fno-common (fc patch)

* Tue Sep 16 2014 Yuri N. Sedunov <aris@altlinux.org> 0.3.1-alt2
- fixed build

* Thu Jul 09 2009 Victor Forsyuk <force@altlinux.org> 0.3.1-alt1
- 0.3.1

* Thu Aug 28 2008 Victor Forsyuk <force@altlinux.org> 0.2-alt1
- Initial build.
