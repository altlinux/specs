Name: postsrsd
Version: 2.0.11
Release: alt1

Summary: Sender Rewriting Scheme daemon for Postfix

License: GPL-3.0-only
Group: Networking/Mail
URL: https://github.com/roehling/postsrsd
# Source-url: https://github.com/roehling/postsrsd/archive/refs/tags/%version.tar.gz
Source: %name-%version.tar

BuildRequires(pre): rpm-macros-cmake
BuildRequires: cmake gcc-c++
BuildRequires: libconfuse-devel

%description
The Sender Rewriting Scheme (SRS) is a technique to forward mails from domains
which deploy the Sender Policy Framework (SPF) to prohibit other Mail Transfer
Agents (MTAs) from sending mails on their behalf.

PostSRSd implements SRS for the Postfix MTA. It provides a daemon that
integrates with Postfix through a socketmap lookup table or a milter interface.

%prep
%setup

%build
%cmake \
    -DFETCHCONTENT_TRY_FIND_PACKAGE_MODE=ALWAYS \
    -DFETCHCONTENT_FULLY_DISCONNECTED=ON \
    -DGENERATE_SRS_SECRET=OFF \
    -DBUILD_TESTING=OFF \
    -DPOSTSRSD_USER=postsrsd \
    -DSYSTEMD_UNITDIR=%_unitdir \
    -DSYSTEMD_SYSUSERSDIR=/usr/lib/sysusers.d \
    -DCMAKE_BUILD_TYPE=Release
%cmake_build

%install
%cmake_install

%post
s="%_sysconfdir/postsrsd.secret"
if [ ! -e "$s" ]; then
    dd if=/dev/urandom bs=18 count=1 2>/dev/null | base64 > "$s"
    chmod 600 "$s"
fi

%files
%_sbindir/postsrsd
%_unitdir/postsrsd.service
/usr/lib/sysusers.d/postsrsd.conf
%doc %_datadir/doc/%name/%name.conf
/var/lib/postsrsd

%changelog
* Tue Mar 24 2026 Vitaly Lipatov <lav@altlinux.ru> 2.0.11-alt1
- initial build for ALT Sisyphus

