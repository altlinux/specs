Group: Engineering
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-fedora-compat
BuildRequires: /usr/bin/gm /usr/bin/gs /usr/bin/svn /usr/bin/xz libcurl-devel liblapack-devel openmpi-devel zlib-devel
# END SourceDeps(oneline)
%add_findreq_skiplist /usr/share/gmt/tools/gmt5syntax
BuildRequires: chrpath
BuildRequires: gcc-c++
# fedora bcond_with macro
%define bcond_with() %{expand:%%{?_with_%{1}:%%global with_%{1} 1}}
%define bcond_without() %{expand:%%{!?_without_%{1}:%%global with_%{1} 1}}
# redefine altlinux specific with and without
%define with()         %{expand:%%{?with_%{1}:1}%%{!?with_%{1}:0}}
%define without()      %{expand:%%{?with_%{1}:0}%%{!?with_%{1}:1}}
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
%global gmthome %{_datadir}/gmt
%global gmtconf %{_sysconfdir}/gmt
%global gmtdoc %{_docdir}/gmt

%bcond_with octave
%if %with octave
%{!?octave_api: %global octave_api %(octave-config -p API_VERSION 2>/dev/null || echo 0)}
%global octave_mdir %(octave-config -p LOCALAPIFCNFILEDIR || echo)
%global octave_octdir %(octave-config -p LOCALAPIOCTFILEDIR || echo)
%endif

%global completion_dir /etc/bash_completion.d

Name:           GMT
Version:        5.4.2
Release:        alt1_3
Summary:        Generic Mapping Tools

License:        LGPLv3+
URL:            http://gmt.soest.hawaii.edu/
Source0:        ftp://ftp.soest.hawaii.edu/gmt/gmt-%{version}-src.tar.xz

BuildRequires:  ctest cmake
BuildRequires:  bash-completion
BuildRequires:  libfftw3-devel
BuildRequires:  libgdal-devel
BuildRequires:  glib2-devel libgio libgio-devel
BuildRequires:  libXt-devel libXaw-devel libXmu-devel libXext-devel
BuildRequires:  libnetcdf-devel
BuildRequires:  libpcre-devel libpcrecpp-devel
BuildRequires:  dcw-gmt
BuildRequires:  gshhg-gmt-nc4
%if %with octave
BuildRequires:  octave-devel
%endif
# less is detected by configure, and substituted in GMT.in
BuildRequires:  less
Requires:       less
Requires:       %{name}-common = %{version}-%{release}
Requires:       dcw-gmt
Requires:       gshhg-gmt-nc4
Provides:       gmt = %{version}-%{release}
%if %without octave
Obsoletes:      GMT-octave <= 4.5.11
%endif

# Do not generate provides for plugins
%global __provides_exclude_from ^%{_libdir}/gmt/.*\\.so$
Source44: import.info

%description
GMT is an open source collection of ~60 tools for manipulating geographic and
Cartesian data sets (including filtering, trend fitting, gridding, projecting,
etc.) and producing Encapsulated PostScript File (EPS) illustrations ranging
from simple x-y plots via contour maps to artificially illuminated surfaces
and 3-D perspective views.  GMT supports ~30 map projections and transforma-
tions and comes with support data such as coastlines, rivers, and political
boundaries.

GMT is developed and maintained by Paul Wessel and Walter H. F.  Smith with
help from a global set of volunteers, and is supported by the National
Science Foundation.

NOTE: Specific executables that conflict with other Fedora packages have been
removed.  These functions can still be accessed via the GMT wrapper script
with: GMT <function> [args]


%package        common
Group: Engineering
Summary:        Common files for %{name}
Provides:       gmt-common = %{version}-%{release}
BuildArch:      noarch

%description    common
The %{name}-common package contains common files for GMT (Generic
Mapping Tools) package.


%package        devel
Group: Development/C
Summary:        Development files for %{name}
Requires:       %{name} = %{version}-%{release}
Provides:       gmt-devel = %{version}-%{release}
Obsoletes:      GMT-static <= 4.5.11

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.


%package        doc
Group: Documentation
Summary:        Documentation for %{name}
Requires:       %{name} = %{version}-%{release}
Provides:       gmt-doc = %{version}-%{release}
Provides:       %{name}-examples = %{version}-%{release}
Obsoletes:      %{name}-examples < %{version}-%{release}
BuildArch:      noarch

%description    doc
The %{name}-doc package provides the documentation for the GMT (Generic
Mapping Tools) package.


%if %with octave
%package        octave
Group: Development/C
Summary:        Octave libraries for %{name}
Requires:       %{name} = %{version}-%{release}
Provides:       gmt-octave = %{version}-%{release}

