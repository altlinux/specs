Group: System/Libraries
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-cmake rpm-macros-fedora-compat
# END SourceDeps(oneline)
# redefine altlinux specific with and without
%define with()         %{expand:%%{?with_%{1}:1}%%{!?with_%{1}:0}}
%define without()      %{expand:%%{?with_%{1}:0}%%{!?with_%{1}:1}}
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
%define autorelease 31

#%%bcond icu 1
%global with_icu 1

Name:           xalan-c
Version:        1.12.0
# The soversion is made from the major and minor version numbers, e.g. 112 for
# version 1.12.x. We could do this automaticallya..
#   %%global so_version %%(echo %%{version} | cut -d . -f -2 | tr -d .)
# a..but we do not do so because we want to make sure we detect any soversion
# update.
%global so_version 112
Release:        alt1_%autorelease
Summary:        Xalan XSLT processor for C/C++

# The entire source is Apache-2.0, except cmake/RunTest.cmake, which is
# libtiff, but is a build-system file that does not contribute to the licenses
# of the binary RPMs.
License:        Apache-2.0
URL:            http://xalan.apache.org/xalan-c/
%global tag Xalan-C_%(echo '%{version}' | tr . _)
%global tar_name xalan_c-%(echo %{version} | cut -d . -f -2)
%global release_url https://github.com/apache/xalan-c/releases/download/%{tag}
Source0:        %{release_url}/%{tar_name}.tar.gz
Source1:        %{release_url}/%{tar_name}.tar.gz.asc
Source2:        %{release_url}/KEYS

BuildRequires:  gnupg2
BuildRequires:  ctest cmake
# Either make or ninja is supported.
BuildRequires:  ninja-build python3-module-ninja_syntax
BuildRequires:  gcc-c++
BuildRequires:  libxerces-c-devel
%if %{with icu}
BuildRequires:  icu-utils libicu-devel
%endif
Source44: import.info

%description
The Apache Xalan-C++ Project provides a library and a command line program to
transform XML documents using a stylesheet that conforms to XSLT 1.0 standards.

Xalan is a project of the Apache Software Foundation.


%package        devel
Group: Development/Other
Summary:        Development files for xalan-c
Requires:       xalan-c = %{version}-%{release}

%description devel
The xalan-c-devel package contains libraries and header files for developing
applications that use xalan-c.


%package doc
Group: Documentation
Summary:        Documentation for xalan-c
BuildArch: noarch

# Doxygen HTML help is not suitable for packaging due to a minified JavaScript
# bundle inserted by Doxygen itself. See discussion at
# https://bugzilla.redhat.com/show_bug.cgi?id=2006555.
#
# Normally, we would enable the Doxygen PDF documentation as a lesser
# substitute, but building it fails with:
#   ! TeX capacity exceeded, sorry [pool size=5905151].

%description doc
Documentation for xalan-c. See https://apache.github.io/xalan-c/ for full HTML
documentation.


%prep

%setup -q -n %{tar_name}


# https://github.com/apache/xalan-c/pull/35
chmod -v a-x NOTICE

# Remove the Autotools build system cruft from the samples; otherwise, it would
# be installed as documentation. We leave the CmakeLists.txt even though it
# cannot be used standalone; it is used in the build (even though the built
# samples are only tested and not installed), and is annoying to exclude.
rm -vf samples/configure samples/configure.in


%build
cp -at . -- /usr/share/gnu-config/config.{guess,sub}
%{fedora_v2_cmake} %{?with_icu:-Dtranscoder=icu} -GNinja
%fedora_v2_cmake_build


%install
%fedora_v2_cmake_install
# Remove CMake-installed docs in favor of using the doc macro. We refer to
# _prefix/share instead of _datadir to mirror how the install path is defined
# in the relevant CMakeLists.txt. Note also that we do *not* want to install
# the HTML version of the API documentation.
rm -rf %{buildroot}%{_prefix}/share/doc/xalan-c/api

# alt fixes for xalan-c.pc
sed -i 's,^Version:,Version: %version,;/^Cflags/d' %buildroot%_pkgconfigdir/xalan-c.pc

%check
%fedora_v2_ctest


%files
%doc --no-dereference LICENSE
%doc CREDITS
%doc KEYS
%doc NOTICE
%doc README.md

%{_bindir}/Xalan

%{_libdir}/libxalanMsg.so.%{so_version}
%{_libdir}/libxalanMsg.so.%{so_version}.*
%{_libdir}/libxalan-c.so.%{so_version}
%{_libdir}/libxalan-c.so.%{so_version}.*


%files devel
%{_libdir}/libxalanMsg.so
%{_libdir}/libxalan-c.so

%{_includedir}/xalanc/

%dir %{_libdir}/cmake/XalanC
%{_libdir}/cmake/XalanC/*.cmake

%{_libdir}/pkgconfig/xalan-c.pc


%files doc
%doc --no-dereference LICENSE

%doc CREDITS
%doc KEYS
%doc NOTICE
%doc README.md
%doc docs/*.md
%doc docs/images/
%doc samples/


%changelog
* Tue Oct 10 2023 Igor Vlasenko <viy@altlinux.org> 1.12.0-alt1_31
- update to new release by fcimport

* Thu Oct 14 2021 Igor Vlasenko <viy@altlinux.org> 1.12.0-alt1_15
- update to new release by fcimport

* Mon Jan 25 2021 Igor Vlasenko <viy@altlinux.ru> 1.12.0-alt1_4
- update to new release by fcimport

* Sun Dec 08 2019 Igor Vlasenko <viy@altlinux.ru> 1.11.0-alt1_16
- merged e2k patch

* Fri Oct 20 2017 Igor Vlasenko <viy@altlinux.ru> 1.11.0-alt1_12
- update to new release by fcimport

* Tue Jul 26 2016 Igor Vlasenko <viy@altlinux.ru> 1.11.0-alt1_9
- update to new release by fcimport

* Sun Dec 27 2015 Igor Vlasenko <viy@altlinux.ru> 1.11.0-alt1_8
- update to new release by fcimport

* Mon Nov 09 2015 Igor Vlasenko <viy@altlinux.ru> 1.11.0-alt1_7
- new version

* Thu Jul 10 2014 Igor Vlasenko <viy@altlinux.ru> 1.11.0-alt1_4
- dependency

