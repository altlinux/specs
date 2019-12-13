%define _unpackaged_files_terminate_build 1
%define oname landslide

%def_with check

Name: python3-module-%oname
Version: 1.1.6
Release: alt2

Summary: Lightweight markup language-based html5 slideshow generator
License: ASLv2.0
Group: Development/Python3
Url: https://pypi.python.org/pypi/landslide
BuildArch: noarch

# https://github.com/adamzap/landslide.git
Source: %name-%version.tar
Patch: landslide-1.1.6-Support-markdown-v3.0.patch

BuildRequires(pre): rpm-build-python3

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
%patch -p1

# unpin deps
sed -i 's/==/>=/g' setup.py requirements.txt

sed -i 's|#!/usr/bin/env python|#!/usr/bin/env python3|' \
    $(find ./ -name '*.py')

%build
%python3_build_debug

%install
%python3_install

%if_with check
%check
cat > tox.ini <<EOF
[testenv]
commands =
    {envpython} tests.py -v
EOF
export PIP_NO_INDEX=YES
export TOXENV=py%{python_version_nodots python3}
tox.py3 --sitepackages -p auto -o -v
%endif

%files
%doc *.md examples
%_bindir/landslide
%python3_sitelibdir/landslide/
%python3_sitelibdir/*.egg-info/


%changelog
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

