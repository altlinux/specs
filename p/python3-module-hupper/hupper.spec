%define oname hupper

Name:           python3-module-%oname
Version:        1.0
Release:        alt2

Summary:        Integrated process monitor for developing servers
Group:          Development/Python3
License:        MIT
BuildArch:      noarch
URL:            https://pypi.python.org/pypi/%{oname}
# https://github.com/Pylons/hupper.git

Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-dev python3(pytest) python3(pytest_cov) python3(watchdog) python3(mock)


%description
hupper is an integrated process monitor that will track changes
to any imported Python files in sys.modules as well as custom paths.
When files are changed the process is restarted.

%prep
%setup

sed -i 's|#!/usr/bin/env python|#!/usr/bin/env python3|' \
    $(find ./ -name '*.py')

%build
%python3_build

%install
%python3_install

%check
PYTHONPATH=%buildroot%python3_sitelibdir py.test3

%files
%doc CHANGES.rst CONTRIBUTING.rst LICENSE.txt README.rst rtd.txt
%python3_sitelibdir/*
%_bindir/*


%changelog
* Tue Nov 12 2019 Andrey Bychkov <mrdrew@altlinux.org> 1.0-alt2
- disable python2

* Sun Oct 14 2018 Igor Vlasenko <viy@altlinux.ru> 1.0-alt1.qa1
- NMU: applied repocop patch

* Mon Oct 16 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 1.0-alt1
- Initial build for ALT.

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sun Feb 19 2017 Kevin Fenzi <kevin@scrye.com> - 0.4.2-1
- Initial version for Fedora. 

