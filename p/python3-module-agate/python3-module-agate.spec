%def_with doc
%define  modulename agate

Name:    python3-module-%modulename
Version: 1.6.0
Release: alt1

Summary: A Python data analysis library that is optimized for humans instead of machines.
License: MIT
Group:   Development/Python3
URL:     https://github.com/wireservice/agate

Packager: Mikhail Gordeev <obirvalger@altlinux.org>

BuildRequires(pre): rpm-build-python3 python3-module-setuptools
BuildRequires: python3-dev
%{?_with_doc:BuildRequires: python3-module-sphinx-sphinx-build-symlink}

BuildArch: noarch

Source:  %modulename-%version.tar
Patch0: %name-%version-alt-disable-import-sphinx_rtd_them.patch

%description
agate is a Python data analysis library that is optimized for humans instead of
machines. It is an alternative to numpy and pandas that solves real-world
problems with readable code.

%prep
%setup -n %modulename-%version
%patch0 -p1

%build
%python3_build

%if_with doc
cd docs
make man text
cd -
%endif

%install
%python3_install

%if_with doc
mkdir -p %buildroot%_man1dir
cp docs/_build/man/*.1 %buildroot%_man1dir
%endif

%files
%python3_sitelibdir/%modulename/
%python3_sitelibdir/*.egg-info
%if_with doc
%doc %_man1dir/*
%doc docs/_build/text/*
%endif

%changelog
* Wed Feb 07 2018 Mikhail Gordeev <obirvalger@altlinux.org> 1.6.0-alt1
- Initial build for Sisyphus
