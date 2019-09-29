Group: Other
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-fedora-compat
BuildRequires: boost-locale-devel
# END SourceDeps(oneline)
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
%global gh_commit ec9672b6cd883193be8451ee4cedab593420ae19
%global gh_short     %(c=%{gh_commit}; echo ${c:0:7})
%global gh_owner  artyom-beilis
%global gh_project nowide
%if 0%{?rhel} && 0%{?rhel} <= 7
%global boost_suffix 169
%global cmake_suffix 3
%global cmake %%cmake%{cmake_suffix}
%endif

Name:       boost-nowide
Version:    0
Release:    alt1_20190813.git%{gh_short}
Summary:    Boost.Nowide makes cross platform Unicode aware programming easier.

License:    Boost
URL:        https://github.com/%{gh_owner}/%{gh_project}

# This is a header only library
BuildArch:  noarch

Source0:    https://github.com/%{gh_owner}/%{gh_project}/archive/%{gh_commit}.tar.gz#/%{name}-%{gh_short}.tar.gz

# Use upstream pull request to have proper cmake files for shared library building
Patch0: https://patch-diff.githubusercontent.com/raw/%{gh_owner}/%{gh_project}/pull/27.patch#/%{name}-PR-27.patch


BuildRequires: ccmake cmake ctest
BuildRequires: gcc-c++
BuildRequires: boost%{?boost_suffix}-devel

# To create the docs
BuildRequires: doxygen
Source44: import.info

%package devel
Group: Other
Requires: %{name} == %{version}-%{release}
# nowide is a header only library on linux
Provides: boost-nowide-static = %{version}-%{release}

Summary: The header files to compile against boost.nowide

%package docs
Group: Other
Requires: %{name} == %{version}-%{release}
Summary: Documentation for using the nowide boost module
BuildArch: noarch

%description
Boost.Nowide is a library implemented by Artyom Beilis
that makes cross platform Unicode aware programming
easier.

The library provides an implementation of standard C and C++ library
functions, such that their inputs are UTF-8 aware on Windows without
requiring to use Wide API.

%description devel
Development files for building against boost-nowide

%description docs
This provides the documentation for boost.nowide in html format.

%prep
%setup -q -n %{gh_project}-%{gh_commit}
%patch0 -p1



%build
# Need to build the static for install and tests to pass
%{fedora_cmake} . -DNOWIDE_BUILD_STATIC=ON -DNOWIDE_SYSTEM_INCLUDE=ON \
         -DBOOST_INCLUDEDIR=%{_includedir}/boost%{?boost_suffix} \
         -DBOOST_LIBRARYDIR=%{_libdir}/boost%{?boost_suffix}
make %{gh_project}

# Build the docs
cd doc
doxygen

%install
%makeinstall_std
# It's header only on linux so remove the libraries generated
rm -f %{buildroot}/usr/lib*/libnowide*

%if %{defined boost_suffix}
mkdir -p %{buildroot}%{_includedir}/boost%{boost_suffix}/boost
mv %{buildroot}%{_includedir}/boost/nowide %{buildroot}%{_includedir}/boost%{boost_suffix}/boost/
rmdir %{buildroot}%{_includedir}/boost
%endif

%check
%__make test

%files
%doc --no-dereference doc/LICENSE_1_0.txt

%files docs
%doc doc/html


%files devel
%if %{undefined boost_suffix}
%{_includedir}/boost/nowide
%else
%{_includedir}/boost%{boost_suffix}/boost/nowide
%endif

%changelog
* Sun Sep 29 2019 Igor Vlasenko <viy@altlinux.ru> 0-alt1_20190813.gitec9672b
- new version

