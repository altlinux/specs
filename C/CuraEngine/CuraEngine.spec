Group: Engineering
# BEGIN SourceDeps(oneline):
BuildRequires: gcc-c++
# END SourceDeps(oneline)
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
Name:           CuraEngine
Version:        15.04
Release:        alt2_5
Summary:        Engine for processing 3D models into G-code instructions for 3D printers
License:        AGPLv3
URL:            https://github.com/Ultimaker/%{name}
Source0:        %{url}/archive/%{version}.tar.gz
BuildRequires:  libpolyclipping-devel >= 6.1.2
# For tests:
BuildRequires:  python

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
CFLAGS='-I. -Ilibs -c %{optflags} -std=c++11 -fomit-frame-pointer -DVERSION=\"%{version}\"' make %{?_smp_mflags}

%install
install -Dpm0755 build/%{name} %{buildroot}/%{_bindir}/%{name}

%check
make test

%files
%doc LICENSE README.md
%{_bindir}/%{name}

%changelog
* Sat Nov 25 2017 Igor Vlasenko <viy@altlinux.ru> 15.04-alt2_5
- rebuild with libpolyclipping

* Thu Mar 16 2017 Igor Vlasenko <viy@altlinux.ru> 15.04-alt1_5
- update to new release by fcimport

* Sun Sep 20 2015 Igor Vlasenko <viy@altlinux.ru> 15.04-alt1_2
- update to new release by fcimport

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

