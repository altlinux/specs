Name:		bs2b
Summary:	The Bauer stereophonic-to-binaural DSP (bs2b) library and plugins
Summary(ru_RU.UTF8): Библиотека стереофонически-бинауральной обработки звука Бауэра с подключаемыми модулями
Version:	3.1.0
Release:	alt1.3
Group:		System/Libraries
License:	Distributable (see COPYING file)
Packager:	Motsyo Gennadi <drool@altlinux.ru>
Url:		http://bs2b.sourceforge.net/
Source0:	http://kent.dl.sourceforge.net/sourceforge/%name/lib%name-%version.tar.bz2
Source1:	%{name}_mp3.sh
Patch0:		lib%name-3.1.0-soname.diff

# Automatically added by buildreq on Sat Feb 28 2009 (-bi)
BuildRequires: gcc-c++ libsndfile-devel

BuildRequires: chrpath

%description
The Bauer stereophonic-to-binaural DSP (bs2b) library and plugins is
designed to improve headphone listening of stereo audio records.
Recommended for headphone prolonged listening to disable superstereo
fatigue without essential distortions.

Author: Boris Mikhaylov

%description -l ru_RU.UTF8
Библиотека стереофонически-бинауральной обработки звука Бауэра с подключаемыми
модулями предназначена для улучшения звучания стереофонических звукозаписей в
наушниках. Рекомендуется при длительном прослушивании аудиозаписей в наушниках
для уменьшения утомляемости из-за суперстерео эффекта, не вносит заметных
искажений звука.

%package -n lib%name
Summary: Shared libraries for bs2b
Group: System/Libraries

%description -n lib%name
Shared libraries for package bs2b.

%package -n lib%name-devel
Summary: Development files for the libbs2b library
Group: Development/C++
Requires: lib%name = %version-%release

%description -n lib%name-devel
Development files for the libbs2b library.

Author: Boris Mikhaylov

%package -n lib%name-devel-static
Summary: Development static libraries for the libbs2b
Group: Development/C++
Requires: lib%name-devel = %version-%release

%description -n lib%name-devel-static
Development static libraries for the libbs2b

Author: Boris Mikhaylov

%prep
%setup -q -n lib%name-%version
%patch0 -p1
%__install -dm 755 examples
%__install -m 755 %SOURCE1 \
	examples

%build
%configure
%make_build
chrpath -d src/.libs/{bs2bconvert,bs2bstream}

%install
%makeinstall

# clean up
%__rm %buildroot%_libdir/*.la
find doc -name 'Makefile*' | xargs %__rm

%files
%doc AUTHORS README ChangeLog COPYING
%doc doc/*.txt
%_bindir/bs2bconvert
%_bindir/bs2bstream

%files -n lib%name
%_libdir/*.so.*

%files -n lib%name-devel
%dir %_includedir/bs2b
%_includedir/bs2b/*.h
%_libdir/*.so
%_pkgconfigdir/*.pc

%files -n lib%name-devel-static
%_libdir/*.a

%changelog
* Thu Jan 26 2012 Motsyo Gennadi <drool@altlinux.ru> 3.1.0-alt1.3
- dropped RPATH on the floor

* Sun Nov 22 2009 Motsyo Gennadi <drool@altlinux.ru> 3.1.0-alt1.2
- fixed russian locale for Summary

* Wed Oct 28 2009 Motsyo Gennadi <drool@altlinux.ru> 3.1.0-alt1.1
- added russian description and summary (fixed #22085). Thanks to Phantom.

* Sun Jun 07 2009 Motsyo Gennadi <drool@altlinux.ru> 3.1.0-alt1
- 3.1.0

* Thu Apr 09 2009 Motsyo Gennadi <drool@altlinux.ru> 3.0.0-alt1
- 3.0.0
- change URL
- add URl for source tarball
- add patch for change soname (thanks to damir@ for hint)

* Sat Feb 28 2009 Motsyo Gennadi <drool@altlinux.ru> 2.2.1-alt1
- initial build for ALT Linux from OpenSUSE package
