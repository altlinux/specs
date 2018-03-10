%def_with docs
Name: beremiz
Version: 1.2
Release: alt1.20180305

Summary: Integrated development environment for machine automation
Summary(ru_RU.UTF-8): Интегрированная среда разработки для ПЛК

License: GPLv3+
Group: Engineering
Url: https://bitbucket.org/skvorl/beremiz

Packager: Anton Midyukov <antohami@altlinux.org>

Source: %name-%version.tar
Source1: %name-16x16.png
Source2: %name-32x32.png
Source3: %name-48x48.png
Source4: poe-16x16.png
Source5: poe-32x32.png
Source6: poe-48x48.png
Patch: CanFestival-PATH.patch

Buildarch: noarch
BuildPreReq: rpm-build-python dos2unix desktop-file-utils

%if_with docs
BuildRequires(pre): rpm-macros-sphinx python-module-sphinx
%endif #docs

%add_python_req_skip __pyjamas__ canfestival_config commondialogs eds_utils gen_cfile gluon gnosis networkeditortemplate nodeeditortemplate nodelist nodemanager subindextable
Requires: python-module-%name = %version-%release
Requires: matiec
Requires: gcc-c++
Requires: CanFestival-3-source

%description
Beremiz is an integrated development environment for machine
automation. It is Free Software, conforming to IEC-61131 among
other standards.

It relies on open standards to be independent of the targeted
device, and let you turn any processor into a PLC. Beremiz
includes tools to create HMI, and to connect your PLC programs
to existing supervisions, databases, or fieldbuses.

With Beremiz, you conform to standards, avoid vendor lock, and
contribute to the better future of Automation.

%description -l ru_RU.UTF-8
Beremiz - это интегрированная среда разработки для ПЛК.
Является свободным программным обеспечением, соответсвует стандарту
МЭК-61131 и другим стандартам.

Beremiz опирается на открытые стандарты, которые не зависят от целевых
устройств. Так что вы можете превратить любой процессор в ПЛК. Beremiz
включает инструменты для создания HMI и подключения ваших программ PLC
к наблюдению, базам данным или полевым шинам.

Используя Beremiz, вы отвечаете стандартам, избегаете вендорлока и
вносите свой вклад в лучшее будущее автоматизации.

%package -n python-module-%name
Summary: Integrated development environment for machine automation
Group: Development/Python
%py_requires matplotlib.backends.backend_wx

%description -n python-module-%name
Integrated development environment for machine automation

%package -n python-module-%name-tests
Summary: Tests for python-module-%name
Group: Development/Python
Requires: python-module-%name = %version-%release
%add_python_req_skip Beremiz PLCOpenEditor controls

%description -n python-module-%name-tests
Tests for python-module-%name

%prep
%setup -n %name-%version
%patch -p2
find . -type f -print0 | xargs -0 dos2unix

%build
%if_with docs
pushd doc
make html
make man
popd
%endif #docs

%install
mkdir -p %buildroot%python_sitelibdir/%name
cp -r . %buildroot%python_sitelibdir/%name
rm -rf %buildroot%python_sitelibdir/%name/doc \
       %buildroot%python_sitelibdir/%name/.hg_archival.txt \
       %buildroot%python_sitelibdir/%name/.hgignore \
       %buildroot%python_sitelibdir/%name/i18n
mkdir -p %buildroot%_docdir/%name-%version
mv %buildroot%python_sitelibdir/%name/COPYING* %buildroot%_docdir/%name-%version
mv %buildroot%python_sitelibdir/%name/README.md %buildroot%_docdir/%name-%version

%if_with docs
cp -r doc/_build/html/* %buildroot%_docdir/%name-%version
mkdir -p %buildroot%_man1dir
cp -r doc/_build/man/*.1 %buildroot%_man1dir
%endif #docs

## == install icons
mkdir -p %buildroot/%_miconsdir
install -m 644 %SOURCE1 %buildroot/%_miconsdir/%name.png
install -m 644 %SOURCE4 %buildroot/%_miconsdir/PLCOpenEditor.png
mkdir -p %buildroot/%_niconsdir
install -m 644 %SOURCE2 %buildroot/%_niconsdir/%name.png
install -m 644 %SOURCE5 %buildroot/%_niconsdir/PLCOpenEditor.png
mkdir -p %buildroot/%_liconsdir
install -m 644 %SOURCE3 %buildroot/%_liconsdir/%name.png
install -m 644 %SOURCE6 %buildroot/%_liconsdir/PLCOpenEditor.png

### == executable file beremiz
cat>%name<<END
#!/bin/sh
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
%_bindir/python2 %python_sitelibdir/%name/Beremiz.py
END
# xterm -T 'Building CanFestival-3' -e bash -c \
mkdir -p %buildroot%_bindir/
install -m 755 %name %buildroot%_bindir/%name

### == executable file beremiz-service
cat>%name<<END
#!/bin/sh
%_bindir/python2 %python_sitelibdir/%name/Beremiz_service.py
END

mkdir -p %buildroot%_bindir/
install -m 755 %name %buildroot%_bindir/%name-service


### == executable file PLCOpenEditor
cat>%name<<END
#!/bin/sh
%_bindir/python2 %python_sitelibdir/%name/PLCOpenEditor.py
END

mkdir -p %buildroot%_bindir/
install -m 755 %name %buildroot%_bindir/plcopeneditor

### == desktop file beremiz
cat>%name.desktop<<END
[Desktop Entry]
Name=Beremiz
Exec=%name
Icon=%name
Terminal=false
Type=Application
Categories=IDE;Development;
END

desktop-file-install --dir=%buildroot%_desktopdir %name.desktop

### == desktop file beremiz-service
cat>%name-service.desktop<<END
[Desktop Entry]
Name=Beremiz-service
Exec=%name-service
Icon=%name
Terminal=false
Type=Application
Categories=IDE;Development;
END

desktop-file-install --dir=%buildroot%_desktopdir %name-service.desktop

### == desktop file PLCOpenEditor
cat>PLCOpenEditor.desktop<<END
[Desktop Entry]
Name=PLCOpenEditor
Exec=plcopeneditor
Icon=PLCOpenEditor
Terminal=false
Type=Application
Categories=IDE;Development;
END

desktop-file-install --dir=%buildroot%_desktopdir PLCOpenEditor.desktop

%files
%_bindir/*
%_miconsdir/*.png
%_niconsdir/*.png
%_liconsdir/*.png
%_desktopdir/*.desktop
%_docdir/%name-%version
%_man1dir/*.1.*

%files -n python-module-%name
%python_sitelibdir/%name
%exclude %python_sitelibdir/%name/tests

%files -n python-module-%name-tests
%python_sitelibdir/%name/tests

%changelog
* Sat Mar 10 2018 Anton Midyukov <antohami@altlinux.org> 1.2-alt1.20180305
- New snapshot

* Thu Sep 28 2017 Anton Midyukov <antohami@altlinux.org> 1.2-alt1.20170917
- New snapshot

* Mon Sep 04 2017 Anton Midyukov <antohami@altlinux.org> 1.2-alt1.20170828
- New snapshot

* Sun Jul 09 2017 Anton Midyukov <antohami@altlinux.org> 1.2-alt1.20170705
- New snapshot
- Added missing requires.

* Sat Jul 01 2017 Anton Midyukov <antohami@altlinux.org> 1.2-alt1.20170628
- Initial build for ALT Linux Sisyphus.
