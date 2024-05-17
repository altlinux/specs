Name: python3-module-jinja2
Version: 3.1.4
Release: alt1

Summary: The new and improved version of a small but fast template engine
License: BSD
Group: Development/Python3
Url: https://pypi.org/project/Jinja2/

# https://github.com/mitsuhiko/jinja2.git
Source0: %name-%version.tar
Source1: pyproject_deps.json

BuildArch: noarch
BuildRequires(pre): rpm-build-pyproject
BuildRequires: python3(pytest)
%pyproject_builddeps_build
%pyproject_builddeps_metadata

%description
Jinja2 is a template engine written in pure Python. It provides a Django
inspired non-XML syntax but supports inline expressions and an optional
sandboxed environment.

%prep
%setup
%pyproject_deps_resync_build
%pyproject_deps_resync_metadata

%build
%pyproject_build

%install
%pyproject_install

%check
%pyproject_run_pytest tests

%files
%python3_sitelibdir/jinja2
%python3_sitelibdir/jinja2-%version.dist-info

%changelog
* Fri May 17 2024 Sergey Bolshakov <sbolshakov@altlinux.org> 3.1.4-alt1
- 3.1.4 released

* Fri Jan 19 2024 Sergey Bolshakov <sbolshakov@altlinux.ru> 3.1.3-alt1
- 3.1.3 released

* Thu Jul 14 2022 Sergey Bolshakov <sbolshakov@altlinux.ru> 3.1.2-alt1
- 3.1.2 released

* Tue May 17 2022 Sergey Bolshakov <sbolshakov@altlinux.ru> 3.1.1-alt1
- 3.1.1 released

* Tue Feb 08 2022 Sergey Bolshakov <sbolshakov@altlinux.ru> 3.0.3-alt1
- 3.0.3 released

* Mon Jun 21 2021 Sergey Bolshakov <sbolshakov@altlinux.ru> 3.0.1-alt1
- 3.0.1 released

* Tue Mar 16 2021 Sergey Bolshakov <sbolshakov@altlinux.ru> 2.11.3-alt1
- 2.11.3 released

* Mon Jul 06 2020 Sergey Bolshakov <sbolshakov@altlinux.ru> 2.11.2-alt1
- 2.11.2 released

* Fri Nov 29 2019 Sergey Bolshakov <sbolshakov@altlinux.ru> 2.10.3-alt1
- 2.10.3 released

* Mon Sep 09 2019 Anton Farygin <rider@altlinux.ru> 2.10.1-alt1
- 2.10.1 (Fixes: CVE-2019-10906)

* Thu Mar 22 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 2.10-alt1
- Updated to upstream version 2.10.

* Sat Jan 14 2017 Michael Shigorin <mike@altlinux.org> 2.9-alt1.dev.git20150726.1.1.1.1
- BOOTSTRAP: introduced doc knob (avoid sphinx)

* Mon Apr 11 2016 Ivan Zakharyaschev <imz@altlinux.org> 2.9-alt1.dev.git20150726.1.1.1
- (NMU) rebuild with rpm-build-python3-0.1.10 (for new-style python3(*) reqs)
  and with python3-3.5 (for byte-compilation).

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 2.9-alt1.dev.git20150726.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 2.9-alt1.dev.git20150726.1
- NMU: Use buildreq for BR.

* Thu Jul 30 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.9-alt1.dev.git20150726
- Version 2.9.dev

* Fri Jul 11 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.8-alt2.git20140610
- New snapshot

* Tue Jan 14 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.8-alt2.git20140110
- New snapshot

* Fri Nov 29 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.8-alt2.git20130807
- Added requirement on tests for python3-module-%oname

* Tue Sep 17 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.8-alt1.git20130807
- Version 2.8

* Wed Mar 27 2013 Aleksey Avdeev <solo@altlinux.ru> 2.7-alt1.git20120916
- New snapshot

* Fri Apr 13 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.7-alt1.git20120313
- New snapshot
- Added module for Python 3

* Fri Dec 23 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.7-alt1.git20111215
- Version 2.7

* Fri Dec 09 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.6-alt1
- Version 2.6

* Fri Nov 25 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.5.5-alt2
- Enabled docs

* Fri Oct 21 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 2.5.5-alt1.1
- Rebuild with Python-2.7 (bootstraping without docs)

* Tue Nov 23 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.5.5-alt1
- Version 2.5.5

* Mon Aug 02 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.5-alt2
- Added requirement on tests package

* Mon Aug 02 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.5-alt1
- Version 2.5
- Extracted tests into separate package
- Added pickles

* Thu Nov 12 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.2.1-alt1.2
- Enable building of documentation

* Thu Nov 12 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.2.1-alt1.1
- Rebuilt with python 2.6 (bootstrap)

* Thu Sep 17 2009 Andrey Rahmatullin <wrar@altlinux.ru> 2.2.1-alt1
- 2.2.1
- enable building of documentation
- build as noarch

* Mon May 04 2009 Andrey Rahmatullin <wrar@altlinux.ru> 2.1.1-alt1
- initial build
