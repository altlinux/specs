%define PCRE /usr/include/pcre/

%define with_sce 1

Name: openscap
Version: 1.3.4
Release: alt1

Summary: Set of open source libraries enabling integration of the SCAP line of standards
License: LGPLv2+
Group: Other
URL: http://www.open-scap.org/

# https://github.com/OpenSCAP/%{name}/releases/download/%{version}/%{name}-%{version}.tar.gz
Source0: %{name}-%{version}.tar

BuildRequires: cmake >= 3
BuildRequires: gcc
BuildRequires: gcc-c++
BuildRequires: swig libxml2-devel libxslt-devel perl-XML-Parser
BuildRequires: rpm-devel
BuildRequires: libgcrypt-devel
BuildRequires: pcre-devel
BuildRequires: libacl-devel
BuildRequires: libselinux-devel libcap-devel
BuildRequires: libblkid-devel
BuildRequires: bzip2-devel
BuildRequires: asciidoc
BuildRequires: openldap-devel
BuildRequires: libGConf-devel
BuildRequires: libdbus-devel
BuildRequires: python3-devel
%ifdef with_check
BuildRequires: ctest
BuildRequires: perl-XML-XPath
BuildRequires: bzip2
%endif
Obsoletes: python2-openscap
Obsoletes: openscap-content-sectool
Obsoletes: openscap-extra-probes
Obsoletes: openscap-extra-probes-sql

%description
OpenSCAP is a set of open source libraries providing an easier path
for integration of the SCAP line of standards. SCAP is a line of standards
managed by NIST with the goal of providing a standard language
for the expression of Computer Network Defense related information.

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

%package devel
Summary: Development files for %{name}
Group: Other

Requires: %{name}%{?_isa} = %{version}-%{release}
Requires: libxml2-devel
Requires: pkgconfig
BuildRequires: doxygen

%description devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

%ifdef with_bindings
%package -n python3-module-openscap
Summary: Python 3 bindings for %{name}
Group: Development/Python3

Requires: %{name}%{?_isa} = %{version}-%{release}
Provides: openscap-python = %{version}-%{release}

%description -n python3-module-openscap
The %{name}-python3 package contains the bindings so that %{name}
libraries can be used by python3.

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

%package -n perl-openscap
Summary: OpenSCAP Perl Library
Group: Development/Perl

Requires: %{name} = %{version}-%{release}
Requires: perl
Provides: openscap-perl = %{version}-%{release}

%description -n perl-openscap
The OpenSCAP Perl Library for easy integration with SCAP.
%endif

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

%package scanner
Summary: OpenSCAP Scanner Tool (oscap)
Group: Other

Requires: %{name}%{?_isa} = %{version}-%{release}
Requires: libcurl >= 7.12.0
BuildRequires: libcurl-devel >= 7.12.0
Obsoletes: openscap-selinux
Obsoletes: openscap-selinux-compat

%description scanner
The %{name}-scanner package contains oscap command-line tool. The oscap
is configuration and vulnerability scanner, capable of performing
compliance checking using SCAP content.

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

%package utils
Summary: OpenSCAP Utilities
Group: Other

Requires: %{name}%{?_isa} = %{version}-%{release}
Requires: rpmdevtools rpm-build
Requires: %{name}-scanner%{?_isa} = %{version}-%{release}

%description utils
The %{name}-utils package contains command-line tools build on top
of OpenSCAP library. Historically, openscap-utils included oscap
tool which is now separated to %{name}-scanner sub-package.

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

%ifdef with_sce
%package engine-sce
Summary: Script Check Engine plug-in for OpenSCAP
Group: Other

Requires: %{name}%{?_isa} = %{version}-%{release}

%description engine-sce
The Script Check Engine is non-standard extension to SCAP protocol. This
engine allows content authors to avoid OVAL language and write their assessment
commands using a scripting language (Bash, Perl, Python, Ruby, ...).

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

%package engine-sce-devel
Summary: Development files for %{name}-engine-sce
Group: Other

Requires: %{name}-devel%{?_isa} = %{version}-%{release}
Requires: %{name}-engine-sce%{?_isa} = %{version}-%{release}
Requires: pkgconfig

%description engine-sce-devel
The %{name}-engine-sce-devel package contains libraries and header files
for developing applications that use %{name}-engine-sce.
%endif

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

%package containers
Summary: Utils for scanning containers
Group: Other

Requires: %{name} = %{version}-%{release}
Requires: %{name}-scanner
BuildArch: noarch

