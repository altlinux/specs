Name:       DoThings
Version:    0.2
Release:    alt2

Summary:    Simple To-Do-List in Termial
License:    BSD
Group:      Toys
Url:        https://pypi.python.org/pypi/DoThings/

BuildArch:  noarch

# https://github.com/MarzinZ/things.git
Source: %name-%version.tar
Patch0: port-on-python3.patch

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-docopt python-tools-2to3

%py3_provides things
%py3_requires docopt


%description
An easy to-do-list in Terminal.

%prep
%setup
%patch0 -p1

find -type f -name '*.py' -exec 2to3 -w -n '{}' +

%build
%python3_build_debug

%install
%python3_install

%check
%__python3 setup.py test
export PATH=$PATH:%buildroot%_bindir
export PYTHONPATH=%buildroot%python3_sitelibdir
things "test"
things all
things done 1
things all

%files
%doc *.md example.png
%_bindir/*
%python3_sitelibdir/*


%changelog
* Thu Jan 30 2020 Andrey Bychkov <mrdrew@altlinux.org> 0.2-alt2
- Porting on Python3.

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 0.2-alt1.git20150320.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Fri Mar 20 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.2-alt1.git20150320
- Initial build for Sisyphus

