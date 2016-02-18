%define modulename qserve

%def_with python3

Name: python-module-qserve
Version: 0.2.8
Release: alt1.1

Summary: job queue server used in mwlib

Group: Development/Python

License: BSD
Url: https://github.com/pediapress/qserve

Source: %name-%version.tar

#BuildPreReq: rpm-build-python
%if_with python3
BuildRequires(pre): rpm-build-python3
#BuildPreReq: python3-devel python-tools-2to3
%endif

BuildArch: noarch

%setup_python_module %modulename

# Automatically added by buildreq on Thu Jan 28 2016 (-bi)
# optimized out: python-base python-modules python-modules-compiler python-modules-email python-modules-encodings python-modules-logging python3 python3-base
BuildRequires: python-devel python-tools-2to3 rpm-build-python3 time

%description
job queue server used in mwlib

%package -n python3-module-%modulename
Summary: job queue server used in mwlib
Group: Development/Python3

%description -n python3-module-%modulename
job queue server used in mwlib

%prep
%setup

%if_with python3
cp -fR . ../python3
find ../python3 -type f -name '*.py' -exec 2to3 -w -n '{}' +
%endif

%build
%python_build

%if_with python3
pushd ../python3
%python3_build
popd
%endif

%install
%python_install

%if_with python3
pushd ../python3
%python3_install
popd
%endif

%files
%python_sitelibdir/qs*

%if_with python3
%files -n python3-module-%modulename
%python3_sitelibdir/qs*
%endif

%changelog
* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 0.2.8-alt1.1
- NMU: Use buildreq for BR.

* Tue Aug 26 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.2.8-alt1
- Version 0.2.8
- Added module for Python 3

* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.1.1-alt1.1
- Rebuild with Python-2.7

* Tue Oct 18 2011 Michael A. Kangin <prividen@altlinux.org> 0.1.1-alt1
- initial build for ALT Linux Sisyphus

