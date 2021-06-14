Name:    rastercarve
Version: 1.0.8
Release: alt1

Summary: Generate G-code to engrave raster images
License: GPL-2.0
Group:   Engineering
URL:     https://github.com/built1n/rastercarve

Packager: Anton Midyukov <antohami@altlinux.org>

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-dev python3-module-setuptools
BuildRequires: python3-module-opencv
BuildRequires: python3-module-numpy
BuildRequires: python3-module-tqdm

BuildArch: noarch

Source:  %name-%version.tar

%description
%summary

%prep
%setup

%build
%python3_build

%install
%python3_install

mkdir -p %buildroot%_bindir
cat > %buildroot%_bindir/%name << EOF
#!/bin/sh
%__python3 -m %name \$@
EOF
chmod 755 %buildroot%_bindir/%name

%check
export PYTHONPATH=%buildroot%python3_sitelibdir
%buildroot%_bindir/%name -h
%buildroot%_bindir/%name --width 10 examples/test.png

%files
%_bindir/%name
%python3_sitelibdir/%name/
%python3_sitelibdir/*.egg-info
%doc *.md

%changelog
* Mon Jun 14 2021 Anton Midyukov <antohami@altlinux.org> 1.0.8-alt1
- Initial build for Sisyphus
