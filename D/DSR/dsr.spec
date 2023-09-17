Name: DSR
Version: 241
Release: alt1

Summary: DSR - A program for modelling of disordered solvents with SHELXL
License: Beerware
Group: Sciences/Chemistry
URL: https://dkratzert.de/dsr.html

BuildArch: noarch

Source: %name-version-%version.zip
Source1: dsrchangelog.html

%add_python3_path %_datadir/%name
%add_findprov_skiplist %_datadir/%name/*

BuildRequires(pre): rpm-build-python3
#BuildRequires: xclip
BuildRequires: /usr/bin/unzip

%description
This program consists of a text database with fragments of molecules and
the DSR program. It acts as a preprocessor for SHELXL .res files. The user
inserts a special command in the SHELXL .res file and the DSR program reads
this information to put a molecule or fragment with the desired atoms on the
position of the target atoms specified by the user. Bond restraints are applied
from the database to the molecule.
Development is on GitHub: https://github.com/dkratzert/dsr

%prep
%setup -n %name-version-%version
cp -a %SOURCE1 .
cd src/dsr_shelx
sed -i 's|#!.*python|&3|' $(find ./ -name '*.py')
sed -i 's|# /usr/bin/env python|#!/usr/bin/env python3|' $(find ./ -name '*.py')

%build
cat > %name.sh << EOF
#!/bin/sh
export DSR_DIR=%_datadir/DSR
PYTHON_EXE=%__python3
if [ \$# -eq 0 ]; then
    \$PYTHON_EXE \$DSR_DIR/dsr.py --help
else
    \$PYTHON_EXE \$DSR_DIR/dsr.py \$*
fi
EOF

%install
mkdir -p %buildroot%_bindir
mkdir -p %buildroot%_datadir/%name
mkdir -p %buildroot%_datadir/%name/manuals
mkdir -p %buildroot%_datadir/%name/example
mkdir -p %buildroot%_datadir/%name/fit

install -m 755 %name.sh %buildroot%_bindir/dsr
install -m 644 src/dsr_shelx/*.py %buildroot%_datadir/%name
install -m 644 src/dsr_shelx/dsr_db.txt %buildroot%_datadir/%name
install -m 644 src/dsr_shelx/olex_dsr_db.txt %buildroot%_datadir/%name
install -m 644 manuals/DSR-manual.pdf %buildroot%_datadir/%name/manuals
install -m 644 example/* %buildroot%_datadir/%name/example
cp -R src/dsr_shelx/fit %buildroot%_datadir/%name

%files
%doc README dsrchangelog.html
%_bindir/dsr
%_datadir/%name

%changelog
* Sun Sep 17 2023 Denis G. Samsonenko <ogion@altlinux.org> 241-alt1
- new version

* Sat Oct 16 2021 Denis G. Samsonenko <ogion@altlinux.org> 235-alt1
- new version
- URL changed

* Fri Sep 24 2021 Denis G. Samsonenko <ogion@altlinux.org> 234-alt1
- new version

* Fri Jul 09 2021 Denis G. Samsonenko <ogion@altlinux.org> 233-alt3
- final fix #39171

* Wed Jul 07 2021 Denis G. Samsonenko <ogion@altlinux.org> 233-alt2
- build with python3 (fix #39171)

* Fri Apr 30 2021 Denis G. Samsonenko <ogion@altlinux.org> 233-alt1
- new version

* Mon Nov 02 2020 Denis G. Samsonenko <ogion@altlinux.org> 232-alt2
- back to use of internal networkx

* Thu Apr 02 2020 Denis G. Samsonenko <ogion@altlinux.org> 232-alt1
- new version

* Sun Jul 14 2019 Denis G. Samsonenko <ogion@altlinux.org> 226-alt2
- exclude networkx and mpmath from package

* Sun Jul 14 2019 Denis G. Samsonenko <ogion@altlinux.org> 226-alt1
- new version

* Sun Jan 20 2019 Denis G. Samsonenko <ogion@altlinux.org> 219-alt1
- new version

* Thu Jan 04 2018 Denis G. Samsonenko <ogion@altlinux.org> 205-alt1
- initial build for ALT
