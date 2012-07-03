Summary: A beta-quality usermode driver for the ECI ADSL USB modem
Name: eciadsl-usermode
Version: 0.12
Release: alt2
Url: http://eciadsl.flashtux.org/
License: GPL
Group: Networking/Other
Packager: Kirill Maslinsky <kirill@altlinux.org>

Source: %name-%version.tar.gz

Requires: ppp, rp-pppoe, tcl, tk

%description
The eciadsl-usermode package contains the driver for the ADSL USB modem
called ECI Hi-Focus. It also support a lot of USB ADSL modems based upon
the Globespan chipset. It is not a kernel module, but a user-mode program
that handles the modem. A kernel module is under development.

%prep
# in this section, we remove old builds, untar the new sources and
# optionally make some patch. in our case, it only contains %setup
# which untar the sources
%setup -q

%build
%configure
make

%install
%makeinstall

%pre
# pre-install script

%post
# post-install script
echo "Now you need to configure the driver. Please read the README"
echo "and INSTALL files located in /usr/share/doc/%name-%version"

%preun
# pre-uninstall script

%postun
# post-uninstall script

%files
# here, we list all the files that form the binary package.
# executable files should be : rwxr-xr-x
%_bindir/eciadsl-start
%_bindir/eciadsl-restart
%_bindir/eciadsl-stop
%_bindir/eciadsl-firmware
%_bindir/eciadsl-synch
%_bindir/eciadsl-pppoeci
%_bindir/eciadsl-doctor
%_bindir/eciadsl-check-hdlc
%_bindir/eciadsl-check-hdlc-bug
%_bindir/eciadsl-config-tk
%_bindir/eciadsl-config-text
%_bindir/eciadsl-remove-dabusb
%_bindir/eciadsl-probe-synch
%_bindir/eciadsl-probe-device
%_bindir/eciadsl-vendor-device.pl
%_bindir/eciadsl-data.pl
%_bindir/eciadsl-uc.pl
%_bindir/eciadsl-makeconfig
%_bindir/eciadsl-testconnection
%_bindir/eciadsl-ctrlui
# compatibility links
#/usr/bin/startmodem
#/usr/bin/eci-load1
#/usr/bin/eci-load2
#/usr/bin/pppoeci
%config %_sysconfdir/eciadsl/modems.db
%config %_sysconfdir/eciadsl/providers.db
%config %_sysconfdir/eciadsl/firmware00.bin
%config %_sysconfdir/eciadsl/synch01.bin
%config %_sysconfdir/eciadsl/modemeci.gif
%doc README
%doc README.es
%doc README.fr
%doc README.it
%doc README.pt
%doc INSTALL
%doc INSTALL.es
%doc INSTALL.fr
%doc INSTALL.it
%doc INSTALL.pt
%doc TROUBLESHOOTING
%doc TROUBLESHOOTING.es
%doc TROUBLESHOOTING.fr
%doc TROUBLESHOOTING.it
%doc TROUBLESHOOTING.pt
%doc BUGS
%doc TODO
%doc rc.adsl


%changelog
* Mon Mar 31 2008 Kirill Maslinsky <kirill@altlinux.org> 0.12-alt2
- fix build (see git log for details)

* Wed Oct 31 2007 Kirill Maslinsky <kirill@altlinux.org> 0.12-alt1
- version up
  + closes (#7989, #13021)
  + cleanup spec (see git log for details)

* Mon Aug 15 2005 Vitaliy Erokhin <greyp@altlinux.org> 0.11beta1-alt1
- First release (0.11beta1)
