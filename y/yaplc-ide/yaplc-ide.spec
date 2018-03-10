Name: yaplc-ide
Version: 1.1.0
Release: alt1.20180112

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
Requires: CanFestival-3-source
Requires: yaplc-rte-source
Requires: libopencm3-source
Requires: libremodbus-source
Requires: yaplc_demos

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
    mkdir -p \$HOME/YAPLC &&
    cd \$HOME/YAPLC &&
    cp -fr %_prefix/src/yaplc-rte RTE
fi

if ! [ -d \$HOME/YAPLC/libopencm3 ]; then
    mkdir -p \$HOME/YAPLC &&
    cd \$HOME/YAPLC &&
    cp -fr %_prefix/src/libopencm3 .
fi

if ! [ -d \$HOME/YAPLC/libremodbus ]; then
    mkdir -p \$HOME/YAPLC &&
    cd \$HOME/YAPLC &&
    cp -fr %_prefix/src/libremodbus .
fi

if ! [ -d \$HOME/YAPLC/CanFestival-3 ]; then
    mkdir -p \$HOME/YAPLC &&
    cd \$HOME/YAPLC &&
    cp -fr %_prefix/src/CanFestival-3 \$HOME/YAPLC/ &&
    cd \$HOME/YAPLC/CanFestival-3/objdictgen &&
    tar -xzf Gnosis_Utils-current.tar.gz &&
    mv Gnosis_Utils*/gnosis . &&
    rm -fr Gnosis_Utils* &&
    cd \$HOME/YAPLC/CanFestival-3 &&
    ./configure &&
    make
fi

if ! [ -d \$HOME/YAPLC_DEMOS ]; then
    mkdir -p \$HOME/YAPLC &&
    cd \$HOME/YAPLC &&
    cp -fr %_docdir/YAPLC_DEMOS .
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
* Sat Mar 10 2018 Anton Midyukov <antohami@altlinux.org> 1.1.0-alt1.20180112
- New version 1.1.0

* Sun Jul 09 2017 Anton Midyukov <antohami@altlinux.org> 0.0-alt2.20170629
- Added missing requires.

* Sun Jul 02 2017 Anton Midyukov <antohami@altlinux.org> 0.0-alt1.20170629
- Initial build for ALT Linux Sisyphus.
