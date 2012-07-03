Name:       sensorfw
Summary:    Sensor Framework
Version:    0.7.2
Group:      System/Kernel and hardware
Release:    alt1.83.2
License:    LGPLv2+
URL:        http://gitorious.org/sensorfw
Source0:    %{name}-%{version}.tar.gz
Source1:    sensorfw-rpmlintrc
Source2:    sensord.service
Source3:    sensord-daemon-conf-setup
Source4:    sensord-aava.conf
Source5:    sensord-icdk.conf
Source6:    sensord-exopc.conf
Source7:    sensord-mrst_cdk.conf
Source8:    sensord-oaktrail.conf
Source9:    sensord-sysconfig.filetrigger
Source100:  sensorfw.yaml
Patch0:     sensorfw-0.7.1-tests-directories.patch
Patch1:     sensorfw-0.7.1-pegatron-accel.patch
Patch2:     sensorfw-0.7.1-oemtablet-accel.patch
Patch3:     sensorfw-0.7.1-oaktrail-accel.patch
Patch4:     sensorfw-0.7.1-oemtablet-als.patch
Patch5:     sensorfw-0.7.1-oemtablet-gyroscope.patch
Patch6:     sensorfw-0.7.1-alsadaptor-ascii-rangefile.patch
Patch7:     fix-initctl.patch
#Requires:   qt
#Requires:   GConf-dbus
Requires:   %{name}-configs
#Requires:   systemd
#Requires(preun): systemd
#Requires(post): /sbin/ldconfig
#Requires(post): systemd
#Requires(postun): /sbin/ldconfig
#Requires(postun): systemd
BuildRequires:  pkgconfig(QtCore)
BuildRequires:  pkgconfig(gconf-2.0)
BuildRequires:  pkgconfig(contextprovider-1.0)
BuildRequires:  doxygen
BuildRequires:  graphviz
BuildRequires:  gcc-c++
Obsoletes:   sensorframework


%description
Sensor Framework provides an interface to hardware sensor drivers through logical sensors. This package contains sensor framework daemon and required libraries.



%package devel
Summary:    Sensor framework daemon libraries development headers
Group:      Development/C++
Requires:   %{name} = %{version}-%{release}
#Requires:   qt-devel

%description devel
Development headers for sensor framework daemon and libraries.


%package tests
Summary:    Unit test cases for sensord
Group:      Development/C++
Requires:   %{name} = %{version}-%{release}
#Requires:   testrunner-lite
#Requires:   python

%description tests
Contains unit test cases for CI environment.


%package contextfw-tests
Summary:    Test cases for sensord acting as context provider
Group:      Development/C++
Requires:   %{name} = %{version}-%{release}
#Requires:   sensorfw-tests
#Requires:   contextkit >= 0.3.6

%description contextfw-tests
Contains test cases for CI environment, for ensuring that sensord provides context properties correctly.


%package doc
Summary:    API documentation for libsensord
Group:      Development/Documentation
Requires:   %{name} = %{version}-%{release}

%description doc
Doxygen-generated API documentation for sensord.


%package configs
Summary:    Sensorfw configuration files
Group:      System/Configuration/Other
BuildArch:    noarch
Requires:   %{name} = %{version}
Provides:   sensord-config
Provides:   config-n900
Provides:   config-aava
Provides:   config-icdk
Provides:   config-ncdk
Provides:   config-oemtablet
Provides:   config-oaktrail

%description configs
Sensorfw configuration files.



%prep
%setup -q -n %{name}-%{version}

# sensorfw-0.7.1-tests-directories.patch
%patch0 -p1
# sensorfw-0.7.1-pegatron-accel.patch
%patch1 -p1
# sensorfw-0.7.1-oemtablet-accel.patch
%patch2 -p1
# sensorfw-0.7.1-oaktrail-accel.patch
%patch3 -p1
# sensorfw-0.7.1-oemtablet-als.patch
%patch4 -p1
# sensorfw-0.7.1-oemtablet-gyroscope.patch
%patch5 -p1
# sensorfw-0.7.1-alsadaptor-ascii-rangefile.patch
%patch6 -p1
# fix-initctl.patch
%patch7 -p2
# >> setup
# << setup
find . -type f -name \*.pr\? | while read f; do sed -i 's|/usr/lib|%_libdir|' $f; done

%build
#unset LD_AS_NEEDED
# >> build pre
#export LD_RUN_PATH=/usr/lib/sensord/
# << build pre

PATH=$PATH:%_qt4dir/bin qmake \
    CONFIG+=mce_disable

%make_build

# >> build post
# << build post
%install
rm -rf %{buildroot}
# >> install pre
# << install pre
%make_install INSTALL_ROOT=%buildroot install

