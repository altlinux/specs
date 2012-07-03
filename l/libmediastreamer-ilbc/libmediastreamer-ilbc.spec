Name: libmediastreamer-ilbc
Version: 2.0.3
Release: alt1

Group: System/Libraries
Summary: An iLBC codec mediastreamer plugin
License: GPLv2+
Url: http://www.linphone.org/eng/download/git.html
Packager: Egor Glukhov <kaman@altlinux.org>

Source: %name-%version.tar
BuildRequires: libmediastreamer-devel >= 2.7.0
BuildRequires: libilbc-devel

%description
Mediastreamer2 is a GPL licensed library to make audio and video
real-time streaming and processing. Written in pure C, it is based
upon the oRTP library.

This package contains an iLBC codec mediastreamer plugin.

%prep
%setup

%autoreconf

%build
export ILBC_LIBS=-lilbc 
export ILBC_CFLAGS=-I/usr
%configure
%make_build

%install
%makeinstall_std

%files
%_libdir/mediastreamer/plugins/*

%changelog
* Thu Mar 24 2011 Egor Glukhov <kaman@altlinux.org> 2.0.3-alt1
- Initial build for Sisyphus
