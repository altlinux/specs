%define _unpackaged_files_terminate_build 1

Name: pam_radius
Summary: PAM Module for RADIUS Authentication
Version: 2.0.1
Release: alt1
Group: System/Base
License: GPLv2+
Url: http://www.freeradius.org/pam_radius_auth/
Vcs: https://github.com/FreeRADIUS/pam_radius.git
Source: %name-%version.tar
Patch: %name-%version.patch

Provides: pam_radius_auth = %EVR
BuildRequires(pre): rpm-macros-pam
BuildRequires: libpam-devel

%description
This is the PAM to RADIUS authentication module. It allows any PAM-capable
machine to become a RADIUS client for authentication and accounting
requests. You will need a RADIUS server to perform the actual
authentication.

%prep
%setup
%patch -p1

%build
export CFLAGS="%optflags -fpic"
%autoreconf
%configure --enable-werror --disable-developer
%make_build

%install
mkdir -p %buildroot{%_pam_modules_dir,%_sysconfdir}
install -m 644 pam_radius_auth.so %buildroot%_pam_modules_dir
install -m 600 pam_radius_auth.conf %buildroot%_sysconfdir/pam_radius_auth.conf

%files
%doc README.md INSTALL USAGE Changelog redhat/pam_sshd_example
%config(noreplace) %attr(0600, root, root) %_sysconfdir/pam_radius_auth.conf
%_pam_modules_dir/pam_radius_auth.so

%changelog
* Tue Feb 15 2022 Alexey Shabalin <shaba@altlinux.org> 2.0.1-alt1
- Initial build upstream master snapshot.