# >> install post
install -D -m644 %{SOURCE2} $RPM_BUILD_ROOT/%{_lib}/systemd/system/sensord.service
install -D -m750 %{SOURCE3} $RPM_BUILD_ROOT/%{_bindir}/sensord-daemon-conf-setup
install -m644 %{SOURCE4} $RPM_BUILD_ROOT%{_sysconfdir}/%{name}/
install -m644 %{SOURCE5} $RPM_BUILD_ROOT%{_sysconfdir}/%{name}/
install -m644 %{SOURCE6} $RPM_BUILD_ROOT%{_sysconfdir}/%{name}/
install -m644 %{SOURCE7} $RPM_BUILD_ROOT%{_sysconfdir}/%{name}/
install -m644 %{SOURCE8} $RPM_BUILD_ROOT%{_sysconfdir}/%{name}/
install -D -m755 sensord.init %buildroot%_initdir/sensord

mkdir -p %{buildroot}/%{_lib}/systemd/system/basic.target.wants
ln -s ../sensord.service %{buildroot}/%{_lib}/systemd/system/basic.target.wants/sensord.service
# << install post

# Install the filetrigger for sensord sysconfig
install -D -m755 %{SOURCE9} %buildroot%_rpmlibdir/sensord-sysconfig.filetrigger

# Generate the default sysconfig for sensord:
mkdir -p -m0755 %buildroot%_sysconfdir/sysconfig
SYSCONFDIR="%buildroot%_sysconfdir" %{SOURCE9}


#%preun
#if systemctl -q is-active sensord.service; then systemctl stop sensord.service; fi

#%post
#/sbin/ldconfig
#if systemctl daemon-reload; then systemctl reload-or-try-restart sensord.service; fi

#%postun
#/sbin/ldconfig
#systemctl daemon-reload ||:

