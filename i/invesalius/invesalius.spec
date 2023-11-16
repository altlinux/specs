%define _unpackaged_files_terminate_build 1
%filter_from_requires /python3(invesalius\(\..*\)\?)/d

Name: invesalius
Version: 3.1.99998
Release: alt1

Summary: InVesalius generates 3D reconstructions of CT and MRI images.
License: GPLv2
Group: Sciences/Medicine

URL: https://invesalius.github.io/
VCS: https://github.com/invesalius/invesalius3.git

Source0: %name-%version.tar
Patch0: upstream-python3.11-pywx4.2.patch
Patch1: set-python-lang-level.patch

BuildRequires: gcc gcc-c++
BuildRequires: /usr/bin/desktop-file-install /usr/bin/convert
BuildRequires: python3-devel
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-Cython
BuildRequires: libnumpy-py3-devel
BuildRequires: libgomp-devel

Requires: python3-module-Pillow
Requires: python3-module-numpy
Requires: python3-module-pypubsub
Requires: python3-module-h5py
Requires: python3-module-imageio
Requires: python3-module-nibabel
Requires: python3-module-psutil
Requires: python3-module-serial
Requires: python3-module-gdcm
Requires: python3-module-scikit-image
Requires: python3-module-scipy
Requires: python3-module-wx
Requires: python3-module-pyacvd
Requires: vtk-python3

%add_python3_req_skip torch
# Packages are no longer supported and are getting moved to optinal requirements
%add_python3_req_skip Theano plaidml-keras

%description
InVesalius generates 3D medical imaging reconstructions based on
a sequence of 2D DICOM files acquired with CT or MRI equipments.
Provides DICOM-support, 2D image segmentation tools, and more.

%prep
%setup
%patch0 -p1
%patch1 -p1

sed -i 's|#!/usr/bin/python|#!/usr/bin/python3|' invesalius/expanduser.py

%build

# build plugins
python3 setup.py build_ext --inplace

%install
%define instdir %_datadir/%name

# install invesalius
mkdir -p %buildroot%instdir
for dir in icons invesalius locale presets samples; do
    cp -far $dir %buildroot%instdir
done

# install plugins
mkdir -p %buildroot%_libdir/%name
cp -far invesalius_cy/*.so %buildroot%_libdir/%name
mkdir -p %buildroot%instdir/%{name}_cy
cp -far invesalius_cy/*.py %buildroot%_libdir/%name/%{name}_cy

# add app
cp -far app.py %buildroot%instdir

# copy icon
mkdir -p %buildroot/{%_miconsdir,%_niconsdir,%_liconsdir}
convert -resize 16x16 icons/%name.ico %buildroot%_miconsdir/%name.png
convert -resize 32x32 icons/%name.ico %buildroot%_niconsdir/%name.png
convert -resize 64x64 icons/%name.ico %buildroot%_liconsdir/%name.png

# launcher
mkdir -p %buildroot%_bindir
cat > %buildroot%_bindir/%name << EOF
#!/bin/sh
export PYTHONPATH=\$PYTHONPATH:"%instdir"
export INVESALIUS_LIBRARY_PATH="%instdir"
cd \$INVESALIUS_LIBRARY_PATH
python3 app.py "\$@"
EOF
chmod +x %buildroot%_bindir/%name

# .desktop
install -dm 755 %buildroot/%_datadir/applications
cat > %name.desktop << EOF
[Desktop Entry]
Name=InVesalius
Type=Application
Terminal=false
Comment=Medical Imaging Public Software
Exec=%name
Icon=%name
Categories=Graphics;Science;
EOF
desktop-file-install --dir=%buildroot%_datadir/applications %name.desktop --vendor=""

%files
%doc LICENSE.txt README.md docs/user_guide_en.pdf
%_bindir/%name
%_datadir/%name
%_libdir/%name
%_datadir/applications/%name.desktop
%_miconsdir/%name.png
%_niconsdir/%name.png
%_liconsdir/%name.png

%changelog
* Fri Oct 20 2023 Elizaveta Morozova <morozovaes@altlinux.org> 3.1.99998-alt1
- Initial build for ALT.

