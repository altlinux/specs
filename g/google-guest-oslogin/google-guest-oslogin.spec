Name:           google-guest-oslogin
Version:        20220721.00
Release:        alt1
Summary:        Google Cloud Guest OS Login
License:        Apache-2.0
Group:          System/Servers
URL:            https://github.com/GoogleCloudPlatform/guest-oslogin
Source:         %name-%version.tar
Requires:       openssh
BuildRequires:  boost-devel
BuildRequires:  gcc-c++
BuildRequires:  libcurl-devel
BuildRequires:  libjson-c-devel
BuildRequires:  pam-devel

Provides:       google-compute-engine-oslogin = %version-%release
#Requires:       google-guest-configs

%description
This package contains several libraries and changes to enable OS Login functionality
for Google Compute Engine.

%prep
%setup -q -n guest-oslogin-%version
sed -i 's,gzip -9,#gzip -9,g' src/Makefile
sed -i 's,\.8\.gz,.8,g' src/Makefile

%build
%make_build LDLIBS='-lcurl -ljson-c -lboost_regex' VERSION=%version

%install
%makeinstall_std DESTDIR=%buildroot LIBDIR=/%_lib PAMDIR=%_pam_modules_dir SYSTEMDDIR=%_unitdir PRESETDIR=%_presetdir VERSION=%version

%files
%doc README.md LICENSE
%attr(0755,root,root) %_bindir/google_authorized_keys
%attr(0755,root,root) %_bindir/google_authorized_keys_sk
%attr(0755,root,root) %_bindir/google_oslogin_nss_cache
%_man8dir/*
/%_lib/libnss*
%_pam_modules_dir/*
%_presetdir/*
%_unitdir/*

%changelog
* Sun Nov 06 2022 Evgeny Sinelnikov <sin@altlinux.org> 20220721.00-alt1
- Initial build for Sisyphus

