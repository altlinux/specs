Name: libmediastreamer-ilbc
Version: 2.1.2
Release: alt3

Group: System/Libraries
Summary: An iLBC codec mediastreamer plugin
License: GPLv2+
Url: http://www.linphone.org/eng/download/git.html
Packager: Alexei Takaseev <taf@altlinux.org>

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
* Fri Mar 03 2017 Alexei Takaseev <taf@altlinux.org> 2.1.2-alt3
- Rebuild with new libmediastreamer 2.15.0

* Tue Aug 09 2016 Alexei Takaseev <taf@altlinux.org> 2.1.2-alt2
- Rebuild with new libmediastreamer 2.14.0

* Tue Nov 03 2015 Alexei Takaseev <taf@altlinux.org> 2.1.2-alt1
- 2.1.2

* Fri Mar 13 2015 Alexei Takaseev <taf@altlinux.org> 2.1.0-alt1
- 2.1.0
- Rebuild with new libmediastreamer

* Fri Jun 14 2013 Alexei Takaseev <taf@altlinux.org> 2.0.3-alt1.qa1.1
- Rebuild with new libmediastreamer

* Fri Apr 19 2013 Dmitry V. Levin (QA) <qa_ldv@altlinux.org> 2.0.3-alt1.qa1
- NMU: rebuilt for updated dependencies.

* Thu Mar 24 2011 Egor Glukhov <kaman@altlinux.org> 2.0.3-alt1
- Initial build for Sisyphus