%files
%defattr(-,root,root,-)
# >> files
%attr(755,root,root)%{_sbindir}/sensord
%dir %{_libdir}/sensord
%{_libdir}/sensord/*.so
%{_libdir}/*.so.*
%config %{_sysconfdir}/dbus-1/system.d/sensorfw.conf
%config %{_sysconfdir}/sensorfw/sensord.conf
%dir %{_sysconfdir}/%{name}
%dir %{_sysconfdir}/%{name}/sensord.conf.d/
%{_datadir}/contextkit/providers/com.nokia.SensorService.context
%doc debian/copyright debian/README COPYING
/%{_lib}/systemd/system/sensord.service
/%{_lib}/systemd/system/basic.target.wants/sensord.service
%exclude %{_bindir}/sensord-daemon-conf-setup
%_initdir/sensord
%_rpmlibdir/sensord-sysconfig.filetrigger
%{_sysconfdir}/sysconfig/sensord
# << files


%files devel
%defattr(-,root,root,-)
# >> files devel
%{_libdir}/*.so
%{_libdir}/pkgconfig/*
%dir %{_includedir}/sensord
%{_includedir}/sensord/*
%{_datadir}/qt4/mkspecs/features/sensord.prf
# << files devel

%files tests
%defattr(-,root,root,-)
# >> files tests
%dir %{_libdir}/sensord/testing
%{_libdir}/sensord/testing/*
%dir %{_datadir}/sensorfw-tests
%attr(755,root,root)%{_datadir}/sensorfw-tests/*.p*
%attr(644,root,root)%{_datadir}/sensorfw-tests/*.xml
%attr(644,root,root)%{_datadir}/sensorfw-tests/*.conf
%attr(755,root,root)%{_bindir}/*
%exclude %_bindir/sensord-daemon-conf-setup
# << files tests

%files contextfw-tests
%defattr(-,root,root,-)
# >> files contextfw-tests
%dir %{_datadir}/sensorfw-contextfw-tests
%attr(755,root,root)%{_datadir}/sensorfw-contextfw-tests/*.sh
%attr(755,root,root)%{_datadir}/sensorfw-contextfw-tests/*.p*
%attr(644,root,root)%{_datadir}/sensorfw-contextfw-tests/*.xml
# << files contextfw-tests

%files doc
%defattr(-,root,root,-)
# >> files doc
%dir %{_defaultdocdir}/sensord
%dir %{_defaultdocdir}/sensord/html
%attr(644,root,root)%{_defaultdocdir}/sensord/html/*
# << files doc

%files configs
%defattr(-,root,root,-)
# >> files configs
%config %{_sysconfdir}/%{name}/sensord.conf.d/*.conf
%config %{_sysconfdir}/%{name}/*.conf
%exclude %{_sysconfdir}/sensorfw/sensord.conf
# << files configs

%changelog
* Fri May 11 2012 Paul Wolneykien <manowar@altlinux.ru> 0.7.2-alt1.83.2
- Take own of the directories, skip the startup-setup script.

* Fri May 11 2012 Paul Wolneykien <manowar@altlinux.ru> 0.7.2-alt1.83.1
- Add sensord sysconfig filetrigger.
- Output detected platform name on service start.

* Tue Apr 17 2012 Paul Wolneykien <manowar@altlinux.ru> 0.7.2-alt1.83
- Adjust the spec for ALT Linux.
* Thu Jun 16 2011 Markus Lehtonen <markus.lehtonen@intel.com> - 0.7.2
- Version bump to 0.7.2 (BMC#12866)
- Remove the hackish sensord-rx_51.modules file
- add rpmlintrc
* Wed Jun  8 2011 Chris Ferron <chris.e.ferron@linux.intel.com> - 0.6.36
- removed Requires for sysklogd as sys log is provided without sysklogd.
* Wed Jun  8 2011 Markus Lehtonen <markus.lehtonen@nokia.com> - 0.6.36
- Remove dependencies to MCE (that is deprecated)
- Sync yaml with spec (the systemd changes)
* Wed Jun  1 2011 Chris Ferron <chris.e.ferron@linux.intel.com> - 0.6.36
- FEA#16109 - [FEA] Implement SystemD as MeeGo init provide
- Updated the sensorfw package to be usable by systemd as needed
  to implement systemd as the init provider of MeeGo. For this
  a systemd sensord.service file was added and installed,
  along with a preexec script to set the correct conf file.
  This will allow systemd to start stop and track the service.
* Thu Apr 28 2011 Peter J Zhu <peter.j.zhu@intel.com> - 0.6.36
- sensorfw should rely on sensorfw-configs to work, which is indispensable parts to run senforfw
* Fri Apr 15 2011 Forrest Zhao <forrest.zhao@intel.com> - 0.6.36
- BMC#7594, fix the bug that orientation is off by 180 degree after
  libqtsensors_meego.so is restored
* Thu Mar 31 2011 Markus Lehtonen <markus.lehtonen@nokia.com> - 0.6.36
- Added sensord-rx_51.modules file to load required kernel modules before
  sensord starts on N900. Required to fix BMC#11699.
* Fri Mar 25 2011 Forrest Zhao <forrest.zhao@intel.com> -0.6.36
- BMC#3680, add adaptor for OEM tablet magnetometer sensor
* Mon Mar 21 2011 Andy Ross <andy.ross@windriver.com> - 0.6.36
- Disable pegatron configuration, it conflicts with sensorfw-pegatron package.
* Fri Mar 18 2011 Markus Lehtonen <markus.lehtonen@nokia.com> - 0.6.36
- Remove SysV init script (fix BMC#12898)
- Fix dependencies of configs subpackage to solve dep problems in image
  creation
* Thu Mar  3 2011 Markus Lehtonen <markus.lehtonen@nokia.com> - 0.6.36
- Fix icdk ALS configuration (BMC#11699). Fix from Catalin Popescu
  <catalinx.popescu@intel.com>
- Separate configuration packages removed. Automatic board detection removing
  the need for this (needed to fix BMC#11698, BMC#1169).
* Wed Mar  2 2011 Markus Lehtonen <markus.lehtonen@nokia.com> - 0.6.36
- Remove preun/post/postun scriptlets to avoid double startup (BMC#12898).
* Tue Feb 22 2011 Forrest Zhao <forrest.zhao@intel.com> - 0.6.36
- Add adaptor for OEM tablet gyroscope sensor
* Thu Feb 17 2011 Forrest Zhao <forrest.zhao@intel.com> - 0.6.36
- Add adaptor for OEM tablet ALS sensor
* Thu Feb 17 2011 Liang Huang <liang.huang@intel.com> - 0.6.36
- Add oaktrail patch back removed by mistake
* Wed Feb 16 2011 Forrest Zhao <forrest.zhao@intel.com> - 0.6.36
- Fix BMC#4545 from sensorfw side
* Wed Feb 16 2011 Liang Huang <liang.huang@intel.com> - 0.6.36
- Add adaptor for Oaktrail accelerometer sensor
* Sun Jan 30 2011 Forrest Zhao <forrest.zhao@intel.com> - 0.6.36
- Add adaptor for PEGATRON accelerometer sensor
- Add adaptor for OEM tablet accelerometer sensor
* Tue Jan 25 2011 Markus Lehtonen <markus.lehtonen@nokia.com> - 0.6.36
- Version bump to 0.6.36 (BMC#12866)
- Enable MCE support
* Mon Jan  3 2011 Markus Lehtonen <markus.lehtonen@nokia.com> - 0.6.32
- Updated ncdk conf to fix screen rotation (refs BMC#8743, BMC#10385)
- Updated packaging: minor yaml/spec changes in %%build and %%install
* Thu Dec 30 2010 Tapio Rantala <ext-tapio.rantala@nokia.com> - 0.6.32
- Fix mce tools package name. This one more fix related to BMC#11352, also
  required to fix BMC#9662 (when mce-tools becomes available in Trunk)
* Fri Dec 17 2010 Markus Lehtonen <markus.lehtonen@nokia.com> - 0.6.32
- Version bump, fixes BMC#11349
- Adds gyro support (enabler for FEA BMC#6950)
* Thu Dec 16 2010 Markus Lehtonen <markus.lehtonen@nokia.com> - 0.6.28_2
- Add sensorfw-config-icdk package. Sensorfw fix to BMC#10385 for icdk.
- Remove unused (and virtually empty) sensorfw-config-cdk package
* Wed Dec 15 2010 Tapio Rantala <ext-tapio.rantala@nokia.com> - 0.6.28_2
- Split tests package
- Use correct directories for tests, add tests-directories.patch
- Fixes BMC#11352
* Mon Nov 29 2010 Markus Lehtonen <markus.lehtonen@nokia.com> - 0.6.28_2
- Change RPM group tag according to MeeGo domain/subsystem
* Fri Nov  5 2010 Shane Bryan <shane.bryan@linux.intel.com> - 0.6.28_2
- Change the acc_trans_matrix for ncdk device back to the identity matrix.
  The current, inversion, matrix is resulting in upsidedown rendering in
  MTF based applications. Sensorfw part of fix to BMC#10385.
* Wed Oct 27 2010 Markus Lehtonen <markus.lehtonen@nokia.com> - 0.6.28_2
- Version bump
- Fixed config file path in config packages
- Add config package for nCDK
* Wed Oct 20 2010 Markus Lehtonen <markus.lehtonen@nokia.com> - 0.6.28_1
- Version bump: new alsadaptor-ascii, bug fixes
* Thu Oct  7 2010 Markus Lehtonen <markus.lehtonen@nokia.com> - 0.6.26.p.gitde0cd945
- Version bump to git head (multiconf patch now in upstream)
* Thu Sep 30 2010 Markus Lehtonen <markus.lehtonen@nokia.com> - sensorfw-0.6.26.p.git45616cdb
- Version bump to git HEAD (adds e.g. adaptors for some new Intel platforms)
- Added device-specific config packages (should be temporary solution, until
  device detection is implemented and working)
* Wed Sep 22 2010 Markus Lehtonen <markus.lehtonen@nokia.com> - 0.6.25
- Version bump to 0.6.25
- Introduce multiconf patch
* Tue Aug 24 2010 Markus Lehtonen <markus.lehtonen@nokia.com> - 0.6.19.p.git82de2729
- added 'unset LD_AS_NEEDED' to spec file to fix missing library deps in
  binaries
* Thu Aug 19 2010 Markus Lehtonen <markus.lehtonen@nokia.com> - 0.6.19.p.git82de2729
- subpkg names fixed
- init script updated
* Tue Aug 17 2010 Markus Lehtonen <markus.lehtonen@nokia.com> - 0.6.19.p.git82de2729
- version bump to git head
- packaging now uses spectacle
* Wed Jun 23 2010 Markus Lehtonen <markus.lehtonen@nokia.com>  - 0.6.17.p.gitba97aa55
- version bump to git head (0.6.17.p.gitba97aa55)
* Fri Jun 11 2010 Kalle Lampila <kalle.lampila@iki.fi>  - 0.6.11.p.git88850dca
- Added status and restart to init script
* Mon Jun  7 2010 Markus Lehtonen <markus.lehtonen@nokia.com> - 0.6.11.p.git88850dca
- now obsoletes sensorframework (sensorframework from Intel)
* Thu Jun  3 2010 Markus Lehtonen <markus.lehtonen@nokia.com> - 0.6.11.p.git88850dca
- init script added
* Tue Jun  1 2010 Markus Lehtonen <markus.lehtonen@nokia.com> - 0.6.11.p.git88850dca
- more packaging fixes
* Mon May 31 2010 Markus Lehtonen <markus.lehtonen@nokia.com> - 0.6.11.p.git88850dca
- graphviz added as builddep
- unneccessary %%post scripts of devel package removed
* Sat May 29 2010 Markus Lehtonen <markus.lehtonen@nokia.com> - 0.6.11.p.git88850dca
- Version bump to git head
- Packaging fixes
* Thu May 27 2010 Markus Lehtonen <markus.lehtonen@nokia.com> - 0.6.11.p.gite106ebb4
- Initial packaging effort
