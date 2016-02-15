# BEGIN SourceDeps(oneline):
BuildRequires: gcc-c++
# END SourceDeps(oneline)
%add_optflags %optflags_shared
%define oldname rtaudio
Summary:        Real-time Audio I/O Library
Name:           librtaudio
Version:        4.0.11
Release:        alt1_10
License:        MIT
Group:          System/Libraries
URL:            http://www.music.mcgill.ca/~gary/rtaudio/
# The original tarball contains nonfree bits. We remove them and create a free tarball:
#    VERSION=4.0.11
#    wget -N http://www.music.mcgill.ca/~gary/rtaudio/release/rtaudio-$VERSION.tar.gz
#    tar zxf rtaudio-$VERSION.tar.gz
#    rm -fr rtaudio-$VERSION/include/ rtaudio-$VERSION/tests/Windows
#    tar zcf rtaudio-$VERSION-fe.tar.gz rtaudio-$VERSION
Source0:        %{oldname}-%{version}-fe.tar.gz
BuildRequires:  libalsa-devel
BuildRequires:  libjack-devel
BuildRequires:  libpulseaudio-devel
Source44: import.info
Provides: rtaudio = %{version}-%{release}


%description
RtAudio is a set of C++ classes that provide a common API for realtime audio
input/output across different operating systems. RtAudio significantly
simplifies the process of interacting with computer audio hardware. It was
designed with the following objectives:

  * object-oriented C++ design
  * simple, common API across all supported platforms
  * allow simultaneous multi-api support
  * support dynamic connection of devices
  * provide extensive audio device parameter control
  * allow audio device capability probing
  * automatic internal conversion for data format, channel number compensation,
    (de)interleaving, and byte-swapping


%package devel
Summary:        Real-time Audio I/O Library
Group:          System/Libraries
Requires:       %{name}%{?_isa} = %{version}
Provides: rtaudio-devel = %{version}-%{release}

%description devel
RtAudio is a set of C++ classes that provide a common API for realtime audio
input/output across different operating systems. RtAudio significantly
simplifies the process of interacting with computer audio hardware. It was
designed with the following objectives:

  * object-oriented C++ design
  * simple, common API across all supported platforms
  * allow simultaneous multi-api support
  * support dynamic connection of devices
  * provide extensive audio device parameter control
  * allow audio device capability probing
  * automatic internal conversion for data format, channel number compensation,
    (de)interleaving, and byte-swapping

%prep
%setup -n %{oldname}-%{version} -q
# Fix encoding issues
for file in tests/teststops.cpp; do
   sed 's|\r||' $file > $file.tmp
   iconv -f ISO-8859-1 -t UTF8 $file.tmp > $file.tmp2
   touch -r $file $file.tmp2
   mv -f $file.tmp2 $file
done

# Remove empty directory
rm -fr tests/Debug

# To pass the optflags properly
sed -i '/CFLAGS *=/d' Makefile.in

# To fix the ppc64 compilation issue
# cp -p /usr/lib/rpm/config.{sub,guess} config/

%build
export CFLAGS="%optflags -fPIC"
%configure --with-jack --with-alsa --with-pulse
# parallel make fails here
make

%install
mkdir -p %{buildroot}%{_includedir} %{buildroot}%{_libdir}
cp -a RtAudio.h RtError.h %{buildroot}%{_includedir}
cp -p lib%{oldname}.so.%{version} %{buildroot}%{_libdir}/
ln -s %{_libdir}/lib%{oldname}.so.%{version} %{buildroot}%{_libdir}/lib%{oldname}.so
# ldconfig -v -n  %{buildroot}%{_libdir}

%files
%doc readme doc/release.txt
%{_libdir}/lib%{oldname}.so.*

%files devel
%doc doc/html doc/images tests
%{_includedir}/*.h
%{_libdir}/lib%{oldname}.so

%changelog
* Mon Feb 15 2016 Igor Vlasenko <viy@altlinux.ru> 4.0.11-alt1_10
- update to new release by fcimport

* Sun Sep 20 2015 Igor Vlasenko <viy@altlinux.ru> 4.0.11-alt1_9
- update to new release by fcimport

* Wed Aug 27 2014 Igor Vlasenko <viy@altlinux.ru> 4.0.11-alt1_7
- update to new release by fcimport

* Tue Jul 01 2014 Igor Vlasenko <viy@altlinux.ru> 4.0.11-alt1_6
- update to new release by fcimport

* Mon Aug 12 2013 Igor Vlasenko <viy@altlinux.ru> 4.0.11-alt1_5
- update to new release by fcimport

* Mon Feb 25 2013 Igor Vlasenko <viy@altlinux.ru> 4.0.11-alt1_4
- fc update

* Mon Jan 14 2013 Igor Vlasenko <viy@altlinux.ru> 4.0.11-alt1_3
- initial fc import

