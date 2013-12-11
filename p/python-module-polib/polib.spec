Name:		python-module-polib
Version:	1.0.3
Release:	alt1
Summary:	Manipulate, create, and modify gettext files
Group:		Development/Python
License:	BSD-like
Source:		polib-%version.tar.gz
URL:		https://bitbucket.org/izi/polib
BuildArch:	noarch

%setup_python_module polib

# TODO python3

# Automatically added by buildreq on Wed Dec 11 2013
# optimized out: python-base python-devel python-module-BeautifulSoup python-module-Pygments python-module-docutils python-module-jinja2 python-module-markupsafe python-module-protobuf python-module-setuptools python-module-simplejson python-module-six python-modules python-modules-compiler python-modules-ctypes python-modules-email python-modules-encodings python-modules-logging python-modules-unittest
BuildRequires: ctags python-module-sphinx time

BuildRequires: python-module-coverage

%description
polib is a library to manipulate, create, modify gettext files (pot, po
and mo files). You can load existing files, iterate through it's
entries, add, modify entries, comments or metadata, etc... or create new
po files from scratch.

%prep
%setup -n polib-%version

%build
%python_build
make -C docs html

%install
%python_install

%check
./runtests.sh

%files
%doc docs/_build/html
%python_sitelibdir_noarch/%{modulename}*

%changelog
* Wed Dec 11 2013 Fr. Br. George <george@altlinux.ru> 1.0.3-alt1
- Initial build for ALT

