%define modname podcastparser
%def_enable check

Name: python-module-%modname
Version: 0.6.3
Release: alt1

Summary: Simple, fast and efficient podcast parser written in Python.
Group: Development/Python
License: BSD
Url: http://gpodder.org/%modname

BuildArch: noarch

Source: %url/%modname-%version.tar.gz

BuildRequires: python-devel python-module-setuptools python-modules-json
BuildRequires: python3-devel rpm-build-python3 python3-module-setuptools
# for check
BuildRequires: python-test python3-test python-module-nose python3-module-nose

%description
The podcast parser project is a library from the gPodder project to provide an
easy and reliable way of parsing RSS- and Atom-based podcast feeds in Python.

%package -n python3-module-%modname
Summary: Simple, fast and efficient podcast parser written in Python3.
Group: Development/Python3
License: BSD

%description -n python3-module-%modname
The podcast parser project is a library from the gPodder project to provide an
easy and reliable way of parsing RSS- and Atom-based podcast feeds in Python.


%prep
%setup -n %modname-%version -a0
mv %modname-%version py3build

%build
%python_build

pushd py3build
%python3_build
popd

%install
%python_install

pushd py3build
%python3_install
popd

%if_enabled check
%check
%__python test_%modname.py

pushd py3build
%__python3 test_%modname.py
popd
%endif

%files
%python_sitelibdir_noarch/%{modname}*
%doc README.md

%files -n python3-module-%modname
%python3_sitelibdir_noarch/%{modname}*
%python3_sitelibdir_noarch/__pycache__/%{modname}*
%doc README.md

%changelog
* Wed Jan 31 2018 Yuri N. Sedunov <aris@altlinux.org> 0.6.3-alt1
- 0.6.3

* Fri Nov 03 2017 Yuri N. Sedunov <aris@altlinux.org> 0.6.2-alt1
- 0.6.2

* Sun Jan 08 2017 Yuri N. Sedunov <aris@altlinux.org> 0.6.1-alt1
- first build for Sisyphus


