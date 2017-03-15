%def_with python3

Summary: Make reStructuredText and Sphinx read and render Doxygen xml output
Version: 4.6.0
Release: alt1
%setup_python_module breathe
Name: python-module-breathe
Source0: breathe-%version.tar.gz
License: BSD
Group: Development/Python
Url: https://github.com/michaeljones/breathe
Buildarch: noarch

BuildPreReq: python-devel
##python-module-setuptools-tests
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel
##python3-module-setuptools-tests
%endif

# Automatically added by buildreq on Mon Jul 11 2016
# optimized out: python-base python-devel python-module-PyStemmer python-module-cssselect python-modules python-modules-compiler python-modules-ctypes python-modules-email python-modules-encodings python3 python3-base
BuildRequires: python-module-docutils python-module-ecdsa python-module-html5lib python-module-pycrypto python-module-pytz python-module-setuptools python-module-snowballstemmer python3-dev python3-module-setuptools

%description
Breathe is an extension to reStructuredText and Sphinx to be able to read and render the Doxygen xml output.

%if_with python3
%package -n python3-module-breathe
Summary: Make reStructuredText and Sphinx read and render Doxygen xml output
Group: Development/Python3
Buildarch: noarch

%description -n python3-module-breathe
Breathe is an extension to reStructuredText and Sphinx to be able to read and render the Doxygen xml output.
%endif

%prep
%setup -n %modulename-%version

%if_with python3
cp -fR . ../python3
%endif

%build
%python_build_debug

%if_with python3
pushd ../python3
%python3_build_debug
popd
%endif

%install
%if_with python3
pushd ../python3
%python3_install
popd
mv %buildroot/%_bindir/breathe-apidoc %buildroot/%_bindir/python3-breathe-apidoc
%endif

%python_install

%files
%python_sitelibdir_noarch/*
%_bindir/breathe-apidoc

%if_with python3
%files -n python3-module-breathe
%python3_sitelibdir_noarch/*
%_bindir/python3-breathe-apidoc
%endif

%changelog
* Mon Mar 13 2017 Fr. Br. George <george@altlinux.ru> 4.6.0-alt1
- Autobuild version bump to 4.6.0

* Mon Jul 11 2016 Fr. Br. George <george@altlinux.ru> 4.2.0-alt1
- Initial build for ALT

