%define _unpackaged_files_terminate_build 1

Name: sbne
Version: 1.3.0
Release: alt1

Summary: Export SMART Notebook .notebook lessons to SVG, PNG and PDF

License: GPL-3.0-or-later
Group: Office
Url: https://github.com/MikeCat2008/smartboard-notebook-exporter

# Source-url: https://github.com/MikeCat2008/smartboard-notebook-exporter/archive/v%version.tar.gz?/%name-%version.tar.gz
Source: %name-%version.tar
Patch: %name-%version-alt-fix-startup-traceback.patch

BuildArch: noarch
BuildRequires(pre): rpm-build-python3

%add_python3_path %_datadir/%name
%add_findprov_skiplist %_datadir/%name/*

%description
Smartboard notebook Exporter (sbne) converts SMART Notebook (.notebook)
lesson files locally into other formats: fixed SVG pages, PNG pages and
PDF files (vector or raster, one file per page or a single merged file).
It comes with a graphical interface (sbne) and an interactive command line
interface (sbne-cli).

%prep
%setup
%patch -p1

%build

%install
mkdir -p %buildroot%_datadir/%name
install -pm644 src/*.py %buildroot%_datadir/%name/
mkdir -p %buildroot%_bindir
cat > %buildroot%_bindir/%name <<'EOF2'
#!/bin/sh
exec %__python3 %_datadir/%name/gui.py "$@"
EOF2
cat > %buildroot%_bindir/%name-cli <<'EOF2'
#!/bin/sh
exec %__python3 %_datadir/%name/main.py "$@"
EOF2
chmod 755 %buildroot%_bindir/%name %buildroot%_bindir/%name-cli
mkdir -p %buildroot%_desktopdir
cat > %buildroot%_desktopdir/%name.desktop <<'EOF2'
[Desktop Entry]
Type=Application
Name=Smartboard notebook Exporter
Comment=Export SMART Notebook lessons to SVG, PNG and PDF
Exec=%name
Terminal=false
Categories=Office;Education;
EOF2

%files
%doc README.md README.es.md docs
%_bindir/%name
%_bindir/%name-cli
%_datadir/%name
%_desktopdir/%name.desktop

%changelog
* Tue Oct 20 2026 Vitaly Lipatov <lav@altlinux.ru> 1.3.0-alt1
- initial build for Sisyphus

