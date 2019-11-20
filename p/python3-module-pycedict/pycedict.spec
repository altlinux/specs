%define oname pycedict

Name: python3-module-%oname
Version: 0.9.2
Release: alt2

Summary: A library for parsing CEDict and adding tone marks to pinyin
License: BSD
Group: Development/Python3
BuildArch: noarch
Url: https://pypi.python.org/pypi/pycedict/
# https://github.com/jdillworth/pycedict.git

Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3

%py3_provides cedict
# %%add3_python_req_skip cedict_parser pinyin


%description
A library made for working with CC-CEDICT (http://cc-cedict.org/wiki/ )
and pinyin.

%prep
%setup

%build
%python3_build_debug

%install
%python3_install

%check
%__python3 setup.py test
%__python3 tests.py -v

%files
%doc *.md
%python3_sitelibdir/*


%changelog
* Wed Nov 20 2019 Andrey Bychkov <mrdrew@altlinux.org> 0.9.2-alt2
- python2 disabled

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 0.9.2-alt1.git20170220.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Mon Dec 25 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 0.9.2-alt1.git20170220
- Updated to upstream version 0.9.2.

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.9.1-alt1.git20150113.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Tue Jan 13 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.9.1-alt1.git20150113
- Initial build for Sisyphus

