Summary: Parser interpreter based on PEG grammars written in Python
Version: 1.9.0
Release: alt1
%setup_python_module arpeggio
Name: python-module-arpeggio
Source0: v%version.tar.gz
BuildArch: noarch
License: MIT
Group: Development/Python
Url: https://github.com/igordejanovic/Arpeggio

# Automatically added by buildreq on Thu Jun 14 2018
# optimized out: ghp-import python-base python-devel python-module-attrs python-module-backports-functools-lru-cache python-module-backports_abc python-module-certifi python-module-click python-module-django python-module-funcsigs python-module-jinja2 python-module-markdown python-module-markupsafe python-module-pluggy python-module-py python-module-pycares python-module-pycparser python-module-setuptools python-module-simplejson python-module-singledispatch python-module-six python-module-tornado python-module-yaml python-modules python-modules-compiler python-modules-ctypes python-modules-email python-modules-encodings python-modules-json python-modules-logging python-modules-wsgiref python-modules-xml python3 python3-base python3-module-click python3-module-jinja2 python3-module-markdown python3-module-markupsafe python3-module-setuptools python3-module-yaml xz
BuildRequires: python-module-cffi python-module-livereload python-module-mkdocs python-module-pytest python-module-zope.interface python3-dev python3-module-livereload python3-module-mkdocs time python-module-futures

%description
Arpeggio is a recursive descent parser with memoization based on PEG
grammars (aka Packrat parser).

%package -n python3-module-arpeggio
Summary: %summary 3
Group: Development/Python3
BuildArch: noarch

%description -n python3-module-arpeggio
Arpeggio is a recursive descent parser with memoization based on PEG
grammars (aka Packrat parser).

%prep
%setup -n Arpeggio-%version

%build
%python_build_debug -b build2
%python3_build_debug -b build3

mkdocs build
mv site site.2
mkdocs.py3 build

%install
ln -sf build2 build
%python_install
ln -sf build3 build
%python3_install

%files -n %packagename
%doc site.2
%python_sitelibdir_noarch/%modulename
%python_sitelibdir_noarch/Arpeggio-*.egg-info

%files -n python3-module-arpeggio
%doc site
%python3_sitelibdir_noarch/%modulename
%python3_sitelibdir_noarch/Arpeggio-*.egg-info

%changelog
* Mon Jan 28 2019 Fr. Br. George <george@altlinux.ru> 1.9.0-alt1
- Autobuild version bump to 1.9.0

* Thu Jun 14 2018 Fr. Br. George <george@altlinux.ru> 1.8.0-alt1
- Autobuild version bump to 1.8.0

* Thu Jun 14 2018 Fr. Br. George <george@altlinux.ru> 1.7.1-alt1
- Initial build for ALT

