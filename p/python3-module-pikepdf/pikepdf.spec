%define _unpackaged_files_terminate_build 1
%def_with check
%def_with docs

%define tomli %(%__python3 -c 'import sys;print(int(sys.version_info < (3, 11)))')

Name: python3-module-pikepdf
Version: 6.2.1
Release: alt2
License: MPL-2.0
Url: https://github.com/pikepdf/pikepdf
Summary: A Python library for reading and writing PDF files
Group: Development/Python
Source: pikepdf-%version.tar
Patch: pikepdf-jbig2dec.patch
Requires: libpoppler-gir

BuildRequires: gcc-c++ libqpdf-devel jbig2dec

BuildRequires(pre): rpm-build-python3

# build backend and its deps
BuildRequires: python3(setuptools)
BuildRequires: python3(wheel)
BuildRequires: python3(setuptools-scm)
BuildRequires: python3(pybind11)

%if_with docs
BuildRequires: ctags python3-module-sphinx-issues python3-module-sphinx_design python3-module-sphinx_rtd_theme python3-module-sphinxcontrib python3-module-sphinxcontrib-applehelp python3-module-sphinxcontrib-devhelp python3-module-sphinxcontrib-htmlhelp python3-module-sphinxcontrib-qthelp python3-module-sphinxcontrib-serializinghtml python3-module-Pillow
%endif

%if_with check
# deps
BuildRequires: python3(PIL)
BuildRequires: python3(lxml)
BuildRequires: python3(packaging)

BuildRequires: python3(pytest)
BuildRequires: python3(hypothesis)
BuildRequires: python3(psutil)
BuildRequires: /proc
%if %tomli
BuildRequires: python3(tomli)
%endif
%endif

%description
pikepdf is based on QPDF, a powerful PDF manipulation and repair library.
Python + QPDF = "py" + "qpdf" = "pyqpdf", which looks like a dyslexia test.
Say it out loud, and it sounds like "pikepdf".

%prep
%setup -n pikepdf-%version
%patch -p0
# disable pytest-xdist (unstable results)
sed -i 's/-n auto//' pyproject.toml

# XXX don't want IPython as dependency
sed -i '/autodoc_mock_imports/s/\]/, "IPython"]/
/IPython.sphinxext/d
' docs/conf.py

# https://github.com/pikepdf/pikepdf/issues/417
sed -i '/[[:space:]]*deprecation[[:space:]]*/d' setup.cfg

%build
%pyproject_build

%install
%pyproject_install
%if_with docs
# docs build requires built C extension, but we can't control the path of build
# artifacts
PYTHONPATH="%buildroot%python3_sitelibdir" make SPHINXBUILD=sphinx-build-3 \
    -C docs html
%endif

%check
%ifarch armh
%define pytest_opts -k 'not test_build_instructions'
%endif
%tox_create_default_config
%tox_check_pyproject -- -vra %{?pytest_opts}

%files
%if_with docs
%doc docs/_build/html
%endif
%doc *.md
%python3_sitelibdir/pikepdf/
%python3_sitelibdir/%{pyproject_distinfo pikepdf}/

%changelog
* Thu Nov 10 2022 Stanislav Levin <slev@altlinux.org> 6.2.1-alt2
- Fixed FTBFS (flit_core 3.7.1).

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

