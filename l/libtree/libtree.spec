%define testsdir %{_localstatedir}/%{name}/tests

Name: libtree
Version: 0.9.0
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

%package -n %{name}-tests
Summary: Tests and test data for %{name}
Group: Other

Requires: %{name}

%description -n %{name}-tests
Tests and test data for %{name}.

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

%package -n %{name}-checkinstall
Summary: Tests and test data for %{name}
Group: Other

Requires: %{name}-tests

%description -n %{name}-checkinstall
Package that runs tests in a build environment.

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

%pre -n %{name}-checkinstall
set -e
cd %{testsdir}
./tests data
cd -

%files
%{_libdir}/*.so
%{_defaultdocdir}/%{name}

%files -n %{name}-devel
%{_includedir}/%{name}/

%files -n %{name}-tests
%{testsdir}/*

%files -n %{name}-checkinstall

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

%changelog
* Sat Nov 05 2022 Alexey Appolonov <alexey@altlinux.org> 0.9.0-alt1
- Empty node names are allowed;
- Empty branch drafts are allowed;
- Node names are accepted as a value if no value is found.

* Wed Nov 10 2021 Alexey Appolonov <alexey@altlinux.org> 0.8.0-alt1
- Ability to customize the format of a string representation of selected data.

* Thu Oct 14 2021 Alexey Appolonov <alexey@altlinux.org> 0.7.1-alt1
- Corrected JSON handler (the bug was introduced in the libtree v0.7.0).

* Mon Oct 11 2021 Alexey Appolonov <alexey@altlinux.org> 0.7.0-alt1
- Algorithm of the XML handler is brought into compliance with the algorithm
  of the JSON handler;
- Corrected ALT Linux "checkinstall" testing scheme;
- Modified tests;
- Build with debuginfo enabled.

* Fri May 28 2021 Alexey Appolonov <alexey@altlinux.org> 0.6.0-alt1
- Improved API;
- Ability to have optional nodes in branch drafts;
- Ability to index selected values.

* Thu Feb 18 2021 Alexey Appolonov <alexey@altlinux.org> 0.5.2-alt1
- Fixed XML parsing;
- Validation of XML documents is optional (disabled by default).

* Tue Feb 16 2021 Alexey Appolonov <alexey@altlinux.org> 0.5.1-alt1
- Corrected handling of exceptions (the code is heavily refactored, be aware!).

* Thu Nov 19 2020 Alexey Appolonov <alexey@altlinux.org> 0.5.0-alt1
- Ability to reserve tree items by passing empty branch drafts.

* Fri Feb 07 2020 Alexey Appolonov <alexey@altlinux.org> 0.4.0-alt1
- Handling attributes of '<...>:<attribute_name>' format;
- Ability to avoid empty lines in string representation of selected data.

* Mon Dec 02 2019 Alexey Appolonov <alexey@altlinux.org> 0.3.1-alt1
- Corrected stringification.

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
