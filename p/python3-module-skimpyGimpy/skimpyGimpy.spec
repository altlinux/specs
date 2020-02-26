%define oname skimpyGimpy

%def_disable check

Name: python3-module-%oname
Version: 1.4
Release: alt3

Summary: Skimpy Gimpy Audio/visual Tools
License: BSD
Group: Development/Python3
Url: https://pypi.python.org/pypi/skimpyGimpy/
BuildArch: noarch

Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3
BuildRequires: python-tools-2to3


%description
Skimpy is a tool for generating HTML visual, PNG visual, and WAVE audio
representations for strings which people can understand but which web
robots and other computer programs will have difficulty understanding.
Skimpy is an example of a Captcha: an acronym for "Completely Automated
Public Turing test to tell Computers and Humans Apart".

%prep
%setup

find ./ -type f -name '*.py' -exec 2to3 -w -n '{}' +

%build
%python3_build_debug

%install
%python3_install

%check
%__python3 setup.py test

%files
%doc README.txt
%python3_sitelibdir/*


%changelog
* Wed Feb 26 2020 Andrey Bychkov <mrdrew@altlinux.org> 1.4-alt3
- Build for python2 disabled.

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 1.4-alt2.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Thu Dec 28 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 1.4-alt2
- Fixed build.

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 1.4-alt1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Fri Oct 24 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.4-alt1
- Initial build for Sisyphus

