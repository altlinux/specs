Group: Other
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
%global debug_package %{nil}
# debug info was always empty, so disable for now

Name:           picojson
Summary:        A header-file-only, JSON parser / serializer in C++
Version:        1.3.0
Release:        alt1_8

License:        BSD
# http://opensource.org/licenses/BSD-2-Clause
URL:            https://github.com/kazuho/picojson
Source0:        https://github.com/kazuho/%{name}/archive/v%{version}/%{name}-%{version}.tar.gz

BuildRequires:  gcc-c++
Source44: import.info

%description
PicoJSON is a tiny JSON parser / serializer for C++ with following properties:
Header-file only, No external dependencies (only uses standard C++ libraries),
STL-friendly (arrays are represented by using std::vector, objects are std::map)
provides both pull interface and streaming (event-based) interface.

%package devel
Group: Other
Summary:        Header files for picojson development
Provides:       %{name}-static = %{version}-%{release}

%description devel
Provide header file for %{name}.

%prep
%setup -qn %{name}-%{version}

%build
echo "Nothing to do"

%check
make test

%install
mkdir -p %{buildroot}%{_includedir}
install -p -m 0644 picojson.h %{buildroot}%{_includedir}/picojson.h

%files devel
%{_includedir}/picojson.h
%doc LICENSE README.mkdn examples

%changelog
* Mon Sep 30 2019 Igor Vlasenko <viy@altlinux.ru> 1.3.0-alt1_8
- new version

