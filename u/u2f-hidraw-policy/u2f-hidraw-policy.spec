Name: u2f-hidraw-policy
Version: 1.0.2
Release: alt1
Summary: Udev rule to allow desktop access to HIDRAW U2F tokens
Group: System/Configuration/Hardware
License: LGPLv2+
Url: https://github.com/amluto/u2f-hidraw-policy
# repacked %url/archive/%version/%name-%version.tar.gz
Source0: %name-%version.tar

# Automatically added by buildreq on Tue Nov 01 2016
# optimized out: pkg-config python-base
BuildRequires: libudev-devel

%description
u2f-hidraw-policy is a udev helper that detects U2F HID tokens as
described by the U2F spec.

%prep
%setup

%build
%make_build CFLAGS="%optflags"

%install
%makeinstall_std

%files
%_udevrulesdir/60-u2f-hidraw.rules
%_udevrulesdir/../u2f_hidraw_id
%doc README.md

%changelog
* Tue Nov 01 2016 Gleb F-Malinovskiy <glebfm@altlinux.org> 1.0.2-alt1
- Initial build.
