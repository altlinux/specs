%define _unpackaged_files_terminate_build 1
%define oname landslide

%def_with check

Name: python-module-%oname
Version: 1.1.6
Release: alt1
Summary: Lightweight markup language-based html5 slideshow generator
License: ASLv2.0
Group: Development/Python
BuildArch: noarch
Url: https://pypi.python.org/pypi/landslide

# https://github.com/adamzap/landslide.git
Source: %name-%version.tar
Patch: landslide-1.1.6-Support-markdown-v3.0.patch

BuildRequires(pre): rpm-build-python3

%if_with check
BuildRequires: python2.7(docutils)
BuildRequires: python2.7(jinja2)
BuildRequires: python2.7(markdown)
BuildRequires: python2.7(pygments)
BuildRequires: python2.7(six)
BuildRequires: python3(docutils)
BuildRequires: python3(jinja2)
BuildRequires: python3(markdown)
BuildRequires: python3(pygments)
BuildRequires: python3(six)
BuildRequires: python3(tox)
%endif

%py_requires markdown

%description
Landslide takes your Markdown, ReST, or Textile file(s) and generates
fancy HTML5 slideshow.

%package -n python3-module-%oname
Summary: Lightweight markup language-based html5 slideshow generator
Group: Development/Python3
%py3_requires markdown

%description -n python3-module-%oname
Landslide takes your Markdown, ReST, or Textile file(s) and generates
fancy HTML5 slideshow.

%prep
%setup
%patch -p1
# unpin deps
sed -i 's/==/>=/g' setup.py requirements.txt

cp -fR . ../python3

%build
%python_build_debug

pushd ../python3
%python3_build_debug
popd

%install
pushd ../python3
%python3_install
popd
pushd %buildroot%_bindir
for i in $(ls); do
	mv $i $i.py3
done
popd

%python_install

%check
cat > tox.ini <<EOF
[testenv]
commands =
    {envpython} tests.py -v
EOF
export PIP_NO_INDEX=YES
export TOXENV=py%{python_version_nodots python},py%{python_version_nodots python3}
tox.py3 --sitepackages -p auto -o -v

%files
%doc *.md examples
%_bindir/landslide
%python_sitelibdir/landslide/
%python_sitelibdir/landslide-%version-py%_python_version.egg-info/

%files -n python3-module-%oname
%doc *.md examples
%_bindir/landslide.py3
%python3_sitelibdir/landslide/
%python3_sitelibdir/landslide-%version-py%_python3_version.egg-info/

%changelog
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

