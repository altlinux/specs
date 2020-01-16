%define modulename dbfpy

Name: python3-module-%modulename
Version: 2.3.0
Release: alt2

Summary: Python module for accessing .dbf (xBase) files
License: Public domain
Group: Development/Python3
Url: http://dbfpy.sourceforge.net/
BuildArch: noarch

Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3
BuildRequires: python-tools-2to3


%description
dbfpy can read and write simple DBF-files. The DBF-format
was developed about 30 years ago and was used by a number
of simple database applications (dBase, Foxpro, Clipper, ...).
The basic datatypes numbers, short text, and dates are available.
Many different extensions have been used; dbfpy can read and write
only simple DBF-files.

%prep
%setup

sed -i '/length = None/s/^/# /' dbfpy/fields.py

find ./ -type f -name '*.py' -exec 2to3 -w -n '{}' +

%build
%python3_build

%install
%python3_install

%files
%doc README CHANGES
%python3_sitelibdir/%modulename/
%python3_sitelibdir/*.egg-info


%changelog
* Thu Jan 16 2020 Andrey Bychkov <mrdrew@altlinux.org> 2.3.0-alt2
- porting on python3

* Tue Sep 02 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.3.0-alt1
- Version 2.3.0

* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 2.2.5-alt1.1
- Rebuild with Python-2.7

* Wed Oct 27 2010 Egor Glukhov <kaman@altlinux.org> 2.2.5-alt1
- Initial build for Sisyphus

