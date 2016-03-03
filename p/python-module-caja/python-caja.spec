# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-python
BuildRequires: /usr/bin/glib-gettextize /usr/bin/gtkdocize /usr/bin/pkg-config /usr/bin/xsltproc pkgconfig(libcaja-extension)
# END SourceDeps(oneline)
%py_provides caja
%define _libexecdir %_prefix/libexec
%define oldname python-caja
Name:           python-module-caja
Version:        1.12.0
Release:        alt1_1
Epoch:          1
Summary:        Python bindings for Caja

Group:          Development/C
License:        GPLv2+ and LGPLv2+
URL:            http://mate-desktop.org
Source0:        http://pub.mate-desktop.org/releases/1.10/%{oldname}-%{version}.tar.xz

BuildRequires:  python-devel
BuildRequires:  mate-file-manager-devel
BuildRequires:  python-module-pygobject3-devel
BuildRequires:  mate-common
Source44: import.info


%description
Python bindings for Caja

%package -n python-module-caja-devel
Summary:        Python bindings for Caja
Group:          Development/C
Requires:       python-module-caja = %{epoch}:%{version}-%{release}

%description -n python-module-caja-devel
Python bindings for Caja


%prep
%setup -n %{oldname}-%{version} -q
sed -i -e 's~#!/usr/bin/python~#!%{__python}~g' examples/background-image.py
sed -i -e 's~#!/usr/bin/python~#!%{__python}~g' examples/block-size-column.py
sed -i -e 's~#!/usr/bin/python~#!%{__python}~g' examples/location-widget-provider.py
sed -i -e 's~#!/usr/bin/python~#!%{__python}~g' examples/md5sum-property-page.py
sed -i -e 's~#!/usr/bin/python~#!%{__python}~g' examples/open-terminal.py
sed -i -e 's~#!/usr/bin/python~#!%{__python}~g' examples/submenu.py
sed -i -e 's~#!/usr/bin/python~#!%{__python}~g' examples/update-file-info-async.py

%build

%configure \
     --disable-static

make %{?_smp_mflags}


%install
%{makeinstall_std}
mkdir -p $RPM_BUILD_ROOT%{_datadir}/caja-python/extensions
find $RPM_BUILD_ROOT -name '*.la' -delete

%find_lang %{oldname} --with-gnome --all-name

%files -f %{oldname}.lang
%doc README AUTHORS COPYING NEWS
%{_libdir}/caja/extensions-2.0/libcaja-python.so
%{_datadir}/caja/extensions/libcaja-python.caja-extension
%dir %{_datadir}/caja-python
%dir %{_datadir}/caja-python/extensions
%{_docdir}/python-caja/examples/

%files -n python-module-caja-devel
%{_libdir}/pkgconfig/caja-python.pc


%changelog
* Wed Feb 17 2016 Igor Vlasenko <viy@altlinux.ru> 1:1.12.0-alt1_1
- new version

* Fri Oct 30 2015 Igor Vlasenko <viy@altlinux.ru> 1:1.10.0-alt1_1
- new version

* Sat Mar 22 2014 Igor Vlasenko <viy@altlinux.ru> 1.8.0-alt1_0
- new version

* Tue Apr 09 2013 Igor Vlasenko <viy@altlinux.ru> 1.6.0-alt1_0
- new version

* Wed Feb 20 2013 Igor Vlasenko <viy@altlinux.ru> 1.5.0-alt3_0
- added py_provides caja

* Sun Feb 17 2013 Igor Vlasenko <viy@altlinux.ru> 1.5.0-alt2_0
- dropped BR: python-module-mate-devel

* Sat Feb 02 2013 Igor Vlasenko <viy@altlinux.ru> 1.5.0-alt1_0
- new version

* Fri Oct 26 2012 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1.4.0-alt1_1.1
- Build for Sisyphus

* Sun Aug 05 2012 Igor Vlasenko <viy@altlinux.ru> 1.4.0-alt1_1
- 20120801 mate snapshot

* Wed Jun 27 2012 Igor Vlasenko <viy@altlinux.ru> 1.2.0-alt1_1
- 20120622 mate snapshot

