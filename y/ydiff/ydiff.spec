%global __ospython %{_bindir}/python3
%global python3_sitelib %(%{__ospython} -c "from distutils.sysconfig import get_python_lib; print(get_python_lib())")

Name:		ydiff
Version:	1.2
Release:	alt1
Summary:	View colored, incremental diff
Group:          File tools
URL:		https://github.com/ymattw/ydiff
License:	BSD
Source0:	%{name}-%{version}.tar
BuildRequires:	python3-devel python3-module-setuptools sed
BuildArch:	noarch

Requires:	python3-module-%{name}
%description
Term based tool to view colored, incremental diff in a Git/Mercurial/Svn
workspace or from stdin, with side by side (similar to diff -y) and auto
pager support.

%package -n	python3-module-%{name}
Summary:	%{summary}
%{?python_provide:%python_provide python3-%{name}}
Group:          File tools
%description -n	python3-module-%{name}
Python library that implements API used by ydiff tool.

%prep
%setup -n %name-%version
/bin/sed -i '/#!\/usr\/bin\/env python/d' ydiff.py

%build
%{__ospython} setup.py build

%install
%{__rm} -rf %{buildroot}
%{__ospython} setup.py install --root %{buildroot} -O1 --skip-build

%files
%doc README.rst
%doc LICENSE
%{_bindir}/ydiff

%files -n python3-module-%{name}
%{python3_sitelib}/__pycache__/*
%{python3_sitelib}/%{name}.py
%{python3_sitelib}/%{name}-%{version}-py%{_python3_version}.egg-info

%changelog
* Fri Oct 07 2022 Ilfat Aminov <aminov@altlinux.org> 1.2-alt1
- initial build for alt sisyphus

* Thu Oct 1 2020 Devrim Gündüz <devrim@gunduz.org> - 1.2-10
- Initial packaging for the PostgreSQL RPM repository to satisfy Patroni
  dependency. Took the spec file from Fedora rawhide.
