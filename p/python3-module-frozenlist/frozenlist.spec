Name: python3-module-frozenlist
Version: 1.3.3
Release: alt1

Summary: A list-like structure which implements collections.abc.MutableSequence 
License: Apache-2.0
Group: Development/Python
Url: https://github.com/aio-libs/frozenlist

Source0: %name-%version-%release.tar

BuildRequires: rpm-build-python3
BuildRequires: python3(setuptools)
BuildRequires: python3(wheel)
BuildRequires: python3(cython)

%description
%summary

%prep
%setup
# use system cython
sed -i '/^cythonize:/ s,.install-cython,,' Makefile

%build
make cythonize
%pyproject_build

%install
%pyproject_install

%files
%python3_sitelibdir/frozenlist
%python3_sitelibdir/frozenlist-%version.dist-info

%changelog
* Tue Jan 24 2023 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.3.3-alt1
- 1.3.3 released

* Wed Feb 09 2022 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.3.0-alt1
- 1.3.0 released
