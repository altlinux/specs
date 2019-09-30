# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
Summary:   Pairing of machines for network testing
Name:      pairing
Version:   1.3
Release:   alt1_8
License:   GPLv2
Group:     Networking/Other
Url:       http://ahorvath.web.cern.ch/ahorvath/pairing/
Source:    %{name}-%{version}.tar.bz2
Source44: import.info

%description
Run this on a set of machines and get them paired up nicely for some
network-related activity.

It uses multicast to find potential partners and TCP to actually pair up with
them.

%prep
%setup -q

# honor user CFLAGS thus fixing empty debugsourcefiles.list
perl -pi -e 's/^(CFLAGS.*)-Wall(.*)/$1\$\(RPM_OPT_FLAGS\) -Wall$2/' Makefile

%build
make

%install
mkdir -p %{buildroot}%{_bindir}
install -m 755 pair %{buildroot}%{_bindir}/pair

%files
%{_bindir}/pair


%changelog
* Mon Sep 30 2019 Igor Vlasenko <viy@altlinux.ru> 1.3-alt1_8
- new version

