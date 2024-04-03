%define _unpackaged_files_terminate_build 1

%def_without kde
%def_without mpv

Name:  qimgv
Version: 1.0.3
Release: alt0.alpha

Summary: Image viewer. Fast, easy to use. Optional video support
License: GPL-3.0-or-later
Group: Graphical desktop/Other
Url: https://github.com/easymodo/qimgv

Source: %name-%version.tar

BuildRequires: cmake
BuildRequires: qt5-svg-devel
BuildRequires: tbb-devel
%if_with kde
BuildRequires: libkf5windowsystem
%endif
%if_with mpv 
BuildRequires: libmpv-devel
%endif

%description
Image viewer. Fast, easy to use. Optional video support.

Key features:

  * Simple UI
  * Fast
  * Easy to use
  * Fully configurable, including themes, shortcuts
  * High quality scaling
  * Basic image editing: Crop, Rotate and Resize
  * Ability to quickly copy / move images to different folders
  * Experimental video playback via libmpv
  * Folder view mode
  * Ability to run shell scripts

%if_with mpv
%package freeworld
Summary: Video support for %name

Requires: %name = %EVR

%description freeworld
Video support for %name.
%endif

%prep
%setup

%build
%cmake \
    -DCMAKE_INSTALL_LIBDIR=%_libdir \
    -DVIDEO_SUPPORT:BOOL=%{?_with_mpv:ON}%{!?_with_mpv:OFF} \
    -DKDE_SUPPORT:BOOL=%{?_with_kde:ON}%{!?_with_kde:OFF}
%cmake_build

%install
%cmake_install

%files
%doc README.md
%_bindir/%name
%_datadir/applications/*.desktop
%_datadir/icons/hicolor/*/*/*.png
%_datadir/icons/hicolor/scalable/*/*.svg
%if_with mpv
%_libdir/lib%{name}_player_mpv.so*
%endif

%changelog
* Mon Apr 01 2024 Dmitrii Fomchenkov <sirius@altlinux.org>  1.0.3-alt0.alpha
- Initial build for ALT Linux
