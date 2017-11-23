# BEGIN SourceDeps(oneline):
BuildRequires: gcc-c++ libGL-devel libGLU-devel libX11-devel
# END SourceDeps(oneline)
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
Name:           opencsg
Version:        1.4.2
Release:        alt1_5
Summary:        Library for Constructive Solid Geometry using OpenGL
Group:          System/Libraries
# license.txt contains a linking exception for CGAL
License:        GPLv2 with exceptions
URL:            http://www.opencsg.org/
Source0:        http://www.opencsg.org/OpenCSG-%{version}.tar.gz
Patch0:         %{name}-build.patch
BuildRequires:  libqt4-declarative libqt4-devel qt4-designer, libfreeglut-devel, libGLEW-devel, dos2unix
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
Summary: OpenCSG development files
Group: Development/Other
Requires: %{name} = %{version}-%{release}

%description devel
Development files for OpenCSG.

%prep
%setup -q -n OpenCSG-%{version}
%patch0 -p1

rm src/Makefile RenderTexture/Makefile Makefile example/Makefile
dos2unix license.txt

# Encoding
iconv --from=ISO-8859-1 --to=UTF-8 changelog.txt > changelog.txt.new && \
touch -r changelog.txt changelog.txt.new && \
mv changelog.txt.new changelog.txt

# New FSF Address
for FILE in src/*.h src/*.cpp include/opencsg.h
do
  sed -i s/"59 Temple Place, Suite 330, Boston, MA 02111-1307 USA"/"51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA"/ $FILE
done

# Use Fedora's glew
rm -rf glew/

%build
%{qmake_qt4}
%make_build

%install
# No make install
chmod g-w lib/*
mkdir -p %{buildroot}/%{_libdir}
mkdir -p %{buildroot}/%{_includedir}
cp -pP lib/* %{buildroot}/%{_libdir}/
cp -p include/opencsg.h %{buildroot}/%{_includedir}/

%files
%doc changelog.txt doc license.txt
%{_libdir}/*so.*

%files devel
%{_includedir}/*
%{_libdir}/*so

%changelog
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

