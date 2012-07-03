BuildRequires: rpm-build-mingw32
BuildRequires: gcc-c++
Name:           mingw32-cxxtest
Version:        3.10.1
Release:        alt1_5
Summary:        A JUnit-like testing framework for C++

Group:          Development/Tools
License:        LGPLv2+
URL:            http://cxxtest.tigris.org
Source0:        http://cxxtest.tigris.org/files/documents/6421/43281/cxxtest-%{version}.tar.gz

BuildArch:      noarch

BuildRequires:  mingw32-filesystem
Requires:       mingw32-filesystem

# Remove the -doc subpackage as it duplicates what's in native cxxtest-doc
Obsoletes:      mingw32-cxxtest-doc < 3.10.1-5
Source44: import.info

%description
CxxTest is a JUnit/CppUnit/xUnit-like framework for C++.
Its advantages over existing alternatives are that it:
 - doesn't require RTTI
 - doesn't require member template functions
 - doesn't require exception handling
 - doesn't require any external libraries (including memory management,
   file/console I/O, graphics libraries)


%prep
%setup -q -n cxxtest

%build


%install
mkdir -p $RPM_BUILD_ROOT/%{_mingw32_includedir}/cxxtest
install -D -p -m 644 cxxtest/* $RPM_BUILD_ROOT/%{_mingw32_includedir}/cxxtest


%files
%doc COPYING
%{_mingw32_includedir}/cxxtest/


%changelog
* Wed Aug 17 2011 Igor Vlasenko <viy@altlinux.ru> 3.10.1-alt1_5
- initial release by fcimport

