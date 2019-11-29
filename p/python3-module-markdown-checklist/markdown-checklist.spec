%define oname markdown-checklist

Name: python3-module-%oname
Version: 0.4.1
Release: alt2

Summary: Python Markdown extension for task lists with checkboxes
License: MIT
Group: Development/Python3
Url: https://pypi.python.org/pypi/markdown-checklist/
BuildArch: noarch

# https://github.com/FND/markdown-checklist.git
Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-markdown
BuildRequires: python3-module-coverage
BuildRequires: python3-module-pytest

%py3_provides markdown_checklist
%py3_requires markdown


%description
Python Markdown extension for lists of tasks with checkboxes.

%prep
%setup

%build
%python3_build_debug

%install
%python3_install

%check
%__python3 setup.py test

%files
%doc README
%python3_sitelibdir/*


%changelog
* Fri Nov 29 2019 Andrey Bychkov <mrdrew@altlinux.org> 0.4.1-alt2
- python2 disabled

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 0.4.1-alt1.git20150127.1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.4.1-alt1.git20150127.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Tue Jan 27 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.4.1-alt1.git20150127
- Initial build for Sisyphus

