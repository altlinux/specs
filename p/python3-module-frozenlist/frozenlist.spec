Name: python3-module-frozenlist
Version: 1.3.0
Release: alt1

Summary: A list-like structure which implements collections.abc.MutableSequence 
License: Apache-2.0
Group: Development/Python
Url: https://github.com/aio-libs/frozenlist

Source0: %name-%version-%release.tar

BuildRequires: rpm-build-python3 python3-module-setuptools
BuildRequires: /usr/bin/cython

%description
%summary

%prep
%setup
# use system cython
sed -i '/^cythonize:/ s,.install-cython,,' Makefile

%build
make cythonize
%python3_build build_ext

%install
%python3_install

%files
%python3_sitelibdir/frozenlist
%python3_sitelibdir/frozenlist-%version-*-info

%changelog
* Wed Feb 09 2022 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.3.0-alt1
- 1.3.0 released
