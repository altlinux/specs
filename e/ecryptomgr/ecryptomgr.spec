Name: ecryptomgr
Version: 0.3
Release: alt1

Summary: Crypto provider installer

License: Public domain
Group: File tools

Source: %name-%version.tar

BuildArch: noarch

%define sdir %_datadir/%name

%description
Crypto provider installer.

run
 $ crypto-install in a dir with downloaded crypto provider distribute.

Supported:
 * CryptoPro 4/5 64/32 bit
 * ViPNet CSP 4.2/4.4 64/32 bit

%prep
%setup

%build
subst "s|^SDIR=.*|SDIR=%sdir|" ecryptomgr.sh

%install
mkdir -p %buildroot%sdir/
install -D ecryptomgr.sh %buildroot%_bindir/ecryptomgr
for i in clean_* install_* uninstall_* test_* ; do
    install $i %buildroot%sdir/
done

%files
%doc README.md
%_bindir/ecryptomgr
%sdir/

%changelog
* Thu Oct 01 2020 Vitaly Lipatov <lav@altlinux.ru> 0.3-alt1
- improve description
- ecryptomgr.sh: add arch detection

* Thu Oct 01 2020 Vitaly Lipatov <lav@altlinux.ru> 0.2-alt1
- add license check support
- unstall_cryptopro.sh: test and fix
- fix install/uninstall CryptoPro on i586
- install_itcs.sh: install libqt4-gui for 32 over 64

* Wed Sep 30 2020 Vitaly Lipatov <lav@altlinux.ru> 0.1-alt1
- initial build for ALT Sisyphus
