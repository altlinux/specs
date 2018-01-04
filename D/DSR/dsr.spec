Summary: DSR - A program for modelling of disordered solvents with SHELXL
Name: DSR
Version: 205
Release: alt1
BuildArch: noarch
URL: https://www.xs3.uni-freiburg.de/research/dsr
License: Beerware
Group: Sciences/Chemistry
Source: %name-%version.tar.gz
Source1: changelog.txt

%add_python_compile_include %_datadir/%name

PreReq: xclip %py_requires networkx

%description
This program consists of a text database with fragments of molecules and
the DSR program. It acts as a preprocessor for SHELXL .res files. The user
inserts a special command in the SHELXL .res file and the DSR program reads
this information to put a molecule or fragment with the desired atoms on the
position of the target atoms specified by the user. Bond restraints are applied
from the database to the molecule.
Development is on GitHub: https://github.com/dkratzert/dsr

%prep
%setup -q
cp -a %SOURCE1 .

%build
cat > %name.sh << EOF
#!/bin/sh
export DSR_DIR=%_datadir/DSR
PYTHON_EXE=\$(which python)
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

install -m 755 %name.sh %buildroot%_bindir/dsr
install -m 644 *.py %buildroot%_datadir/%name
install -m 644 dsr_db.txt %buildroot%_datadir/%name
install -m 644 manuals/DSR-manual.pdf %buildroot%_datadir/%name/manuals
install -m 644 example/* %buildroot%_datadir/%name/example

%files
%doc README changelog.txt
%_bindir/dsr
%_datadir/%name

%changelog
* Thu Jan 04 2018 Denis G. Samsonenko <ogion@altlinux.org> 205-alt1
- initial build for ALT
