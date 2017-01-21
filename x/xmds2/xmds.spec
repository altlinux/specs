%def_disable check

Name: xmds2
Version: 2.2.3
Release: alt1

Summary: xmds - an extensible multi-dimensional simulator for PDEs (Partial Differential Equations) and ODEs
License: GPLv2+
Group: Sciences/Mathematics
Url: http://www.xmds.org
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://download.sourceforge.net/xmds/xmds-%version.tar.gz
Source: xmds-%version.tar
BuildArch: noarch

%py_requires h5py lxml mpmath numpy

# Automatically added by buildreq on Sun Dec 10 2017 (-bi)
# optimized out: gcc-c++ glibc-kernheaders-generic glibc-kernheaders-x86 libfftw3-devel libhdf5-8-seq libstdc++-devel openmpi python-base python-devel python-module-OpenSSL python-module-PyStemmer python-module-Pygments python-module-SQLAlchemy python-module-appdirs python-module-argcomplete python-module-asn1crypto python-module-babel python-module-backports.ssl_match_hostname python-module-backports_abc python-module-bottle python-module-certifi python-module-cffi python-module-chardet python-module-cryptography python-module-cssselect python-module-cycler python-module-dateutil python-module-docutils python-module-enum34 python-module-execnet python-module-funcsigs python-module-functools32 python-module-idna python-module-imagesize python-module-ipaddress python-module-jinja2 python-module-linecache2 python-module-lxml python-module-markupsafe python-module-matplotlib python-module-numpy python-module-ordereddict python-module-packaging python-module-pbr python-module-py python-module-pycares python-module-pycparser python-module-pycurl python-module-pyinotify python-module-pymongo python-module-pyparsing python-module-pytest python-module-pytest-shutil python-module-pytest-virtualenv python-module-pytz python-module-requests python-module-rlcompleter2 python-module-servicemanager python-module-setuptools python-module-simplejson python-module-singledispatch python-module-six python-module-snowballstemmer python-module-sphinx python-module-subprocess32 python-module-tornado python-module-traceback2 python-module-typing python-module-unittest2 python-module-urllib3 python-module-webencodings python-module-whoosh python-modules python-modules-compiler python-modules-ctypes python-modules-email python-modules-encodings python-modules-json python-modules-logging python-modules-unittest python-modules-wsgiref python-modules-xml xz zlib-devel
BuildRequires: hdf5-8-tools libgsl-devel libhdf5-devel openmpi-devel python-module-alabaster python-module-cheetah python-module-h5py python-module-html5lib python-module-mock python-module-mpmath python-module-ndg-httpsclient python-module-ntlm python-module-numpydoc python-module-pytest-fixture-config python-module-sphinxcontrib-websupport python-module-zope.interface xmds

%description
Welcome to XMDS2, a software package that allows the fast and easy
solution of sets of ordinary, partial and stochastic differential
equations, using a variety of efficient numerical algorithms.

%prep
%setup

%build
source %_libdir/openmpi/bin/mpivars.sh
export PYTHONPATH=$PWD
python bin/xmds2 --reconfigure
%make_build

%install
source %_libdir/openmpi/bin/mpivars.sh
%python_build_install

mkdir -p %buildroot/%_docdir/%name-%version-%release
cp -fR documentation %buildroot/%_docdir/%name-%version-%release/
mkdir -p %buildroot/%_docdir/%name-%version-%release/examples
cp examples/* %buildroot/%_docdir/%name-%version-%release/examples
install -d %buildroot%_man1dir
install -p -m644 man/* %buildroot%_man1dir/

%check
source %_libdir/openmpi/bin/mpivars.sh
export PATH=$PATH:%buildroot%_bindir
export PYTHONPATH=$PWD
./run_tests.py -v

%files
%_docdir/%name-%version-%release
%_bindir/*
%_man1dir/*
%python_sitelibdir/*

%changelog
* Sat Jan 21 2017 Dmitry V. Levin <ldv@altlinux.org> 2.2.3-alt1
- 2.2.2 -> 2.2.3.

* Sat Mar 14 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.2.2-alt1
- Version 2.2.2

* Tue May 03 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 1.6-alt4
- fix build

* Fri Dec 14 2007 Denis Medvedev <nbr@altlinux.ru> 1.6-alt3
- Added description about PAE

* Fri Aug 31 2007 Denis Medvedev <nbr@altlinux.ru> 1.6-alt2
- Recompiled without mpi, who really needs mpi should recompile fftw with mpi too

* Tue Aug 28 2007 Denis Medvedev <nbr@altlinux.ru> 1.6-alt1
- Initial ALT release

