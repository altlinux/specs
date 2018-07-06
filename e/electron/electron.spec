# TODO: build from sources
Name: electron
Version: 2.0.4
Release: alt1

Summary: Build cross platform desktop apps with JavaScript, HTML, and CSS

License: MIT License
Url: https://electronjs.org/
Group: Development/Other

# Source-url: https://github.com/electron/electron/releases/download/v%version/electron-v%version-linux-x64.zip
Source: %name-%version.tar
# Source1-url: https://github.com/electron/electron/releases/download/v%version/electron-v%version-linux-ia32.zip
Source1: %name-%version-i586.tar

Source2: patch_binary.sh

ExclusiveArch: x86_64 i586

%set_verify_elf_method skip
#add_findreq_skiplist %_libdir/%name/bin/code
AutoReq:yes,nonodejs,nonodejs_native,nomono,nopython,nomingw32,nomingw64,noshebang
AutoProv: no

BuildRequires: libgtk+3 libxkbfile libnss libnspr libXtst libalsa libcups libXScrnSaver libGConf
# bundled:
# library libnode.so not found
# library libffmpeg.so not found

%description
Build cross platform desktop apps with JavaScript, HTML, and CSS.

%prep
%setup
%ifarch i586
tar xfv %SOURCE1
%endif

%build
sh %SOURCE2 ./%name

%install
mkdir -p %buildroot%_libdir/%name/
cp -a * %buildroot%_libdir/%name/
mkdir -p %buildroot%_bindir/
ln -rs %buildroot%_libdir/%name/%name %buildroot/%_bindir/%name

%files
%_bindir/%name
%_libdir/%name/

%changelog
* Thu Jul 05 2018 Vitaly Lipatov <lav@altlinux.ru> 2.0.4-alt1
- new version 2.0.4 (with rpmrb script)
- GTK3 now

* Sun May 20 2018 Vitaly Lipatov <lav@altlinux.ru> 1.8.7-alt1
- new version 1.8.7 (with rpmrb script)

* Sat Jan 06 2018 Vitaly Lipatov <lav@altlinux.ru> 1.7.10-alt1
- new version 1.7.10 (with rpmrb script)

* Thu Jul 13 2017 Vitaly Lipatov <lav@altlinux.ru> 1.6.11-alt1
- initial release for ALT Sisyphus (just pack binaries)
