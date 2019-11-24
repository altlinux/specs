%define testsdir %{_localstatedir}/%{name}/tests

Name: libtree
Version: 0.3.0
Release: alt1

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

%package -n %{name}-checkinstall
Summary: Tests and test data for %{name}
Group: Other

Requires: %{name}

%description -n %{name}-checkinstall
Tests and test data for %{name}.

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

%prep
%setup

%build
%make_build
%make_build -C ./tests

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
cp tests/bin/tests %{buildroot}%{testsdir}
cp -r tests/data %{buildroot}%{testsdir}

%post -n %{name}-checkinstall
cd %{testsdir}
./tests data
cd -

%files
%{_libdir}/*.so
%{_defaultdocdir}/%{name}

%files -n %{name}-devel
%{_includedir}/%{name}/

%files -n %{name}-checkinstall
%{testsdir}/*

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

%changelog
* Sat Nov 23 2019 Alexey Appolonov <alexey@altlinux.org> 0.3.0-alt1
- Shorter representation of JSON bool values.

* Sat Nov 23 2019 Alexey Appolonov <alexey@altlinux.org> 0.2.0-alt1
- Corrected and modified JSON procedures;
- Using headers and lib from buildroot to build checkinstall package,
  no bootstrapping is needed.

* Fri Nov 15 2019 Alexey Appolonov <alexey@altlinux.org> 0.1.0-alt2
- Build with tests activated.

* Fri Nov 15 2019 Alexey Appolonov <alexey@altlinux.org> 0.1.0-alt1
- Initial release;
- Tests are not yet activated.
