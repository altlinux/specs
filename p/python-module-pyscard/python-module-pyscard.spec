%define rname pyscard

Name:           python-module-%rname
Version:        1.6.16
Release:        alt1
Summary:        A framework for building smart card aware applications in Python

Group:          Development/Python
Packager: 	Andrey Cherepanov <cas@altlinux.org>

# The entire source code is LGPLv2+ except for ClassLoader.py (Python),
# and Synchronization.py, Observer.py (CC-BY-SA 3.0), according to
# http://sourceforge.net/p/pyscard/code/619/

License:        LGPLv2+ and Python and CC-BY-SA
URL:            http://ludovicrousseau.blogspot.cz/2014/07/pyscard-unofficial-version-1616.html
Source0:        http://ludovic.rousseau.free.fr/softwares/pcsc-lite/%{rname}-%{version}.tar.gz

BuildRequires(pre): rpm-build-python
BuildRequires:  python-devel
BuildRequires:  python-module-distribute
BuildRequires:  libpcsclite-devel
BuildRequires:  swig >= 1.3.31

Requires:       pcsc-lite
Provides:	pyscard = %version-%release

%description
The pyscard smartcard library is a framework for building smart card
aware applications in Python. The smartcard module is built on top of
the PCSC API Python wrapper module.

%prep
%setup -q -n %rname-%version
# license file is CRLF terminated -- prevent a rpmlint warning
sed -i 's/\r//' LICENSE

%build
%python_build

%install
%python_install
chmod 755 %buildroot%python_sitelibdir/smartcard/scard/_scard.so

%files
%doc README LICENSE
%doc smartcard/doc/*
%doc smartcard/Examples
%python_sitelibdir/*

%changelog
* Tue Mar 17 2015 Andrey Cherepanov <cas@altlinux.org> 1.6.16-alt1
- Initial build in Sisyphus (ALT #30840)

