# BEGIN SourceDeps(oneline):
BuildRequires: /usr/bin/doxygen gcc-c++ libomxil-bellagio-devel
# END SourceDeps(oneline)
%add_optflags %optflags_shared
Name:           libomxil-bellagio
Version:        0.9.3
Release:        alt1_12
Summary:        OpenMAX Integration Layer

Group:          System/Libraries
License:        LGPLv2+
URL:            http://omxil.sourceforge.net
Source0:        http://downloads.sourceforge.net/omxil/%{name}-%{version}.tar.gz
#https://sourceforge.net/tracker/?func=detail&aid=3477869&group_id=160680&atid=816817
Patch0:         libomxil-bellagio-0.9.3-fix_Werror.patch
Patch1:         libomxil-bellagio-0.9.3-unused.patch
#https://sourceforge.net/tracker/?func=detail&aid=3477871&group_id=160680&atid=816817
Patch2:         libomxil-bellagio-0.9.3-nodoc.patch
Patch3:         http://git.buildroot.net/buildroot/plain/package/multimedia/bellagio/bellagio-0.9.3-dynamicloader-linking.patch
Patch4:         http://git.buildroot.net/buildroot/plain/package/multimedia/bellagio/bellagio-0.9.3-parallel-build.patch
Patch5:         http://git.buildroot.net/buildroot/plain/package/multimedia/bellagio/bellagio-0.9.3-segfault-on-removeFromWaitResource.patch
Patch6:         omxil_version.patch
BuildRequires:  doxygen
BuildRequires:  libtool
Source44: import.info


%description
The OpenMAX IL API defines a standardized media component interface to
enable developers and platform providers to integrate and communicate
with multimedia codecs implemented in hardware or software.

The libomxil shared library implements the OpenMAX IL Core functionalities.
Three dynamically loadable components are also included: OMX alsa sink
component, OMX mp3,aac,ogg decoder component and OMX volume control component.


%package        devel
Summary:        Development files for %{name}
Group:          Development/C
Requires:       %{name} = %{version}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%package        test
Summary:        Test cases for %{name}
Group:          Development/C
Requires:       %{name} = %{version}

%description    test
The %{name}-test package contains binaries for testing %{name}.


%prep
%setup -q
%patch0 -p1 -b .fix_werror
%patch1 -p1 -b .unused
%patch2 -p1 -b .nodoc
%patch3 -p1 -b .dynl
%patch4 -p1 -b .pb
%patch5 -p1 -b .sf
%patch6 -p0 -b .orig
autoreconf -vif

%build
%configure --disable-static

# remove rpath from libtool
sed -i.rpath 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' libtool
sed -i.rpath 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' libtool

#Race condition with the library creation
make %{?_smp_mflags} || make %{?_smp_mflags}

#Build the tests files so they can be installed later
ln -sf src bellagio
make check LDFLAGS="-L$PWD/src/.libs" \
    CFLAGS="$RPM_OPT_FLAGS -I$PWD/include -I$PWD"


%install
make install DESTDIR=$RPM_BUILD_ROOT INSTALL="install -p"
find $RPM_BUILD_ROOT -name '*.la' -exec rm -f {} ';'


#Manually install test binaries
mkdir -p $RPM_BUILD_ROOT%{_bindir}
for f in audio_effects/.libs/{omxaudiomixertest,omxvolcontroltest} resource_manager/.libs/{omxprioritytest,omxrmtest} ; do
  install -pm 0755 test/components/${f} $RPM_BUILD_ROOT%{_bindir}
done

#Avoid docdir
rm -rf $RPM_BUILD_ROOT%{_datadir}/doc/%{name}


%files
%doc AUTHORS ChangeLog COPYING NEWS README TODO
%{_bindir}/omxregister-bellagio
%{_libdir}/*.so.*
%dir %{_libdir}/bellagio
%{_libdir}/bellagio/*.so*
%dir %{_libdir}/omxloaders
%{_libdir}/omxloaders/*.so*
%{_mandir}/man1/omxregister-bellagio.1.*

%files devel
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/pkgconfig/libomxil-bellagio.pc

%files test
%{_bindir}/omxaudiomixertest
%{_bindir}/omxprioritytest
%{_bindir}/omxrmtest
%{_bindir}/omxvolcontroltest


%changelog
* Mon Feb 15 2016 Igor Vlasenko <viy@altlinux.ru> 0.9.3-alt1_12
- update to new release by fcimport

* Sun Sep 20 2015 Igor Vlasenko <viy@altlinux.ru> 0.9.3-alt1_11
- update to new release by fcimport

* Wed Aug 27 2014 Igor Vlasenko <viy@altlinux.ru> 0.9.3-alt1_10
- update to new release by fcimport

* Tue Jul 01 2014 Igor Vlasenko <viy@altlinux.ru> 0.9.3-alt1_9
- update to new release by fcimport

* Mon Aug 05 2013 Igor Vlasenko <viy@altlinux.ru> 0.9.3-alt1_8
- update to new release by fcimport

* Fri Apr 26 2013 Igor Vlasenko <viy@altlinux.ru> 0.9.3-alt1_7
- initial fc import

