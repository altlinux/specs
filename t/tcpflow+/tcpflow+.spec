Name: tcpflow+
Version: 1.4.4
Release: alt1
License: GPLv3
Group: Monitoring
URL: https://github.com/simsong/tcpflow
Summary: Network traffic recorder (new version)

Source0: %{name}-%{version}.tar

BuildRequires: gcc-c++ boost-devel libcairo-devel libpcap-devel zlib-devel
BuildRequires: openssl-devel

%description
tcpflow is a program that captures data (or reads in a pcap file)
transmitted as part of TCP connections (flows), and stores the data in
a way that is convenient for protocol analysis and debugging. Each TCP
flow is stored in its own file. Thus, the typical TCP flow will be
stored in two files, one for each direction. tcpflow can also process
stored 'tcpdump' packet flows.

%prep
%setup

%build
%autoreconf
%configure
%make_build

%install
%makeinstall_std

%files
%_bindir/tcpflow
%_man1dir/tcpflow.1.gz

%changelog
* Mon Nov 17 2014 Paul Wolneykien <manowar@altlinux.org> 1.4.4-alt1
- New/alternative tcpflow version. Initial build for ALT Linux.
- Freshed up to v1.4.4 with the help of cronbuild and update-source-functions.

