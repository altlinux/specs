# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-python
BuildRequires: python-devel
# END SourceDeps(oneline)
%define _libexecdir %_prefix/libexec
%{!?python_sitelib: %define python_sitelib %(%{__python} -c "from distutils.sysconfig import get_python_lib; print get_python_lib(0)")}

### Abstract ###

Name: 		mate-doc-utils
Version: 	1.4.0
Release: 	alt1_1.1
License: 	GPLv2+ and LGPLv2+ and GFDL
Group: 		Development/Tools
Summary: 	Documentation utilities for MATE
URL: 		http://pub.mate-desktop.org
Source: 	http://pub.mate-desktop.org/releases/1.4/%{name}-%{version}.tar.xz

BuildArch: noarch

### Patches ###

# Fedora-specific script for packaging:
#Source1000: mate-doc-utils-get-snapshot.sh
# To generate tarball for Source0:
#   sh mate-doc-utils-get-snapshot.sh %{githash}

# RH bug #438638 / GNOME bug #524207
Patch1: mate-doc-utils-0.14.0-package.patch

#Patch2: mate-doc-utils_rename.patch

### Dependencies ###

Requires: libxml2 >= 2.6.12
Requires: xsltproc libxslt >= 1.1.8
Requires: libxml2-python
# for /usr/share/aclocal
Requires: automake
# for /usr/share/mate/help
Requires: mate-doc-utils-stylesheets = %{version}-%{release}
Requires: gnome-doc-utils

### Build Dependencies ###

BuildRequires: libxml2-devel >= 2.6.12
BuildRequires: libxslt-devel >= 1.1.8
BuildRequires: libxml2-python

BuildRequires: intltool
BuildRequires: gettext
BuildRequires: scrollkeeper
BuildRequires: librarian-devel
BuildRequires: mate-common


%description
mate-doc-utils is a collection of documentation utilities for the MATE
project. Notably, it contains utilities for building documentation and
all auxiliary files in your source tree.

# note that this is an "inverse dependency" subpackage
%package stylesheets
Summary: XSL stylesheets used by mate-doc-utils
License: LGPLv2+
Group: Development/Tools
# for /usr/share/pkgconfig
# for /usr/share/xml
Requires: xml-common
Requires: gnome-doc-utils-xslt

%description stylesheets
The mate-doc-utils-stylesheets package contains XSL stylesheets which
are used by the tools in mate-doc-utils.

%prep
%setup -q -n %{name}-%{version}
%patch1 -p1 -b .package
#%patch2 -p1 -b .mate-doc-utils_rename

# need for complete mate-doc-utils_rename.patch
#mv -f $RPM_BUILD_DIR/%{name}-%{version}/xml2po/xml2po.pc.in $RPM_BUILD_DIR/%{name}-%{version}/xml2po/matexml2po.pc.in
#mv -f $RPM_BUILD_DIR/%{name}-%{version}/xml2po/xml2po.1 $RPM_BUILD_DIR/%{name}-%{version}/xml2po/matexml2po.1
#mv -f $RPM_BUILD_DIR/%{name}-%{version}/xml2po/xml2po.1.xml $RPM_BUILD_DIR/%{name}-%{version}/xml2po/matexml2po.1.xml
#mv -f $RPM_BUILD_DIR/%{name}-%{version}/xml2po/xml2po/xml2po.py.in $RPM_BUILD_DIR/%{name}-%{version}/xml2po/xml2po/#matexml2po.py.in
#mv -f $RPM_BUILD_DIR/%{name}-%{version}/rng/mallard/mallard.rnc $RPM_BUILD_DIR/%{name}-%{version}/rng/mallard/matemallard.rnc
#mv -f $RPM_BUILD_DIR/%{name}-%{version}/rng/mallard/mallard.rng $RPM_BUILD_DIR/%{name}-%{version}/rng/mallard/matemallard.rng

NOCONFIGURE=1 ./autogen.sh

%build
%configure --disable-scrollkeeper --enable-build-utils
make

%install
make install DESTDIR=$RPM_BUILD_ROOT

sed -i -e '/^Requires:/d' $RPM_BUILD_ROOT%{_datadir}/pkgconfig/xml2po.pc

