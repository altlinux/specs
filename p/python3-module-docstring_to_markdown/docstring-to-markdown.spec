%define  modulename docstring_to_markdown
%define  _unpackaged_files_terminate_build 1

%def_enable check

Name:    python3-module-%modulename
Version: 0.11
Release: alt1

Summary: On the fly conversion of Python docstrings to markdown
License: LGPL-2.1
Group:   Development/Python3
URL:     https://github.com/python-lsp/docstring-to-markdown

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-dev python3-module-setuptools

%if_enabled check
BuildRequires: python3(pytest) python3(pytest-cov)
%endif

BuildArch: noarch

Source:  %modulename-%version.tar

%description
On the fly conversion of Python docstrings to markdown.
It can recognise reStructuredText and convert multiple
of its features to Markdown.

%prep
%setup -n %modulename-%version

# don't run flake8 checks during package build
sed -i '/--flake8/d' setup.cfg

%build
%python3_build

%install
%python3_install

%check
python3 -m pytest -vv

%files
%python3_sitelibdir/%modulename/
%python3_sitelibdir/*.egg-info
%doc *.md

%changelog
* Sat Dec 10 2022 Ivan A. Melnikov <iv@altlinux.org> 0.11-alt1
- Initial build for Sisyphus
