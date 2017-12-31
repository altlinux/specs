%global with_check 0

%add_python3_compile_include %_libexecdir/uranium

Name:    Uranium
Version: 3.0.3
Release: alt1

Summary:  A Python framework for building Desktop applications.
License: LGPL-3.0
Group:   Development/Python3
URL:     https://github.com/Ultimaker/Uranium

Packager: Anton Midyukov <antohami@altlinux.org>

BuildRequires(pre): rpm-build-python3 rpm-macros-cmake
BuildRequires: python3-devel cmake
BuildRequires:  %_bindir/doxygen
BuildRequires:  %_bindir/msgmerge

# Tests
%if 0%{?with_check}
BuildRequires:  python3-module-Arcus = %version
BuildRequires:  python3-module-numpy
BuildRequires:  python3-module-scipy
BuildRequires:  python3-module-PyQt5
BuildRequires:  python3-module-pytest
BuildRequires:  python3-module-typing
%endif

#Requires: python3-module-typing

BuildArch: noarch

Source: %name-%version.tar

%description
%summary

%package doc
Summary: Documentation for %name package
Group: Documentation

%description doc
Documentation for Uranium, a Python framework for building 3D printing
related applications.

%prep
%setup
# Upstream installs to lib/python3/dist-packages
# We want to install to %%{python3_sitelib}
sed -i 's|lib/python${PYTHON_VERSION_MAJOR}/dist-packages|%(echo %python3_sitelibdir | sed -e s@%_prefix/@@)|g' CMakeLists.txt

# empty file. appending to the end to make sure we are not overriding
# a non empty file in the future
echo '# empty' >> UM/Settings/ContainerRegistryInterface.py

%build
%cmake
%cmake_build
%cmake_build doc

%install
%cmakeinstall_std
mv %buildroot/%_datadir/cmake-* %buildroot/%_datadir/cmake

# Sanitize the location of locale files
pushd %buildroot%_datadir
mv uranium/resources/i18n locale
ln -s ../../locale uranium/resources/i18n
rm locale/uranium.pot
rm locale/*/uranium.po
popd

%find_lang uranium

%check
%if 0%{?with_check}
pip3 freeze
# The failing tests are reported at:
# https://github.com/Ultimaker/Uranium/issues/225
# Skipping
%_bindir/python3 -m pytest -v -k "not getMimeTypeForFile"
%endif

%files -f uranium.lang
%doc LICENSE README.md
%python3_sitelibdir/*
%_libexecdir/uranium
%_datadir/uranium
%_datadir/cmake/Modules/*

%files doc
%doc html LICENSE

%changelog
* Sun Dec 31 2017 Anton Midyukov <antohami@altlinux.org> 3.0.3-alt1
- New version 3.0.3

* Wed Nov 22 2017 Anton Midyukov <antohami@altlinux.org> 2.4.0-alt1
- Initial build for Sisyphus
