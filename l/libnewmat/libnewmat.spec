Epoch: 1
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
%define major	1
%define majorminor	%{major}.0
%define lname	newmat
%define libname lib%{lname}%{major}
%define libdev  lib%{lname}-devel

Name: libnewmat
Version: 10E
Release: alt1_3
Summary: C++ library for manipulating matrices
Group: System/Libraries
License: Public Use
Url: http://www.robertnz.net/nm_intro.htm
Source0: http://www.robertnz.net/ftp/newmat10.tar.gz
BuildRequires: gcc-c++
Source44: import.info

%description
This C++ library is intended for scientists and engineers who need to
manipulate a variety of types of matrices using standard matrix
operations. Emphasis is on the kind of operations needed in statistical
calculations such as least squares, linear equation solve and
eigenvalues.

%package -n %{libname}
Group: System/Libraries
Summary: C++ library for manipulating matrices

%description -n %{libname}
This C++ library is intended for scientists and engineers who need to
manipulate a variety of types of matrices using standard matrix
operations. Emphasis is on the kind of operations needed in statistical
calculations such as least squares, linear equation solve and
eigenvalues.

%package -n %{libdev}
Summary: Development files for %name
Group: Development/C++
Requires: %{libname} = %{?epoch:%epoch:}%{version}-%{release}
Provides: %{lname}-devel = %{version}-%{release}
#Provides: lib%{lname}-devel = %{version}-%{release}

%description -n %{libdev}
This package contains libraries and header files for
developing applications that use %name.

%prep
%setup -qcn %{name}-%{version}

echo 'libnewmat.so.$(MAJOR).$(MINOR): $(newmat_lobj)' >> nm_gnu.mak
echo '	$(CXX) $(LDFLAGS) -shared -Wl,-soname,libnewmat.so.$(MAJOR) -o $@ $^' >> nm_gnu.mak

%build

%make_build -f nm_gnu.mak CXXFLAGS="%optflags -fPIC" libnewmat.so.%{majorminor}

%install
# Create dirs
install -d -m 0755 %{buildroot}%{_includedir}/newmat
install -d -m 0755 %{buildroot}%{_libdir}/
# Install files
install -m 0755 libnewmat.so.%{majorminor} %{buildroot}%{_libdir}/
install -m 0644 *.h %{buildroot}%{_includedir}/newmat
# Lib symlinks
ln -s libnewmat.so.%{majorminor} %{buildroot}%{_libdir}/libnewmat.so.%{major}
ln -s libnewmat.so.%{majorminor} %{buildroot}%{_libdir}/libnewmat.so

%files -n %{libname}
%doc --no-dereference COPYING
%_libdir/libnewmat.so.%{major}
%_libdir/libnewmat.so.%{major}.*

%files -n %{libdev}
%doc nm10.htm README AUTHORS example.cpp sl_ex.cpp nl_ex.cpp garch.cpp test_exc.cpp rbd.css add_time.png
%dir %{_includedir}/newmat/
%{_includedir}/newmat/*.h
%{_libdir}/libnewmat.so


%changelog
* Sun Dec 05 2021 Igor Vlasenko <viy@altlinux.org> 1:10E-alt1_3
- fixed build
- downgraded to stable version

* Thu Feb 10 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 11beta-alt4
- Rebuilt for debuginfo

* Fri Dec 17 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 11beta-alt3
- Added operator>> for GeneralMatrix
- Fixed newmat.h

* Wed Oct 20 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 11beta-alt2
- Rebuilt for soname set-versions

* Sun Mar 22 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 11beta-alt1
- Initial build for Sisyphus

* Fri Feb 06 2009 Pascal < pascal22p at parois.net > - 10D-2
- Correction of soname.
* Sat Jan 10 2009 Pascal < pascal22p at parois.net > - 10D-1
- Fisrt spec file.

