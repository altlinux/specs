# BEGIN SourceDeps(oneline):
BuildRequires: /usr/bin/desktop-file-validate /usr/bin/glib-genmarshal /usr/bin/glib-gettextize /usr/bin/gtkdocize /usr/bin/pkg-config
# END SourceDeps(oneline)
BuildRequires: /usr/bin/db2html
%define _libexecdir %_prefix/libexec
%define oldname caja-actions
Summary:	Caja extension for customizing the context menu
Name:		mate-file-manager-actions
Version:	1.8.1
Release:	alt1_1
Group:		Graphical desktop/MATE
License:	GPLv2+ and LGPLv2+

# upstream is located at github, but links from tag releases doesn't match copied link in
# web-browser, in result fedora-rewiew-tool will fail.
# so i decided to release on fedorapeople to have a valid download link
URL:		https://github.com/NiceandGently/caja-actions
Source0:	http://raveit65.fedorapeople.org/Mate/SOURCE/%{oldname}-%{version}.tar.xz

BuildRequires:	mate-file-manager-devel
BuildRequires:	libuuid-devel
BuildRequires:	libSM-devel
BuildRequires:	libunique-devel
BuildRequires:	mate-common
BuildRequires:	libxml2-devel
BuildRequires:	yelp-tools
BuildRequires:	libgtop2-devel
BuildRequires:	dblatex

Requires:       mate-file-manager-actions-doc = %{version}-%{release}
Source44: import.info


%description
Caja actions is an extension for Caja, the MATE file manager.
It provides an easy way to configure programs to be launch on files 
selected in Caja interface

%package doc
Summary:	Documentations for %{oldname}
Group:		Documentation
BuildArch:  noarch

%description doc
This package contains the documentation for %{oldname}

%package	devel
Summary:	Development tools for the caja-actions
Group:		Development/C
Requires:	mate-file-manager-actions = %{version}-%{release}

%description	devel
This package contains headers and shared libraries needed for development
with caja-actions.

%prep
%setup -n %{oldname}-%{version} -q
#NOCONFIGURE=1 ./autogen.sh

%build
%configure \
	--with-gtk=2 \
    --enable-gtk-doc \
    --enable-html-manuals \
    --enable-pdf-manuals \
    --enable-deprecated

make %{?_smp_mflags} 

%install
%{makeinstall_std}

find $RPM_BUILD_ROOT -type f -name "*.la" -exec rm -f {} ';'
find $RPM_BUILD_ROOT -type f -name "*.a" -exec rm -f {} ';'

# clean docs dirs
rm -f $RPM_BUILD_ROOT%{_docdir}/%{oldname}-%{version}/INSTALL
rm -f $RPM_BUILD_ROOT%{_docdir}/%{oldname}-%{version}/ChangeLog-2008
rm -f $RPM_BUILD_ROOT%{_docdir}/%{oldname}-%{version}/ChangeLog-2009
rm -f $RPM_BUILD_ROOT%{_docdir}/%{oldname}-%{version}/ChangeLog-2010
rm -f $RPM_BUILD_ROOT%{_docdir}/%{oldname}-%{version}/ChangeLog-2011
rm -f $RPM_BUILD_ROOT%{_docdir}/%{oldname}-%{version}/ChangeLog-2012
rm -f $RPM_BUILD_ROOT%{_docdir}/%{oldname}-%{version}/MAINTAINERS

# move doc dir for > f19
mv $RPM_BUILD_ROOT%{_docdir}/%{oldname}-%{version} $RPM_BUILD_ROOT%{_docdir}/%{oldname}

%find_lang %{oldname} --with-gnome --all-name


%check
desktop-file-validate $RPM_BUILD_ROOT%{_datadir}/applications/cact.desktop


%files
%doc AUTHORS COPYING COPYING-DOCS ChangeLog NEWS README
%{_bindir}/caja-actions-run
%{_bindir}/caja-actions-config-tool
%{_bindir}/caja-actions-new
%{_bindir}/caja-actions-print
%{_libexecdir}/caja-actions/
%{_libdir}/caja-actions/
%{_libdir}/caja/extensions-2.0/libcaja-actions-menu.so
%{_libdir}/caja/extensions-2.0/libcaja-actions-tracker.so
%{_datadir}/caja-actions/
%{_datadir}/icons/hicolor/*/apps/caja-actions.*
%{_datadir}/applications/cact.desktop

%files doc -f %{oldname}.lang
%{_docdir}/caja-actions/html/
%{_docdir}/caja-actions/pdf/
%{_docdir}/caja-actions/objects-hierarchy.odg

%files devel
%{_includedir}/caja-actions/
%{_datadir}/gtk-doc/html/caja-actions-3/


%changelog
* Wed Feb 17 2016 Igor Vlasenko <viy@altlinux.ru> 1.8.1-alt1_1
- new version

* Wed Oct 21 2015 Igor Vlasenko <viy@altlinux.ru> 1.8.0-alt1_2
- new version

* Tue Jun 10 2014 Igor Vlasenko <viy@altlinux.ru> 1.7.1-alt2_1
- rebuild with libgtop

* Tue Apr 01 2014 Igor Vlasenko <viy@altlinux.ru> 1.7.1-alt1_1
- new fc release

* Mon Mar 24 2014 Igor Vlasenko <viy@altlinux.ru> 1.7.0-alt1_1
- new fc release

* Sat Mar 22 2014 Igor Vlasenko <viy@altlinux.ru> 1.7.0-alt1_0
- new fc release

* Fri Feb 22 2013 Igor Vlasenko <viy@altlinux.ru> 1.5.0-alt2_0101
dropped obsolete mate-conf BR:

* Wed Feb 20 2013 Igor Vlasenko <viy@altlinux.ru> 1.5.0-alt1_0101
- initial import

