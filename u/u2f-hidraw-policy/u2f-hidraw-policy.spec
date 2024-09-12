Name: u2f-hidraw-policy
Version: 1.0.2
Release: alt2
Summary: Udev rule to allow desktop access to HIDRAW U2F tokens
Group: System/Configuration/Hardware
License: LGPLv2+
Url: https://github.com/amluto/u2f-hidraw-policy
# repacked %url/archive/%version/%name-%version.tar.gz
Source0: %name-%version.tar

Patch0: u2f-hidraw-policy-1.0.2-alt-udev-dir.patch

# Automatically added by buildreq on Tue Nov 01 2016
# optimized out: pkg-config python-base
BuildRequires: libudev-devel

%description
u2f-hidraw-policy is a udev helper that detects U2F HID tokens as
described by the U2F spec.

%prep
%setup
%patch0 -p1

%build
%make_build CFLAGS="%optflags"

%install
%makeinstall_std UDEV_DIR=%_udevrulesdir/../

%files
%_udevrulesdir/60-u2f-hidraw.rules
%_udevrulesdir/../u2f_hidraw_id
%doc README.md

%changelog
* Thu Sep 12 2024 Gleb F-Malinovskiy <glebfm@altlinux.org> 1.0.2-alt2
- Fixed build with the new version of %%_udevrulesdir macro.

* Tue Nov 01 2016 Gleb F-Malinovskiy <glebfm@altlinux.org> 1.0.2-alt1
- Initial build.
