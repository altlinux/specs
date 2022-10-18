%define oname PasteDeploy
%def_without bootstrap
%def_with check

Name: python3-module-%oname
Version: 3.0.1
Release: alt1
Epoch: 1

Summary: Load, configure, and compose WSGI applications and servers

License: MIT/X11
Group: Development/Python3
BuildArch: noarch
Url: https://github.com/Pylons/pastedeploy

Source: %name-%version.tar

%py3_provides %oname
%py3_requires Paste
%if_with bootstrap
%add_python3_req_skip paste.script.templates
%endif

BuildRequires(pre): rpm-build-python3

BuildRequires: python3-module-setuptools
BuildRequires: python3-module-wheel

%if_with check
BuildRequires: python3-module-pytest-cov
%endif

%description
This tool provides code to load WSGI applications and servers from
URIs; these URIs can refer to Python Eggs for INI-style configuration
files. Paste Script provides commands to serve applications based on
this configuration file.

%prep
%setup

%build
%pyproject_build

%install
%pyproject_install

%check
%tox_check_pyproject

%files
%python3_sitelibdir/paste/deploy
%python3_sitelibdir/%oname-%version.dist-info

%changelog
* Tue Oct 18 2022 Grigory Ustinov <grenka@altlinux.org> 1:3.0.1-alt1
- Automatically updated to 3.0.1.

* Mon Oct 17 2022 Grigory Ustinov <grenka@altlinux.org> 1:3.0-alt1
- Automatically updated to 3.0.

* Sat Oct 15 2022 Grigory Ustinov <grenka@altlinux.org> 1:2.1.1-alt1
- Automatically updated to 2.1.1.
- Build with check.

* Tue May 25 2021 Anton Midyukov <antohami@altlinux.org> 1:2.0.1-alt2
- build python3 module only

* Wed Feb 06 2019 Alexey Shabalin <shaba@altlinux.org> 1:2.0.1-alt1
- 2.0.1

* Tue May 29 2018 Andrey Bychkov <mrdrew@altlinux.org> 1:1.5.2-alt2.2
- fix requires(2)

* Mon May 28 2018 Andrey Bychkov <mrdrew@altlinux.org> 1:1.5.2-alt2.1
- fix requires

* Wed May 16 2018 Andrey Bychkov <mrdrew@altlinux.org> 1:1.5.2-alt2
- rebuild with python3.6

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 1:1.5.2-alt1.hg20131227.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Fri Jan 29 2016 Mikhail Efremov <sem@altlinux.org> 1:1.5.2-alt1.hg20131227.1
- NMU: Use buildreq for BR.

* Mon Jul 14 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1:1.5.2-alt1.hg20131227
- Version 1.5.2

* Fri Mar 22 2013 Aleksey Avdeev <solo@altlinux.ru> 1:1.5.1-alt1.hg20120916.1
- Rebuild with Python-3.3

* Sat Sep 22 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1:1.5.1-alt1.hg20120916
- New snapshot

* Fri May 04 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1:1.5.1-alt1.hg20120315
- New snapshot
- Added module for Python 3

* Thu Dec 08 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1:1.5.1-alt1.hg20110815
- Version 1.5.1

* Mon Oct 24 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 1:1.3.4-alt1.hg20101028.1.1
- Rebuild with Python-2.7

* Sun Jun 26 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1:1.3.4-alt1.hg20101028.1
- Added %%py_provides PasteDeploy

* Wed Nov 24 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1:1.3.4-alt1.hg20101028
- New snapshot

* Thu Nov 19 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.3.4-alt1.svn20090714.2
- Rebuilt with python 2.6

* Tue Sep 29 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.3.4-alt1.svn20090714.1
- Version 1.3.4

* Sun Apr 05 2009 Denis Klimov <zver@altlinux.org> 1.3.3-alt1
- Initial build for ALT Linux

