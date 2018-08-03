Name: python-module-parso
Version: 0.3.1
Release: alt1
License: MIT
Summary: A Python3 Parser
Group: Development/Python3
Source: v%version.tar.gz
BuildArch: noarch

# Automatically added by buildreq on Sat Aug 04 2018
# optimized out: python-base python-module-OpenSSL python-module-PyStemmer python-module-Pygments python-module-SQLAlchemy python-module-asn1crypto python-module-attrs python-module-babel python-module-cffi python-module-chardet python-module-cryptography python-module-docutils python-module-enum34 python-module-funcsigs python-module-idna python-module-imagesize python-module-ipaddress python-module-jinja2 python-module-lxml python-module-markupsafe python-module-ndg-httpsclient python-module-ntlm python-module-pkg_resources python-module-pluggy python-module-py python-module-pycparser python-module-pytest python-module-pytz python-module-requests python-module-simplejson python-module-six python-module-sphinx python-module-sphinxcontrib python-module-typing python-module-urllib3 python-module-webencodings python-module-whoosh python-modules python-modules-compiler python-modules-ctypes python-modules-distutils python-modules-email python-modules-encodings python-modules-json python-modules-logging python-modules-multiprocessing python-modules-unittest python-modules-xml python3 python3-base python3-dev python3-module-OpenSSL python3-module-Pygments python3-module-babel python3-module-cffi python3-module-chardet python3-module-cryptography python3-module-docutils python3-module-idna python3-module-imagesize python3-module-jinja2 python3-module-markupsafe python3-module-pkg_resources python3-module-pytz python3-module-requests python3-module-six python3-module-sphinx python3-module-urllib3 sh3 xz
BuildRequires: ctags python-module-alabaster python-module-docopt python-module-html5lib python-module-setuptools python-module-sphinxcontrib-websupport python3-module-alabaster python3-module-setuptools python3-module-sphinxcontrib-websupport time
BuildRequires(pre): rpm-build-python3 rpm-build-python

%description
Parso is a Python parser that supports error recovery and round-trip
parsing for different Python versions (in multiple Python versions).
Parso is also able to list multiple syntax errors in your python file.

Parso has been battle-tested by jedi. It was pulled out of jedi to be
useful for other projects as well.

Parso consists of a small API to parse Python and analyse the syntax tree.

%package -n python3-module-parso
Group: Development/Python
Summary: A Python3 Parser

%description -n python3-module-parso
Parso is a Python3 parser that supports error recovery and round-trip
parsing for different Python3 versions (in multiple Python3 versions).
Parso is also able to list multiple syntax errors in your python file.

%prep
%setup -n parso-%version

%build
%python_build
%python3_build -b build3
make -C docs html
%make -C docs SPHINXBUILD=py3_sphinx-build BUILDDIR=_build3 html

%install
%python_install
mv build build2
mv build3 build
%python3_install

%files
%doc docs/_build/html/*
%python_sitelibdir_noarch/*

%files -n python3-module-parso
%doc docs/_build3/html/*
%python3_sitelibdir_noarch/*

%changelog
* Fri Aug 03 2018 Fr. Br. George <george@altlinux.ru> 0.3.1-alt1
- Autobuild version bump to 0.3.1

