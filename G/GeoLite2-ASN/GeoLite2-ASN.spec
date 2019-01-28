# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}

Name:           GeoLite2-ASN
Version: 20190122
Release: alt1
Summary:        Free IP geolocation %name database
License:        CC-BY-SA
Group:          Sciences/Geosciences
URL:            https://dev.maxmind.com/geoip/geoip2/geolite2/
Source0:        https://geolite.maxmind.com/download/geoip/database/%{name}_%{version}.tar.gz
BuildArch:      noarch

# recommends
# Requires:     geoipupdate

%description 
GeoLite2 Autonomous System Number database is a free IP geolocation database
comparable to, but less accurate than, MaxMind's GeoIP2 database.

This product includes GeoLite2 data created by MaxMind,
available from http://www.maxmind.com.

%prep
%setup -q -n %{name}_%{version}


%install
install -D -p -m 0644 %{name}.mmdb %{buildroot}%{_datadir}/GeoIP/%{name}.mmdb

%files
%doc --no-dereference COPYRIGHT.txt LICENSE.txt
%dir %{_datadir}/GeoIP
# to allow updates using geoipupdate
%verify(not md5 size mtime) %{_datadir}/GeoIP/%{name}.mmdb

%changelog
* Mon Jan 28 2019 Igor Vlasenko <viy@altlinux.ru> 20190122-alt1
- repocop cronbuild 20190128. At your service.

* Thu Jan 24 2019 Igor Vlasenko <viy@altlinux.ru> 20180925-alt1
- new version
