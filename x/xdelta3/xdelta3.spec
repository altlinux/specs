Summary: A binary delta generator
Name: xdelta3
Version: 3.0u
Release: alt1
Source0: http://xdelta.googlecode.com/files/%name-%version.tar
Patch0: %name-%version-%release.patch
Url: http://xdelta.org
License: GPL
Group: File tools

%description
Xdelta3 is the third and latest release of Xdelta, which is a set of
tools and APIs for reading and writing compressed deltas. Deltas
encode the differences between two versions of a document. This
release features a completely new compression engine, several
algorithmic improvements, a fully programmable interface modelled
after zlib, in addition to a command-line utility, use of the RFC3284
(VCDIFF) encoding, a python extension, and now 64-bit support.

%prep
%setup -q
%patch0 -p1

%build
make  all \
	xdelta3 \
	xdelta3-decoder \
	xdelta3-tools \
	xdelta3-everything \
	xdelta3-all.o
ar cr libxdelta3.a xdelta3-all.o
ranlib libxdelta3.a
chmod 644 COPYING

%install
mkdir -p %buildroot%_bindir

install -m 755 xdelta3 \
	xdelta3-decoder \
	xdelta3-tools \
	xdelta3-everything %buildroot%_bindir

%files
%doc COPYING README
%_bindir/*

%changelog
* Tue Nov 25 2008 Anton Farygin <rider@altlinux.ru> 3.0u-alt1
- new version

* Fri Dec 14 2007 Anton Farygin <rider@altlinux.ru> 3.0t-alt1
- first build for Sisyphus
