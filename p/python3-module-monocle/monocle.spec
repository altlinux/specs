%define _unpackaged_files_terminate_build 1

%define oname monocle

Name: python3-module-%oname
Version: 0.40
Release: alt1

Summary: An async programming framework with a blocking look-alike syntax
License: MIT
Group: Development/Python3
Url: https://pypi.python.org/pypi/monocle/
BuildArch: noarch

# https://github.com/saucelabs/monocle.git
Source0: %name-%version.tar
Patch0: port-on-python3.patch

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-twisted-core-test python3-module-tornado
BuildRequires: python3-module-nose python3-module-OpenSSL
BuildRequires: python3-module-service-identity
BuildRequires: python-tools-2to3

%py3_provides %oname
%py3_requires twisted.python tornado logging multiprocessing
%py3_requires service_identity


%description
monocle straightens out event-driven code using Python's generators. It
aims to be portable between event-driven I/O frameworks, and currently
supports Twisted and Tornado.

%prep
%setup
%patch0 -p1

find ./ -type f -name '*.py' -exec 2to3 -w -n '{}' +

%build
%python3_build_debug

%install
%python3_install

%check
%if 0
%__python3 setup.py test
%endif

%files
%doc PKG-INFO
%python3_sitelibdir/*


%changelog
* Mon Jan 20 2020 Andrey Bychkov <mrdrew@altlinux.org> 0.40-alt1
- Version updated to 0.40
- porting on python3.

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 0.38-alt1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Tue Jan 17 2017 Igor Vlasenko <viy@altlinux.ru> 0.38-alt1
- automated PyPI update

* Tue Mar 24 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.29-alt1.git20150323
- Initial build for Sisyphus