%description    octave
The %{name}-octave package contains and Octave interface for developing
applications that use %{name}.
%endif


%prep
%setup -q -n gmt-%{version}


%build
mkdir build
pushd build
%{fedora_cmake} \
  -DGSHHG_ROOT=%{_prefix} \
  -DGMT_INSTALL_MODULE_LINKS=on \
  -DGMT_INSTALL_TRADITIONAL_FOLDERNAMES=off \
  -DGMT_MANDIR=%{_mandir} \
  -DLICENSE_RESTRICTED=LGPL \
%if %with octave
  -DGMT_OCTAVE=BOOL:ON \
%endif
  -DGMT_OPENMP=BOOL:ON \
  -DGMT_USE_THREADS=BOOL:ON \
  -DBASH_COMPLETION_DIR=%{completion_dir} \
  ..
%make_build


%install
make -C build DESTDIR=$RPM_BUILD_ROOT install
#Setup configuration files 
mkdir -p $RPM_BUILD_ROOT%{gmtconf}/{mgg,dbase,mgd77}
pushd $RPM_BUILD_ROOT%{gmthome}/
# put conf files in %{gmtconf} and do links in %{gmthome}
for file in mgg/gmtfile_paths dbase/grdraster.info \
    mgd77/mgd77_paths.txt; do
  mv $file $RPM_BUILD_ROOT%{gmtconf}/$file
  ln -s ../../../..%{gmtconf}/$file $RPM_BUILD_ROOT%{gmthome}/$file
done
popd

# Don't ship .bat files
find $RPM_BUILD_ROOT -name \*.bat -delete
# kill rpath
for i in `find %buildroot{%_bindir,%_libdir,/usr/libexec,/usr/lib,/usr/sbin} -type f -perm -111`; do
	chrpath -d $i ||:
done


%files
%doc COPYING.LESSERv3 COPYINGv3 LICENSE.TXT README
%{_bindir}/*
%{_libdir}/*.so.5*
%{_libdir}/gmt/

%files common
%doc COPYING.LESSERv3 COPYINGv3 LICENSE.TXT
%dir %{gmtconf}
%dir %{gmtconf}/mgg
%dir %{gmtconf}/dbase
%dir %{gmtconf}/mgd77
%config(noreplace) %{gmtconf}/mgg/gmtfile_paths
%config(noreplace) %{gmtconf}/dbase/grdraster.info 
%config(noreplace) %{gmtconf}/mgd77/mgd77_paths.txt
%{gmthome}/
%{completion_dir}/*
%{_mandir}/man1/*.1*
%{_mandir}/man5/*.5*

%files devel
%{_includedir}/*
%{_libdir}/*.so
%{_mandir}/man3/*.3*

%files doc
%{gmtdoc}/

%if %with octave
%files octave
%{octave_mdir}/*.m
%{octave_octdir}/*.mex
%endif


%changelog
* Sat Nov 18 2017 Igor Vlasenko <viy@altlinux.ru> 5.4.2-alt1_3
- new version

* Thu Nov 16 2017 Igor Vlasenko <viy@altlinux.ru> 5.2.1-alt3_3
- added gmt-5.2.1-alt-tmp_usage.patch

* Mon Aug 28 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 5.2.1-alt2_3
- Rebuilt with libnetcdf11.

* Wed Mar 02 2016 Igor Vlasenko <viy@altlinux.ru> 5.2.1-alt1_3
- rebuild with libgdal

* Mon Apr 07 2014 Igor Vlasenko <viy@altlinux.ru> 5.1.1-alt2_1
- DGMT_INSTALL_MODULE_LINKS=on

* Sat Apr 05 2014 Igor Vlasenko <viy@altlinux.ru> 5.1.1-alt1_1
- import

* Sat Jan 04 2014 Igor Vlasenko <viy@altlinux.ru> 4.5.11-alt1_2
- update to new release by fcimport

* Thu Sep 19 2013 Igor Vlasenko <viy@altlinux.ru> 4.5.9-alt1_6
- update to new release by fcimport

* Thu Aug 22 2013 Igor Vlasenko <viy@altlinux.ru> 4.5.9-alt1_5
- update to new release by fcimport

* Fri Apr 12 2013 Igor Vlasenko <viy@altlinux.ru> 4.5.9-alt1_4
- update from fc import

* Tue Jan 29 2013 Cronbuild Service <cronbuild@altlinux.org> 4.5.8-alt2_1
- rebuild to get rid of unmets

* Thu Jan 03 2013 Igor Vlasenko <viy@altlinux.ru> 4.5.8-alt1_1
- initial fc import

