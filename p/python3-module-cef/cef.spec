%define oname cef

Name: python3-module-%oname
Version: 0.5
Release: alt3

Summary: Module that emits CEF logs
License: MPL
Group: Development/Python3
Url: https://pypi.python.org/pypi/cef
BuildArch: noarch

# https://github.com/mozilla/cef.git
Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-pytest python-tools-2to3

%py3_provides %oname


%description
Most Mozilla Services applications need to generate CEF logs. A CEF Log
is a formatted log that can be used by ArcSight, a central application
used by the infrasec team to manage application security.

The cef module provide a log_cef function that can be used to emit CEF
logs.

%prep
%setup

find ./ -type f -name '*.py' -exec 2to3 -w -n '{}' +

%build
%python3_build_debug

%install
%python3_install

%check
%if 0
py.test3
%endif

%files
%doc *.txt
%python3_sitelibdir/*


%changelog
* Mon Jan 13 2020 Andrey Bychkov <mrdrew@altlinux.org> 0.5-alt3
- porting on python3

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 0.5-alt2.git20121017.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Mon Mar 02 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.5-alt2.git20121017
- Fixed build

* Wed Oct 29 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.5-alt1.git20121017
- Initial build for Sisyphus

