
Name:           python-module-configshell
License:        ASL 2.0
Group:          Development/Python
Summary:        A framework to implement simple but nice CLIs
Version:        1.1.fb25
Release:        alt1
URL:            https://github.com/open-iscsi/configshell-fb
Source:         %name-%version.tar
BuildArch:      noarch

BuildRequires: python-devel
BuildRequires: python-module-setuptools
BuildRequires: python-module-six

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-six


%description
A framework to implement simple but nice configuration-oriented
command-line interfaces.


%package -n python3-module-configshell
Summary:        A framework to implement simple but nice CLIs
Group:          Development/Python

%description -n python3-module-configshell
A framework to implement simple but nice configuration-oriented
command-line interfaces.

%prep
%setup

rm -rf ../python3
cp -a . ../python3

%build
%python_build

pushd ../python3
%python3_build
popd

%install
%python_install

pushd ../python3
%python3_install
popd

%files
%python_sitelibdir/*
%doc COPYING README.md

%files -n python3-module-configshell
%doc COPYING README.md
%python3_sitelibdir/*

%changelog
* Fri Dec 21 2018 Alexey Shabalin <shaba@altlinux.org> 1.1.fb25-alt1
- 1.1.fb25

* Thu Jul 31 2014 Lenar Shakirov <snejok@altlinux.ru> 1.1.fb13-alt1
- First build for ALT (based on Fedora 1.1.fb13-2.fc21.src)