%description containers
Tool for scanning Atomic containers.

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

%prep
%setup -q
mkdir build

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

%build
cd build
cmake %{?_cmake_skip_rpath} \
	-DCMAKE_SKIP_INSTALL_RPATH:BOOL=yes \
	-DCMAKE_C_FLAGS:STRING="%{optflags} -I%{PCRE}" \
	-DCMAKE_CXX_FLAGS:STRING="%{optflags} -I%{PCRE}" \
	-DPCRE_INCLUDE_DIR="%{PCRE}" \
	-DCMAKE_INSTALL_PREFIX="%{prefix}" \
	-DINCLUDE_INSTALL_DIR:PATH="%{_includedir}" \
	-DLIB_INSTALL_DIR:PATH="%{_libdir}" \
	-DSYSCONF_INSTALL_DIR:PATH="%{_sysconfdir}" \
	-DSHARE_INSTALL_PREFIX:PATH="%{_datadir}" \
	-DLIB_DESTINATION="%{_lib}" \
	%if "%{_lib}" == "lib64"
	-DLIB_SUFFIX="64" \
	%else
	-DLIB_SUFFIX="" \
	%endif
	%ifndef with_bindings
	-DENABLE_PYTHON3=FALSE \
	-DENABLE_PERL=FALSE \
	%endif
	%ifndef with_sce
	-DENABLE_SCE=OFF \
	%endif
	-DENABLE_DOCS=ON \
	..
%make_build
%make_build docs

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

%check
%ifdef with_check
ctest -V %{?_smp_mflags}
%endif

%install
cd build
%make_install DESTDIR=%{buildroot} install
cd ..
cp AUTHORS NEWS README.md COPYING docs/oscap-scan.cron \
	%{buildroot}%{_defaultdocdir}/%{name}/

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

%files
%{_defaultdocdir}/%{name}/AUTHORS
%{_defaultdocdir}/%{name}/NEWS
%{_defaultdocdir}/%{name}/README.md
%{_defaultdocdir}/%{name}/COPYING
%{_defaultdocdir}/%{name}/manual/
%dir %{_datadir}/openscap
%dir %{_datadir}/openscap/schemas
%dir %{_datadir}/openscap/xsl
%dir %{_datadir}/openscap/cpe
%{_libdir}/libopenscap.so.*
%{_datadir}/openscap/schemas/*
%{_datadir}/openscap/xsl/*
%{_datadir}/openscap/cpe/*

%ifdef with_bindings
%files -n python3-module-openscap
%{_libdir}/python3/site-packages/*

%files -n perl-openscap
%{perl_vendorlib}/vendor_perl/openscap_pm.pm
%{perl_vendorarch}/vendor_perl/openscap_pm.so
%endif

%files devel
%{_defaultdocdir}/%{name}/html/
%{_libdir}/libopenscap.so
%{_libdir}/pkgconfig/*.pc
%{_includedir}/openscap
%ifdef with_sce
%exclude %{_includedir}/openscap/sce_engine_api.h
%endif

%ifdef with_sce
%files engine-sce-devel
%{_libdir}/libopenscap_sce.so
%{_includedir}/openscap/sce_engine_api.h
%endif

%files scanner
%{_mandir}/man8/oscap.8.xz
%{_bindir}/oscap
%{_bindir}/oscap-chroot
%{_sysconfdir}/bash_completion.d

%files utils
%{_defaultdocdir}/%{name}/oscap-scan.cron
%{_mandir}/man8/*
%exclude %{_mandir}/man8/oscap.8.xz
%exclude %{_mandir}/man8/oscap-docker.8.xz
%{_bindir}/*
%exclude %{_bindir}/oscap
%exclude %{_bindir}/oscap-docker
%exclude %{_bindir}/oscap-chroot

%ifdef with_sce
%files engine-sce
%{_libdir}/libopenscap_sce.so.*
%endif

%files containers
%{_bindir}/oscap-docker
%{_mandir}/man8/oscap-docker.8.xz
%{python3_sitelibdir_noarch}/oscap_docker_python/*

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

%changelog
* Fri Apr 09 2021 Alexey Appolonov <alexey@altlinux.org> 1.3.4-alt1
- New version;
- Build of the openscap-engine-sce package is enabled.

* Mon Apr 01 2019 Alexey Appolonov <alexey@altlinux.org> 1.3.0-alt1
- Initial ALT Linux release;
- openscap-engine-sce is excluded from the build due to undefined symbol
  in libopenscap_sce.so.25.0.0.
