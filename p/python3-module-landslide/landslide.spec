%define oname landslide

%def_with check

Name: python3-module-%oname
Version: 2.0.0
Release: alt1

Summary: Lightweight markup language-based html5 slideshow generator

License: Apache-2.0
Group: Development/Python3
URL: https://pypi.org/project/landslide
VCS: https://github.com/adamzap/landslide

BuildArch: noarch

Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3
BuildRequires: python3(setuptools)
BuildRequires: python3(wheel)

%if_with check
BuildRequires: python3(docutils)
BuildRequires: python3(jinja2)
BuildRequires: python3(markdown)
BuildRequires: python3(pygments)
BuildRequires: python3(six)
BuildRequires: python3(tox)
%endif

%py3_requires markdown


%description
Landslide takes your Markdown, ReST, or Textile file(s) and generates
fancy HTML5 slideshow.

%prep
%setup

%build
%pyproject_build

%install
%pyproject_install

%check
%pyproject_run_pytest tests.py

%files
%doc *.md examples
%_bindir/%oname
%python3_sitelibdir/%oname
%python3_sitelibdir/%oname-%version.dist-info

%changelog
* Fri May 31 2024 Grigory Ustinov <grenka@altlinux.org> 2.0.0-alt1
- Build new version.

* Mon Jan 29 2024 Grigory Ustinov <grenka@altlinux.org> 1.1.6-alt3
- Moved on modern pyproject macros.

* Fri Dec 13 2019 Andrey Bychkov <mrdrew@altlinux.org> 1.1.6-alt2
- build for python2 disabled

* Thu May 09 2019 Stanislav Levin <slev@altlinux.org> 1.1.6-alt1
- 1.1.3 -> 1.1.6.

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 1.1.3-alt2.git20150525.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Wed Dec 20 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 1.1.3-alt2.git20150525
- Fixed build.

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 1.1.3-alt1.git20150525.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Mon Aug 24 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.1.3-alt1.git20150525
- Initial build for Sisyphus

