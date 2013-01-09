Group: Development/Tools
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-python
BuildRequires: python-devel
# END SourceDeps(oneline)
%define _libexecdir %_prefix/libexec
Name:           mate-doc-utils
Summary:        MATE Desktop doc utils
Version:        1.5.0
Release:        alt1_2

License:        GPLv2+ and LGPLv2+
URL:            http://mate-desktop.org
Source0:        http://pub.mate-desktop.org/releases/1.5/%{name}-%{version}.tar.xz

#For users upgrading from the unofficial MATE desktop Fedora repo
Obsoletes: mate-doc-utils-stylesheets < %{version}-%{release}
Provides: mate-doc-utils-stylesheets = %{version}-%{release}

# for /usr/share/aclocal
Requires: automake
# for the validation with xsltproc to use local dtds
Requires: docbook-dtds
# for /usr/share/pkgconfig
# for /usr/share/xml
Requires: xml-common
# for /usr/share/xml/mallard
Requires: gnome-doc-utils-xslt

BuildArch:      noarch

BuildRequires:  mate-common
BuildRequires:  intltool
BuildRequires:  pkgconfig(libxslt)
BuildRequires:  pkgconfig(rarian)
BuildRequires:  pkgconfig(libxml-2.0)
BuildRequires:  pkgconfig(gnome-doc-utils)

Requires:       mate-common
Requires:       gnome-doc-utils

#Fix https://bugzilla.redhat.com/show_bug.cgi?id=888807
Patch0: fix_mock_build_errors.patch
Source44: import.info
Patch33: mate-doc-utils-0.14.0-package.patch

%description
mate-doc-utils is a collection of documentation utilities for the Mate
project.  Notably, it contains utilities for building documentation and
all auxiliary files in your source tree, and it contains the DocBook
XSLT style sheets that were once distributed with Yelp.

%prep
%setup -q
%patch0 -p1
NOCONFIGURE=1 ./autogen.sh
%patch33 -p1

%build
%configure --disable-scrollkeeper
make %{?_smp_mflags}


%install
make install DESTDIR=%{buildroot}
%find_lang %{name}
#Remove unnecessary python sitepackages provided by gnome-doc-utils
rm -rf $RPM_BUILD_ROOT/%{python_sitelibdir_noarch}/*
rm -rf $RPM_BUILD_ROOT/%{python_sitelibdir_noarch}/xml2po/
rm -rf %{buildroot}/%{_mandir}/man1/*
rm -rf $RPM_BUILD_ROOT/%{_datadir}/xml/mallard
rm -rf $RPM_BUILD_ROOT/%{_bindir}/xml2po
rm -rf $RPM_BUILD_ROOT/%{_datadir}/pkgconfig/xml2po.pc
#Debian script not needed
rm -rf $RPM_BUILD_ROOT/%{_datadir}/mate-doc-utils/mate-debian.sh

%files -f %{name}.lang
%doc AUTHORS README NEWS COPYING COPYING.GPL COPYING.LGPL
%{_bindir}/mate-doc-prepare
%{_bindir}/mate-doc-tool
%{_datadir}/aclocal/mate-doc-utils.m4
%{_datadir}/mate/help/mate-doc-make
%{_datadir}/mate/help/mate-doc-xslt
%{_datadir}/omf/mate-doc-make
%{_datadir}/omf/mate-doc-xslt
%{_datadir}/mate-doc-utils
%{_datadir}/xml/mate
%{_datadir}/pkgconfig/mate-doc-utils.pc

%changelog
* Wed Jan 09 2013 Igor Vlasenko <viy@altlinux.ru> 1.5.0-alt1_2
- new fc release

* Thu Nov 01 2012 Igor Vlasenko <viy@altlinux.ru> 1.5.0-alt1_1
- use F19 import base

* Wed Oct 24 2012 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1.4.0-alt1_1.1
- Build for Sisyphus

* Wed Aug 01 2012 Igor Vlasenko <viy@altlinux.ru> 1.4.0-alt1_1
- 20120801 mate snapshot

* Fri Jun 22 2012 Igor Vlasenko <viy@altlinux.ru> 1.2.1-alt2_2
- 20120622 mate snapshot

* Mon Apr 30 2012 Igor Vlasenko <viy@altlinux.ru> 1.2.1-alt1_2
- converted by srpmconvert script

