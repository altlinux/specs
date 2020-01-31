%define oname slacker

Name:       python3-module-%oname
Version:    0.6.8
Release:    alt2

Summary:    Slack API client
License:    ASLv2.0
Group:      Development/Python3
Url:        https://pypi.python.org/pypi/slacker

BuildArch:  noarch

# https://github.com/os/slacker.git
Source:     %name-%version.tar

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-requests python3-module-mock
BuildRequires: python3-module-tox

%py3_provides %oname
%py3_requires requests


%description
Slacker is a full-featured Python interface for the Slack API.

%prep
%setup

%build
%python3_build_debug

%install
%python3_install

%check
%__python3 setup.py test -v

%files
%doc *.rst
%python3_sitelibdir/*


%changelog
* Fri Jan 31 2020 Andrey Bychkov <mrdrew@altlinux.org> 0.6.8-alt2
- Build for python2 disabled.

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 0.6.8-alt1.git20150717.1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.6.8-alt1.git20150717.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Sat Jul 25 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.6.8-alt1.git20150717
- Initial build for Sisyphus

