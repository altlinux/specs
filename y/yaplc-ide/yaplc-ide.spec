Name: yaplc-ide
Version: 0.0
Release: alt2.20170629

Summary: Extensions for Beremiz, allowing to create applications YAPLC/RTE
Summary(ru_RU.UTF-8): Расширения для Beremiz, позволяющие создавать приложения YAPLC/RTE

License: GPLv3+
Group: Engineering
Url: https://github.com/nucleron/IDE

Packager: Anton Midyukov <antohami@altlinux.org>

Source: %name-%version.tar
Buildarch: noarch
BuildPreReq: rpm-build-python desktop-file-utils
%add_python_req_skip Beremiz CodeFileTreeNode ConfigTreeNode PLCControler controls editors targets util xmlclass
Requires: python-module-beremiz
Requires: matiec
Requires: yapyserial
Requires: gcc-c++
Requires: arm-none-eabi-gcc-c++
Requires: stm32flash
Requires: git-core
Requires: zenity

%description
Extensions for Beremiz, allowing to create applications YAPLC/RTE.

%description -l ru_RU.UTF-8
Расширения для Beremiz, позволяющие создавать приложения YAPLC/RTE.

%prep
%setup

%install
mkdir -p %buildroot%python_sitelibdir/%name
cp -r . %buildroot%python_sitelibdir/%name

### == executable file
cat>%name<<END
#!/bin/sh
if ! [ -d \$HOME/YAPLC/RTE ]; then
    zenity  --question \\
            --text="\$HOME/YAPLC/RTE does not exist!!! Download?"
    if [ $? -eq "0" ]; then
        mkdir -p \$HOME/YAPLC &&
        cd \$HOME/YAPLC &&
        xterm -T 'Downloaded YAPLC/RTE' -e bash -c 'git clone https://github.com/nucleron/RTE &&
        zenity --info --text="RTE downloaded successfully" ||
        zenity --error --text="RTE downloaded failed" '
    fi
fi
if ! [ -d \$HOME/YAPLC/libopencm3 ]; then
    zenity  --question \\
            --text="\$HOME/YAPLC/libopencm3 does not exist!!! Download?"
    if [ $? -eq "0" ]; then
        mkdir -p \$HOME/YAPLC &&
        cd \$HOME/YAPLC &&
        xterm -T 'Downloaded YAPLC/RTE' -e bash -c 'git clone https://github.com/nucleron/libopencm3 &&
        zenity --info --text="libopencm3 downloaded successfully" ||
        zenity --error --text="libopencm3 downloaded failed" '
    fi
fi
if ! [ -d \$HOME/YAPLC/freemodbus-v1.5.0 ]; then
    zenity  --question \\
            --text="\$HOME/YAPLC/freemodbus-v1.5.0 does not exist!!! Download?"
    if [ $? -eq "0" ]; then
        mkdir -p \$HOME/YAPLC &&
        cd \$HOME/YAPLC &&
        xterm -T 'Downloaded YAPLC/RTE' -e bash -c 'git clone https://github.com/nucleron/freemodbus-v1.5.0 &&
        zenity --info --text="freemodbus-v1.5.0 downloaded successfully" ||
        zenity --error --text="freemodbus-v1.5.0 downloaded failed" '
    fi
fi
if ! [ -d \$HOME/YAPLC/CanFestival-3 ]; then
    zenity  --question \\
            --text="\$HOME/YAPLC/CanFestival-3 does not exist!!! Download?"
    if [ $? -eq "0" ]; then
        mkdir -p \$HOME/YAPLC &&
        cd \$HOME/YAPLC &&
        xterm -T 'Downloaded YAPLC/CanFestival-3' -e bash -c 'git clone https://github.com/nucleron/CanFestival-3 &&
        cd \$HOME/YAPLC/CanFestival-3/objdictgen &&
        tar -xzf Gnosis_Utils-current.tar.gz &&
        mv Gnosis_Utils*/gnosis . &&
        rm -fr Gnosis_Utils* &&
        cd .. &&
        ./configure &&
        make &&
        zenity --info --text="CanFestival-3 downloaded successfully" ||
        zenity --error --text="CanFestival-3 downloaded failed" '
    fi
fi
python2 %python_sitelibdir/%name/yaplcide.py
END

mkdir -p %buildroot%_bindir/
install -m755 %name %buildroot%_bindir/%name

### == desktop file
cat>%name.desktop<<END
[Desktop Entry]
Name=YAPLC-IDE
Exec=%name
Icon=beremiz
Terminal=false
Type=Application
Categories=IDE;Development;
END

desktop-file-install --dir=%buildroot%_desktopdir %name.desktop

%files
%_bindir/%name
%python_sitelibdir/%name
%_desktopdir/%name.desktop

%changelog
* Sun Jul 09 2017 Anton Midyukov <antohami@altlinux.org> 0.0-alt2.20170629
- Added missing requires.

* Sun Jul 02 2017 Anton Midyukov <antohami@altlinux.org> 0.0-alt1.20170629
- Initial build for ALT Linux Sisyphus.
