Group: Engineering
# BEGIN SourceDeps(oneline):
BuildRequires: gcc-c++
# END SourceDeps(oneline)
Name:           CuraEngine
Version:        14.03
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
sed -i 's|#include "../clipper/clipper.hpp"|#include <polyclipping/clipper.hpp>|' utils/*.h
sed -i 's|\($(CXX).*\)|\1 $(LIBS)|g' Makefile
sed -i 's| clipper/clipper.cpp||g' Makefile

# allow redefinition of CFLAGS and do not build it static
sed -i 's|CFLAGS +=|CFLAGS?=|' Makefile
sed -i 's|--static||g' Makefile

%build
LIBS="-lpolyclipping" CFLAGS="-I. -c %{optflags} -fomit-frame-pointer" make %{?_smp_mflags}

%install
install -Dpm0755 %{name} %{buildroot}/%{_bindir}/%{name}

%check
make test

%files
%doc LICENSE README.md
%{_bindir}/%{name}

%changelog
* Tue Jul 01 2014 Igor Vlasenko <viy@altlinux.ru> 14.03-alt1_1
- update to new release by fcimport

* Sat Jun 07 2014 Igor Vlasenko <viy@altlinux.ru> 14.01-alt1_1
- by request of Dmitry Derjavin <dd@>

