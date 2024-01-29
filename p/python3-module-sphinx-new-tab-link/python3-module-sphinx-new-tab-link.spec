%define        oname sphinx_new_tab_link

Name:          python3-module-sphinx-new-tab-link
Version:       0.2.1
Release:       alt1

Summary:       Open external links in new tabs of the browser in Sphinx HTML documents
License:       MIT
Group:         Development/Python3
Url:           https://ftnext.github.io/sphinx-new-tab-link/guide.html
Vcs:           https://github.com/ftnext/sphinx-new-tab-link.git
BuildArch:     noarch

Source:        %name-%version.tar
Patch:         fix-doc.patch
BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-sphinx
BuildRequires: python3-module-myst-parser

%description
Open external links in new tabs of the browser in Sphinx HTML documents.


%prep
%setup
%autopatch

sed -i 's|sphinx-build|sphinx-build-3|' docs/Makefile

%build
%python3_build_debug

%make -C docs html

%install
%python3_install

%files
%doc README.md docs/_build/html/*
%python3_sitelibdir_noarch/%{oname}*


%changelog
* Fri Jan 26 2024 Pavel Skrylev <majioa@altlinux.org> 0.2.1-alt1
- Initial build v0.2.1 for Sisyphus
