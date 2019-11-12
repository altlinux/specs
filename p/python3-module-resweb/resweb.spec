%define oname resweb

Name: python3-module-%oname
Version: 0.1.7
Release: alt3

Summary: Pyres web interface
License: MIT
Group: Development/Python3
Url: https://pypi.python.org/pypi/resweb/
# https://github.com/Pyres/resweb.git
BuildArch: noarch

Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-pyres python3-module-flask
BuildRequires: python3-module-setproctitle python3-module-simplejson
BuildRequires: python-tools-2to3

%py3_provides %oname


%description
Resweb originally started as part of the pyres project. However, I
realized that for many reasons, both it and pyres would benefit from
being their own projects. Hopefully this will help the release schedule
of both pyres and resweb.

%prep
%setup

find ./ -type f -name '*.py' -exec 2to3 -w -n '{}' +

%build
%python3_build_debug

%install
%python3_install

%check
python3 setup.py test

%files
%doc *.md
%_bindir/*
%python3_sitelibdir/*


%changelog
* Tue Nov 12 2019 Andrey Bychkov <mrdrew@altlinux.org> 0.1.7-alt3
- disable python2

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 0.1.7-alt2.git20130813.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Wed Dec 27 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 0.1.7-alt2.git20130813
- Fixed build dependencies.

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.1.7-alt1.git20130813.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 0.1.7-alt1.git20130813.1
- NMU: Use buildreq for BR.

* Fri Nov 21 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1.7-alt1.git20130813
- Initial build for Sisyphus

