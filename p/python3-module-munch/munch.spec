%define oname munch

%def_with check

Name:               python3-module-munch
Version:            4.0.0
Release:            alt1

Summary:            A dot-accessible dictionary (a la JavaScript objects)

Group:              Development/Python3
License:            MIT
URL:                https://pypi.io/project/munch

Source:             %name-%version.tar

BuildArch:          noarch

BuildRequires:      rpm-build-python3
BuildRequires:      python3-module-pbr

%if_with check
BuildRequires:      python3-module-pytest
BuildRequires:      python3-module-six
%endif

%description
munch is a fork of David Schoonover's **Bunch** package, providing similar
functionality. 99 percent of the work was done by him, and the fork was made
mainly for lack of responsiveness for fixes and maintenance on the original
code.

Munch is a dictionary that supports attribute-style access, a la
JavaScript.

%prep
%setup

%build
export PBR_VERSION=%version
%python3_build

%install
export PBR_VERSION=%version
%python3_install

%check
py.test-3 -v

%files
%doc README.md LICENSE.txt
%python3_sitelibdir/%oname
%python3_sitelibdir/%oname-%version-py%_python3_version.egg-info

%changelog
* Mon Jul 17 2023 Grigory Ustinov <grenka@altlinux.org> 4.0.0-alt1
- Automatically updated to 4.0.0.

* Mon May 15 2023 Grigory Ustinov <grenka@altlinux.org> 3.0.0-alt1
- Automatically updated to 3.0.0.

* Thu Jul 28 2022 Grigory Ustinov <grenka@altlinux.org> 2.5.0-alt1
- Build new version.

* Wed Jul 28 2021 Grigory Ustinov <grenka@altlinux.org> 2.1.1-alt2
- Drop python2 support.

* Tue Jun 13 2017 Lenar Shakirov <snejok@altlinux.ru> 2.1.1-alt1
- Initial build for ALT (based on 2.1.1-1.fc27.src)

