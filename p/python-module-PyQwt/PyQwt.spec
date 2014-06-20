%define oldname PyQwt

Name:           python-module-PyQwt
Version:        5.2.0
Release:        alt3
Summary:        Python bindings for Qwt

Group:          Development/Python
# GPLv2+ exceptions (see COPYING.PyQwt)
License:        GPLv2+ with exceptions
URL:            http://pyqwt.sourceforge.net/
Source0:        http://downloads.sourceforge.net/pyqwt/%{oldname}-%{version}.tar.gz

# manually link libqwt, don't hardcode -lqwt
Patch1: PyQwt-5.2.0-qwt_manual_link.patch

BuildRequires(pre): rpm-build-python
BuildRequires:  python-devel
BuildRequires:  sip-devel
BuildRequires:  python-module-PyQt4-devel
BuildRequires:  python-module-numpy
BuildRequires:  libqwt-devel
BuildRequires: 	gcc-c++
BuildRequires: 	libnumpy-devel
BuildRequires: 	libqt4-devel
BuildRequires: 	libXext-devel
BuildRequires: 	libX11-devel

Requires:       python-module-PyQt4
Requires:       python-module-numpy python-module-numpy-addons python-module-numpy-testing

Provides:	%oldname = %version-%release

%add_findprov_skiplist %{python_sitelibdir}/PyQt4/Qwt5/.*\.so$

%description
PyQwt is a set of Python bindings for the Qwt C++ class library which extends
the Qt framework with widgets for scientific and engineering applications. It
provides a widget to plot 2-dimensional data and various widgets to display and
control bounded or unbounded floating point values.

%package devel
Summary: Files needed to build other bindings on PyQwt
Group:   Development/Python
Requires: python-module-PyQwt = %{version}-%{release}
Requires: python-module-PyQt4
Requires: libqwt6-devel
Provides: %oldname-devel = %version-%release
%description devel
Files needed to build other bindings for Qwt C++ classes that inherit from
any of the PyQwt classes.


%prep
%setup -n %{oldname}-%{version} -q

%patch1 -p1 -b .manual_link_qwt

# mark examples non-executable
find qt4examples/ -name "*.py" | xargs chmod a-x


%build
QWTINC="-I %{_includedir}/qwt"
QWTLIB=-lqwt
pushd configure
%{__python} configure.py $QWTINC $QWTLIB --disable-numarray --disable-numeric
popd

# Remove RPATH
find -name 'Makefile' | xargs sed -i 's|-Wl,-rpath,/usr/lib(64)?||g;s|-Wl,-rpath,.* ||g'

make %{?_smp_mflags} -C configure


%install
make DESTDIR=%{buildroot} install -C configure
# move the generated pdf and html documentation to devel-doc directory
mkdir devel-doc
mv sphinx/build/latex/PyQwt.pdf devel-doc
rm sphinx/build/html/.buildinfo
mv sphinx/build/html devel-doc

# non-executable scripts
chmod 755 %{buildroot}/%{python_sitelibdir}/PyQt4/Qwt5/grace.py
chmod 755 %{buildroot}/%{python_sitelibdir}/PyQt4/Qwt5/qplt.py


%files
%doc ANNOUNCEMENT-%{version} README
%doc COPYING*
%{python_sitelibdir}/PyQt4/Qwt5/
%{python_sitelibdir}/PyQt4/uic/widget-plugins/qwt.py*


%files devel
%doc devel-doc/*
%doc qt4examples/ 
%{_datadir}/sip/PyQt4/Qwt5/


%changelog
* Fri Jun 20 2014 Andrey Cherepanov <cas@altlinux.org> 5.2.0-alt3
- Rebuild with new version of python-module-sip (ALT #30129)

* Mon Jan 27 2014 Andrey Cherepanov <cas@altlinux.org> 5.2.0-alt2
- Build in Sisyphus

* Tue Jan 08 2013 Igor Vlasenko <viy@altlinux.ru> 5.2.0-alt1_19
- initial fc import

