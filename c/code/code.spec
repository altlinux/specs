Name: code
Version: 1.1.12
Release: alt2

Summary: Visual Studio Code

License: Multiple, see https://code.visualstudio.com/license
Url: https://github.com/dotnet
Group: Development/Other

# Get from https://code.visualstudio.com/Download
Source: %name-%version.tar
Source1: %name-%version-i586.tar

Source2: code.desktop
Source3: code.png

Source4: %name-%version-fakecppunmets.tar

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
%setup -a4
%ifarch i586
rm -f resources/app/node_modules/vsda/build/Release/vsda_linux64.node
tar xfv %SOURCE1
%endif

%build
cd fakecppunmets
make

%install
mkdir -p %buildroot%_libdir/%name/
cp -a * %buildroot%_libdir/%name/
mkdir -p %buildroot%_bindir/
ln -rs %buildroot%_libdir/%name/bin/code %buildroot/%_bindir/code
install -m644 fakecppunmets/libfakecppunmets-code.so.0 %buildroot%_libdir/
rm -rf %buildroot%_libdir/%name/fakecppunmets/

install -m644 -D %SOURCE2 %buildroot%_desktopdir/%name.desktop
install -m644 -D %SOURCE3 %buildroot%_pixmapsdir/code.png

%files
%_bindir/code
%_libdir/%name/
%_libdir/libfakecppunmets-code.so.0
%_desktopdir/%name.desktop
%_pixmapsdir/code.png

%changelog
* Sun May 21 2017 Vitaly Lipatov <lav@altlinux.ru> 1.1.12-alt2
- add libfakecppunmets to fix unnneded BAD ELF symbols due libstd++ (MersenneTwister and so on)

* Sun May 21 2017 Vitaly Lipatov <lav@altlinux.ru> 1.1.12-alt1
- initial release for ALT Sisyphus
