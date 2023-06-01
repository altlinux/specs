Summary: A binary delta generator
Name: xdelta3
Version: 3.1.0
Epoch: 1
Release: alt2
Source0: http://xdelta.googlecode.com/files/%name-%version.tar
BuildRequires: gcc-c++ liblzma-devel
Url: http://xdelta.org
License: GPLv2
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

%build
%autoreconf
%configure
%make

%install
%makeinstall

%files
%doc COPYING README.md
%_bindir/*
%_man1dir/*.1*

%changelog
* Thu Jun 01 2023 Fr. Br. George <george@altlinux.org> 1:3.1.0-alt2
- Build with liblzma-devel (fix Genshin Impact / Lutris issue)

* Wed Nov 07 2018 Anton Farygin <rider@altlinux.ru> 1:3.1.0-alt1
- 3.1.0

* Wed Jun 29 2016 Anton Farygin <rider@altlinux.ru> 1:3.0.11-alt1
- new version

* Tue Oct 20 2015 Anton Farygin <rider@altlinux.ru> 1:3.0.8-alt1
- new version

* Wed Apr 17 2013 Dmitry V. Levin (QA) <qa_ldv@altlinux.org> 3.0u-alt1.qa1
- NMU: rebuilt for debuginfo.

* Tue Nov 25 2008 Anton Farygin <rider@altlinux.ru> 3.0u-alt1
- new version

* Fri Dec 14 2007 Anton Farygin <rider@altlinux.ru> 3.0t-alt1
- first build for Sisyphus
