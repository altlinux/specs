Group: System/Libraries
# BEGIN SourceDeps(oneline):
BuildRequires: libGLU-devel libX11-devel libglvnd-devel
# END SourceDeps(oneline)
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
Name:           opencsg
Version:        1.5.0
Release:        alt1_2
Summary:        Library for Constructive Solid Geometry using OpenGL
# This is GPLv2+ since 1.5.0
# Bundled rendertexture is licensed as zlib
# Bundled glew is removed
License:        GPLv2+ and zlib
URL:            http://www.opencsg.org/
Source:         http://www.opencsg.org/OpenCSG-%{version}.tar.gz
# Makes this build fine in Fedora, and with unbundled glew
# Includes https://github.com/floriankirsch/OpenCSG/pull/3
Patch:          opencsg-build.patch
BuildRequires:  libfreeglut-devel
BuildRequires:  gcc-c++
BuildRequires:  libGLEW-devel
# NB: OpenCSG uses qmake as a build system, but does not use Qt itself
BuildRequires:  qt5-base-devel

# https://github.com/floriankirsch/OpenCSG/commits/master/RenderTexture/
# Indicates this was once 2.0.3 but has been changed since
Provides:       bundled(rendertexture) = 2.0.3^
Source44: import.info

%description
OpenCSG is a library that does image-based CSG rendering using OpenGL.

CSG is short for Constructive Solid Geometry and denotes an approach to model
complex 3D-shapes using simpler ones. I.e., two shapes can be combined by
taking the union of them, by intersecting them, or by subtracting one shape
of the other. The most basic shapes, which are not result of such a CSG
operation, are called primitives. Primitives must be solid, i.e., they must
have a clearly defined interior and exterior. By construction, a CSG shape is
also solid then.

Image-based CSG rendering (also z-buffer CSG rendering) is a term that denotes
algorithms for rendering CSG shapes without an explicit calculation of the
geometric boundary of a CSG shape. Such algorithms use frame-buffer settings
of the graphics hardware, e.g., the depth and stencil buffer, to compose CSG
shapes. OpenCSG implements a variety of those algorithms, namely the
Goldfeather algorithm and the SCS algorithm, both of them in several variants.

%package devel
Group: Development/Other
Summary: OpenCSG development files
Requires: %{name} = %{version}-%{release}

%description devel
Development files for OpenCSG.

%package doc
Group: System/Libraries
Summary: OpenCSG documentation
BuildArch: noarch

%description doc
Documentation for OpenCSG.

%prep
%setup -q -n OpenCSG-%{version}
%patch0 -p1


rm src/Makefile RenderTexture/Makefile Makefile example/Makefile

# Encoding
iconv --from=ISO-8859-1 --to=UTF-8 changelog.txt > changelog.txt.new && \
touch -r changelog.txt changelog.txt.new && \
mv changelog.txt.new changelog.txt

# Use Fedora's glew
rm -r glew/


%build
CPPFLAGS="${CPPFLAGS:-%optflags -DPIC -fPIC}"
export CPPFLAGS
qmake-qt5 \
	QMAKE_CFLAGS="${CFLAGS:-%optflags -DPIC -fPIC}" \
	QMAKE_CXXFLAGS="${CXXFLAGS:-%optflags -DPIC -fPIC}" \
	%nil
%make_build


%install
# No make install
chmod g-w lib/*
mkdir -p %{buildroot}/%{_libdir}
mkdir -p %{buildroot}/%{_includedir}
cp -pP lib/* %{buildroot}/%{_libdir}/
cp -p include/opencsg.h %{buildroot}/%{_includedir}/


%files
%doc README.md
%doc --no-dereference copying.txt
%{_libdir}/libopencsg.so.1
%{_libdir}/libopencsg.so.1.*

%files devel
%{_includedir}/opencsg.h
%{_libdir}/libopencsg.so

%files doc
%doc changelog.txt doc
%doc --no-dereference copying.txt


%changelog
* Tue Sep 26 2023 Alexey Sheplyakov <asheplyakov@altlinux.org> 1.5.0-alt1_2
- use qmake-qt5 (to build on LoongArch and riscv), while at it trimmed
  build dependencies

* Sat May 07 2022 Igor Vlasenko <viy@altlinux.org> 1.5.0-alt1_1
- update to new release by fcimport

* Wed Oct 10 2018 Igor Vlasenko <viy@altlinux.ru> 1.4.2-alt1_8
- update to new release by fcimport

* Thu Nov 23 2017 Igor Vlasenko <viy@altlinux.ru> 1.4.2-alt1_5
- new version

* Tue Dec 16 2014 Igor Vlasenko <viy@altlinux.ru> 1.4.0-alt2_1
- moved to sisyphus for dd@

* Mon Oct 20 2014 Igor Vlasenko <viy@altlinux.ru> 1.4.0-alt1_1
- update to new release by fcimport

* Wed Sep 10 2014 Igor Vlasenko <viy@altlinux.ru> 1.3.3-alt1_3
- update to new release by fcimport

* Thu Jun 26 2014 Igor Vlasenko <viy@altlinux.ru> 1.3.3-alt1_2
- update to new release by fcimport

* Wed Nov 20 2013 Igor Vlasenko <viy@altlinux.ru> 1.3.2-alt1_10
- update to new release by fcimport

* Thu Oct 10 2013 Igor Vlasenko <viy@altlinux.ru> 1.3.2-alt1_9
- update to new release by fcimport

* Fri Apr 26 2013 Igor Vlasenko <viy@altlinux.ru> 1.3.2-alt1_8
- initial fc import

