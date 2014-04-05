Group: Other
Name:           dcw-gmt
Version:        1.1.1
Release:        alt1_1
Summary:        Digital Chart of the World (DCW) for GMT

License:        LGPLv3+
URL:            http://www.soest.hawaii.edu/wessel/dcw/
Source0:        http://www.soest.hawaii.edu/pwessel/dcw/%{name}-%{version}.tar.gz
BuildArch:      noarch
Source44: import.info


%description
DCW-GMT is an enhancement to the original 1:1,000,000 scale vector basemap of
the world available from the Princeton University Digital Map and Geospatial
Information Center and from GeoCommunity at
http://data.geocomm.com/readme/dcw/dcw.html.  To read and process the data you
should install GMT, the Generic Mapping Tools.


%prep
%setup -q

# Nothing to build

%install
mkdir -p %{buildroot}/%{_datadir}/%{name}
cp -a *.nc *.txt %{buildroot}/%{_datadir}/%{name}/


%files
%doc COPYING.LESSERv3 COPYINGv3 LICENSE.TXT README.TXT
%{_datadir}/%{name}/


%changelog
* Sat Apr 05 2014 Igor Vlasenko <viy@altlinux.ru> 1.1.1-alt1_1
- import

