# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-python
# END SourceDeps(oneline)
%{!?python_sitelib: %global python_sitelib %(%{__python} -c "from distutils.sysconfig import get_python_lib; print(get_python_lib())")}

Name: sugar-datastore
Version: 0.98.1
Release: alt1_1
Summary: Sugar Datastore

Group: Development/C
License: GPLv2+
URL: http://sugarlabs.org/
Source0: http://download.sugarlabs.org/sources/sucrose/glucose/%{name}/%{name}-%{version}.tar.bz2

BuildRequires: python-devel
Source44: import.info
BuildRequires: rpmbuild-helper-sugar-activity
Obsoletes: sugar-datastore-service < %version
Conflicts: sugar-datastore-service < %version

%description
sugar-datastore is a simple log like datastore able to connect with multiple
backends. The datastore supports connectionig and disconnecting from
backends on the fly to help the support the limit space/memory
characteristics of the OLPC system and the fact that network services
may become unavailable at times

%prep
%setup -q

%build
%configure
make %{?_smp_mflags} V=1

%install
make install DESTDIR=%{buildroot} INSTALL='install -p'

#Remove libtool archives.
find %{buildroot} -name '*.la' -exec rm -f {} ';'
# hack: move arch-dependent py+so
%ifarch x86_64
mkdir -p %{buildroot}%{python_sitelibdir}/
mv %{buildroot}%{python_sitelibdir_noarch}/* %{buildroot}%{python_sitelibdir}/
%endif


%files
%doc AUTHORS COPYING NEWS README
%{python_sitelibdir}/*
%{_bindir}/*
%{_datadir}/dbus-1/services/*.service

%changelog
* Wed Mar 13 2013 Igor Vlasenko <viy@altlinux.ru> 0.98.1-alt1_1
- update from fc18 release

* Wed Nov 28 2012 Igor Vlasenko <viy@altlinux.ru> 0.96.0-alt1_1
- new version; import from fc17 release

