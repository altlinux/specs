Name: psi-plus-plugin-psimedia
Version: 1.0.3
Release: alt2

Summary: PsiMedia plugin for Psi+
License: GPLv2.1
Group:  Networking/Instant messaging

URL: http://delta.affinix.com/psimedia/
Packager: Nazarov Denis <nenderus@altlinux.org>

Source0: http://delta.affinix.com/download/psimedia/psimedia-1.0.3.tar.bz2

Patch0: 0010-psimedia-varrate-asterisk.diff
Patch1: 0020-psimedia-win32-compilation-paths.diff
Patch2: 0030-psimedia-uvcvideo-fix.diff
Patch3: 0040-psimedia-2.6.38-compilation-fix.diff
Patch4: 0050-psimedia-drop-v4lsrc-gst-plugin.diff

Requires: psi-plus

BuildRequires: gcc-c++
BuildRequires: gst-plugins-devel >= 0.10.22
BuildRequires: liboil-devel >= 0.3
BuildRequires: libqt4-network >= 4.4.0
BuildRequires: libspeex-devel >= 1.2
BuildRequires: phonon-devel
BuildRequires: python-module-z3c
BuildRequires: python-module-z3c.recipe
BuildRequires: qconf

%description
PsiMedia is a thick abstraction layer for providing audio and video RTP services to Psi-like IM clients.
The implementation is based on GStreamer.

%prep
%setup -n psimedia-1.0.3
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1

%build
qconf
./configure
%make_build

%install
install -Dp -m 0644 gstprovider/libgstprovider.so %buildroot%_libdir/psi-plus/plugins/libgstprovider.so

%files
%doc README TODO
%_libdir/psi-plus/plugins/libgstprovider.so

%changelog
* Thu Jun 23 2011 Nazarov Denis <nenderus@altlinux.org> 1.0.3-alt2
- Add 5 patches

* Wed Jun 22 2011 Nazarov Denis <nenderus@altlinux.org> 1.0.3-alt0.M60T.1
- Build for branch t6

* Wed Jun 22 2011 Nazarov Denis <nenderus@altlinux.org> 1.0.3-alt1
- Initial build for ALT Linux
