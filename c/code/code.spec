Name: code
Version: 1.25.0
Release: alt1

Summary: Visual Studio Code

License: Multiple, see https://code.visualstudio.com/license
Url: https://code.visualstudio.com/
Group: Development/Other

# The same like from https://code.visualstudio.com/Download
# Source-url: https://vscode-update.azurewebsites.net/%version/linux-x64/stable
Source: %name-%version.tar
# Source1-url: https://vscode-update.azurewebsites.net/%version/linux-ia32/stable
Source1: %name-%version-i586.tar

Source2: code.desktop
Source3: code.png

ExclusiveArch: x86_64 i586

%set_verify_elf_method skip
%add_findreq_skiplist %_libdir/%name/bin/code
AutoReq:yes,nonodejs,nonodejs_native,nomono,nopython,nomingw32,nomingw64,noshebang
AutoProv: no

# /usr/lib64/code/resources/app/node_modules.asar.unpacked/keytar/build/Release/keytar.node: library libsecret-1.so.0
BuildRequires: libsecret

# we need it for AutoReq
BuildRequires: libgtk+2 libxkbfile libnss libnspr libXtst libalsa libcups libXScrnSaver libGConf

%description
Visual Studio Code is a new choice of tool that combines the simplicity
of a code editor with what developers need for the core edit-build-debug cycle.
See https://code.visualstudio.com/docs/setup/linux for installation instructions and FAQ.

%prep
%setup
%ifarch i586
rm -f resources/app/node_modules/vsda/build/Release/vsda_linux64.node
tar xfv %SOURCE1
%endif

%build

%install
mkdir -p %buildroot%_libdir/%name/
cp -a * %buildroot%_libdir/%name/
mkdir -p %buildroot%_bindir/
ln -rs %buildroot%_libdir/%name/bin/code %buildroot/%_bindir/code
ln -rs %buildroot%_libdir/%name/bin/code %buildroot/%_bindir/vscode
install -m644 -D %SOURCE2 %buildroot%_desktopdir/%name.desktop
install -m644 -D %SOURCE3 %buildroot%_pixmapsdir/code.png

%files
%_bindir/code
%_bindir/vscode
%_libdir/%name/
%_desktopdir/%name.desktop
%_pixmapsdir/code.png

%changelog
* Fri Jul 06 2018 Vitaly Lipatov <lav@altlinux.ru> 1.25.0-alt1
- new version 1.25.0 (with rpmrb script)
- use direct download links

* Thu Jul 05 2018 Vitaly Lipatov <lav@altlinux.ru> 1.24.1-alt1
- new version 1.24.1

* Fri May 18 2018 Vitaly Lipatov <lav@altlinux.ru> 1.23.1-alt1
- new version 1.23.1 (ALT bug 34012)

* Sat Feb 24 2018 Vitaly Lipatov <lav@altlinux.ru> 1.20.1-alt1
- new version 1.20.1

* Wed Jan 10 2018 Vitaly Lipatov <lav@altlinux.ru> 1.19.1-alt1
- new version 1.19.1

* Fri Dec 08 2017 Vitaly Lipatov <lav@altlinux.ru> 1.18.1-alt1
- new version 1.18.1

* Sun Oct 22 2017 Vitaly Lipatov <lav@altlinux.ru> 1.17.2-alt1
- new version 1.17.2

* Tue Jun 13 2017 Vitaly Lipatov <lav@altlinux.ru> 1.13.0-alt1
- new version 1.13.0

* Thu Jun 01 2017 Vitaly Lipatov <lav@altlinux.ru> 1.12.2-alt1
- initial release for ALT Sisyphus
