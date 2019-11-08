%define oname collect-exceptions

Name: python3-module-%oname
Version: 0.0.5
Release: alt3

Summary: Python exception collector
License: BSD
Group: Development/Python3
Url: https://pypi.python.org/pypi/collect-exceptions/
# https://github.com/Yemsheng/collect-exceptions.git
BuildArch: noarch

Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3
BuildRequires: python-tools-2to3

%py3_provides collect_exceptions


%description
'collect-exceptions' is a python exception collector. It can collect
django and celery exception.

%prep
%setup

find ./ -type f -name '*.py' -exec 2to3 -w -n '{}' +

%build
%python3_build_debug

%install
%python3_install

%files
%doc *.md
%python3_sitelibdir/*


%changelog
* Fri Nov 08 2019 Andrey Bychkov <mrdrew@altlinux.org> 0.0.5-alt3
- disable python2

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 0.0.5-alt2.git20150209.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Fri Dec 08 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 0.0.5-alt2.git20150209
- Fixed build.

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.0.5-alt1.git20150209.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Mon Feb 09 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.0.5-alt1.git20150209
- Initial build for Sisyphus

