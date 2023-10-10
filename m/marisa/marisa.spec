BuildRequires: chrpath
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-perl rpm-build-python rpm-build-python3 rpm-build-ruby
BuildRequires: perl-podlators
# END SourceDeps(oneline)
Group: Development/C
%add_optflags %optflags_shared
%define fedora 38
# fedora bcond_with macro
%define bcond_with() %{expand:%%{?_with_%{1}:%%global with_%{1} 1}}
%define bcond_without() %{expand:%%{!?_without_%{1}:%%global with_%{1} 1}}
# redefine altlinux specific with and without
%define with()         %{expand:%%{?with_%{1}:1}%%{!?with_%{1}:0}}
%define without()      %{expand:%%{?with_%{1}:0}%%{!?with_%{1}:1}}
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
# python2 is not available on RHEL > 7 and not needed on Fedora > 28
%if 0%{?rhel} > 7 || 0%{?fedora} > 28
# disable python2 by default
%bcond_with python2
%else
%bcond_without python2
%endif

Name:          marisa
Version:       0.2.6
Release:       alt1_5
Summary:       Static and spece-efficient trie data structure library

License:       BSD-2-Clause OR LGPL-2.1-or-later
URL:  https://github.com/s-yata/marisa-trie
Source0: https://github.com/s-yata/marisa-trie/archive/refs/tags/v%{version}.tar.gz#/%{name}-%{version}.tar.gz

BuildRequires: autoconf, automake, libtool
BuildRequires: gcc
BuildRequires: gcc-c++
BuildRequires: swig
BuildRequires: perl-devel
BuildRequires: rpm-build-perl
%if %{with python2}
BuildRequires: python-devel
%endif
BuildRequires: python3-devel
BuildRequires: python3-module-pkg_resources python3-module-setuptools
BuildRequires: libruby-devel
Source44: import.info

%description
Matching Algorithm with Recursively Implemented StorAge (MARISA) is a
static and space-efficient trie data structure. And libmarisa is a C++
library to provide an implementation of MARISA. Also, the package of
libmarisa contains a set of command line tools for building and
operating a MARISA-based dictionary.

A MARISA-based dictionary supports not only lookup but also reverse
lookup, common prefix search and predictive search.

%package -n libmarisa0
Summary:        Shared library for the %name library
Group:          System/Libraries
Provides: marisa0 = %{version}-%{release}

%description -n libmarisa0
Matching Algorithm with Recursively Implemented StorAge (MARISA) is a
static and space-efficient trie data structure. And libmarisa is a C++
library to provide an implementation of MARISA. Also, the package of
libmarisa contains a set of command line tools for building and
operating a MARISA-based dictionary.

A MARISA-based dictionary supports not only lookup but also reverse
lookup, common prefix search and predictive search.

This package contains the shared library.


%package -n libmarisa-devel
Group: Development/C
Summary:       Development files for %{name}
Requires:      libmarisa0 = %EVR
Provides: %name-devel = %EVR
Provides: marisa-devel = %{version}-%{release}

%description -n libmarisa-devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.


%package tools
Group: Development/C
Summary:       Tools for %{name}
Requires:      libmarisa0 = %EVR

%description tools
The %{name}-tools package contains tools for developing applications
that use %{name}.


%package perl
Group: Development/C
Summary:       Perl language binding for marisa
Requires:      libmarisa0 = %EVR

%description perl
Perl language binding for marisa


%if %{with python2}
%package -n python-module-marisa
Group: Development/C
Summary:       Python language binding for marisa
Requires:      libmarisa0 = %EVR
# Remove before F30
Provides:      %{name}-python = %{version}-%{release}
Provides:      %{name}-python = %{version}-%{release}
Obsoletes:     %{name}-python < %{version}-%{release}
%{?python_provide:%python_provide python2-%{name}}

%description -n python-module-marisa
Python 2 language binding for marisa
%endif


%package -n python3-module-marisa
Group: Development/C
Summary:       Python 3 language binding for marisa
Requires:      libmarisa0 = %EVR
%{?python_provide:%python_provide python3-%{name}}

%description -n python3-module-marisa
Python 3 language binding for marisa


%package ruby
Group: Development/C
Summary: Ruby language binding for marisa
Requires:      libmarisa0 = %EVR

%description ruby
Ruby language binding for groonga


%prep
%setup -q -n %{name}-trie-%{version}



%build


