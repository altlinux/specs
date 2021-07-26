Name:           python3-module-configshell
License:        Apache-2.0
Group:          Development/Python3
Summary:        A framework to implement simple but nice CLIs
Version:        1.1.fb25
Release:        alt2
URL:            https://github.com/open-iscsi/configshell-fb
Source:         %name-%version.tar
BuildArch:      noarch

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-six

%description
A framework to implement simple but nice configuration-oriented
command-line interfaces.

%prep
%setup

%build
%python3_build

%install
%python3_install

%files
%doc COPYING README.md
%python3_sitelibdir/*

%changelog
* Mon Jul 26 2021 Grigory Ustinov <grenka@altlinux.org> 1.1.fb25-alt2
- Drop python2 support.

* Fri Dec 21 2018 Alexey Shabalin <shaba@altlinux.org> 1.1.fb25-alt1
- 1.1.fb25

* Thu Jul 31 2014 Lenar Shakirov <snejok@altlinux.ru> 1.1.fb13-alt1
- First build for ALT (based on Fedora 1.1.fb13-2.fc21.src)

