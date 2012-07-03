# Unpackaged files in buildroot should terminate build
%define _unpackaged_files_terminate_build 1

Name: djmount
Version: 0.71
Release: alt1.1

Summary: FUSE filesystem for accessing Media Server content via UPnP
License: %gpl2plus
Group: Networking/Other
URL: http://djmount.sourceforge.net/
Packager: Artem Zolochevskiy <azol@altlinux.ru>

# http://downloads.sourceforge.net/djmount/djmount-0.71.tar.gz
Source: djmount-0.71.tar
Patch0: djmount-alt-upnp.patch

BuildRequires(pre): rpm-build-licenses
BuildRequires: libfuse-devel libupnp-devel

%description
djmount is a UPnP AV client. It mounts as a Linux filesystem (using FUSE)
the media content of compatible UPnP AV devices.

djmount discovers automatically all UPnP AV Media Servers on the network,
and make the content available in a directory tree. All shared files
(e.g. Audio or Video files) are directly visible and can be played using
your favorite media player.

%prep
%setup
%patch0 -p2

%build
%configure --with-external-libupnp
%make_build

%install
%make_install DESTDIR=%buildroot install

# COPYING as symlinks
ln -sf %_licensedir/GPL-2 COPYING

%files
%doc -d AUTHORS ChangeLog COPYING NEWS README search_help.txt THANKS TODO 
%_bindir/*

%changelog
* Thu Feb 02 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.71-alt1.1
- Fixed build

* Mon Nov 10 2008 Artem Zolochevskiy <azol@altlinux.ru> 0.71-alt1
- initial build for Sisyphus

