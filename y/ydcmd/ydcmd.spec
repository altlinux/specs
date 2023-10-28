Name: ydcmd
Version: 2.12.1
Release: alt1

Summary: Command line Yandex.Disk client

Group: Networking/File transfer
License: BSD-2-Clause
Url: https://github.com/abbat/ydcmd

BuildArch: noarch

# Source-url: https://github.com/abbat/ydcmd/archive/refs/heads/master.zip
Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3

%description
Command-line tool to upload, retrieve and manage data in Yandex.Disk service
(https://disk.yandex.com), designed for use in scripts.

%prep
%setup

%build

%install
install -d %buildroot%_bindir/
install -d %buildroot%python3_sitelibdir/

%__subst 's|env python|env python3|g' ydcmd.py

install -m755 ydcmd.py %buildroot%python3_sitelibdir/ydcmd.py

ln -sr %buildroot%python3_sitelibdir/ydcmd.py %buildroot%_bindir/ydcmd

install -d %buildroot%_man1dir
#install -d %buildroot%_mandir/ru/man1
#install -d %buildroot%_mandir/tr/man1

install -m644 man/ydcmd.1    %buildroot%_man1dir/ydcmd.1
#install -m644 man/ydcmd.ru.1 %buildroot%_mandir/ru/man1/ydcmd.1
#install -m644 man/ydcmd.tr.1 %buildroot%_mandir/tr/man1/ydcmd.1

%files
%doc README.md README.en.md README.tr.md ydcmd.cfg
%_bindir/ydcmd
%python3_sitelibdir/ydcmd.py*
#%python3_sitelibdir/__pycache__/ydcmd.*
%_man1dir/ydcmd.1*
#%_mandir/ru/man1/ydcmd.1*
#%_mandir/tr/man1/ydcmd.1*

%changelog
* Sat Oct 28 2023 Vitaly Lipatov <lav@altlinux.ru> 2.12.1-alt1
- initial build for ALT Sisyphus

* Wed Aug 17 2022 Anton Batenev <antonbatenev@yandex.ru> 2.12.1-1
- Initial RPM release
