Name: pam_8021x
Version: 0.0.20140107
Release: alt1

Summary: Pluggable Authentication Module for 802.1x authentication protocol

License: %gpl2plus
Group: System/Configuration/Networking
Url: https://github.com/ehbello/pam-8021x

Source: %name-%version.tar
Patch0: %name-%version-%release.patch
Patch1: %name-0.0.20140107-compilation-fixes.patch

BuildRequires(pre): rpm-build-licenses
# due to PAM policy:
BuildRequires(pre): libpam-devel
# due to the non-use of deprecated g_type_init():
BuildPreReq: glib2-devel >= 2.36
BuildRequires: libdbus-devel libdbus-glib-devel libnm-util-devel NetworkManager-devel

%set_pam_name %name

%package -n %pam_name
Summary: %summary
License: %license
Group: %group
Provides: %name = %EVR

%global long_desc This is the PAM to 802.1x protocol authentication module.\
\
This module talks with NetworkManager daemon sending messages through D-BUS\
system to get authentication with 802.1x protocol.\
\
This first version only creates the needed network connection for a\
specific 802.1x configuration with PEAP/MSCHAPv2 authentication. It still\
does not check if authentication succeeds.\

%description
%long_desc

%description -n %pam_name
%long_desc

%prep
%setup
%patch1 -p1
%patch0 -p1

%build
%autoreconf
%configure
# No effect: export CFLAGS
%make_build CFLAGS="$CFLAGS -Werror"

ln -sfv %_licensedir/GPL-2 COPYING
# Just another copy (with non-significant additional text);
# we don't care whether it is there:
rm -f LICENSE

%install
%makeinstall_std pammoddir=%_pam_modules_dir

%check
%make_build check

%files -n %pam_name
%doc AUTHORS NEWS README COPYING
%_pam_modules_dir/*

%changelog
* Mon Nov 20 2017 Ivan Zakharyaschev <imz@altlinux.org> 0.0.20140107-alt1
- initial build for ALT Sisyphus.
