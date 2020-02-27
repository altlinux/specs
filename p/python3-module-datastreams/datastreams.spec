%define oname datastreams

Name: python3-module-%oname
Version: 0.2.6
Release: alt2

Summary: A module for managing data in streams
License: AGPLv3
Group: Development/Python3
Url: https://pypi.python.org/pypi/datastreams/

BuildArch: noarch

# https://github.com/csu/datastreams.git
Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3

%py3_provides %oname
%py3_requires pymongo wsgiref


%description
A module for managing data in streams.

%prep
%setup

sed -i 's|from datastreams|from .datastreams|' %oname/__init__.py

%build
%python3_build_debug

%install
%python3_install

%files
%doc *.md
%python3_sitelibdir/*


%changelog
* Thu Feb 27 2020 Andrey Bychkov <mrdrew@altlinux.org> 0.2.6-alt2
- Build for python2 disabled.

* Wed May 16 2018 Andrey Bychkov <mrdrew@altlinux.org> 0.2.6-alt1.git20150113.1.2
- (NMU) rebuild with python3.6

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.2.6-alt1.git20150113.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 0.2.6-alt1.git20150113.1
- NMU: Use buildreq for BR.

* Wed Jan 14 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.2.6-alt1.git20150113
- Initial build for Sisyphus

