Name: code
Version: 1.19.1
Release: alt1

Summary: Visual Studio Code

License: Multiple, see https://code.visualstudio.com/license
Url: https://code.visualstudio.com/
Group: Development/Other

# Get from https://code.visualstudio.com/Download
Source: %name-%version.tar
Source1: %name-%version-i586.tar

Source2: code.desktop
Source3: code.png

ExclusiveArch: x86_64 i586

%set_verify_elf_method skip
%add_findreq_skiplist %_libdir/%name/bin/code
AutoReq:yes,nonodejs,nonodejs_native,nomono,nopython,nomingw32,nomingw64,noshebang
AutoProv: no

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
# replace strange missed functions with exit
sed -E -i -e "s@(_ZN10crash_keys17SetVari|_ZN15MersenneTwister12in|_ZN15MersenneTwister13ge|_ZN15MersenneTwisterC1Ev|_ZN15MersenneTwisterD1Ev)@exit\x0MersenneTwisterD1Ev@g" ./code
#_ZN10crash_keys17SetVari ationsListERKSt6vectorISsSaISsEE
#_ZN15MersenneTwister12in it_genrandEj
#_ZN15MersenneTwister13ge nrand_int32Ev
#_ZN15MersenneTwisterC1Ev
#_ZN15MersenneTwisterD1Ev
#exit

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
