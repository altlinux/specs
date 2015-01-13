Group: Engineering
# BEGIN SourceDeps(oneline):
BuildRequires: gcc-c++
# END SourceDeps(oneline)
Name:           CuraEngine
Version:        14.12.1
Release:        alt1_1
Summary:        Engine for processing 3D models into G-code instructions for 3D printers
License:        AGPLv3
URL:            https://github.com/Ultimaker/%{name}
Source0:        %{url}/archive/%{version}.tar.gz
BuildRequires:  polyclipping-devel >= 6.1.2
Source44: import.info
# For tests:

%description
%{name} is a C++ console application for 3D printing G-code generation. It
has been made as a better and faster alternative to the old Skeinforge engine.

This is just a console application for G-code generation. For a full graphical
application look at cura with is the graphical frontend for %{name}.

%prep
%setup -q

# bundled clipper
rm -rf clipper
sed -i 's|#include <clipper/clipper.hpp>|#include <polyclipping/clipper.hpp>|' src/utils/*.h 
sed -i 's|-lclipper|-lpolyclipping|g' Makefile
sed -i 's| $(BUILD_DIR)/libclipper.a||g' Makefile

# allow redefinition of CFLAGS and do not build it static
sed -i 's|CFLAGS +=|CFLAGS?=|' Makefile
sed -i 's|--static||g' Makefile

%build
CFLAGS="-I. -Ilibs -c %{optflags} -std=c++11 -fomit-frame-pointer" make %{?_smp_mflags}

%install
install -Dpm0755 build/%{name} %{buildroot}/%{_bindir}/%{name}

%check
make test

%files
%doc LICENSE README.md
%{_bindir}/%{name}

%changelog
* Tue Jan 13 2015 Igor Vlasenko <viy@altlinux.ru> 14.12.1-alt1_1
- update to new release by fcimport

* Mon Oct 27 2014 Igor Vlasenko <viy@altlinux.ru> 14.03-alt1_3
- update to new release by fcimport

* Wed Aug 27 2014 Igor Vlasenko <viy@altlinux.ru> 14.03-alt1_2
- update to new release by fcimport

* Tue Jul 01 2014 Igor Vlasenko <viy@altlinux.ru> 14.03-alt1_1
- update to new release by fcimport

* Sat Jun 07 2014 Igor Vlasenko <viy@altlinux.ru> 14.01-alt1_1
- by request of Dmitry Derjavin <dd@>

