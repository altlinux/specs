Name:    pydxcluster
Version: 2.21
Release: alt1

Summary: pyDxCluster is python (tk) HAM Dx Cluster for Linux users
License: GPLv3
Group:   Communications
URL:     http://sourceforge.net/projects/pydxcluster/

Packager: Andrey Cherepanov <cas@altlinux.org>

BuildRequires: python-module-pygame
BuildRequires: python-module-requests
BuildRequires: python-modules-tkinter

BuildArch: noarch

Source:  pyDXCluster_v2_21.tar.gz
Patch:   pydxcluster-use-system-config.patch

%description
pyDxCluster is python (tk) HAM Dx Cluster for Linux users
Feautres:
- connect to any cluster server
- connect to any reverse beacon server
- connect to PSKReporter server
- send spot
- band selecting
- send/receive data (callsign, frequency) to/from FlDigi with
  fldigi-shell - send command to cluster
- save all data to config (host, port,username,password, bandselections,
  QRZ .com username and password, and alll window positions)
- if you registred qrz.com, Qrzcq.com or hamqth.com user, puit the
  username and password to Entry's, and view on "Detailed view" window
  all data from spots.
- Callsing Hunter window: observ 10 different callsign, and mark
  specific color on the cluster list. memorise last heard frequency
- Separated console, and detailed info, and Callsign hunter window

%prep
%setup -c %name-%version
%patch -p2

%install
install -Dm0755 pyDxCluster_v2_21.py %buildroot%_bindir/%name
install -d %buildroot%_datadir/%name
cp pydxcluster.cfg default.col %buildroot%_datadir/%name

%files
%doc LICENSE.txt LICENSZ_HUN.txt
%_bindir/%name
%dir %_datadir/%name
%_datadir/%name/*

%changelog
* Sun Nov 29 2015 Andrey Cherepanov <cas@altlinux.org> 2.21-alt1
- Initial build for ALT Linux
