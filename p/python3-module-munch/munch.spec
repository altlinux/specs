%global modname munch

Name:               python3-module-munch
Version:            2.1.1
Release:            alt2
Summary:            A dot-accessible dictionary (a la JavaScript objects)

Group:              Development/Python3
License:            MIT
URL:                https://pypi.io/project/munch
Source0:            %modname-%version.tar

BuildArch:          noarch

BuildRequires:      rpm-build-python3

%description
munch is a fork of David Schoonover's **Bunch** package, providing similar
functionality. 99 percent of the work was done by him, and the fork was made
mainly for lack of responsiveness for fixes and maintenance on the original
code.

Munch is a dictionary that supports attribute-style access, a la
JavaScript.

%prep
%setup -n %modname-%version

# Remove shebang to make rpmlint happy.
sed -i '/\/usr\/bin\/python/d' munch/__init__.py

# Remove bundled egg-info in case it exists
rm -rf %modname.egg-info

%build
%python3_build

%install
%python3_install

%files
%doc README.md LICENSE.txt
%python3_sitelibdir/%modname/
%python3_sitelibdir/%modname-%{version}*

%changelog
* Wed Jul 28 2021 Grigory Ustinov <grenka@altlinux.org> 2.1.1-alt2
- Drop python2 support.

* Tue Jun 13 2017 Lenar Shakirov <snejok@altlinux.ru> 2.1.1-alt1
- Initial build for ALT (based on 2.1.1-1.fc27.src)

