Group: Other
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
Name:           gshhg-gmt-nc4
Version:        2.3.3
Release:        alt1_5
Summary:        Global Self-consistent Hierarchical High-resolution Geography (GSHHG)

License:        LGPLv3+
URL:            http://www.soest.hawaii.edu/pwessel/gshhg/
# seems to be derived at least from 2 Public Domain datasets, 
# CIA World DataBank II and World Vector Shoreline (already in fedora),
# then modified.
Source0:        http://www.soest.hawaii.edu/pwessel/gshhg/gshhg-gmt-%{version}.tar.gz
BuildArch:      noarch
Obsoletes:      GMT-coastlines < 2.2.4-2
Provides:       GMT-coastlines = %{version}-%{release}
Source44: import.info


%description
GSHHG is a high-resolution shoreline data set amalgamated from two databases:
Global Self-consistent Hierarchical High-resolution Shorelines (GSHHS) and
CIA World Data Bank II (WDBII).  GSHHG contains vector descriptions at five
different resolutions of land outlines, lakes, rivers, and political
boundaries.  This data for use by GMT, the Generic Mapping Tools.

This package contains the crude, low, and intermediate resolution data.
Install the -all, -full, or -high sub-packages to get full, high, or all of
the resolution data respectively. 


%package        full
Group: Other
Summary:        GSHHG - full resolution
Requires:       %{name}
Obsoletes:      GMT-coastlines-full < 2.2.4-2
Provides:       GMT-coastlines-full = %{version}-%{release}

%description    full
%{summary}.


%package        high
Group: Other
Summary:        GSHHG - high resolution
Requires:       %{name}
Obsoletes:      GMT-coastlines-high < 2.2.4-2
Provides:       GMT-coastlines-high = %{version}-%{release}

%description    high
%{summary}.


%package        all
Group: Other
Summary:        GSHHG - all resolutions
Requires:       %{name}
Requires:       %{name}-full
Requires:       %{name}-high
Obsoletes:      GMT-coastlines-all < 2.2.4-2
Provides:       GMT-coastlines-all = %{version}-%{release}

%description    all
%{summary}.


%prep
%setup -q -n gshhg-gmt-%{version} 

%install
mkdir -p %{buildroot}/%{_datadir}/%{name}
cp -a *.nc %{buildroot}/%{_datadir}/%{name}


%files
%doc COPYING.LESSERv3 COPYINGv3 LICENSE.TXT README.TXT
%dir %{_datadir}/%{name}
%{_datadir}/%{name}/*_[cil].nc

%files full
%{_datadir}/%{name}/*_f.nc

%files high
%{_datadir}/%{name}/*_h.nc


%changelog
* Sat Nov 18 2017 Igor Vlasenko <viy@altlinux.ru> 2.3.3-alt1_5
- new version

* Sat Apr 05 2014 Igor Vlasenko <viy@altlinux.ru> 2.3.0-alt1_1
- import

