%define oname bcdoc

Name:       python3-module-%oname
Version:    0.16.0
Release:    alt4

Summary:    ReST document generation tools for botocore
License:    ASLv2.0
Group:      Development/Python
Url:        https://pypi.python.org/pypi/bcdoc/

BuildArch:  noarch

# https://github.com/boto/bcdoc.git
# branch: develop
Source:     %name-%version.tar

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-six python3-module-docutils
BuildRequires: python3-module-pytest

%py3_provides %oname


%description
Tools to help document botocore-based projects.

%prep
%setup

%build
%python3_build_debug

%install
%python3_install

%check
%__python3 setup.py test
py.test3

%files
%doc *.rst
%python3_sitelibdir/*


%changelog
* Fri Jan 31 2020 Andrey Bychkov <mrdrew@altlinux.org> 0.16.0-alt4
- Build for python2 disabled.

* Thu Feb 08 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 0.16.0-alt3.git20150617
- Updated build dependencies.

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 0.16.0-alt2.git20150617.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Mon Dec 04 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 0.16.0-alt2.git20150617
- Fixed build.

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.16.0-alt1.git20150617.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Sat Aug 08 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.16.0-alt1.git20150617
- Version 0.16.0

* Tue Feb 24 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.13.0-alt1.git20150223
- Version 0.13.0

* Wed Nov 12 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.12.2-alt1.git20140304
- Initial build for Sisyphus

