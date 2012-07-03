%define rname taglib-sharp

Summary: A library for reading and writing tags to audio files.
Name: libtag-sharp
Version: 2.0.3.7
Release: alt2.git20110301
License: LGPL
Group: Development/Other
Packager: Mono Maintainers Team <mono@packages.altlinux.org>
URL: http://www.taglib-sharp.com/

Source0: %name-%version.tar
Patch0: %name-%version-%release.patch

BuildRequires: /proc
BuildRequires:  mono-devel rpm-build-mono mono-mcs libgnome-sharp-devel gcc-c++

%description
TagLib# is a FREE and Open Source library for the .NET 2.0 and Mono frameworks
which will let you tag your software with as much or as little detail as you like without
slowing you down. It supports a large variety of movie and music formats which abstract
away the work, handling all the different cases, so all you have to do is access 
file.Tag.Title, file.Tag.Lyrics, or my personal favorite file.Tag.Pictures.

%package devel
Summary: Development files %name
Group: Development/Other
Requires: %name = %version-%release

%description devel
This package includes development files for the %name.

%prep
%setup -q
%patch0 -p1

%build
./autogen.sh --disable-docs
%configure --disable-static --disable-docs
%make_build

%install
%make_install install DESTDIR=%buildroot

%files
%doc README ChangeLog AUTHORS NEWS
%_monodir/%rname
%_monogacdir/*

%files devel
%_pkgconfigdir/*

%changelog
* Thu Mar 10 2011 Alexey Shabalin <shaba@altlinux.ru> 2.0.3.7-alt2.git20110301
- git snapshot 20110301

* Wed Apr 07 2010 Alexey Shabalin <shaba@altlinux.ru> 2.0.3.7-alt1
- 2.0.3.7

* Fri Mar 12 2010 Alexey Shabalin <shaba@altlinux.ru> 2.0.3.6-alt1
- 2.0.3.6

* Fri Oct 23 2009 Alexey Shabalin <shaba@altlinux.ru> 2.0.3.3-alt1
- 2.0.3.3

* Wed Jul 08 2009 Alexey Shabalin <shaba@altlinux.ru> 2.0.3.2-alt2.svn20090518
- move pkgconfig files from main to devel package

* Tue Jun 09 2009 Alexey Shabalin <shaba@altlinux.ru> 2.0.3.2-alt1.svn20090518
- 2.0.3.2 + svn r134348

* Thu Nov 20 2008 Alexey Shabalin <shaba@altlinux.ru> 2.0.3.0-alt1
- 2.0.3.0

* Tue Dec 11 2007 Alexey Shabalin <shaba@altlinux.ru> 2.0.2.0-alt2
- fix build for x86_64 (patch1)

* Thu Dec 06 2007 Alexey Shabalin <shaba@altlinux.ru> 2.0.2.0-alt1
- Initial build for Sisyphus
- disable build docs (need fix install path)
