Name: pymunk
Version: 5.5.0
Release: alt1
%setup_python_module %name
Summary: Empty package %packagename
Group: Development/Python
License: MIT
Source: %name-%version.zip

%add_python_req_skip py2exe ctypeslib
%add_python3_req_skip py2exe ctypeslib

# Automatically added by buildreq on Mon Oct 28 2019
# optimized out: python-base python-module-OpenSSL python-module-PyStemmer python-module-Pygments python-module-SQLAlchemy python-module-babel python-module-backports python-module-backports.ssl_match_hostname python-module-cffi python-module-chardet python-module-cryptography python-module-cssselect python-module-docutils python-module-enum34 python-module-idna python-module-imagesize python-module-ipaddress python-module-jinja2 python-module-lxml python-module-markupsafe python-module-ndg-httpsclient python-module-ntlm python-module-pkg_resources python-module-pycparser python-module-pytz python-module-requests python-module-simplejson python-module-six python-module-sphinx python-module-sphinxcontrib python-module-typing python-module-urllib3 python-module-webencodings python-module-whoosh python-modules python-modules-compiler python-modules-ctypes python-modules-distutils python-modules-email python-modules-encodings python-modules-json python-modules-logging python-modules-multiprocessing python-modules-unittest python-modules-xml python3 python3-base python3-dev python3-module-OpenSSL python3-module-Pygments python3-module-babel python3-module-cffi python3-module-chardet python3-module-cryptography python3-module-docutils python3-module-idna python3-module-imagesize python3-module-jinja2 python3-module-markupsafe python3-module-packaging python3-module-pkg_resources python3-module-pytz python3-module-requests python3-module-sphinx python3-module-urllib3 sh4 xz
BuildRequires: ctags python-module-alabaster python-module-html5lib python-module-setuptools python-module-sphinxcontrib-websupport python3-module-alabaster python3-module-setuptools python3-module-sphinxcontrib-applehelp python3-module-sphinxcontrib-devhelp python3-module-sphinxcontrib-htmlhelp python3-module-sphinxcontrib-jsmath python3-module-sphinxcontrib-qthelp python3-module-sphinxcontrib-serializinghtml time unzip

BuildRequires(pre): python3-devel

%description
Empty package

%package examples
Summary: Example files for %name
Group: Development/Python
BuildArch: noarch
Obsoletes: %name
%description examples
Example files for %packagename

%package -n %packagename
Summary: Python wrapper for the chipmunk 2D physics engine
Group: Development/Python
Requires: libchipmunk
%description -n %packagename
Pymunk is a Python wrapper for the wrapper for the chipmunk 2D physics
engine. It aims to be easy to use, "Pythonic", and non-intrusive.

%package -n python3-module-%name
Summary: Python3 wrapper for the chipmunk 2D physics engine
Group: Development/Python3
Requires: libchipmunk
%description -n python3-module-%name
Pymunk is a Python3 wrapper for the wrapper for the chipmunk 2D physics
engine. It aims to be easy to use, "Pythonic", and non-intrusive.

%prep
%setup

%build
export CFLAGS="-fPIC -O2 -g"
%python_build -b build3
make -C docs/src SPHINXBUILD=sphinx-build BUILDDIR=../../build2 html
%python3_build -b build2
make -C docs/src SPHINXBUILD=sphinx-build-3 BUILDDIR=../../build3 html

%install
rm -f build && ln -s build3 build
%python_install

rm -f build && ln -s build2 build
%python3_install

%check
python3 setup.py check

%files examples
%doc examples

%files -n python3-module-%name
%doc *txt build3/html
%python3_sitelibdir/%modulename
%python3_sitelibdir/%modulename-*
%python3_sitelibdir/pymunkoptions

%files -n %packagename
%doc *txt build2/html
%python_sitelibdir/%modulename
%python_sitelibdir/%modulename-*
%python_sitelibdir/pymunkoptions

%changelog
* Mon Oct 28 2019 Fr. Br. George <george@altlinux.ru> 5.5.0-alt1
- Autobuild version bump to 5.5.0
- Introduce Python3 package
- Rename %name to %name-examples, as it is

* Mon Oct 31 2016 Fr. Br. George <george@altlinux.ru> 5.1.0-alt1
- Autobuild version bump to 5.1.0
- Fix still queer _libload.py

* Tue Jul 26 2016 Fr. Br. George <george@altlinux.ru> 5.0.0-alt1
- Autobuild version bump to 5.0.0

* Wed Oct 16 2013 Fr. Br. George <george@altlinux.ru> 4.0.0-alt1
- Autobuild version bump to 4.0.0
- Drop inactual patch

* Sun Mar 03 2013 Fr. Br. George <george@altlinux.ru> 3.0.0-alt1
- Autobuild version bump to 3.0.0
- Provide clean version of libload.py
- Add required internal libchipmunk functions

* Sun Mar 03 2013 Fr. Br. George <george@altlinux.ru> 2.1.0-alt1
- Initial build from scratch

