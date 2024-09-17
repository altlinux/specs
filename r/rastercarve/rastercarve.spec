%ifarch %ix86
%def_without check
%endif

Name:    rastercarve
Version: 1.0.8
Release: alt2

Summary: Generate G-code to engrave raster images
License: GPL-2.0
Group:   Engineering
URL:     https://github.com/built1n/rastercarve

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-dev
BuildRequires: python3-module-wheel python3-module-setuptools
BuildRequires: python3-module-opencv
BuildRequires: python3-module-numpy
BuildRequires: python3-module-tqdm
BuildRequires: liblapack

BuildArch: noarch

Source: %name-%version.tar
Patch: %name-%version-%release.patch

%description
%summary.

%prep
%setup
%patch -p1

%build
%pyproject_build

%install
%pyproject_install

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
%python3_sitelibdir/%name-%version.dist-info
%doc *.md

%changelog
* Tue Sep 17 2024 Anton Midyukov <antohami@altlinux.org> 1.0.8-alt2
- add patches from upstream
- disable check on %%ix86 (opencv is unsupported them)

* Mon Jun 14 2021 Anton Midyukov <antohami@altlinux.org> 1.0.8-alt1
- Initial build for Sisyphus
