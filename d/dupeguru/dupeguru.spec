%define _unpackaged_files_terminate_build 1

%def_with check

Name: dupeguru
Version: 4.3.1
Release: alt2

Summary: GUI tool to find duplicate files in a system
License: GPL-3.0
Group: File tools
URL: https://github.com/arsenetar/dupeguru

BuildRequires(pre): rpm-build-python3

BuildRequires: python3-devel
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-wheel
BuildRequires: /usr/bin/pyrcc5

BuildRequires: python3(mutagen)
BuildRequires: python3(polib)
BuildRequires: python3(semantic_version)
BuildRequires: python3(send2trash)
BuildRequires: python3(sphinx)

%if_with check
BuildRequires: /usr/bin/pytest3
BuildRequires: python3(sqlite3)
%endif

AutoProv: yes,nopython
AutoReq: yes,nopython

%filter_from_requires /python3(core)/d
%filter_from_requires /python3(hscommon.trans)/d
%filter_from_requires /python3(qt.error_report_dialog)/d
%filter_from_requires /python3(qt.platform)/d
%filter_from_requires /python3(qt.util)/d

Requires: python3(mutagen)
Requires: python3(send2trash)
Requires: python3(semantic_version)
Requires: python3(sqlite3)

Source: %name-%version.tar

# sync with 4.3.1-3 from Debian unstable
Patch: %name-%version-%release.patch

%description
dupeGuru is a tool to find duplicate files on your computer.

It can scan either filenames or contents. The filename scan features a
fuzzy matching algorithm that can find duplicate filenames even when
they are not exactly the same.

dupeGuru is customizable: you can tweak its matching engine to find
exactly the kind of duplicates you want to find.

%prep
%setup
%patch -p1
sed -i "s|Categories=.*|Categories=Qt;System;Filesystem;|" pkg/dupeguru.desktop

%build
export NO_VENV=true
%python3_build
%make qt/dg_rc.py
%make build/help
%make i18n

%install
export NO_VENV=true
%python3_install \
                  --install-lib=%_datadir/dupeguru \
                  --install-scripts=%_datadir/dupeguru

# run check here, as we'll remove the test directories later
%if_with check
pushd %buildroot
PYTHONPATH=$PWD pytest3
popd
%endif

# simulate debian/rules (execute_after_dh_install) and debian/files
mkdir -p %buildroot%_libexecdir/dupeguru
mkdir -p %buildroot%_datadir/dupeguru/locale/

rm -frv %buildroot%_includedir
rm -frv %buildroot%_datadir/dupeguru/core/pe/modules/
rm -frv %buildroot%_datadir/dupeguru/core/tests/
rm -frv %buildroot%_datadir/dupeguru/hscommon/tests/
rm -frv %buildroot%_datadir/dupeguru/qt/pe/modules/
rm -frv %buildroot%_datadir/dupeguru/dupeguru

mkdir -pv %buildroot%_libexecdir/dupeguru/core/
mv -v %buildroot%_datadir/dupeguru/core/pe \
    %buildroot%_libexecdir/dupeguru/core/
mkdir -pv %buildroot%_libexecdir/dupeguru/qt/
mv -v %buildroot%_datadir/dupeguru/qt/pe \
    %buildroot%_libexecdir/dupeguru/qt/

cp -v run.py %buildroot%_datadir/dupeguru/run.py
cp -arv locale/ %buildroot%_datadir/dupeguru/
find %buildroot%_datadir/dupeguru/locale/ \
    ! -name "*.mo" -type f -delete -print
cp -v images/dgse_logo_128.png	%buildroot%_datadir/dupeguru

mkdir -pv %buildroot/%_desktopdir
cp -v pkg/dupeguru.desktop %buildroot/%_desktopdir

# create wrapper script in /usr/bin
mkdir -pv %buildroot/usr/bin/
cat <<EOF > %buildroot%_bindir/%name
#!/bin/sh
python3 %_datadir/dupeguru/run.py "\$@"
EOF
chmod a+x %buildroot/%_bindir/%name

# simulate debian/links
mkdir -pv %buildroot%_pixmapsdir
ln -srv %buildroot%_datadir/dupeguru/dgse_logo_128.png %buildroot%_pixmapsdir/dupeguru.png
ln -srv %buildroot%_libexecdir/dupeguru/core/pe %buildroot%_datadir/dupeguru/core/pe
ln -srv %buildroot%_libexecdir/dupeguru/qt/pe %buildroot%_datadir/dupeguru/qt/pe

# copy missed file
cp -pv qt/dg_rc.py %buildroot%_datadir/dupeguru/qt/dg_rc.py

# copy help files
cp -rpv build/help %buildroot%_datadir/dupeguru/

%files
%doc CONTRIBUTING.md CREDITS LICENSE README.md Windows.md macos.md
%doc help/changelog 
%_bindir/dupeguru
%_desktopdir/dupeguru.desktop
%_pixmapsdir/dupeguru.png
%dir %_libexecdir/dupeguru
%_libexecdir/dupeguru/*
%exclude %_libexecdir/dupeguru/core/pe/block.pyi
%exclude %_libexecdir/dupeguru/core/pe/cache.pyi
%exclude %_libexecdir/dupeguru/qt/pe/block.pyi
%dir %_datadir/dupeguru
%_datadir/dupeguru/*
%exclude %_libexecdir/dupeguru/core/pe/__pycache__
%exclude %_libexecdir/dupeguru/qt/pe/__pycache__
%exclude %_libexecdir/dupeguru/core/pe/*.py?
%exclude %_libexecdir/dupeguru/qt/pe/*.py?
%exclude %_datadir/dupeguru/core/gui/__pycache__
%exclude %_datadir/dupeguru/core/me/__pycache__
%exclude %_datadir/dupeguru/core/__pycache__
%exclude %_datadir/dupeguru/core/se/__pycache__
%exclude %_datadir/dupeguru/hscommon/gui/__pycache__
%exclude %_datadir/dupeguru/hscommon/jobprogress/__pycache__
%exclude %_datadir/dupeguru/hscommon/__pycache__
%exclude %_datadir/dupeguru/qt/me/__pycache__
%exclude %_datadir/dupeguru/qt/__pycache__
%exclude %_datadir/dupeguru/qt/se/__pycache__

%changelog
* Sun Mar 29 2026 Nikolay Strelkov <snk@altlinux.org> 4.3.1-alt2
- Added python3(sqlite3) dependency for p11.
- Placed help files in the correct folder for offline usage.

* Sun Nov 09 2025 Nikolay Strelkov <snk@altlinux.org> 4.3.1-alt1
- Initial build for Sisyphus
