%define oname plaster-pastedeploy

Name: python3-module-%oname
Version: 0.4.1
Release: alt2

Summary: A PasteDeploy binding to the plaster configuration loader
License: MIT
Group: Development/Python3
URL: https://github.com/Pylons/plaster_pastedeploy
BuildArch: noarch

# https://github.com/Pylons/plaster_pastedeploy.git
Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-dev python3(paste.deploy) python3(plaster) python3(pytest)

%py3_requires paste.deploy


%description
plaster_pastedeploy is a plaster plugin that provides a
plaster.Loader that can parse ini files according to the standard set
by PasteDeploy. It supports the wsgi plaster protocol, implementing
the plaster.protocols.IWSGIProtocol interface.

%prep
%setup

%build
%python3_build

%install
%python3_install

%check
PYTHONPATH="./src" py.test3

%files
%doc CHANGES.rst LICENSE.txt README.rst
%python3_sitelibdir/*


%changelog
* Fri Dec 06 2019 Andrey Bychkov <mrdrew@altlinux.org> 0.4.1-alt2
- build for python2 disabled

* Sun Oct 14 2018 Igor Vlasenko <viy@altlinux.ru> 0.4.1-alt1.qa1
- NMU: applied repocop patch

* Tue Oct 17 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 0.4.1-alt1
- Initial build for ALT.

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Jul 08 2017 Randy Barlow <bowlofeggs@fedoraproject.org> - 0.3.2-2
- Depend on python2-paste-deploy instead of python-paste-deploy.

* Mon Jul 03 2017 Randy Barlow <bowlofeggs@fedoraproject.org> - 0.3.2-1
- Initial release.