autoreconf -i
%configure --disable-static
sed -i 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' libtool
sed -i 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' libtool
%{make_build}

# build Perl bindings
pushd bindings/perl
/usr/bin/perl Makefile.PL INC="-I%{_builddir}/%{name}-trie-%{version}/include" LIBS="-L%{_builddir}/%{name}-trie-%{version}/lib/%{name}/.libs -lmarisa" INSTALLDIRS=vendor
%{make_build}
popd

# build Python bindings
# Regenerate Python bindings
%{make_build} --directory=bindings swig-python

pushd bindings/python
%if %{with python2}
%{__python} setup.py build_ext --include-dirs="%{_builddir}/%{name}-trie-%{version}/include" --library-dirs="%{_builddir}/%{name}-trie-%{version}/lib/%{name}/.libs"
%python_build
%endif

%{__python3} setup.py build_ext --include-dirs="%{_builddir}/%{name}-trie-%{version}/include" --library-dirs="%{_builddir}/%{name}-trie-%{version}/lib/%{name}/.libs"
%python3_build
popd

# build Ruby bindings
# Regenerate ruby bindings
pushd bindings
%{make_build} swig-ruby
popd

pushd bindings/ruby
ruby extconf.rb --with-opt-include="%{_builddir}/%{name}-trie-%{version}/include" --with-opt-lib="%{_builddir}/%{name}-trie-%{version}/lib/%{name}/.libs" --vendor
%{make_build}
popd

%install
%makeinstall_std INSTALL="install -p"

# install Perl bindings
pushd bindings/perl
%makeinstall_std INSTALL="install -p"
# Remove hidden files
rm -f %{buildroot}%{perl_vendor_archlib}/auto/marisa/.packlist
# %{_fixperms} -c %{buildroot}%{perl_vendor_archlib}/*
popd

# install Python bindings
pushd bindings/python
%if %{with python2}
%python_install
%endif
%python3_install
rm -rf %{buildroot}/%{python3_sitelibdir}/marisa-0.0.0-py%{__python3_version}.egg-info
popd

# install Ruby bindings
pushd bindings/ruby
%if 0%{?fedora} || 0%{?rhel} > 7
%makeinstall_std INSTALL="install -p"
%else
%makeinstall_std INSTALL="install -p" hdrdir=%{_includedir} arch_hdrdir="%{_includedir}/\$(arch)" rubyhdrdir=%{_includedir}
%endif
popd

find $RPM_BUILD_ROOT -name '*.la' -exec rm -f {} ';'
find $RPM_BUILD_ROOT -name 'perllocal.pod' -exec rm -f {} ';'
rm -f $RPM_BUILD_ROOT%{perl_vendor_archlib}/sample.pl


chrpath -d %buildroot%{perl_vendor_archlib}/auto/marisa/*.so



%files -n libmarisa0
%doc docs/style.css AUTHORS README.md docs/readme.en.html
%lang(ja) %doc docs/readme.ja.html
%doc --no-dereference COPYING.md
%_libdir/libmarisa.so.0
%_libdir/libmarisa.so.0.*

%files -n libmarisa-devel
%{_includedir}/marisa*
%{_libdir}/*.so
%{_libdir}/pkgconfig/*.pc

%files tools
%{_bindir}/marisa-benchmark
%{_bindir}/marisa-build
%{_bindir}/marisa-common-prefix-search
%{_bindir}/marisa-dump
%{_bindir}/marisa-lookup
%{_bindir}/marisa-predictive-search
%{_bindir}/marisa-reverse-lookup

%files perl
%{perl_vendor_archlib}/marisa.pm
%{perl_vendor_archlib}/auto/marisa
%{perl_vendor_archlib}/benchmark.pl

%if %{with python2}
%files -n python-module-marisa
%{python_sitelibdir}/_marisa.so
%{python_sitelibdir}/marisa.py*
%{python_sitelibdir}/marisa-0.0.0-py2.?.egg-info
%endif

%files -n python3-module-marisa
%{python3_sitelibdir}/__pycache__/marisa*
%{python3_sitelibdir}/_marisa*.so
%{python3_sitelibdir}/marisa.py

%files ruby
%{ruby_vendorarchdir}/marisa.so

%changelog
* Tue Oct 10 2023 Igor Vlasenko <viy@altlinux.org> 0.2.6-alt1_5
- update to new release by fcimport

* Wed Sep 28 2022 Igor Vlasenko <viy@altlinux.org> 0.2.4-alt1_57
- new version

