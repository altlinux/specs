# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-python
BuildRequires: gcc-c++
# END SourceDeps(oneline)
%add_optflags %optflags_shared
%{echo 


}

Name:           libkdtree++
Version:        0.7.0
Release:        alt1_7
Summary:        C++ template container implementation of kd-tree sorting
URL:            http://libkdtree.alioth.debian.org/
License:        Artistic 2.0
Group:          System/Libraries
BuildRequires:  autoconf automake python-devel swig

Source0:        http://alioth.debian.org/frs/download.php/2702/libkdtree++-0.7.0.tar.bz2

# patch to make GCC 4.7 happy (fixed in upstream git, not yet in release):
Patch0:         libkdtree++-0.7.0-pedantic.patch
# patch to make pkgconfig file (.pc) (submitted to upstream mailing list
# on 29-Sep-2012):
Patch1:         libkdtree++-0.7.0-pkgconfig.patch
# patch to build examples/test with %{optflags}
Patch2:         libkdtree++-0.7.0-examples-optflags.patch
Source44: import.info
%add_findprov_skiplist %{python_sitelibdir}/.*\.so$

%description
%{summary}.


%package devel
Summary:        C++ template container implementation of kd-tree sorting
Group:          Development/C
Provides:       libkdtree++-static = %{version}
BuildArch:      noarch

%description devel
%{summary}.


%package -n python-module-libkdtree++
Summary:        Python language bindings for libkdtree++
Group:          Development/Python

%description -n python-module-libkdtree++
%{summary}.


%package examples
Summary:        Examples for libkdtree++
Group:          Development/C
BuildArch:      noarch

%description examples
%{summary}.


%prep
%setup -q -n %{name}_%{version}
%patch0 -p1 -b .pkgconfig
%patch1 -p1 -b .pkgconfig
%patch2 -p1 -b .examples-optflags

# convert files from ISO-8859-1 to UTF-8 encoding
for f in README
do
  iconv -fiso88591 -tutf8 $f >$f.new
  touch -r $f $f.new
  mv $f.new $f
done


%build
autoreconf -f -i
%configure
make

cd python-bindings
make CPPFLAGS="%{optflags} -fPIC `pkg-config --cflags python`"
cd ..

%check
cd examples
make %{?_smpflags} CPPFLAGS="%{optflags}"
./test_kdtree
./test_hayne
cd ..

cd python-bindings
python py-kdtree_test.py
cd ..

%install
make install DESTDIR=%{buildroot}
install -d %{buildroot}%{python_sitelibdir}
install -pm 0755 python-bindings/_kdtree.so %{buildroot}%{python_sitelibdir}/
install -d %{buildroot}%{python_sitelibdir_noarch}
install -pm 0644 python-bindings/kdtree.py %{buildroot}%{python_sitelibdir_noarch}/

%files devel
%doc COPYING AUTHORS README NEWS TODO ChangeLog
%{_includedir}/kdtree++/
%{_datadir}/pkgconfig/*.pc

%files -n python-module-libkdtree++
%doc COPYING AUTHORS README NEWS TODO ChangeLog
%{python_sitelibdir}/_kdtree.so
%{python_sitelibdir_noarch}/kdtree.py
%{python_sitelibdir_noarch}/kdtree.pyc
%{python_sitelibdir_noarch}/kdtree.pyo

%files examples
%doc examples/CMakeLists.txt
%doc examples/Makefile
%doc examples/test*.cpp

%changelog
* Tue Jul 01 2014 Igor Vlasenko <viy@altlinux.ru> 0.7.0-alt1_7
- update to new release by fcimport

* Mon Aug 12 2013 Igor Vlasenko <viy@altlinux.ru> 0.7.0-alt1_6
- update to new release by fcimport

* Thu Apr 25 2013 Igor Vlasenko <viy@altlinux.ru> 0.7.0-alt1_5
- initial fc import

