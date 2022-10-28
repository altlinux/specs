%def_with check
%def_with docs

Name: python3-module-pikepdf
Version: 6.2.1
Release: alt1
License: MPL-2.0
Url: https://github.com/pikepdf/pikepdf
Summary: A Python library for reading and writing PDF files
Group: Development/Python
Source: pikepdf-%version.tar.gz
Patch: pikepdf-jbig2dec.patch
Requires: libpoppler-gir

# Automatically added by buildreq on Wed Jun 15 2022
# optimized out: alt-os-release ca-trust git-core glibc-kernheaders-generic glibc-kernheaders-x86 libgpg-error libp11-kit libstdc++-devel mercurial mpdecimal python3 python3-base python3-dev python3-module-PasteDeploy python3-module-Pillow python3-module-Pygments python3-module-alabaster python3-module-attrs python3-module-babel python3-module-cffi python3-module-charset-normalizer python3-module-docutils python3-module-idna python3-module-imagesize python3-module-jinja2 python3-module-lxml python3-module-markupsafe python3-module-packaging python3-module-paste python3-module-pep517 python3-module-pip python3-module-pkg_resources python3-module-pyparsing python3-module-pytz python3-module-requests python3-module-setuptools python3-module-sphinx python3-module-tomli python3-module-urllib3 sh4 xz
BuildRequires: gcc-c++ libqpdf-devel python3-module-PasteScript python3-module-build python3-module-flit python3-module-mpl_toolkits python3-module-pybind11 python3-module-setuptools_scm python3-module-sphinxcontrib python3-module-wheel jbig2dec

%if_with docs
BuildRequires: ctags python3-module-sphinx-issues python3-module-sphinx_design python3-module-sphinx_rtd_theme python3-module-sphinxcontrib python3-module-sphinxcontrib-applehelp python3-module-sphinxcontrib-devhelp python3-module-sphinxcontrib-htmlhelp python3-module-sphinxcontrib-qthelp python3-module-sphinxcontrib-serializinghtml python3-module-wheel
%endif

%if_with check

BuildRequires: pytest3 python3-module-hypothesis python3-module-psutil
BuildRequires: /proc
%endif

%description
pikepdf is based on QPDF, a powerful PDF manipulation and repair library.
Python + QPDF = "py" + "qpdf" = "pyqpdf", which looks like a dyslexia test.
Say it out loud, and it sounds like "pikepdf".

%prep
%setup -n pikepdf-%version
%patch -p0
# XXX what's that?
sed -i '/"-n auto"/d' pyproject.toml

# XXX don't want IPython as dependency
sed -i '/autodoc_mock_imports/s/\]/, "IPython"]/
/IPython.sphinxext/d
' docs/conf.py

%build
python3 -m build -n -w
%if_with docs
pip3 install --no-deps --root=build -I dist/pikepdf*%{version}*.whl
PYTHONPATH=`pwd`/build%python3_sitelibdir make SPHINXBUILD=sphinx-build-3 -C docs html
%endif

%install
pip3 install --no-deps --root=%buildroot -I dist/pikepdf*%{version}*.whl

%if_with check
%check
%ifnarch armh
PYTHONPATH=%buildroot%python3_sitelibdir pytest3
%else
# XXX this SEGFAULTs deep in there
PYTHONPATH=%buildroot%python3_sitelibdir pytest3 -k 'not test_build_instructions'
%endif
%endif

%files
%if_with docs
%doc docs/_build/html
%endif
%doc *.md
%python3_sitelibdir/*pikepdf*

%changelog
* Fri Oct 28 2022 Fr. Br. George <george@altlinux.org> 6.2.1-alt1
- Autobuild version bump to 6.2.1

* Wed Jun 15 2022 Fr. Br. George <george@altlinux.org> 5.1.5-alt1
- Autobuild version bump to 5.1.5

* Sun Apr 17 2022 Fr. Br. George <george@altlinux.org> 5.1.2-alt1
- Autobuild version bump to 5.1.2
- Switch to modern build scheme
- Introduce tests
- Introduce documentation (no IPython though)

* Sat Jun 19 2021 Fr. Br. George <george@altlinux.ru> 2.12.2-alt1
- Autobuild version bump to 2.12.2

* Wed Jan 13 2021 Fr. Br. George <george@altlinux.ru> 2.3.0-alt1
- Autobuild version bump to 2.3.0

* Tue Dec 29 2020 Fr. Br. George <george@altlinux.ru> 2.2.4-alt1
- Initial build for ALT

