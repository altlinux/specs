# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-python3
BuildRequires: gcc-c++
# END SourceDeps(oneline)
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %_var
%global modname pycxx

Name:           python3-module-pycxx-devel
Version:        7.1.7
Release:        alt1

Summary:        Write Python extensions in C++

Group:          Development/Python3
License:        BSD
URL:            http://CXX.sourceforge.net/

BuildArch:      noarch

Source0:        %modname-%version.tar.gz
# Patch0:  remove unnecessary 'Src/' directory from include path in sources
Patch0:         python-pycxx-6.2.8-change-include-paths.patch

BuildRequires:  python3-devel

%description
PyCXX is a set of classes to help create extensions of Python in the
C++ language. The first part encapsulates the Python C API taking care
of exceptions and ref counting. The second part supports the building
of Python extension modules in C++.

%prep
%setup -n %modname-%version
%patch0 -p1 -b .change-include-paths

%build
%__python3 setup.py build

%install
INSTALL='setup.py install
        --root=%buildroot
        --prefix=%_prefix
        --install-headers=%_includedir/CXX
        --install-data=%_usrsrc'

%__python3 $INSTALL

# Write pkg-config PyCXX.pc file
mkdir -p %buildroot%_datadir/pkgconfig
cat > %buildroot%_datadir/pkgconfig/PyCXX.pc <<EOF
prefix=%_prefix
exec_prefix=%_prefix
includedir=%_includedir
srcdir=%_usrsrc/CXX

Name: PyCXX
Description: Write Python extensions in C++
Version: %version
Cflags: -I\${includedir}
EOF

%files -n python3-module-pycxx-devel
%doc README.html COPYRIGHT Doc/Python3/
%dir %_includedir/CXX
%_includedir/CXX/*.hxx
%_includedir/CXX/*.h
%_includedir/CXX/Python3
%python3_sitelibdir_noarch/CXX*
%dir %_usrsrc/CXX
%_usrsrc/CXX/*.cxx
%_usrsrc/CXX/*.c
%_usrsrc/CXX/Python3
%_datadir/pkgconfig/PyCXX.pc


%check
export PKG_CONFIG_PATH=%buildroot%_datadir/pkgconfig:%buildroot%_libdir/pkgconfig
test "$(pkg-config --modversion PyCXX)" = "%version"

%changelog
* Thu Jun 16 2022 Grigory Ustinov <grenka@altlinux.org> 7.1.7-alt1
- Build new version.

* Thu Jul 08 2021 Grigory Ustinov <grenka@altlinux.org> 7.1.5-alt1
- Build new version.

* Sun Jun 21 2020 Grigory Ustinov <grenka@altlinux.org> 7.1.4-alt1
- Build new version.

* Wed Dec 18 2019 Grigory Ustinov <grenka@altlinux.org> 7.1.3-alt2
- Fixed FTBFS.

* Wed Jul 10 2019 Grigory Ustinov <grenka@altlinux.org> 7.1.3-alt1
- Build new version.

* Wed Apr 17 2019 Grigory Ustinov <grenka@altlinux.org> 7.1.2-alt1
- Initial build for Sisyphus.

* Wed Mar 15 2017 Igor Vlasenko <viy@altlinux.ru> 6.2.8-alt1_4
- update to new release by fcimport

* Fri Sep 30 2016 Igor Vlasenko <viy@altlinux.ru> 6.2.8-alt1_2
- update to new release by fcimport

* Wed Mar 02 2016 Igor Vlasenko <viy@altlinux.ru> 6.2.4-alt1_12.20130805svn280
- update to new release by fcimport

* Mon Oct 19 2015 Igor Vlasenko <viy@altlinux.ru> 6.2.4-alt1_10.20130805svn280
- update to new release by fcimport

* Thu Jun 26 2014 Igor Vlasenko <viy@altlinux.ru> 6.2.4-alt1_9.20130805svn280
- update to new release by fcimport

* Thu Sep 19 2013 Igor Vlasenko <viy@altlinux.ru> 6.2.4-alt1_7.20130805svn280
- update to new release by fcimport

* Thu Feb 21 2013 Igor Vlasenko <viy@altlinux.ru> 6.2.4-alt1_5
- update to new release by fcimport

* Sat Jan 05 2013 Igor Vlasenko <viy@altlinux.ru> 6.2.4-alt1_3
- initial fc import

