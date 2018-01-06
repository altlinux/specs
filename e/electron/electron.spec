# TODO: build from sources
Name: electron
Version: 1.7.10
Release: alt1

Summary: Build cross platform desktop apps with JavaScript, HTML, and CSS

License: MIT License
Url: https://electronjs.org/
Group: Development/Other

# Source-url: https://github.com/electron/electron/releases/download/v%version/electron-v%version-linux-x64.zip
Source: %name-%version.tar
# Source1-url: https://github.com/electron/electron/releases/download/v%version/electron-v%version-linux-ia32.zip
Source1: %name-%version-i586.tar

ExclusiveArch: x86_64 i586

%set_verify_elf_method skip
#add_findreq_skiplist %_libdir/%name/bin/code
AutoReq:yes,nonodejs,nonodejs_native,nomono,nopython,nomingw32,nomingw64,noshebang
AutoProv: no

BuildRequires: libgtk+2 libxkbfile libnss libnspr libXtst libalsa libcups libXScrnSaver libGConf

%description
Build cross platform desktop apps with JavaScript, HTML, and CSS.

%prep
%setup
%ifarch i586
tar xfv %SOURCE1
%endif

%build
# replace strange missed functions with exit
sed -E -i -e "s@(_ZN10crash_keys17SetVari|_ZN15MersenneTwister12in|_ZN15MersenneTwister13ge|_ZN15MersenneTwisterC1Ev|_ZN15MersenneTwisterD1Ev)@exit\x0MersenneTwisterD1Ev@g" ./%name
#_ZN10crash_keys17SetVari ationsListERKSt6vectorISsSaISsEE
#_ZN15MersenneTwister12in it_genrandEj
#_ZN15MersenneTwister13ge nrand_int32Ev
#_ZN15MersenneTwisterC1Ev
#_ZN15MersenneTwisterD1Ev

%install
mkdir -p %buildroot%_libdir/%name/
cp -a * %buildroot%_libdir/%name/
mkdir -p %buildroot%_bindir/
ln -rs %buildroot%_libdir/%name/%name %buildroot/%_bindir/%name

%files
%_bindir/%name
%_libdir/%name/

%changelog
* Sat Jan 06 2018 Vitaly Lipatov <lav@altlinux.ru> 1.7.10-alt1
- new version 1.7.10 (with rpmrb script)

* Thu Jul 13 2017 Vitaly Lipatov <lav@altlinux.ru> 1.6.11-alt1
- initial release for ALT Sisyphus (just pack binaries)
