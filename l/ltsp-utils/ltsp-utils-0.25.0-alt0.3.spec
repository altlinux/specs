%def_with info
%def_without admin
%def_without cfg

%define bname ltsp
Name: %bname-utils
%define ver 0.25
%define rel 0
Version: %ver.%rel
Release: alt0.3
Summary: Utilities for LTSP server
License: GPL2
Group: Networking/Other
URL: http://www.%bname.org
Source: ftp://%bname.mirrors.tds.net/pub/%bname/tarballs/%name-%ver-%rel.tar.bz2
BuildArch: noarch
%{?_with_info:Provides: %{bname}info = %version-%release}
%{?_with_admin:Provides: %{bname}admin = %version-%release}
%{?_with_cfg:Provides: %{bname}cfg = %version-%release}

%description
This package includes the following utilities for LTSP server:
%if_with info
%{bname}info  - for querying the workstation, to learn things, such as
            which sound daemon is being used.
%endif
%{?_with_admin:%{bname}admin - for installing and managing the packages on an LTSP server}
%{?_with_cfg:%{bname}cfg   - for configuring the services on an LTSP server}


%prep
%setup -n %name


%install
%{?_with_info:install -pD -m 0755 %{bname}info %buildroot%_bindir/%{bname}info}
%{?_with_admin:install -pD -m 0755 %{bname}admin %buildroot%_sbindir/%{bname}admin}
%{?_with_cfg:install -pD -m 0755 %{bname}cfg %buildroot%_sbindir/%{bname}cfg}
bzip2 --best --keep --force ChangeLog


%files
%doc ChangeLog.*
%{?_with_info:%_bindir/%{bname}info}
%{?_with_admin:%_sbindir/%{bname}admin}
%{?_with_cfg:%_sbindir/%{bname}cfg}


%changelog
* Mon Aug 06 2007 Led <led@altlinux.ru> 0.25.0-alt0.3
- removed %{bname}info-sound.sh

* Tue Jun 26 2007 Led <led@altlinux.ru> 0.25.0-alt0.2
- cleaned up duplicates of ChangeLog
- fixed License

* Thu Apr 26 2007 Led <led@altlinux.ru> 0.25.0-alt0.1
- initial build
- added %{bname}info-sound.sh
