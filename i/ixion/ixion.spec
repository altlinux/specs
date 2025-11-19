Name: ixion
Version: 0.20.0
Release: alt1
Url: https://gitlab.com/ixion/ixion
License: MPL-2.0
Source: %name-%version.tar.gz
Group: Sciences/Mathematics
Summary: Threaded multi-target formula parser & interpreter

BuildRequires: boost-filesystem-devel
BuildRequires: boost-program_options-devel
BuildRequires: ctags
BuildRequires: doxygen
BuildRequires: gcc-c++
BuildRequires: mdds-devel
BuildRequires: python3-dev
BuildRequires: python3-module-breathe >= 4.36.0
BuildRequires: python3-module-sphinx_piccolo_theme
BuildRequires: python3-module-sphinx_rtd_theme
BuildRequires: python3-module-sphinxcontrib-applehelp
BuildRequires: python3-module-sphinxcontrib-devhelp
BuildRequires: python3-module-sphinxcontrib-htmlhelp
BuildRequires: python3-module-sphinxcontrib-jsmath
BuildRequires: python3-module-sphinxcontrib-qthelp
BuildRequires: python3-module-sphinxcontrib-serializinghtml

%description
Ixion is a general purpose formula parser, interpreter, formula cell
dependency tracker and spreadsheet document model backend all in one
package.

%package -n lib%name
Group: Development/C++
Summary: Threaded multi-target formula parser & interpreter library

%description -n lib%name
%summary

%package -n lib%name-devel
Group: Development/C++
Summary: Threaded multi-target formula parser & interpreter library, development

%description -n lib%name-devel
%summary

%package -n python3-module-%name
Group:  Development/Python3
Summary: Python biondings for %name, a general purpose formula parser and interpreter

%description -n python3-module-%name
%summary

%prep
%setup
sed -i 's/sphinx-build/sphinx-build-3/g' Makefile.am

%build
%autoreconf
%configure CXXFLAGS="-fexcess-precision=fast"
%make_build
%make_build doc

%install
%makeinstall_std

%check
%make_build check

%files
%doc README.md
%_bindir/*

%files -n lib%name
%_libdir/lib*.so.*

%files -n lib%name-devel
%doc doc/_build
%_includedir/*
%_libdir/lib*.so
%_pkgconfigdir/*.pc

%files -n python3-module-%name
%python3_sitelibdir/*

%changelog
* Mon Oct 27 2025 Andrey Cherepanov <cas@altlinux.org> 0.20.0-alt1
- Updated to 0.20.0

* Fri Feb 02 2024 Daniel Zagaynov <kotopesutility@altlinux.org> 0.19.0-alt1
- Updated to 0.19.0

* Fri Aug 25 2023 Daniel Zagaynov <kotopesutility@altlinux.org> 0.18.1-alt1
- Updated to 0.18.1

* Thu Jan 13 2022 Fr. Br. George <george@altlinux.ru> 0.17.0-alt1
- Initial build for ALT
