%define oname Alquimia

Name: python3-module-%oname
Version: 0.7.1
Release: alt2

Summary: An API to work with JSON schemas in SQLAlchemy
License: LGPLv3+
Group: Development/Python3
Url: https://pypi.python.org/pypi/Alquimia/
BuildArch: noarch

# https://github.com/dutradda/alquimia.git
Source: %name-%version.tar
Patch0: port-on-python3.patch

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-pytest python-tools-2to3
BuildRequires: python3-module-jsonschema python3-module-SQLAlchemy

%py3_provides alquimia
%py3_requires jsonschema sqlalchemy


%description
An API to work with JSON schemas in SQLAlchemy.

%prep
%setup
%patch0 -p1

find -type f -name '*.py' -exec 2to3 -w -n '{}' +

%build
%python3_build_debug

%install
%python3_install

%check
%__python3 setup.py test -v

%files
%doc *.md docs/*.rst docs/example.py
%python3_sitelibdir/*


%changelog
* Tue Jan 14 2020 Andrey Bychkov <mrdrew@altlinux.org> 0.7.1-alt2
- porting on python3

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 0.7.1-alt1.git20150718.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Wed Jul 29 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.7.1-alt1.git20150718
- Initial build for Sisyphus

