Name: lv2core
Version: 4.0
Release: alt1

Summary: Core LV2 specification
License: LGPLv2+
Group: Development/C
Url: http://lv2plug.in/spec/

Packager: Egor Glukhov <kaman@altlinux.org>
Source0: %name-%version.tar

BuildRequires: gcc-c++ python-modules-compiler python-modules-logging

%description
LV2 is a standard for plugins and matching host applications, primarily
targeted at audio processing and generation.

LV2 is a successor to LADSPA, created to address the limitations of
LADSPA which many applications have outgrown.  Compared to LADSPA, all
plugin data is moved from the code to a separate data file, and the code
has been made as generic as possible.  As a result, LV2 can be
independently extended retaining compatibility wherever possible), and
virtually any feasible plugin features can be implemented in an LV2
plugin.

More information about LV2 can be found at <http://lv2plug.in>.

This package is the "core" LV2 specification in usual source package
form. The major version of this package refers to the LV2 specification
revision contained, while the minor version refers only to this package.

%prep
%setup

%build
./waf configure --prefix=%_prefix/ --libdir=%_libdir/
./waf

%install
DESTDIR=%buildroot ./waf install
mkdir -p %buildroot%_pkgconfigdir
mv %buildroot%_prefix/pkgconfig/%name.pc %buildroot%_pkgconfigdir

%files
%doc AUTHORS COPYING ChangeLog README
%_includedir/lv2.h
%_libdir/lv2/%name.lv2/*
%_pkgconfigdir/%name.pc
%_bindir/lv2config

%changelog
* Sat Aug 20 2011 Egor Glukhov <kaman@altlinux.org> 4.0-alt1
- New version

* Thu Jul 15 2010 Egor Glukhov <kaman@altlinux.org> 3.0-alt1
- initial build for Sisyphus
