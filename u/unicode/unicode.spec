Name: unicode
Version: 3.1
Release: alt1

Summary: display unicode character properties
License: GPLv3
Group: Text tools
Url: http://kassiopeia.juls.savba.sk/~garabik/software/unicode.html
VCS: https://github.com/garabik/unicode
BuildArch: noarch

Source0: %name-%version.tar

BuildRequires(pre): rpm-build-python3

%description
unicode is a simple command line utility that displays
properties for a given unicode character, or searches
unicode database for a given name.

%prep
%setup

%build
%python3_build

%install
%python3_install

%files
%doc README* COPYING
%_bindir/%name
%_bindir/paracode
%python3_sitelibdir/%name-%version-py%_python3_version.egg-info

%changelog
* Tue Jun 04 2024 Grigory Ustinov <grenka@altlinux.org> 3.1-alt1
- Build new version.

* Mon Jun 19 2023 Grigory Ustinov <grenka@altlinux.org> 2.9-alt1
- Build new version (Closes: #46493).

* Wed Nov 27 2019 Andrey Bychkov <mrdrew@altlinux.org> 2.7-alt1
- Version updated to 2.7
- porting on python3

* Sat Oct 22 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.9.4-alt1.1
- Rebuild with Python-2.7

* Sat Mar 27 2010 Andrey Rahmatullin <wrar@altlinux.ru> 0.9.4-alt1
- 0.9.4

* Thu Nov 12 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.9.2-alt1.1
- Rebuilt with python 2.6

* Wed Jul 01 2009 Andrey Rahmatullin <wrar@altlinux.ru> 0.9.2-alt1
- initial build
