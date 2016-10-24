%def_with python3

Name: python-module-novaclient
Version: 6.0.0
Release: alt1
Summary: Python API and CLI for OpenStack Nova

Group: Development/Python
License: ASL 2.0
Url: http://docs.openstack.org/developer/python-novaclient
Source: %name-%version.tar

BuildArch: noarch

Requires: python-module-simplejson
Requires: python-module-keystoneclient
#Requires: python-module-keyring

BuildRequires: python-devel
BuildRequires: python-module-d2to1
BuildRequires: python-module-setuptools
BuildRequires: python-module-pbr >= 1.6
BuildRequires: python-module-sphinx
BuildRequires: python-module-oslosphinx
BuildRequires: python-module-reno >= 1.8.0
BuildRequires: python-module-keystoneauth1 >= 2.10.0
BuildRequires: python-module-iso8601 >= 0.1.11
BuildRequires: python-module-oslo.i18n >= 2.1.0
BuildRequires: python-module-oslo.serialization >= 1.10.0
BuildRequires: python-module-oslo.utils >= 3.16.0
BuildRequires: python-module-prettytable >= 0.7
BuildRequires: python-module-requests >= 2.10.0
BuildRequires: python-module-simplejson >= 2.2.0
BuildRequires: python-module-six >= 1.9.0
BuildRequires: python-module-babel >= 2.3.4

BuildRequires: python-module-keystoneclient >= 2.0.0
BuildRequires: python-module-cinderclient >= 1.6.0
BuildRequires: python-module-glanceclient >= 2.3.0

%if_with python3
BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-pbr >= 1.6
BuildRequires: python3-module-keystoneauth1 >= 2.10.0
BuildRequires: python3-module-babel >= 2.3.4
BuildRequires: python3-module-six >= 1.9.0
BuildRequires: python3-module-iso8601 >= 0.1.11
BuildRequires: python3-module-prettytable >= 0.7
BuildRequires: python3-module-requests >= 2.10.0
BuildRequires: python3-module-oslo.utils >= 3.16.0
BuildRequires: python3-module-oslo.serialization >= 1.10.0
BuildRequires: python3-module-simplejson >= 2.2.0

BuildRequires: python3-module-keystoneclient >= 2.0.0
BuildRequires: python3-module-cinderclient >= 1.6.0
BuildRequires: python3-module-glanceclient >= 2.3.0

%endif

%description
This is a client for the OpenStack Nova API. There's a Python API (the
novaclient module), and a command-line script (nova). Each implements 100 percent of
the OpenStack Nova API.

%if_with python3
%package -n python3-module-novaclient
Summary: Python API and CLI for OpenStack Nova
Group: Development/Python3
Requires: python3-module-simplejson
Requires: python3-module-keystoneclient
#Requires: python3-module-keyring

%description -n python3-module-novaclient
This is a client for the OpenStack Nova API. There's a Python API (the
novaclient module), and a command-line script (nova). Each implements 100 percent of
the OpenStack Nova API.
%endif


%package doc
Summary: Documentation for OpenStack Nova API Client
Group: Development/Documentation

%description doc
This is a client for the OpenStack Nova API. There's a Python API (the
novaclient module), and a command-line script (nova). Each implements 100 percent of
the OpenStack Nova API.

This package contains auto-generated documentation.

%prep
%setup

# Remove bundled egg-info
rm -rf python_novaclient.egg-info

# Let RPM handle the requirements
rm -f {,test-}requirements.txt

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

# disabling git call for last modification date from git repo
sed '/^html_last_updated_fmt.*/,/.)/ s/^/#/' -i doc/source/conf.py
python setup.py build_sphinx
# Fix hidden-file-or-dir warnings
rm -fr doc/build/html/.buildinfo

%install
%if_with python3
pushd ../python3
%python3_install
popd
mv %buildroot%_bindir/nova %buildroot%_bindir/python3-nova
%endif

%python_install

mkdir -p %buildroot%_sysconfdir/bash_completion.d
install -pm 644 tools/nova.bash_completion \
    %buildroot%_sysconfdir/bash_completion.d/nova

# Delete tests
rm -fr %buildroot%python_sitelibdir/tests
rm -fr %buildroot%python_sitelibdir/*/tests
rm -fr %buildroot%python3_sitelibdir/tests
rm -fr %buildroot%python3_sitelibdir/*/tests

install -p -D -m 644 doc/build/man/nova.1 %buildroot%_man1dir/nova.1

%files
%doc README.rst
%doc LICENSE
%_bindir/nova
%python_sitelibdir/*
%_sysconfdir/bash_completion.d
%_man1dir/nova.*

%if_with python3
%files -n python3-module-novaclient
%_bindir/python3-nova
%python3_sitelibdir/*
%endif

%files doc
%doc doc/build/html

%changelog
* Tue Oct 18 2016 Alexey Shabalin <shaba@altlinux.ru> 6.0.0-alt1
- 6.0.0

* Thu Apr 14 2016 Alexey Shabalin <shaba@altlinux.ru> 3.3.1-alt1
- 3.3.1

* Mon Mar 28 2016 Alexey Shabalin <shaba@altlinux.ru> 2.30.2-alt1
- 2.30.2

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 2.30.1-alt1.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 2.30.1-alt1.1
- NMU: Use buildreq for BR.

* Thu Oct 29 2015 Alexey Shabalin <shaba@altlinux.ru> 2.30.1-alt1
- 2.30.1

* Fri Oct 02 2015 Alexey Shabalin <shaba@altlinux.ru> 2.23.2-alt2
- drop Requires: python-module-keyring

* Tue Aug 25 2015 Alexey Shabalin <shaba@altlinux.ru> 2.23.2-alt1
- 2.23.2

* Tue Mar 31 2015 Alexey Shabalin <shaba@altlinux.ru> 2.23.0-alt1
- 2.23.0

* Tue Mar 10 2015 Alexey Shabalin <shaba@altlinux.ru> 2.22.0-alt1
- 2.22.0
- add python3 package

* Thu Jul 24 2014 Lenar Shakirov <snejok@altlinux.ru> 2.17.0-alt1
- New version (based on Fedora 2.17.0-2.fc21.src)

* Thu Sep 27 2012 Pavel Shilovsky <piastry@altlinux.org> 2.8.0.26-alt1
- Initial release for Sisyphus (based on Fedora)

