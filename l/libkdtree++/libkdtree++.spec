%add_optflags %optflags_shared

# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %_var

# see https://bugzilla.altlinux.org/52768
%def_disable py_module

Name: libkdtree++
Version: 0.7.5
Release: alt1

Summary: C++ template container implementation of kd-tree sorting

Url: https://github.com/nvmd/libkdtree
VCS: https://github.com/nvmd/libkdtree

Group: System/Libraries
License: Artistic-2.0

%if_enabled py_module
BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel
%endif

BuildRequires: gcc-c++
BuildRequires: autoconf automake swig

Source0: %name-%version.tar

# patch to make pkgconfig file (.pc) (submitted to upstream mailing list
# on 29-Sep-2012):
Patch1: libkdtree++-0.7.0-pkgconfig.patch
# patch to build examples/test with optflags
Patch2: libkdtree++-0.7.0-examples-optflags.patch
# patch for Python 3 compatibility, portions from Debian
#Patch4:         libkdtree++-0.7.0-py3.patch

%description
%summary.

%package devel
Group: Development/C
Summary: C++ template container implementation of kd-tree sorting
Provides: libkdtree++-static = %EVR
BuildArch: noarch
%description devel
%summary.

%if_enabled py_module
%package -n python3-module-libkdtree++
Group: System/Libraries
Provides: %name-python3 = %EVR
Summary: Python3 language bindings for libkdtree++
%description -n python3-module-libkdtree++
%summary.
%endif

%package examples
Group: Development/C
Summary: Examples for libkdtree++
BuildArch: noarch
%description examples
%summary.

%prep
%setup
%patch1 -p1 -b .pkgconfig
%patch2 -p1 -b .examples-optflags
#%patch4 -p1 -b .py3

%build
autoreconf -f -i
%configure
make

%if_enabled py_module
cd python-bindings
make CPPFLAGS="%optflags -fPIC `pkg-config --cflags python3`"
cd ..
%endif

%check
cd examples
make %{?_smpflags} CPPFLAGS="%optflags"
./test_kdtree
./test_hayne
cd ..

%if_enabled py_module
cd python-bindings
python3 py-kdtree_test.py
cd ..
%endif

%install
make install DESTDIR=%buildroot

%if_enabled py_module
install -d %buildroot%python3_sitelibdir
install -pm 0755 python-bindings/_kdtree.so %buildroot%python3_sitelibdir/
install -d %buildroot%python3_sitelibdir_noarch
install -pm 0644 python-bindings/kdtree.py %buildroot%python3_sitelibdir_noarch/
%endif

%files devel
%doc COPYING AUTHORS README.md NEWS TODO ChangeLog
%_includedir/kdtree++/
%_datadir/pkgconfig/*.pc

%if_enabled py_module
%files -n python3-module-libkdtree++
%doc COPYING AUTHORS README NEWS TODO ChangeLog
%python3_sitelibdir/_kdtree.so
%python3_sitelibdir_noarch/kdtree.py
%python3_sitelibdir_noarch/__pycache__/*
%endif

%files examples
%doc examples/CMakeLists.txt
%doc examples/Makefile
%doc examples/test*.cpp

%changelog
* Mon Oct 13 2025 Aleksandr Shamaraev <shad@altlinux.org> 0.7.5-alt1
- 0.7.3 -> 0.7.5
- change upstream url

* Wed Jul 23 2025 Aleksandr Shamaraev <shad@altlinux.org> 0.7.3-alt1
- 0.7.0 -> 0.7.3
- url changed and vcs added
- spec cleanup

* Wed Jan 22 2025 Aleksandr Shamaraev <shad@altlinux.org> 0.7.0-alt3
- disabled python module (close #52768)

* Thu Oct 17 2019 Igor Vlasenko <viy@altlinux.ru> 0.7.0-alt2_24
- update to new release by fcimport

* Sat May 25 2019 Igor Vlasenko <viy@altlinux.ru> 0.7.0-alt2_21
- update to new release by fcimport

* Mon Nov 23 2015 Igor Vlasenko <viy@altlinux.ru> 0.7.0-alt2_8
- fixed build

* Wed Aug 27 2014 Igor Vlasenko <viy@altlinux.ru> 0.7.0-alt1_8
- update to new release by fcimport

* Tue Jul 01 2014 Igor Vlasenko <viy@altlinux.ru> 0.7.0-alt1_7
- update to new release by fcimport

* Mon Aug 12 2013 Igor Vlasenko <viy@altlinux.ru> 0.7.0-alt1_6
- update to new release by fcimport

* Thu Apr 25 2013 Igor Vlasenko <viy@altlinux.ru> 0.7.0-alt1_5
- initial fc import

