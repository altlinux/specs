%define soname      1

Name: burp
Version: 2.1.24
Release: alt1

Summary: Backup and Restore

Packager: Vitaly Lipatov <lav@altlinux.ru>

# Source-url: https://github.com/grke/burp/archive/%version.tar.gz
Source: %name-%version.tar

Url: http://burp.grke.org
Group: File tools
License: Affero GNU General Public License version 3 (AGPL v3)

# Automatically added by buildreq on Wed Aug 10 2016
# optimized out: glibc-devel-static gnu-config libcom_err-devel libkrb5-devel libncurses-devel libstdc++-devel libtinfo-devel perl pkg-config python-base python-modules python3 python3-base
BuildRequires: gcc-c++ libacl-devel librsync-devel libssl-devel libuthash-devel  zlib-devel

BuildPreReq: libncurses-devel

# %_localstatedir
BuildRequires: rpm-macros-intro-conflicts

%description
Burp is a backup and restore program. It uses librsync in order to save on the
amount of space that is used by each backup. It also uses VSS (Volume Shadow
Copy Service) to make snapshots when backing up Windows computers.

%prep
%setup

%build
%autoreconf
%configure \
    --sysconfdir="%_sysconfdir/burp" \
    --disable-static \
    --with-tcp-wrappers

%make_build

%install
%makeinstall_std install-all


%files
#doc CHANGELOG CONTRIBUTORS LICENSE README* TODO
%doc %_docdir/%name/
%dir %_sysconfdir/burp/
%config(noreplace) %_sysconfdir/burp/burp-server.conf
%config(noreplace) %_sysconfdir/burp/burp.conf
%config(noreplace) %_sysconfdir/burp/CA.cnf
%dir %_sysconfdir/burp/clientconfdir/
%config %_sysconfdir/burp/clientconfdir/testclient
%dir %_sysconfdir/burp/clientconfdir/incexc
%config %_sysconfdir/burp/clientconfdir/incexc/example
%dir %_datadir/%name/
%_datadir/%name/scripts/
%_bindir/vss_strip
%_sbindir/burp
%_sbindir/burp_ca
%_sbindir/bedup
%_sbindir/bsigs
%_sbindir/bsparse
%_man8dir/*

%changelog
* Tue Dec 05 2017 Vitaly Lipatov <lav@altlinux.ru> 2.1.24-alt1
- new version 2.1.24 (with rpmrb script)

* Wed Aug 10 2016 Vitaly Lipatov <lav@altlinux.ru> 2.0.44-alt1
- initial build for ALT Linux Sisyphus

