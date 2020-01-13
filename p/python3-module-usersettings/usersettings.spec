%define oname usersettings

Name: python3-module-%oname
Version: 1.0.7
Release: alt3

Summary: Portable Local Settings Storage
License: BSD
Group: Development/Python3
Url: https://pypi.python.org/pypi/usersettings/
BuildArch: noarch

# https://github.com/glvnst/usersettings.git
Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-appdirs
BuildRequires: python-tools-2to3

%py3_provides %oname
%py3_requires appdirs


%description
"usersettings" is a python module for easily managing persistent
settings using an editable format and stored in an OS-appropriate
location (windows/os x/linux are supported).

%prep
%setup

find ./ -type f -name '*.py' -exec 2to3 -w -n '{}' +

%build
%python3_build_debug

%install
%python3_install

%check
%if 0
%__python3 setup.py test
export PYTHONPATH=$PWD
%__python3 examples/usersettings-example.py
%endif

%files
%doc *.md docs/* examples
%python3_sitelibdir/*


%changelog
* Mon Jan 13 2020 Andrey Bychkov <mrdrew@altlinux.org> 1.0.7-alt3
- porting on python3

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 1.0.7-alt2.git20130531.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Wed Mar 11 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.7-alt2.git20130531
- Fixed build

* Sun Jan 18 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.7-alt1.git20130531
- Initial build for Sisyphus

