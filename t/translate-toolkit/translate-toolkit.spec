%define modname translate

Name: translate-toolkit
Version: 2.2.5
Release: alt1

Summary: Tools and API for translation and localization engineering.

License: %gpl2plus
Group: Development/Python
Url: http://toolkit.translatehouse.org/

Source: %name-%version.tar
BuildArch: noarch

BuildRequires(pre): rpm-build-licenses
BuildPreReq: rpm-build-python
BuildRequires: python-devel python-module-distribute
BuildRequires: python-module-sphinx python-modules-wsgiref python-modules-sqlite3 python-module-BeautifulSoup4

Requires: python-module-diff-match-patch python-module-translate

%setup_python_module %modname

%description
The Translate Toolkit is created by localizers for localizers. It contains
several utilities, as well as an API for building localization tools.

Some of the tools include:

* File format converters
* Quality checking tools
* Tools for counting, grepping, terminology extraction, and pseudo-localization

%package -n python-module-%modname
Summary: Module for building localization tools
Group: Development/Python

%description -n python-module-%modname
Features of the API include:

* Support for multiple file formats
* Language information and language support code (including language detection)
* Code for translation memory, terminology matching and indexed search
* Several helper classes and functions for tools built on the Translate Toolkit.

%package -n %name-doc
Summary: Documentation for Translate Toolkit
Group: Development/Documentation

%description -n %name-doc
Documentation for Translate Toolkit

%prep
%setup -n %name-%version

%build
%python_build
pushd docs
%make man
gzip -9 _build/man/*.1
#no hidden files
find _build -name '.?*' -exec rm '{}' \+
popd

%install
%python_install

install -d %buildroot%_man1dir
install -pm 644 docs/_build/man/*.gz %buildroot%_man1dir
rm -fr %buildroot%python_sitelibdir/%modname/docs/

%files
%doc docs/{features,history,license}.rst
%{_bindir}/*
%_man1dir/*

%files -n python-module-%modname
# Don't pack PyLuceneIndexer since it requires absent PyLucene for work
%exclude %python_sitelibdir/%modname/search/indexing/PyLuceneIndexer*
%python_sitelibdir/%modname
%python_sitelibdir/*.egg-info

%files -n %name-doc
%doc docs/_build/html

%changelog
* Mon Jan 15 2018 Vladimir Didenko <cow@altlinux.ru> 2.2.5-alt1
- New version
- add dependency to python-module-translate (closes: #34461)

* Wed Jul 5 2017 Vladimir Didenko <cow@altlinux.ru> 2.2.3-alt1
- New version

* Wed Mar 22 2017 Vladimir Didenko <cow@altlinux.ru> 2.1.0-alt1
- New version

* Thu Mar 16 2017 Vladimir Didenko <cow@altlinux.ru> 2.0.0-alt1
- New version

* Mon Dec 7 2015 Vladimir Didenko <cow@altlinux.ru> 1.13.0-alt1
- Initial build
