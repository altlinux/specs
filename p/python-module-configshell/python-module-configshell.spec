%def_without python3

Name:           python-module-configshell
License:        ASL 2.0
Group:          Development/Python
Summary:        A framework to implement simple but nice CLIs
Version:        1.1.fb13
Release:        alt1
URL:            https://github.com/agrover/configshell-fb
Source:         %{name}-%{version}.tar
BuildArch:      noarch
BuildRequires:  python-devel python-module-setuptools
Requires: python-module-pyparsing python-module-urwid

%description
A framework to implement simple but nice configuration-oriented
command-line interfaces.

%if_with python3
%package -n python3-module-configshell
Summary:        A framework to implement simple but nice CLIs
Group:          Development/Python
BuildArch:      noarch
BuildRequires:  rpm-build-python3
BuildRequires:  python3-module-setuptools
Requires:       python3-module-pyparsing python3-module-urwid

%description -n python3-module-configshell
A framework to implement simple but nice configuration-oriented
command-line interfaces.

%endif

%prep
%setup

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
%python_install

%if_with python3
pushd ../python3
%python3_install
popd
%endif

%files
%{python_sitelibdir}/*
%doc COPYING README.md

%if_with python3
%files -n python3-module-configshell
%doc COPYING README.md
%{python3_sitelibdir}/*
%endif

%changelog
* Thu Jul 31 2014 Lenar Shakirov <snejok@altlinux.ru> 1.1.fb13-alt1
- First build for ALT (based on Fedora 1.1.fb13-2.fc21.src)

