%define oname tldextract

%def_without check

Name: python3-module-%oname
Version: 3.3.0
Release: alt1

Summary: Accurately separate the TLD from the registered domain and subdomains of a URL

License: BSD
Group: Development/Python3
Url: https://pypi.python.org/pypi/tldextract/

# https://github.com/john-kurkowski/tldextract.git
Source: %name-%version.tar

BuildArch: noarch

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-setuptools_scm

%py3_provides %oname

BuildRequires: python3-module-pytest

Conflicts: python-module-%oname
Obsoletes: python-module-%oname

%description
tldextract accurately separates the gTLD or ccTLD (generic or country
code top-level domain) from the registered domain and subdomains of a
URL, using the Public Suffix List.

%prep
%setup

%build
export SETUPTOOLS_SCM_PRETEND_VERSION=%version
%python3_build

%install
export SETUPTOOLS_SCM_PRETEND_VERSION=%version
%python3_install

%check
export SETUPTOOLS_SCM_PRETEND_VERSION=%version
python3 setup.py test

%files
%doc *.md
%_bindir/*
%python3_sitelibdir/%oname
%python3_sitelibdir/*.egg-info

%changelog
* Sat May 28 2022 Grigory Ustinov <grenka@altlinux.org> 3.3.0-alt1
- Automatically updated to 3.3.0.

* Fri Jul 23 2021 Grigory Ustinov <grenka@altlinux.org> 1.5.1-alt1.git20141205.3
- Drop python2 support.

* Wed May 16 2018 Andrey Bychkov <mrdrew@altlinux.org> 1.5.1-alt1.git20141205.1.2
- (NMU) rebuild with python3.6

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 1.5.1-alt1.git20141205.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 1.5.1-alt1.git20141205.1
- NMU: Use buildreq for BR.

* Tue Jan 20 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.5.1-alt1.git20141205
- Initial build for Sisyphus

