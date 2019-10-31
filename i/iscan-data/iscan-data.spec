# TODO: generate udev rules like does make-policy-file script

# FIXTHEIR: never use release in source releases
%define rel 2

Name: iscan-data
Version: 1.39.1
Release: alt1

Summary: Image Scan! for Linux data files

License: GPL
Group: Graphics
Url: http://download.ebz.epson.net/dsc/search/01/search/?OSC=LX

# Source-url: http://support.epson.net/linux/src/scanner/iscan/iscan-data_%version-%rel.tar.gz
Source: %name-%version.tar

Conflicts: iscan-free < 2.30.0

BuildArch: noarch

%description
Provides the necessary support files for Image Scan! for Linux,
including device information and policy file generation logic.

Image Scan! for Linux will not function without this package.

%prep
%setup

%build
%configure
%make_build

%install
%makeinstall_std
mkdir -p %buildroot%_sharedstatedir/%name
make %name.hwdb
mkdir -p %buildroot/lib/udev/hwdb.d/
install -m 0644 %name.hwdb %buildroot/lib/udev/hwdb.d/
rm -rf %buildroot%_libdir/

#post
#
#  Create udev rules and FDI files.
#
#STATE_DIR=%_sharedstatedir/%name
#VERSION=%version-%rel
#PATH=%_libdir/%name:$PATH
#make-policy-file --force --quiet --mode udev \
#    --registry $STATE_DIR/clean-files --pkg-vers "$VERSION" || true
#if type xsltproc &> /dev/null; then
#    make-policy-file --force --quiet --mode fdi \
#        --registry $STATE_DIR/clean-files --pkg-vers "$VERSION" || true
#    udevadm control --reload_rules >/dev/null 2>&1 || true
#else
#    echo "Failed to setup automatic scanner configuration via HAL." >&2
#    echo "If you have trouble accessing your scanner as a regular user, please" >&2
#    echo "install xsltproc and run \"%_libdir/%name/make-policy-file --mode fdi\"" >&2
#    echo "to enable this feature." >&2
#fi
#udevadm hwdb --update >/dev/null 2>&1 || true

#postun
#udevadm hwdb --update >/dev/null 2>&1 || true

%files
%doc COPYING
%doc NEWS
%doc KNOWN-PROBLEMS
%doc SUPPORTED-DEVICES

%_datadir/iscan-data/scsi
%_datadir/iscan-data/usb
%_datadir/iscan-data/fs-blacklist
%_datadir/iscan-data/epkowa.desc
%_datadir/iscan-data/fdi.xsl
%_datadir/iscan-data/sled10.custom.fdi
%_datadir/iscan-data/device/*.xml
#_libdir/%name/make-policy-file
%_sharedstatedir/%name/
/lib/udev/hwdb.d/%name.hwdb

%changelog
* Thu Oct 31 2019 Vitaly Lipatov <lav@altlinux.ru> 1.39.1-alt1
- initial build for ALT Sisyphus
- skip udev rules
