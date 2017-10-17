%define oname plaster-pastedeploy

%def_with python3

Name: python-module-%oname
Version: 0.4.1
Release: alt1
BuildArch: noarch
Group: Development/Python

License: MIT
Summary: A PasteDeploy binding to the plaster configuration loader
URL:     https://github.com/Pylons/plaster_pastedeploy

# https://github.com/Pylons/plaster_pastedeploy.git
Source: %name-%version.tar

BuildRequires: python-dev python2.7(paste.deploy) python2.7(plaster) python2.7(pytest)
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildRequires: python3-dev python3(paste.deploy) python3(plaster) python3(pytest)
%endif

%py_requires paste.deploy

%description
plaster_pastedeploy is a plaster plugin that provides a
plaster.Loader that can parse ini files according to the standard set
by PasteDeploy. It supports the wsgi plaster protocol, implementing
the plaster.protocols.IWSGIProtocol interface.

%package -n python3-module-%oname
Summary:  A PasteDeploy binding to the plaster configuration loader
Group: Development/Python3
%py3_requires paste.deploy

%description -n python3-module-%oname
plaster_pastedeploy is a plaster plugin that provides a
plaster.Loader that can parse ini files according to the standard set
by PasteDeploy. It supports the wsgi plaster protocol, implementing
the plaster.protocols.IWSGIProtocol interface.

%prep
%setup

%if_with python3
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
%python_install

%if_with python3
pushd ../python3
%python3_install
popd
%endif

%check
PYTHONPATH="./src" py.test

%if_with python3
pushd ../python3
PYTHONPATH="./src" py.test3
popd
%endif

%files
%doc CHANGES.rst LICENSE.txt README.rst
%python_sitelibdir/*

%files -n python3-module-%oname
%doc CHANGES.rst LICENSE.txt README.rst
%python3_sitelibdir/*

%changelog
* Tue Oct 17 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 0.4.1-alt1
- Initial build for ALT.

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Jul 08 2017 Randy Barlow <bowlofeggs@fedoraproject.org> - 0.3.2-2
- Depend on python2-paste-deploy instead of python-paste-deploy.

* Mon Jul 03 2017 Randy Barlow <bowlofeggs@fedoraproject.org> - 0.3.2-1
- Initial release.
