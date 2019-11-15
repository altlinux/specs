%define testsdir %{_localstatedir}/%{name}/tests
%def_without bootstrap

Name: libtree
Version: 0.1.0
Release: alt2

Summary: C++ lib that helps to work with tree-like data structures
License: GPLv3
Group: Development/C++

Packager: Alexey Appolonov <alexey@altlinux.org>

# http://git.altlinux.org/people/alexey/packages/?p=libtree.git
Source: %{name}-%{version}.tar

BuildRequires: gcc-c++
BuildRequires: libxml++2-devel
BuildRequires: jsoncpp-devel >= 1.8.4

%description
%{summary}.

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

%package -n %{name}-devel
Summary: %{name} headers
Group: Development/Other

Requires: %{name}
BuildArch: noarch

Requires: libxml++2-devel
Requires: jsoncpp-devel >= 1.8.4

%description -n %{name}-devel
Development package for %{name}.

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

%if_without bootstrap
%package -n %{name}-checkinstall
Summary: Tests and test data for %{name}
Group: Other

BuildRequires: %{name}-devel

Requires: %{name}

%description -n %{name}-checkinstall
Tests and test data for %{name}.
%endif

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

%prep
%setup

%build
%make_build
%if_without bootstrap
%make_build -C ./tests
%endif

%install
mkdir -p %{buildroot}%{_libdir}
mkdir -p %{buildroot}%{_includedir}/%{name}
mkdir -p %{buildroot}%{_defaultdocdir}/%{name}
mkdir -p %{buildroot}%{testsdir}
# Executables
cp bin/%{name}.so %{buildroot}%{_libdir}
# Includes
cp src/*.h %{buildroot}%{_includedir}/%{name}
# Documentation
cp COPYING %{buildroot}%{_defaultdocdir}/%{name}/
# Tests
%if_without bootstrap
cp tests/bin/tests %{buildroot}%{testsdir}
cp -r tests/data %{buildroot}%{testsdir}
%endif

%if_without bootstrap
%post -n %{name}-checkinstall
cd %{testsdir}
./tests data
cd -
%endif

%files
%{_libdir}/*.so
%{_defaultdocdir}/%{name}

%files -n %{name}-devel
%{_includedir}/%{name}/

%if_without bootstrap
%files -n %{name}-checkinstall
%{testsdir}/*
%endif

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

%changelog
* Fri Nov 15 2019 Alexey Appolonov <alexey@altlinux.org> 0.1.0-alt2
- Build with tests activated.

* Fri Nov 15 2019 Alexey Appolonov <alexey@altlinux.org> 0.1.0-alt1
- Initial release;
- Tests are not yet activated.
