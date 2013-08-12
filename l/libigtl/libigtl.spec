# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-fedora-compat
BuildRequires: gcc-c++
# END SourceDeps(oneline)
Group: Other
%add_optflags %optflags_shared
%define fedora 19
%global _short_name igtl
%global _full_name openigtlink
%global _full_cap_name OpenIGTLink
%global _ver_major 1
%global _ver_minor 9
%global _ver_release 7

Name:		lib%{_short_name}
Version:	%{_ver_major}.%{_ver_minor}.%{_ver_release}
Release:	alt1_11
Summary:	Network communication library for image-guided therapy

License:	BSD
URL:		https://github.com/openigtlink/OpenIGTLink/
Source0:	https://github.com/openigtlink/OpenIGTLink/tarball/development/openigtlink-OpenIGTLink-00c007f.tar.gz

# Generate documentation: sent upstream https://github.com/openigtlink/OpenIGTLink/pull/6
Patch0:		%{name}-0001-Add-generation-of-doxygen-documentation.patch
Patch1:		%{name}-0002-Add-doxygen-and-papers-dir.patch
Patch2:		%{name}-0003-Use-original-doxyfile.patch
# fix build on non-x86 arches
Patch3:		%{name}-0004-sign-ness-of-char-type-is-platform-dependent.patch

BuildRequires: ctest cmake
# For documentation:
BuildRequires: /usr/bin/latex texlive-latex-recommended
BuildRequires:	gnuplot
BuildRequires:	graphviz
BuildRequires:	doxygen
# Including fonts for fedora 18 and later
%if 0%{?fedora} >= 18
BuildRequires:	texlive-latex-recommended
BuildRequires:	texlive-fonts-recommended
BuildRequires:	texlive-fonts-recommended
%endif
Source44: import.info


%description
OpenIGTLink provides a standardized mechanism for communications among computers
and devices in operating rooms (OR) for wide variety of image-guided therapy 
(IGT) applications. Examples of such applications include:

* Stereotactic surgical guidance using optical position sensor.
* Intraoperative image guidance using real-time MRI.
* Robot-assisted intervention with robotic device + surgical planning software

OpenIGTLink is a set of digital messaging formats and rules (protocol) used 
for data exchange on a local area network (LAN). The specification of 
OpenIGTLink and its reference implementation, the OpenIGTLink Library, are 
available free of charge for any purpose including commercial use. 

An OpenIGTLink interface is available in popular medical image processing and 
visualization software 3D Slicer.

%package	devel
Group: Other
Summary:	Development files for %{name}
Requires:	%{name}%{?_isa} = %{version}-%{release}

%description	devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%package	doc
Summary:	Documentation for %{name}
Group:		Documentation
Requires:	%{name}%{?_isa} = %{version}-%{release}

%description	doc
The %{name}-doc package contains documentation for %{name}

%prep
%setup -q -n %{_full_name}-%{_full_cap_name}-4caf9cf
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1

# Build documentation with pdflatex instead of latex + dvips
sed -i s/dvips/pdftex/ Documents/Papers/InsightJournal2008/OpenIGTLinkIJ2008.tex

%build
mkdir -p %{_target_platform}
pushd %{_target_platform}
%{fedora_cmake} .. \
    -DBUILD_SHARED_LIBS:BOOL=ON \
    -DBUILD_EXAMPLES:BOOL=ON \
    -DCMAKE_BUILD_TYPE:STRING="RelWithDebInfo"\
    -DCMAKE_VERBOSE_MAKEFILE=ON\
    -DOpenIGTLink_INSTALL_LIB_DIR=%{_lib} \
    -DOpenIGTLink_INSTALL_PACKAGE_DIR=%{_libdir}/cmake/%{_full_cap_name}/ \
    -DBUILD_TESTING=ON \
    -DBUILD_DOCUMENTATION=ON \
    -DPDFLATEX_COMPILER=%{_bindir}/pdflatex

popd

make %{?_smp_mflags} -C %{_target_platform}

%install
%makeinstall_std -C %{_target_platform}

find %{buildroot} -name '*.la' -exec rm -f {} ';'

# Install documentation
mkdir -p %{buildroot}%{_docdir}/%{name}-%{version}
cp LICENSE.txt %{buildroot}%{_docdir}/%{name}-%{version}/
cp README %{buildroot}%{_docdir}/%{name}-%{version}/

pushd %{_target_platform}
cp Documents/Papers/InsightJournal2008/OpenIGTLinkIJ2008.pdf %{buildroot}%{_docdir}/%{name}-%{version}/
cp -r Documents/Doxygen/html %{buildroot}%{_docdir}/%{name}-%{version}/
popd

%check
make test -C %{_target_platform}

%files
%dir %{_docdir}/%{name}-%{version}
%{_docdir}/%{name}-%{version}/LICENSE.txt
%{_docdir}/%{name}-%{version}/README
%{_libdir}/*.so.*
# hack; explicitly added docdir if not owned
%doc %dir %{_docdir}/%{name}-%{version}

%files devel
%dir %{_includedir}/%{_short_name}/
%{_includedir}/%{_short_name}/*
%{_libdir}/*.so
%{_libdir}/cmake/%{_full_cap_name}/

%files doc
%{_docdir}/%{name}-%{version}/OpenIGTLinkIJ2008.pdf
%{_docdir}/%{name}-%{version}/html/
# hack; explicitly added docdir if not owned
%doc %dir %{_docdir}/%{name}-%{version}


%changelog
* Mon Aug 12 2013 Igor Vlasenko <viy@altlinux.ru> 1.9.7-alt1_11
- update to new release by fcimport

* Tue Apr 30 2013 Igor Vlasenko <viy@altlinux.ru> 1.9.7-alt1_10
- update to new release by fcimport

* Thu Apr 25 2013 Igor Vlasenko <viy@altlinux.ru> 1.9.7-alt1_9
- initial fc import

