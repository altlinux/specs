Name:           qtbrowserplugin
Version:        2.4
Release:        alt3
Summary:        Qt Solutions Component: Browser Plugin

License:        BSD
Group: 		Development/C++
URL:            http://qt.gitorious.org/qt-solutions/qt-solutions
Source0:        qtbrowserplugin-%{version}.tar
# Patch to build as a library
Patch0:         qtbrowserplugin-lib.patch

BuildRequires:  gcc-c++
BuildRequires:  libqt4-declarative libqt4-devel qt4-designer

# -debuginfo useless for (only) static libs
%global debug_package   %{nil}

%description
The QtBrowserPlugin solution is useful for implementing plugins
for web browser.


%package        devel
Group:		Development/C++
Summary:        Development files for %{name}
Requires:       libqt4-declarative qt4-designer
Provides:       %{name}-static = %{version}-%{release}

%description    devel
The QtBrowserPlugin solution is useful for implementing plugins
for web browser.


%prep
%setup -q
%patch0 -p1

%build
%global optflags_lto %optflags_lto -ffat-lto-objects
%{qmake_qt4}
%make_build

%install
mkdir -p %buildroot%_libdir
cp -p libqtbrowserplugin.* %buildroot%_libdir
mkdir -p %buildroot%_includedir
cp -p src/*.h %buildroot%_includedir

%files devel
%doc doc examples README.TXT
%_includedir/*
%_libdir/lib%name.a

%changelog
* Sun Sep 19 2021 Andrey Cherepanov <cas@altlinux.org> 2.4-alt3
- FTBFS: fix build with LTO.

* Sat Sep 09 2017 Andrey Cherepanov <cas@altlinux.org> 2.4-alt2
- Build in Sisyphus

* Wed Mar 15 2017 Igor Vlasenko <viy@altlinux.ru> 2.4-alt1_8
- update to new release by fcimport

* Wed Mar 02 2016 Igor Vlasenko <viy@altlinux.ru> 2.4-alt1_7
- update to new release by fcimport

* Mon Oct 19 2015 Igor Vlasenko <viy@altlinux.ru> 2.4-alt1_5
- update to new release by fcimport

* Mon Nov 10 2014 Igor Vlasenko <viy@altlinux.ru> 2.4-alt1_4
- new version

