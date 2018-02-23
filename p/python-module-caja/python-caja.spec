# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-python
BuildRequires: /usr/bin/glib-gettextize /usr/bin/gtkdocize /usr/bin/xsltproc
# END SourceDeps(oneline)
%py_provides caja
%define _libexecdir %_prefix/libexec
%define oldname python-caja
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
%global _description\
Python bindings for Caja

Name:           python-module-caja
Version:        1.20.0
Release:        alt1_1
Epoch:          1
Summary:        Python bindings for Caja

Group:          Development/Other
License:        GPLv2+ and LGPLv2+
URL:            http://mate-desktop.org
Source0:        http://pub.mate-desktop.org/releases/1.20/%{oldname}-%{version}.tar.xz

BuildRequires:  python-devel
BuildRequires:  mate-file-manager-devel
BuildRequires:  python-module-pygobject3-common-devel
BuildRequires:  mate-common
Source44: import.info


%description %_description

%package -n python-module-caja-devel
Summary:        Python bindings for Caja
Group:          Development/Other
Requires:       %{name} = %{epoch}:%{version}-%{release}

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

%make_build


%install
%{makeinstall_std}
mkdir -p $RPM_BUILD_ROOT%{_datadir}/caja-python/extensions
find $RPM_BUILD_ROOT -name '*.la' -delete

# We use %%doc instead
rm $RPM_BUILD_ROOT%{_docdir}/python-caja/README

%find_lang %{oldname} --with-gnome --all-name

%files -n python-module-caja -f %{oldname}.lang
%doc README AUTHORS COPYING NEWS
%{_libdir}/caja/extensions-2.0/libcaja-python.so
%{_datadir}/caja/extensions/libcaja-python.caja-extension
%dir %{_datadir}/caja-python
%dir %{_datadir}/caja-python/extensions
%{_docdir}/python-caja/examples/

%files -n python-module-caja-devel
%{_libdir}/pkgconfig/caja-python.pc


%changelog
* Thu Feb 22 2018 Vladimir D. Seleznev <vseleznv@altlinux.org> 1:1.20.0-alt1_1
- new fc release

* Sun Oct 22 2017 Vladimir D. Seleznev <vseleznv@altlinux.org> 1:1.19.0-alt1_1
- new fc release

* Wed Oct 12 2016 Vladimir D. Seleznev <vseleznv@altlinux.org> 1:1.16.0-alt1_1
- update to mate 1.16

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

