Name: kmscube
Version: 0.0.20181211
Release: alt1

Summary: Bare metal graphics demo using DRM/KMS 
License: X11
Group: Graphics
Url: https://gitlab.freedesktop.org/mesa/kmscube

Source: %name-%version.tar

BuildRequires: libdrm-devel libgbm-devel libEGL-devel libGLES-devel

%description
kmscube is a little demonstration program for how to drive bare metal graphics
without a compositor like X11, wayland or similar, using DRM/KMS (kernel mode
setting), GBM (graphics buffer manager) and EGL for rendering content using
OpenGL or OpenGL ES.

%prep
%setup

%build
%autoreconf
%configure
%make_build

%install
%makeinstall_std

%files
%_bindir/kmscube

%changelog
* Thu Dec 13 2018 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.0.20181211-alt1
- initial
