%define oname cinderclient


Name: python-module-%oname
Version: 4.0.1
Release: alt1
Epoch: 1
Summary: Python API and CLI for OpenStack Cinder

Group: Development/Python
License: Apache-2.0
Url: http://docs.openstack.org/developer/python-%oname
Source: https://tarballs.openstack.org/python-%oname/python-%oname-%version.tar.gz

BuildArch: noarch

BuildRequires: python-devel
BuildRequires: python-module-setuptools
BuildRequires: python-module-pbr >= 2.0.0
BuildRequires: python-module-prettytable >= 0.7.1
BuildRequires: python-module-keystoneauth1 >= 3.4.0
BuildRequires: python-module-simplejson >= 3.5.1
BuildRequires: python-module-babel >= 2.3.4
BuildRequires: python-module-six >= 1.10.0
BuildRequires: python-module-oslo.i18n >= 3.15.3
BuildRequires: python-module-oslo.utils >= 3.33.0
BuildRequires: python-module-oslo.serialization >= 2.18.0

BuildRequires: python-module-sphinx
BuildRequires: python-module-openstackdocstheme >= 1.18.1
BuildRequires: python-module-reno >= 2.5.0


BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-pbr >= 2.0.0
BuildRequires: python3-module-prettytable >= 0.7.1
BuildRequires: python3-module-keystoneauth1 >= 3.4.0
BuildRequires: python3-module-simplejson >= 3.5.1
BuildRequires: python3-module-babel >= 2.3.4
BuildRequires: python3-module-six >= 1.10.0
BuildRequires: python3-module-oslo.i18n >= 3.15.3
BuildRequires: python3-module-oslo.utils >= 3.33.0
BuildRequires: python3-module-oslo.serialization >= 2.18.0

BuildRequires: python3-module-sphinx
BuildRequires: python3-module-openstackdocstheme >= 1.18.1
BuildRequires: python3-module-reno >= 2.5.0

%description
This is a client for the OpenStack Cinder API. There's a Python API (the cinderclient module), and a command-line script (cinder). Each implements 100%% of the OpenStack Cinder API.

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR

%description tests
This package contains tests for %oname.

%package -n python3-module-%oname
Summary: Python API and CLI for OpenStack Cinder
Group: Development/Python3

%description -n python3-module-%oname
This is a client for the OpenStack Cinder API. There's a Python API (the cinderclient module), and a command-line script (cinder). Each implements 100%% of the OpenStack Cinder API.

%package -n python3-module-%oname-tests
Summary: Tests for %oname
Group: Development/Python3
Requires: python3-module-%oname = %EVR

%description -n python3-module-%oname-tests
This package contains tests for %oname.

%prep
%setup -n python-%oname-%version

# Remove bundled egg-info
rm -rf python_cinderclient.egg-info

# Let RPM handle the requirements
rm -f {,test-}requirements.txt

rm -rf ../python3
cp -a . ../python3

%build
%python_build

pushd ../python3
%python3_build
popd

#sed -i 's/warn.*//' ./setup.cfg
# disabling git call for last modification date from git repo
#sed '/^html_last_updated_fmt.*/,/.)/ s/^/#/' -i doc/source/conf.py
python3 setup.py build_sphinx
# for some reason previous command no longer autogenerates manpage
PBR_VERSION=%version %make -C doc html

mkdir man/
cp -fR doc/build/html/* man/

# Fix hidden-file-or-dir warnings
rm -fr doc/*/html/.buildinfo

%install
%python_install
mv %buildroot%_bindir/cinder %buildroot%_bindir/cinder.py2

pushd ../python3
%python3_install
popd

install -p -D -m 644 tools/cinder.bash_completion %buildroot%_sysconfdir/bash_completion.d/cinder.bash_completion
# install -p -D -m 644 doc/build/man/cinder.1 %buildroot%_man1dir/cinder.1

%files
%doc LICENSE *.rst man/
%_bindir/cinder.py2
%python_sitelibdir/*
%_sysconfdir/bash_completion.d/cinder.bash_completion
# %_man1dir/cinder.1*
%exclude %python_sitelibdir/*/tests

%files tests
%python_sitelibdir/*/tests

%files -n python3-module-%oname
%doc LICENSE *.rst man/
%_bindir/cinder
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*/tests

%files -n python3-module-%oname-tests
%python3_sitelibdir/*/tests

%changelog
* Mon Dec 10 2018 Alexey Shabalin <shaba@altlinux.org> 1:4.0.1-alt1
- 4.0.1

* Tue Aug 14 2018 Andrey Bychkov <mrdrew@altlinux.org> 1:3.5.0-alt2
- Rebuild with openstackdocstheme

* Wed Mar 28 2018 Andrey Bychkov <mrdrew@altlinux.org> 1:3.5.0-alt1
- Updated to version 3.5.0
  Fixed sphinx_doc errors

* Mon Mar 12 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 1:1.11.0-alt2
- Updated build dependencies.

* Mon May 29 2017 Alexey Shabalin <shaba@altlinux.ru> 1:1.11.0-alt1
- 1.11.0
- add test packages

* Tue Oct 18 2016 Alexey Shabalin <shaba@altlinux.ru> 1:1.9.0-alt1
- 1.9.0

* Wed Apr 13 2016 Alexey Shabalin <shaba@altlinux.ru> 1:1.6.0-alt1
- 1.6.0

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 1:1.4.0-alt1.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 1:1.4.0-alt1.1
- NMU: Use buildreq for BR.

* Thu Oct 29 2015 Alexey Shabalin <shaba@altlinux.ru> 1:1.4.0-alt1
- 1.4.0

* Thu Oct 15 2015 Alexey Shabalin <shaba@altlinux.ru> 1:1.1.2-alt1
- 1.1.2
- fixed version

* Tue Mar 10 2015 Alexey Shabalin <shaba@altlinux.ru> 1.11.1-alt1
- 1.11.1
- add python3 package

* Wed Jul 23 2014 Lenar Shakirov <snejok@altlinux.ru> 1.0.9-alt1
- New version (based on Fedora 1.0.9-1.fc21.src)

* Thu Sep 27 2012 Pavel Shilovsky <piastry@altlinux.org> 0.2.26-alt1
- Initial release for Sisyphus (based on Fedora)
