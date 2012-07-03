Name:       sensorfw-pegatron
Summary:    Sensor framework integration for Pegatron Lucid tablets
Version:    0.4
Release:    alt1.67.3
Group:      System/Configuration/Other
License:    GPLv2
URL:        http://www.intel.com
Source0:    %{name}-%{version}.tar.bz2
Source100:  sensorfw-pegatron.yaml
Source101:  pegatron-lucid.sysconfig
Patch0:     pegaorient-isvalid.patch
BuildRequires:  libqt4-devel
BuildRequires:  sensorfw-devel
BuildRequires:  gcc-c++


%description
Sensor framework integration for Pegatron Lucid tablets (sold as
WeTab and ExoPC).  Includes support for synchronous ACPI
notification of orientation changes, raw accelerometer output, and
ambient light sensor.




%prep
%setup -q -n %{name}-%{version}
%patch0 -p2

# >> setup
# << setup
find . -type f -name \*.pr\? | while read f; do sed -i 's|/usr/lib|%_libdir|' $f; done

%build
# >> build pre
# << build pre

PATH=$PATH:%_qt4dir/bin qmake

%make_build

# >> build post
# << build post
%install
rm -rf %{buildroot}
# >> install pre
# << install pre
%make_install INSTALL_ROOT=%buildroot install
mv -v %buildroot%_sysconfdir/acpi/events/pegaorient-acpid.conf %buildroot%_sysconfdir/acpi/events/pegaorient

# >> install post
# << install post

install -D -m0644 %{SOURCE101} %buildroot%_sysconfdir/sensorfw/pegatron-lucid.sysconfig


%files
%defattr(-,root,root,-)
%_libdir/sensord/libpegaorient.so
%_sysconfdir/acpi/events/pegaorient
%_sysconfdir/sensorfw/pegaals-range
%_sysconfdir/sensorfw/sensord-pegatron.conf
%_sysconfdir/X11/xorg.conf.d/80-suppress-accel.conf
%_sysconfdir/sensorfw/pegatron-lucid.sysconfig
# >> files
# << files


%changelog
* Sat May 12 2012 Paul Wolneykien <manowar@altlinux.ru> 0.4-alt1.67.3
- Turn on and start the acpid daemon if the platform is detected.
- Remove the symlynk.

* Fri May 11 2012 Paul Wolneykien <manowar@altlinux.ru> 0.4-alt1.67.2
- Add a sysconfig part for sensord detecting the Pegatron Lucid
  platform.

* Fri Apr 27 2012 Paul Wolneykien <manowar@altlinux.ru> 0.4-alt1.67.1
- Install the symlink to Pegatron configuration file in the conf.d.

* Tue Apr 17 2012 Paul Wolneykien <manowar@altlinux.ru> 0.4-alt1.67
- Fix the [plugins] section in the sensord config.
- Fix the acpid rule to match netlink events too.
- Fix file masks. Fix acpid conf for Pegatron.
- Add patch fixing a private field access.
- Adjust the spec for ALT Linux.

* Wed Apr  6 2011 Andy Ross <andy.ross@windriver.com> - 0.4
- Fix usage with Qt Mobility, remove need for contextkit workaround
  (BMC#14818)
* Wed Apr  6 2011 Andy Ross <andy.ross@windriver.com> - 0.3.1
- Fix wrong orientation at startup (BMC#15043)
* Mon Mar  7 2011 Andy Ross <andy.ross@windriver.com> - 0.3
- Support new sensorfw configuration file location
* Wed Feb  9 2011 Andy Ross <andy.ross@windriver.com> - 0.2.1
- Initial OBS revision
