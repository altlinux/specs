%define rname pyscard

Name:       python3-module-%rname
Version:    2.0.5
Release:    alt1

Summary:    A framework for building smart card aware applications in Python
License:    LGPLv2+ and Python and CC-BY-SA
Group:      Development/Python3
URL:        https://sourceforge.net/projects/pyscard/
Packager:   Andrey Cherepanov <cas@altlinux.org>

Source0:    %rname-%version.tar

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-wheel

BuildRequires:  python3-module-Pyro4
BuildRequires:  libpcsclite-devel
BuildRequires:  swig >= 1.3.31

Requires:   pcsc-lite
Provides:   pyscard = %version-%release

%description
The pyscard smartcard library is a framework for building smart card
aware applications in Python. The smartcard module is built on top of
the PCSC API Python wrapper module.

%prep
%setup -q -n %rname-%version

# license file is CRLF terminated -- prevent a rpmlint warning
subst 's/\r//' LICENSE
# Adapt to use Pyro4
subst 's/Pyro\./Pyro4./g' smartcard/pyro/PyroReader.py

# fix import of bsddb
sed -i 's|_bsddb|bsddb3._pybsddb|' smartcard/CardNames.py
sed -i 's|from bsddb import|from bsddb3 import|' smartcard/CardNames.py

%build
%pyproject_build

%install
%pyproject_install
# chmod 755 %buildroot%python3_sitelibdir/smartcard/scard/_scard.so

%files
%doc README.md LICENSE
%doc smartcard/doc/*
%doc smartcard/Examples
%python3_sitelibdir/*


%changelog
* Sat Feb 25 2023 Anton Zhukharev <ancieg@altlinux.org> 2.0.5-alt1
- 1.9.9 -> 2.0.5 (closes: #44926).
- Modernize building.

* Wed Feb 19 2020 Andrey Bychkov <mrdrew@altlinux.org> 1.9.9-alt2
- Porting on python3 (without wx support).

* Sat Aug 10 2019 Andrey Cherepanov <cas@altlinux.org> 1.9.9-alt1
- New version.

* Thu Mar 28 2019 Andrey Cherepanov <cas@altlinux.org> 1.9.8-alt1
- New version.

* Thu Jun 21 2018 Andrey Cherepanov <cas@altlinux.org> 1.9.7-alt1
- New version.

* Tue Aug 22 2017 Andrey Cherepanov <cas@altlinux.org> 1.9.6-alt1
- New version

* Sun Feb 19 2017 Andrey Cherepanov <cas@altlinux.org> 1.9.5-alt1
- new version 1.9.5

* Thu Jun 09 2016 Andrey Cherepanov <cas@altlinux.org> 1.9.4-alt1
- New version
- Add watch file
- Support Pyro4 Python module

* Tue Mar 17 2015 Andrey Cherepanov <cas@altlinux.org> 1.6.16-alt1
- Initial build in Sisyphus (ALT #30840)

