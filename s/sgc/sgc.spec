Name: sgc
Version: 0.2.1
Release: alt2
Summary: A GUI toolkit for Pygame
Group: Development/Python
License: BSD
Source: %name-%version.tar.gz
BuildArch: noarch

%setup_python_module %name

# Automatically added by buildreq on Thu Mar 06 2014
# optimized out: fonts-bitmap-misc libX11-locales python-base python-devel python-module-BeautifulSoup python-module-Pygments python-module-SQLAlchemy python-module-distribute python-module-docutils python-module-genshi python-module-html5lib python-module-jinja2 python-module-jinja2-tests python-module-lxml python-module-nose python-module-numpy python-module-numpy-testing python-module-protobuf python-module-simplejson python-module-whoosh python-modules python-modules-compiler python-modules-ctypes python-modules-email python-modules-encodings python-modules-logging python-modules-unittest xauth xkbcomp xkeyboard-config xorg-server-common xorg-xvfb
BuildRequires: ctags python-module-pygame python-module-sphinx python-modules-json time xvfb-run

BuildRequires: python-devel

%description
%summary

%package -n %packagename
Group: Development/Python
Summary: %summary
%description -n %packagename
A GUI toolkit for Pygame, to ease game development for Pygame developers.

This is a lightweight toolkit, with focus on the attention to detail. It
is also customisable, allowing developers to theme the widgets to match
their game. With no code changes it can be switched to use either
a normal Pygame display or an OpenGL display.

%package -n %packagename-docs
Group: Development/Python
Summary: %summary documentation
%description -n %packagename-docs
%summary

%prep
%setup
cat > makedocs <<@@@
sleep 5
make -C docs html
@@@

%build
%python_build
PYTHONPATH="$(realpath `pwd`)" xvfb-run sh makedocs

%install
%python_install

%files -n %packagename
%python_sitelibdir_noarch/sgc*

%files -n %packagename-docs
%doc docs/_build/html/* example

%changelog
* Thu Feb 07 2019 Fr. Br. George <george@altlinux.ru> 0.2.1-alt2
- Insert 5 sec delay for start xvfb-run

* Thu Mar 06 2014 Fr. Br. George <george@altlinux.ru> 0.2.1-alt1
- Autobuild version bump to 0.2.1
- Rename documentation package

* Thu Mar 06 2014 Fr. Br. George <george@altlinux.ru> 0.2-alt1
- Initial build from scratch

