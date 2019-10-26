Summary: Parser interpreter based on PEG grammars written in Python
Version: 1.9.2
Release: alt1
%setup_python_module arpeggio
Name: python-module-arpeggio
Source0: v%version.tar.gz
BuildArch: noarch
License: MIT
Group: Development/Python
Url: https://github.com/igordejanovic/Arpeggio

# Automatically added by buildreq on Sat Oct 26 2019
# optimized out: ghp-import python-base python-module-apipkg python-module-atomicwrites python-module-attrs python-module-backports_abc python-module-certifi python-module-click python-module-configparser python-module-contextlib2 python-module-funcsigs python-module-futures python-module-importlib_metadata python-module-iniconfig python-module-jinja2 python-module-markdown python-module-markupsafe python-module-more-itertools python-module-packaging python-module-pathlib2 python-module-pkg_resources python-module-pluggy python-module-py python-module-pycares python-module-pycparser python-module-pyparsing python-module-scandir python-module-setuptools python-module-simplejson python-module-singledispatch python-module-six python-module-tornado python-module-wcwidth python-module-yaml python-module-zipp python-modules python-modules-compiler python-modules-ctypes python-modules-distutils python-modules-email python-modules-encodings python-modules-json python-modules-logging python-modules-wsgiref python-modules-xml python3 python3-base python3-dev python3-module-click python3-module-jinja2 python3-module-markdown python3-module-markupsafe python3-module-pkg_resources python3-module-setuptools python3-module-yaml sh4 xz
BuildRequires: python-module-cffi python-module-livereload python-module-mkdocs python-module-pytest python-module-pytest-runner python-module-zope.interface python3-module-livereload python3-module-mkdocs time

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
rm -rf build && ln -sf build2 build
%python_install
##rm -rf %buildroot%python_sitelibdir_noarch/examples

rm -rf build && ln -sf build3 build
%python3_install
# XXX move examples out of the module
##rm -rf %buildroot%python3_sitelibdir_noarch/examples

%files -n %packagename
%doc site.2 examples
%python_sitelibdir_noarch/%modulename
%python_sitelibdir_noarch/Arpeggio-*.egg-info

%files -n python3-module-arpeggio
%doc site examples
%python3_sitelibdir_noarch/%modulename
%python3_sitelibdir_noarch/Arpeggio-*.egg-info

%changelog
* Sat Oct 26 2019 Fr. Br. George <george@altlinux.ru> 1.9.2-alt1
- Autobuild version bump to 1.9.2

* Mon Jan 28 2019 Fr. Br. George <george@altlinux.ru> 1.9.0-alt1
- Autobuild version bump to 1.9.0

* Thu Jun 14 2018 Fr. Br. George <george@altlinux.ru> 1.8.0-alt1
- Autobuild version bump to 1.8.0

* Thu Jun 14 2018 Fr. Br. George <george@altlinux.ru> 1.7.1-alt1
- Initial build for ALT

