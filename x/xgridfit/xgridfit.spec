# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-python
# END SourceDeps(oneline)
Requires: python-module-libxml2
# %%name or %%version is ahead of its definition. Predefining for rpm 4.0 compatibility.
%define name xgridfit
%define version 2.2
%{!?python_sitelib: %global python_sitelib %(%{__python} -c "from distutils.sysconfig import get_python_lib; print (get_python_lib())")}

%global alphatag 20100725cvs
%global patchlevel a

%global archivever %{!?alphatag:%{version}%{?patchlevel}}%{?alphatag:%{name}}

Name:    xgridfit
Version: 2.2
Release: alt3_14%{?patchlevel:.%{patchlevel}}%{?alphatag:.%{alphatag}}
Summary: Font hinting tool

# This is where we drop fontforge
Group:   Publishing
License: LGPLv2
URL:     http://%{name}.sf.net/
Source0: %{!?alphatag:http://downloads.sourceforge.net/%{name}/}%{name}-%{archivever}.tar.gz
Patch1:  %{name}-2.2a-maindir-in-python.patch


BuildArch: noarch

BuildRequires:   python-devel

Requires:        %{_bindir}/xsltproc fontforge libfontforge, python-module-libxml2
Requires(post):  %{_bindir}/xmlcatalog
Requires(preun): %{_bindir}/xmlcatalog
Source44: import.info

%description
Xgridfit is a high-level, XML-based language for gridfitting, or a.'hintinga.',
fonts. The Xgridfit program compiles an XML source file into tables and
instructions that relate to the gridfitting of glyphs. Xgridfit does not
insert these elements into a font itself, but rather relies on FontForge, the
Open-Source font editor, to do so.


%package doc
Group:    Documentation
Summary:  Font hinting tool use documentation
# Does not really make sense without the tool itself
Requires: %{name} = %{version}

%description doc
Xgridfit font hinting tool user documentation.


%prep
%setup -q -n %{name}
%patch1 -p1 -b .mip

%build


%install
rm -fr %{buildroot}

make install DESTDIR=%{buildroot} \
             BINDIR=%{_bindir} \
             MANDIR=%{_mandir} \
             MAINDIR=%{_datadir}/xml/%{name}-%{version}

# Simplify preun/post catalog logic
ln -s catalog.xml \
      %{buildroot}%{_datadir}/xml/%{name}-%{version}/schemas/catalog-%{version}.%{release}.xml

%post
cd %{_sysconfdir}/xml
[ -e catalog ] || xmlcatalog --noout --create catalog
xmlcatalog --noout --add \
  nextCatalog %{_datadir}/xml/%{name}-%{version}/schemas/catalog-%{version}.%{release}.xml "" catalog >/dev/null
:


%preun
xmlcatalog --noout --del \
  %{_datadir}/xml/%{name}-%{version}/schemas/catalog-%{version}.%{release}.xml \
  %{_sysconfdir}/xml/catalog >/dev/null >/dev/null
:



%files
%doc COPYING ChangeLog

%{_datadir}/xml/%{name}-%{version}
%{_mandir}/man1/*

%{python_sitelibdir_noarch}/*

#%defattr(0755,root,root,0755)
%{_bindir}/*


%files doc
%doc docs/*


%changelog
* Tue Jul 26 2016 Igor Vlasenko <viy@altlinux.ru> 2.2-alt3_14.a.20100725cvs
- update to new release by fcimport

* Sun Sep 20 2015 Igor Vlasenko <viy@altlinux.ru> 2.2-alt3_12.a.20100725cvs
- update to new release by fcimport

* Tue Jul 01 2014 Igor Vlasenko <viy@altlinux.ru> 2.2-alt3_11.a.20100725cvs
- update to new release by fcimport

* Mon Aug 12 2013 Igor Vlasenko <viy@altlinux.ru> 2.2-alt3_10.a.20100725cvs
- update to new release by fcimport

* Wed Mar 13 2013 Igor Vlasenko <viy@altlinux.ru> 2.2-alt3_9.a.20100725cvs
- fixed build

* Fri Feb 22 2013 Igor Vlasenko <viy@altlinux.ru> 2.2-alt2_9.a.20100725cvs
- update to new release by fcimport

* Fri Jul 27 2012 Igor Vlasenko <viy@altlinux.ru> 2.2-alt2_8.a.20100725cvs
- update to new release by fcimport

* Wed Mar 21 2012 Igor Vlasenko <viy@altlinux.ru> 2.2-alt2_7.a.20100725cvs
- rebuild to get rid of #27020

* Sat Jan 21 2012 Igor Vlasenko <viy@altlinux.ru> 2.2-alt1_7.a.20100725cvs
- update to new release by fcimport

* Sat Oct 22 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 2.2-alt1_6.a.20100725cvs.1
- Rebuild with Python-2.7

* Wed Aug 03 2011 Igor Vlasenko <viy@altlinux.ru> 2.2-alt1_6.a.20100725cvs
- initial release by fcimport

