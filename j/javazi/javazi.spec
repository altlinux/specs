Name: javazi
Version: %{get_version tzdata}
Release: alt1

Summary: Timezone data for Java
License: Public Domain
Group: System/Base
Url: https://www.iana.org/time-zones
BuildArch: noarch

Requires: tzdata = %{get_SVR tzdata}
Provides: tzdata-java = %EVR
Obsoletes: tzdata-java < %EVR

BuildRequires: tzdata-source

%description
This package contains timezone information for use by Java runtimes.

%install
mkdir -p %buildroot%_datadir/javazi{,-1.8}

%files
%_datadir/javazi*

%changelog
* Tue Feb 20 2018 Dmitry V. Levin <ldv@altlinux.org> 2018c-alt1
- Bootstrap.
