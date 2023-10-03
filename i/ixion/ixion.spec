Name: ixion
Version: 0.18.1
Release: alt1
Url: https://gitlab.com/ixion/ixion
License: MPL-2.0
Source: %name-%version.tar.gz
Group: Sciences/Mathematics
Summary: Threaded multi-target formula parser & interpreter

# Automatically added by buildreq on Thu Jan 13 2022
# optimized out: boost-devel boost-devel-headers glibc-kernheaders-generic glibc-kernheaders-x86 libgpg-error libstdc++-devel perl pkg-config python3 python3-base python3-module-Pygments python3-module-alabaster python3-module-babel python3-module-charset-normalizer python3-module-docutils python3-module-idna python3-module-imagesize python3-module-jinja2 python3-module-markupsafe python3-module-packaging python3-module-pkg_resources python3-module-pytz python3-module-requests python3-module-sphinx python3-module-urllib3 sh4 xz
BuildRequires: boost-filesystem-devel boost-program_options-devel ctags doxygen gcc-c++ mdds-devel python3-dev python3-module-breathe python3-module-sphinx_rtd_theme python3-module-sphinxcontrib-applehelp python3-module-sphinxcontrib-devhelp python3-module-sphinxcontrib-htmlhelp python3-module-sphinxcontrib-jsmath python3-module-sphinxcontrib-qthelp python3-module-sphinxcontrib-serializinghtml

## BuildRequires: boost-filesystem-devel boost-program_options-devel gcc-c++ mdds-devel python3-dev

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
* Fri Aug 25 2023 Daniel Zagaynov <kotopesutility@altlinux.org> 0.18.1-alt1
- Updated to 0.18.1

* Thu Jan 13 2022 Fr. Br. George <george@altlinux.ru> 0.17.0-alt1
- Initial build for ALT
