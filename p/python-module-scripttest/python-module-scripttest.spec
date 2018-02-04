%define module_name scripttest
%def_with python3

Name:		python-module-scripttest
Version:	1.3
Release:	alt1.1
Summary:	Helper to test command-line scripts

Group:		Development/Python
License:	MIT
URL:		http://pypi.python.org/pypi/ScriptTest/
Source0:	%{name}-%{version}.tar.gz
# Issue preventing build and usage on ext4.
BuildArch:	noarch

BuildRequires:	python-devel python-module-setuptools

%if_with python3
BuildRequires(pre): rpm-build-python3 python3-module-setuptools
%endif

%description
ScriptTest is a library to help you test your interactive
command-line applications.

With it you can easily run the command (in a subprocess) and see
the output (stdout, stderr) and any file modifications.

%if_with python3
%package -n python3-module-%module_name
Summary: Helper to test command-line scripts
Group: Development/Python3

%description -n python3-module-%module_name
ScriptTest is a library to help you test your interactive
command-line applications.

With it you can easily run the command (in a subprocess) and see
the output (stdout, stderr) and any file modifications.
%endif

%prep
%setup

%if_with python3
cp -fR . ../python3
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
%python_sitelibdir/*


%if_with python3
%files -n python3-module-%module_name
%python3_sitelibdir/*
%endif

%changelog
* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 1.3-alt1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Sun Jun 04 2017 Lenar Shakirov <snejok@altlinux.ru> 1.3-alt1
- Version 1.3
- Python3 enabled

* Sat Sep 15 2012 Pavel Shilovsky <piastry@altlinux.org> 1.0.4-alt1
- Initial release for Sisyphus (based on Fedora)
