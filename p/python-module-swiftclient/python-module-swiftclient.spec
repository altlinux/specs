%def_with python3

Name: python-module-swiftclient
Version: 2.6.0
Release: alt1.1
Summary: Client Library for OpenStack Object Storage API
License: ASL 2.0
Url: http://pypi.python.org/pypi/%name
Source0: %name-%version.tar
Group: Development/Python

BuildArch: noarch

Requires: python-module-futures
Requires: python-module-requests

# Automatically added by buildreq on Thu Jan 28 2016 (-bi)
# optimized out: pyflakes python-base python-devel python-module-PyStemmer python-module-Pygments python-module-babel python-module-cffi python-module-chardet python-module-cryptography python-module-cssselect python-module-enum34 python-module-flake8 python-module-genshi python-module-hacking python-module-jinja2 python-module-jinja2-tests python-module-markupsafe python-module-mccabe python-module-ndg-httpsclient python-module-ntlm python-module-pbr python-module-pyasn1 python-module-pytz python-module-requests python-module-setuptools python-module-six python-module-snowballstemmer python-module-sphinx python-module-sphinx_rtd_theme python-module-urllib3 python-modules python-modules-compiler python-modules-ctypes python-modules-email python-modules-encodings python-modules-json python-modules-logging python-modules-multiprocessing python-modules-unittest python-tools-pep8 python3 python3-base python3-module-Pygments python3-module-babel python3-module-cffi python3-module-cryptography python3-module-cssselect python3-module-docutils python3-module-enum34 python3-module-flake8 python3-module-genshi python3-module-jinja2 python3-module-markupsafe python3-module-mccabe python3-module-ndg-httpsclient python3-module-ntlm python3-module-pbr python3-module-pip python3-module-pycparser python3-module-pytz python3-module-setuptools python3-module-six python3-module-snowballstemmer python3-module-yieldfrom.http.client python3-pyflakes python3-tools-pep8 xz
BuildRequires: python-module-alabaster python-module-d2to1 python-module-docutils python-module-futures python-module-html5lib python-module-oslosphinx python3-module-chardet python3-module-d2to1 python3-module-hacking python3-module-html5lib python3-module-jinja2-tests python3-module-sphinx python3-module-urllib3 python3-module-yieldfrom.urllib3 rpm-build-python3 time

#BuildRequires: python-devel
#BuildRequires: python-module-setuptools
#BuildRequires: python-module-pbr >= 0.6
#BuildRequires: python-module-d2to1
#BuildRequires: python-module-sphinx
#BuildRequires: python-module-oslosphinx
#BuildRequires: python-module-futures >= 2.1.3
#BuildRequires: python-module-requests >= 1.1
#BuildRequires: python-module-six >= 1.5.2

%if_with python3
BuildRequires(pre): rpm-build-python3
#BuildRequires: python3-devel
#BuildRequires: python3-module-setuptools
#BuildRequires: python3-module-pbr >= 0.6
#BuildRequires: python3-module-sphinx
#BuildRequires: python3-module-oslosphinx
#BuildRequires: python3-module-d2to1
#BuildRequires: python3-module-requests >= 1.1
#BuildRequires: python3-module-six >= 1.5.2
%endif

# /usr/bin/swift collision with older swift-im rhbz#857900
Conflicts: swift < 2.0-alt1

%description
Client library and command line utility for interacting with Openstack
Object Storage API.

%if_with python3
%package -n python3-module-swiftclient
Summary: Client Library for OpenStack Object Storage API
Group: Development/Python3
Requires: python3-module-requests

%description -n python3-module-swiftclient
Client library and command line utility for interacting with Openstack
Object Storage API.
%endif


%package doc
Summary: Documentation for OpenStack Object Storage API Client
Group: Development/Documentation

%description doc
Documentation for the client library for interacting with Openstack
Object Storage API.

%prep
%setup

# Let RPM handle the dependencies
rm -f test-requirements.txt requirements.txt

# Remove bundled egg-info
rm -rf python_swiftclient.egg-info
%if_with python3
rm -rf ../python3
cp -a . ../python3
%endif

%build
%python_build
%if_with python3
pushd ../python3
%python3_build
popd
%endif

%install
%if_with python3
pushd ../python3
%python3_install
popd
mv %buildroot%_bindir/swift %buildroot%_bindir/python3-swift
%endif

%python_install

# Delete tests
rm -fr %buildroot%python_sitelibdir/*/tests
rm -fr %buildroot%python3_sitelibdir/*/tests

export PYTHONPATH="$( pwd ):$PYTHONPATH"
pushd doc
make html
popd

install -p -D -m 644 doc/manpages/swift.1 %buildroot%_man1dir/swift.1

# Fix hidden-file-or-dir warnings
rm -fr doc/build/html/.doctrees doc/build/html/.buildinfo

%files
%doc LICENSE README.rst
%_bindir/swift
%python_sitelibdir/*
%_man1dir/swift.1*

%if_with python3
%files -n python3-module-swiftclient
%_bindir/python3-swift
%python3_sitelibdir/*
%endif

%files doc
%doc LICENSE doc/build/html

%changelog
* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 2.6.0-alt1.1
- NMU: Use buildreq for BR.

* Wed Dec 30 2015 Alexey Shabalin <shaba@altlinux.ru> 2.6.0-alt1
- 2.6.0

* Tue Mar 31 2015 Alexey Shabalin <shaba@altlinux.ru> 2.4.0-alt1
- 2.4.0

* Tue Mar 10 2015 Alexey Shabalin <shaba@altlinux.ru> 2.3.1-alt1
- 2.3.1
- add python3 package

* Tue Aug 12 2014 Lenar Shakirov <snejok@altlinux.ru> 2.1.0-alt1
- New version (based on Fedora 2.1.0-1.fc21.src)

* Thu Nov 08 2012 Pavel Shilovsky <piastry@altlinux.org> 1.7.0-alt1
- Initial release for Sisyphus (based on Fedora)
