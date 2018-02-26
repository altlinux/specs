# BEGIN SourceDeps(oneline):
BuildRequires: gcc-c++
# END SourceDeps(oneline)
# Copyright (c) 2007 oc2pus <toni@links2linux.de>
# Copyright (c) 2007-2009 Hans de Goede <hdegoede@redhat.com>
# This file and all modifications and additions to the pristine
# package are under the same license as the package itself.
#
# Please submit bugfixes or comments to us at the above email addresses

%define _version 2008.03.30
 
Name:           Io-language
Version:        20080330
Release:        alt2_9.2
Summary:        Io is a small, prototype-based programming language
Group:          System/Libraries
License:        BSD
URL:            http://www.iolanguage.com/
# To get this file do wget http://github.com/stevedekorte/io/tarball/%{_version}
Source0:        %{name}-%{version}.tar.gz
Patch0:         AddonBuilder_io_libdir.patch
Patch1:         Io-2007-10-10-gcc43.patch
Patch2:         Io-2007-10-10-missing-protos.patch
Patch3:         Io-language-20080330-py27.patch
BuildRequires:  e2fsprogs-devel libe2fs-devel libfreetype-devel libfreeglut-devel libgmp-devel libgmp_cxx-devel
BuildRequires:  libedit-devel libevent-devel libjpeg-devel libpng-devel
BuildRequires:  libsamplerate-devel libsndfile-devel libtiffxx-devel libtiff-devel
BuildRequires:  libxml2-devel MySQL-devel libode-devel libOpenSP-devel libpcre-devel
BuildRequires:  libportaudio2-devel postgresql-devel python-devel libsoundtouch-devel
BuildRequires:  libsqlite3-devel taglib-devel libncurses-devel libcairo-devel
BuildRequires:  libuuid-devel libreadline-devel
Source44: import.info
Patch33: Io-language-20080330-alt-open-mode.patch

%description
Io is a small, prototype-based programming language. The ideas in
Io are mostly inspired by Smalltalk (all values are objects), Self
(prototype-based), NewtonScript (differential inheritance), Act1
(actors and futures for concurrency), LISP (code is a runtime
inspectable/modifiable tree) and Lua (small, embeddable).


%package        devel
Summary:        Development files for %{name}
Group:          Development/C
Requires:       %{name} = %{version}-%{release}

%description devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.


%package graphics-and-sound
Summary:        Io graphics and sound support
Group:          System/Libraries
Requires:       %{name} = %{version}-%{release}

%description graphics-and-sound
Io graphics and sound support, this package includes IO bindings needed to
write Io programs which want to display graphics and / or produce sound
(OpenGL, Image loading, PortAudio, etc.).


%package extras
Summary:        Io extra addons
Group:          System/Libraries
Requires:       %{name} = %{version}-%{release}

%description extras
This package includes addons for Io which require additional libraries to be
installed. This includes the Python and Socket addons.


%package postgresql
Summary:        Io postgresql bindings
Group:          System/Libraries
Requires:       %{name} = %{version}-%{release}

%description postgresql
Io postgresql bindings.


%package mysql
Summary:        Io mysql bindings
Group:          System/Libraries
Requires:       %{name} = %{version}-%{release}

%description mysql
Io mysql bindings


%prep
%setup -q -n stevedekorte-io-6a5f734
%patch0 -p1
%patch1 -p1 -b .gcc43
%patch2 -p1 -b .protos
%patch3 -p1
sed -i 's|/lib/io/addons|/%{_lib}/io/addons|g' libs/iovm/io/AddonLoader.io
# building Io while Io-language-devel is installed results in binaries getting
# linked against the installed version, instead of the just build one <sigh>
if [ -f /usr/include/io/IoVM.h ]; then
  echo "Error building Io while Io-language-devel is installed does not work!"
  exit 1
fi
# libstdc++.so is searched and not found ...
sed -i -e 's|dependsOnLib("stdc++")||g' addons/SoundTouch/build.io
# remove add-ons which we do not want to build ever
rm -fr addons/AVCodec
# for %doc
mv addons/OpenGL/docs OpenGL
iconv -f MACINTOSH -t UTF8 libs/basekit/license/bsd_license.txt > license.txt
sed -i 's/\r//g' license.txt `find OpenGL -type f`
# for debuginfo
chmod -x addons/NullAddon/source/IoNullAddon.?
%patch33 -p1
# alt pcre
sed -i s,pcre.h,pcre/pcre.h, addons/Regex/source/Regex.h addons/Regex/build.io


%build
make %{?_smp_mflags} INSTALL_PREFIX=%{_prefix} OPTIMIZE="$RPM_OPT_FLAGS" \
  DLL_COMMAND='-shared -Wl,-soname="libiovmall.so.2"'


