%define        _unpackaged_files_terminate_build 1
%define        pypiname speaklater
%define        mname speaklater

Name:          python3-module-%pypiname
Version:       1.3
Release:       alt3
Summary:       Implements a lazy string for python useful for use with gettext
License:       BSD
Group:         Development/Python3
Url:           https://pypi.python.org/pypi/speaklater/
Vcs:           https://github.com/mitsuhiko/speaklater.git

BuildArch:     noarch
Source:        %name-%version.tar
Patch:         %name-%EVR.patch
BuildRequires(pre): rpm-build-pyproject
BuildRequires: python3(setuptools)
BuildRequires: python3(wheel)

%pyproject_runtimedeps_metadata
%pyproject_builddeps_build

%description
A module that provides lazy strings for translations. Basically you get
an object that appears to be a string but changes the value every time
the value is evaluated based on a callable you provide.

For example you can have a global lazy_gettext function that returns a
lazy string with the value of the current set language.

%prep
%setup
%autopatch -p1

%build
%pyproject_build

%install
%pyproject_install

%files
%doc README
%python3_sitelibdir/%{pypiname}.py
%python3_sitelibdir/%{mname}*/METADATA
%python3_sitelibdir/__pycache__

%changelog
* Tue Jan 30 2024 Pavel Skrylev <majioa@altlinux.org> 1.3-alt3
- * rollback 1.3 version in Sisyphus

* Mon Feb 10 2020 Andrey Bychkov <mrdrew@altlinux.org> 1.3-alt2
- Build for python2 disabled.

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 1.3-alt1.git20120701.1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 1.3-alt1.git20120701.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Tue Oct 21 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.3-alt1.git20120701
- Initial build for Sisyphus

