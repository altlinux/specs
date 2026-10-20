%define _unpackaged_files_terminate_build 1
%define pypi_name newline_iwb_converter

Name: newline-iwb-converter
Version: 0.3.0
Release: alt1

Summary: Convert Newline whiteboard IWB lessons to SVG and PDF

License: GPL-3.0-only
Group: Office
Url: https://github.com/MatteoGheza/newline-iwb-converter

# Source-url: %__pypi_url %pypi_name
Source: %name-%version.tar

BuildArch: noarch
BuildRequires(pre): rpm-macros-python3
BuildRequires: rpm-build-python3
BuildRequires: python3-module-setuptools python3-module-wheel

%add_python3_path %_datadir/%name
%add_findprov_skiplist %_datadir/%name/*

%description
Newline IWB Converter extracts the pages of Newline interactive whiteboard
lessons (.iwb files) as SVG images (iwb2svg) and builds a multi-page PDF
from them (iwb2pdf). Images can be embedded, copied next to the pages or left
as external references. If Inkscape is installed, iwb2pdf uses it for better
SVG rendering, otherwise it falls back to svglib.

%prep
%setup

%build
%pyproject_build

%install
%pyproject_install
# the converter is an application: keep its modules private
mkdir -p %buildroot%_datadir/%name
mv %buildroot%python3_sitelibdir_noarch/%pypi_name %buildroot%python3_sitelibdir_noarch/%{pyproject_distinfo %name} \
    %buildroot%_datadir/%name/
rm -v %buildroot%_bindir/*
for t in iwb2svg iwb2pdf; do
cat > %buildroot%_bindir/$t <<'EOF2'
#!/usr/bin/python3
import sys
sys.path.insert(0, '%_datadir/%name')
from %pypi_name.@T@ import main
sys.exit(main())
EOF2
sed -i "s/@T@/$t/" %buildroot%_bindir/$t
chmod 755 %buildroot%_bindir/$t
done

%files
%doc README.md
%_bindir/iwb2svg
%_bindir/iwb2pdf
%_datadir/%name

%changelog
* Tue Oct 20 2026 Vitaly Lipatov <lav@altlinux.ru> 0.3.0-alt1
- initial build for Sisyphus