%install
# upstreams make install installs lots of unwanted parts of the addons, so DIY
mkdir -p $RPM_BUILD_ROOT%{_bindir}
mkdir -p $RPM_BUILD_ROOT%{_libdir}/io/addons
mkdir -p $RPM_BUILD_ROOT%{_includedir}
install -m 755 _build/binaries/io $RPM_BUILD_ROOT%{_bindir}
install -m 755 _build/dll/libiovmall.so \
  $RPM_BUILD_ROOT%{_libdir}/libiovmall.so.2
ln -s libiovmall.so.2 $RPM_BUILD_ROOT%{_libdir}/libiovmall.so
cp -a _build/headers $RPM_BUILD_ROOT%{_includedir}/io
# install the addons
for i in addons/*; do
  # skip unbuild addons
  if [ -d $i/_build ]; then
    ADDON=`basename $i`
    mkdir -p $RPM_BUILD_ROOT%{_libdir}/io/addons/$ADDON/_build/dll
    install -m 755 $i/_build/dll/libIo$ADDON.so \
      $RPM_BUILD_ROOT%{_libdir}/io/addons/$ADDON/_build/dll
    install -p -m 644 $i/depends $RPM_BUILD_ROOT%{_libdir}/io/addons/$ADDON
    # Io doesn't find the addon if this file isn't present
    touch $RPM_BUILD_ROOT%{_libdir}/io/addons/$ADDON/build.io
  fi
done


%files
%doc license.txt
%{_bindir}/io
%{_libdir}/libiovmall.so.2
%dir %{_libdir}/io
%dir %{_libdir}/io/addons
%{_libdir}/io/addons/AsyncRequest
%{_libdir}/io/addons/BigNum
%{_libdir}/io/addons/Blowfish
%{_libdir}/io/addons/Box
%{_libdir}/io/addons/Cairo 
%{_libdir}/io/addons/CGI
%{_libdir}/io/addons/ContinuedFraction
%{_libdir}/io/addons/Curses
%{_libdir}/io/addons/DistributedObjects
%{_libdir}/io/addons/EditLine
%{_libdir}/io/addons/Flux
%{_libdir}/io/addons/Fnmatch
%{_libdir}/io/addons/LZO
%{_libdir}/io/addons/Libxml2
%{_libdir}/io/addons/Loki
%{_libdir}/io/addons/MD5
%{_libdir}/io/addons/NetworkAdapter
%{_libdir}/io/addons/NotificationCenter
%{_libdir}/io/addons/NullAddon
%{_libdir}/io/addons/Random
%{_libdir}/io/addons/Range
%{_libdir}/io/addons/Rational
%{_libdir}/io/addons/ReadLine
%{_libdir}/io/addons/Regex
%{_libdir}/io/addons/SHA1
%{_libdir}/io/addons/SQLite3
%{_libdir}/io/addons/SqlDatabase
%{_libdir}/io/addons/Syslog
%{_libdir}/io/addons/SystemCall
%{_libdir}/io/addons/Thread
%{_libdir}/io/addons/UUID
%{_libdir}/io/addons/User
%{_libdir}/io/addons/Volcano
%{_libdir}/io/addons/Zlib

%files devel
%doc docs/*
%{_libdir}/libiovmall.so
%{_includedir}/io

%files graphics-and-sound
%doc OpenGL
%{_libdir}/io/addons/Font
%{_libdir}/io/addons/Image
%{_libdir}/io/addons/LibSndFile
%{_libdir}/io/addons/OpenGL
%{_libdir}/io/addons/PortAudio
%{_libdir}/io/addons/TagLib

%files extras
%{_libdir}/io/addons/Python
%{_libdir}/io/addons/SampleRateConverter
%{_libdir}/io/addons/Socket
%{_libdir}/io/addons/SoundTouch

%files postgresql
%{_libdir}/io/addons/Postgre*

%files mysql
%{_libdir}/io/addons/MySQL


%changelog
* Wed Mar 21 2012 Igor Vlasenko <viy@altlinux.ru> 20080330-alt2_9.2
- rebuild to get rid of #27020

* Tue Feb 21 2012 Igor Vlasenko <viy@altlinux.ru> 20080330-alt1_9.2
- update to new release by fcimport

* Wed Feb 01 2012 Igor Vlasenko <viy@altlinux.ru> 20080330-alt1_8.2
- update to new release by fcimport

* Thu Dec 08 2011 Igor Vlasenko <viy@altlinux.ru> 20080330-alt1_7.2
- update to new release by fcimport

* Fri Nov 25 2011 Igor Vlasenko <viy@altlinux.ru> 20080330-alt1_6.2
- update to new release by fcimport

* Thu Oct 27 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 20080330-alt1_6.1
- Rebuild with Python-2.7

* Thu Jul 21 2011 Igor Vlasenko <viy@altlinux.ru> 20080330-alt1_6
- initial release by fcimport