rm -f $RPM_BUILD_ROOT%{python_sitelibdir_noarch}/xml2po/__init__.pyc
rm -f $RPM_BUILD_ROOT%{python_sitelibdir_noarch}/xml2po/__init__.py
rm -f $RPM_BUILD_ROOT%{python_sitelibdir_noarch}/xml2po/modes/__init__.pyc
rm -f $RPM_BUILD_ROOT%{python_sitelibdir_noarch}/xml2po/__init__.pyo
rm -f $RPM_BUILD_ROOT%{python_sitelibdir_noarch}/xml2po/modes/__init__.pyo
rm -f $RPM_BUILD_ROOT%{python_sitelibdir_noarch}/xml2po/modes/basic.pyc
rm -f $RPM_BUILD_ROOT%{python_sitelibdir_noarch}/xml2po/modes/basic.pyo
rm -f $RPM_BUILD_ROOT%{python_sitelibdir_noarch}/xml2po/modes/docbook.pyc
rm -f $RPM_BUILD_ROOT%{python_sitelibdir_noarch}/xml2po/modes/docbook.pyo
rm -f $RPM_BUILD_ROOT%{python_sitelibdir_noarch}/xml2po/modes/gs.py
rm -f $RPM_BUILD_ROOT%{python_sitelibdir_noarch}/xml2po/modes/gs.pyc
rm -f $RPM_BUILD_ROOT%{python_sitelibdir_noarch}/xml2po/modes/gs.pyo
rm -f $RPM_BUILD_ROOT%{python_sitelibdir_noarch}/xml2po/modes/__init__.py
rm -f $RPM_BUILD_ROOT%{python_sitelibdir_noarch}/xml2po/modes/basic.py
rm -f $RPM_BUILD_ROOT%{python_sitelibdir_noarch}/xml2po/modes/docbook.py
rm -f $RPM_BUILD_ROOT%{python_sitelibdir_noarch}/xml2po/modes/ubuntu.py
rm -f $RPM_BUILD_ROOT%{python_sitelibdir_noarch}/xml2po/modes/xhtml.py
rm -f $RPM_BUILD_ROOT%{python_sitelibdir_noarch}/xml2po/modes/mallard.py
rm -f $RPM_BUILD_ROOT%{python_sitelibdir_noarch}/xml2po/modes/mallard.pyc
rm -f $RPM_BUILD_ROOT%{python_sitelibdir_noarch}/xml2po/modes/mallard.pyo
rm -f $RPM_BUILD_ROOT%{python_sitelibdir_noarch}/xml2po/modes/ubuntu.pyc
rm -f $RPM_BUILD_ROOT%{python_sitelibdir_noarch}/xml2po/modes/ubuntu.pyo
rm -f $RPM_BUILD_ROOT%{python_sitelibdir_noarch}/xml2po/modes/xhtml.pyc
rm -f $RPM_BUILD_ROOT%{python_sitelibdir_noarch}/xml2po/modes/xhtml.pyo
rm -f $RPM_BUILD_ROOT%{_datadir}/xml/mallard/1.0/mallard.rnc
rm -f $RPM_BUILD_ROOT%{_datadir}/xml/mallard/1.0/mallard.rng
rm -f $RPM_BUILD_ROOT%{_datadir}/pkgconfig/xml2po.pc
rm -rf $RPM_BUILD_ROOT%{_datadir}/man
rm -f $RPM_BUILD_ROOT%{_bindir}/xml2po

%find_lang %{name}

%files -f %{name}.lang
#%doc AUTHORS README NEWS COPYING COPYING.GPL COPYING.LGPL
%{_bindir}/*
%{_datadir}/pkgconfig/mate-doc-utils.pc
%{_datadir}/aclocal/mate-doc-utils.m4
%{_datadir}/mate/help/mate-doc-make
%{_datadir}/mate/help/mate-doc-xslt
%{_datadir}/omf/mate-doc-make
%{_datadir}/omf/mate-doc-xslt
%{_datadir}/mate-doc-utils
#%doc %{_mandir}/man1/xml2po.1.gz
#%{python_sitelibdir_noarch}/xml2po/

%files stylesheets
#%{_datadir}/pkgconfig/xml2po.pc
%{_datadir}/xml/mate
#%{_datadir}/xml/mallard

%changelog
* Wed Oct 24 2012 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1.4.0-alt1_1.1
- Build for Sisyphus

* Wed Aug 01 2012 Igor Vlasenko <viy@altlinux.ru> 1.4.0-alt1_1
- 20120801 mate snapshot

* Fri Jun 22 2012 Igor Vlasenko <viy@altlinux.ru> 1.2.1-alt2_2
- 20120622 mate snapshot

* Mon Apr 30 2012 Igor Vlasenko <viy@altlinux.ru> 1.2.1-alt1_2
- converted by srpmconvert script

