%add_python_req_skip XenAPI
%add_python_req_skip fencing
%add_python_req_skip fencing_snmp
Name: fence-agents
Summary: Fence Agents
Version: 4.0.24
Release: alt3%ubt
License: GPLv2+ and LGPLv2+
Group: System/Base
URL: http://sourceware.org/cluster/wiki/

Source0: %name-%version.tar.xz
Patch0: fence-agents-pve-4.0.24-alt.patch

BuildRequires(pre): rpm-build-ubt
BuildRequires: autoconf-archive python-module-pexpect python-module-pycurl python-module-requests python-module-suds sudo xml-utils xsltproc

%description
Fence Agents is a collection of scripts to handle remote
power management for several devices.

%prep
%setup -q
%patch0 -p2

sed -i '/^.*pywsman.*/d' configure.ac
rm -fr fence/agents/{amt_ws,sbd}

%build
%autoreconf
export PYTHON="/usr/bin/python"
%configure --localstatedir=%_var
%make_build

%install
%make DESTDIR=%buildroot install

ln -sf ../../sbin/fence_scsi %buildroot%_datadir/cluster/fence_scsi_check
ln -sf ../../sbin/fence_scsi %buildroot%_datadir/cluster/fence_scsi_check_hardreboot

%package common
BuildArch: noarch
Group: System/Base
Summary: Common utilities for fence agents

%description common
Fence Agents is a collection of scripts and libraries to handle remote power management for various devices.

%files common
%doc doc/COPYING.* doc/COPYRIGHT doc/README.licence
%_datadir/fence
%_datadir/cluster
%exclude %_datadir/cluster/fence_scsi_check*
%_datadir/fence/fencing.py
%_datadir/fence/fencing_snmp.py
%exclude %_sbindir/fence_ack_manual
%exclude %_man8dir/fence_ack_manual.8*
%exclude %_sbindir/fence_dummy
%exclude %_man8dir/fence_dummy.8*
%exclude %_sbindir/fence_zvm
%exclude %_man8dir/fence_zvm.8*

%package alom
BuildArch: noarch
Group: System/Base
Summary: Fence agent for SUN ALOM
Requires: telnet openssh-clients
Requires: fence-agents-common = %version-%release

%description alom
The fence-agents-apc package contains a fence agent for SUN ALOM

%files alom
%_sbindir/fence_alom
%_man8dir/fence_alom.8*

%package apc
BuildArch: noarch
Group: System/Base
Summary: Fence agent for APC devices
Requires: telnet openssh-clients
Requires: fence-agents-common = %version-%release

%description apc
The fence-agents-apc package contains a fence agent for APC devices that are accessed via telnet or SSH.

%files apc
%_sbindir/fence_apc
%_man8dir/fence_apc.8*

%package apc-snmp
BuildArch: noarch
Group: System/Base
Summary: Fence agent for APC devices (SNMP)
Requires: net-snmp-utils
Requires: fence-agents-common = %version-%release

%description apc-snmp
The fence-agents-apc-snmp package contains a fence agent for APC devices that are accessed via the SNMP protocol.

%files apc-snmp
%_sbindir/fence_apc_snmp
%_man8dir/fence_apc_snmp.8*
%_sbindir/fence_tripplite_snmp
%_man8dir/fence_tripplite_snmp.8*

%package amt
BuildArch: noarch
Group: System/Base
Summary: Fence agent for Intel AMT devices
Requires: amtterm
Requires: fence-agents-common = %version-%release

%description amt
The fence-agents-amt package contains a fence agent for AMT compatibile devices that are accessed via 3rd party software.

%files amt
%_sbindir/fence_amt
%_man8dir/fence_amt.8*

#%package amt-ws
#BuildArch: noarch
#License: ASL 2.0
#Group: System/Base
#Summary: Fence agent for Intel AMT (WS-Man) devices
#Requires: fence-agents-common >= %version-%release
#Requires: openwsman-python3

#%description amt-ws
#The fence-agents-amt-ws package contains a fence agent for AMT (WS-Man) devices.

#%files amt-ws
#%_sbindir/fence_amt_ws
#%_man8dir/fence_amt_ws.8*

%package bladecenter
BuildArch: noarch
Group: System/Base
Summary: Fence agent for IBM BladeCenter
Requires: telnet openssh-clients
Requires: fence-agents-common = %version-%release

%description bladecenter
The fence-agents-bladecenter package contains a fence agent for IBM BladeCenter devices that are accessed via telnet or SSH.

%files bladecenter
%_sbindir/fence_bladecenter
%_man8dir/fence_bladecenter.8*

%package brocade
BuildArch: noarch
Group: System/Base
Summary: Fence agent for Brocade switches
Requires: telnet openssh-clients
Requires: fence-agents-common = %version-%release

%description brocade
The fence-agents-bladecenter package contains a fence agent for Brocade devices that are accessed via telnet or SSH.

%files brocade
%_sbindir/fence_brocade
%_man8dir/fence_brocade.8*

%package cisco-mds
BuildArch: noarch
Group: System/Base
Summary: Fence agent for Cisco MDS 9000 series
Requires: net-snmp-utils
Requires: fence-agents-common = %version-%release

%description cisco-mds
The fence-agents-cisco-mds package contains a fence agent for Cisco MDS 9000 series devices that are accessed via the SNMP protocol.

%files cisco-mds
%_sbindir/fence_cisco_mds
%_man8dir/fence_cisco_mds.8*

%package cisco-ucs
BuildArch: noarch
Group: System/Base
Summary: Fence agent for Cisco UCS series
Requires: fence-agents-common = %version-%release

%description cisco-ucs
The fence-agents-cisco-ucs package contains a fence agent for Cisco UCS series devices that are accessed via the SNMP protocol.

%files cisco-ucs
%_sbindir/fence_cisco_ucs
%_man8dir/fence_cisco_ucs.8*

%package compute
BuildArch: noarch
Group: System/Base
Summary: Fence agent for Nova compute nodes
Requires: fence-agents-common = %version-%release

%description compute
The fence-agents-compute package contains a fence agent for Nova compute nodes.

%files compute
%_sbindir/fence_compute
%_man8dir/fence_compute.8*

%package docker
BuildArch: noarch
Group: System/Base
Summary: Fence agent for Docker
Requires: fence-agents-common = %version-%release

%description docker
The fence-agents-docker package contains a fence agent for Docker images that are accessed over HTTP.

%files docker
%_sbindir/fence_docker
%_man8dir/fence_docker.8*

%package drac
BuildArch: noarch
Group: System/Base
Summary: Fence agent for Dell DRAC
Requires: telnet
Requires: fence-agents-common = %version-%release

%description drac
The fence-agents-drac package contains a fence agent for Dell DRAC IV series devices that are accessed via telnet.

%files drac
%_sbindir/fence_drac
%_man8dir/fence_drac.8*

%package drac5
BuildArch: noarch
Group: System/Base
Summary: Fence agent for Dell DRAC 5
Requires: telnet openssh-clients
Requires: fence-agents-common = %version-%release

%description drac5
The fence-agents-drac5 package contains a fence agent for Dell DRAC 5 series devices that are accessed via telnet or SSH.

%files drac5
%_sbindir/fence_drac5
%_man8dir/fence_drac5.8*

%package eaton-snmp
BuildArch: noarch
Group: System/Base
Summary: Fence agent for Eaton network power switches
Requires: net-snmp-utils
Requires: fence-agents-common = %version-%release

%description eaton-snmp
The fence-agents-eaton-snmp package contains a fence agent for Eaton network power switches that are accessed via the SNMP protocol.

%files eaton-snmp
%_sbindir/fence_eaton_snmp
%_man8dir/fence_eaton_snmp.8*

%package emerson
BuildArch: noarch
Group: System/Base
Summary: Fence agent for Emerson devices (SNMP)
Requires: fence-agents-common = %version-%release

%description emerson
The fence-agents-emerson package contains a fence agent for Emerson devices that are accessed via the SNMP protocol.

%files emerson
%_sbindir/fence_emerson
%_man8dir/fence_emerson.8*

%package eps
BuildArch: noarch
Group: System/Base
Summary: Fence agent for ePowerSwitch 8M+ power switches
Requires: fence-agents-common = %version-%release

%description eps
The fence-agents-eps package contains a fence agent for ePowerSwitch 8M+ power switches that are accessed via the HTTP(s) protocol.

%files eps
%_sbindir/fence_eps
%_man8dir/fence_eps.8*

%package hpblade
BuildArch: noarch
Group: System/Base
Summary: Fence agent for HP BladeSystem devices
Requires: telnet openssh-clients
Requires: fence-agents-common = %version-%release

%description hpblade
The fence-agents-hpblade package contains a fence agent for HP BladeSystem devices that are accessed via telnet or SSH.

%files hpblade
%_sbindir/fence_hpblade
%_man8dir/fence_hpblade.8*

%package hds-cb
BuildArch: noarch
Group: System/Base
Summary: Fence agent for Hitachi Compute Blade systems
Requires: telnet
Requires: fence-agents-common = %version-%release

%description hds-cb
The fence-agents-hds-cb package contains a fence agent for Hitachi Compute Blades that are accessed via telnet.

%files hds-cb
%_sbindir/fence_hds_cb
%_man8dir/fence_hds_cb.8*

%package ibmblade
BuildArch: noarch
Group: System/Base
Summary: Fence agent for IBM BladeCenter
Requires: net-snmp-utils
Requires: fence-agents-common = %version-%release

%description ibmblade
The fence-agents-ibmblade package contains a fence agent for IBM BladeCenter devices that are accessed via the SNMP protocol.

%files ibmblade
%_sbindir/fence_ibmblade
%_man8dir/fence_ibmblade.8*

%package ifmib
BuildArch: noarch
Group: System/Base
Summary: Fence agent for devices with IF-MIB interfaces
Requires: net-snmp-utils
Requires: fence-agents-common = %version-%release

%description ifmib
The fence-agents-ifmib package contains a fence agent for IF-MIB interfaces that are accessed via the SNMP protocol.

%files ifmib
%_sbindir/fence_ifmib
%_man8dir/fence_ifmib.8*

%package ilo2
BuildArch: noarch
Group: System/Base
Summary: Fence agent for HP iLO2 devices
Requires: gnutls-utils
Requires: fence-agents-common = %version-%release

%description ilo2
The fence-agents-ilo2 package contains a fence agent for HP iLO2 devices that are accessed via the HTTP(s) protocol.

%files ilo2
%_sbindir/fence_ilo
%_sbindir/fence_ilo2
%_man8dir/fence_ilo.8*
%_man8dir/fence_ilo2.8*

%package ilo-mp
BuildArch: noarch
Group: System/Base
Summary: Fence agent for HP iLO MP devices
Requires: telnet openssh-clients
Requires: fence-agents-common = %version-%release

%description ilo-mp
The fence-agents-ilo-mp package contains a fence agent for HP iLO MP devices that are accessed via telnet or SSH.

%files ilo-mp
%_sbindir/fence_ilo_mp
%_man8dir/fence_ilo_mp.8*

%package ilo-moonshot
BuildArch: noarch
Group: System/Base
Summary: Fence agent for HP iLO Moonshot devices
Requires: telnet openssh-clients
Requires: fence-agents-common = %version-%release

%description ilo-moonshot
The fence-agents-ilo-moonshot package contains a fence agent for HP iLO Moonshot devices that are accessed via telnet or SSH.

%files ilo-moonshot
%_sbindir/fence_ilo_moonshot
%_man8dir/fence_ilo_moonshot.8*

%package ilo-ssh
BuildArch: noarch
Group: System/Base
Summary: Fence agent for HP iLO devices over SSH
Requires: openssh-clients
Requires: fence-agents-common = %version-%release

%description ilo-ssh
The fence-agents-ilo-ssh package contains a fence agent for HP iLO devices that are accessed via telnet or SSH.

%files ilo-ssh
%_sbindir/fence_ilo_ssh
%_man8dir/fence_ilo_ssh.8*
%_sbindir/fence_ilo3_ssh
%_man8dir/fence_ilo3_ssh.8*
%_sbindir/fence_ilo4_ssh
%_man8dir/fence_ilo4_ssh.8*

%package intelmodular
BuildArch: noarch
Group: System/Base
Summary: Fence agent for devices with Intel Modular interfaces
Requires: net-snmp-utils
Requires: fence-agents-common = %version-%release

%description intelmodular
The fence-agents-intelmodular package contains a fence agent for Intel Modular interfaces that are accessed via the SNMP protocol.

%files intelmodular
%_sbindir/fence_intelmodular
%_man8dir/fence_intelmodular.8*

%package ipdu
BuildArch: noarch
Group: System/Base
Summary: Fence agent for IBM iPDU network power switches
Requires: net-snmp-utils
Requires: fence-agents-common = %version-%release

%description ipdu
The fence-agents-ipdu package contains a fence agent for IBM iPDU network power switches that are accessed via the SNMP protocol.

%files ipdu
%_sbindir/fence_ipdu
%_man8dir/fence_ipdu.8*

%package ipmilan
BuildArch: noarch
Group: System/Base
Summary: Fence agent for devices with IPMI interface
Requires: ipmitool
Requires: fence-agents-common = %version-%release

%description ipmilan
The fence-agents-ipmilan package contains a fence agent for devices with IPMI interface.

%files ipmilan
%_sbindir/fence_ipmilan
%_man8dir/fence_ipmilan.8*
%_sbindir/fence_idrac
%_man8dir/fence_idrac.8*
%_sbindir/fence_ilo3
%_man8dir/fence_ilo3.8*
%_sbindir/fence_ilo4
%_man8dir/fence_ilo4.8*
%_sbindir/fence_imm
%_man8dir/fence_imm.8*

%package kdump
Group: System/Base
Summary: Fence agent for use with kdump crash recovery service
Requires: fence-agents-common = %version-%release

%description kdump
The fence-agents-kdump package contains a fence agent for use with kdump crash recovery service.

%files kdump
%_sbindir/fence_kdump
%_libexecdir/fence_kdump_send
%_man8dir/fence_kdump.8*
%_man8dir/fence_kdump_send.8*

%package ldom
BuildArch: noarch
Group: System/Base
Summary: Fence agent for Sun LDom virtual machines
Requires: telnet openssh-clients
Requires: fence-agents-common = %version-%release

%description ldom
The fence-agents-ldom package contains a fence agent for APC devices that are accessed via telnet or SSH.

%files ldom
%_sbindir/fence_ldom
%_man8dir/fence_ldom.8*

%package lpar
BuildArch: noarch
Group: System/Base
Summary: Fence agent for IBM LPAR
Requires: telnet openssh-clients
Requires: fence-agents-common = %version-%release

%description lpar
The fence-agents-lpar package contains a fence agent for IBM LPAR devices that are accessed via telnet or SSH.

%files lpar
%_sbindir/fence_lpar
%_man8dir/fence_lpar.8*

%package mpath
BuildArch: noarch
Group: System/Base
Summary: Fence agent for reservations over Device Mapper Multipath
Requires: multipath-tools
Requires: fence-agents-common = %version-%release

%description mpath
The fence-agents-mpath package contains fence agent for SCSI persisent reservation over Device Mapper Multipath.

%files mpath
%_sbindir/fence_mpath
%_man8dir/fence_mpath.8*

%package netio
BuildArch: noarch
Group: System/Base
Summary: Fence agent for Koukaam NETIO devices
Requires: telnet openssh-clients
Requires: fence-agents-common = %version-%release

%description netio
The fence-agents-netio package contains a fence agent for Koukaam NETIO devices that are accessed via telnet or SSH.

%files netio
%_sbindir/fence_netio
%_man8dir/fence_netio.8*

%package ovh
BuildArch: noarch
Group: System/Base
Summary: Fence agent for OVH provider
Requires: fence-agents-common = %version-%release

%description ovh
The fence-agents-apc package contains a fence agent for OVH hosting provider.

%files ovh
%_sbindir/fence_ovh
%_man8dir/fence_ovh.8*

%package pve
BuildArch: noarch
Group: System/Base
Summary: Fence agent for PVE
Requires: fence-agents-common = %version-%release

%description pve
The fence-agents-apc package contains a fence agent for PVE.

%files pve
%_sbindir/fence_pve
%_man8dir/fence_pve.8*

%package raritan
BuildArch: noarch
Group: System/Base
Summary: Fence agent for Raritan Dominion PX
Requires: fence-agents-common = %version-%release

%description raritan
The fence-agents-apc package contains a fence agent for Raritan Dominion PX.

%files raritan
%_sbindir/fence_raritan
%_man8dir/fence_raritan.8*

%package rcd-serial
BuildArch: noarch
Group: System/Base
Summary: Fence agent for RCD serial
Requires: fence-agents-common = %version-%release

%description rcd-serial
The fence-agents-apc package contains a fence agent for RCD serial.

%files rcd-serial
%_sbindir/fence_rcd_serial
%_man8dir/fence_rcd_serial.8*

%package rhevm
BuildArch: noarch
Group: System/Base
Summary: Fence agent for RHEV-M
Requires: fence-agents-common = %version-%release

%description rhevm
The fence-agents-rhevm package contains a fence agent for RHEV-M via REST API.

%files rhevm
%_sbindir/fence_rhevm
%_man8dir/fence_rhevm.8*

%package rsa
BuildArch: noarch
Group: System/Base
Summary: Fence agent for IBM RSA II
Requires: telnet openssh-clients
Requires: fence-agents-common = %version-%release

%description rsa
The fence-agents-rsa package contains a fence agent for IBM RSA II devices that are accessed via telnet or SSH.

%files rsa
%_sbindir/fence_rsa
%_man8dir/fence_rsa.8*

%package rsb
BuildArch: noarch
Group: System/Base
Summary: Fence agent for Fujitsu RSB
Requires: telnet openssh-clients
Requires: fence-agents-common = %version-%release

%description rsb
The fence-agents-rsb package contains a fence agent for Fujitsu RSB devices that are accessed via telnet or SSH.

%files rsb
%_sbindir/fence_rsb
%_man8dir/fence_rsb.8*

%package sanbox2
BuildArch: noarch
Group: System/Base
Summary: Fence agent for QLogic SANBox2 FC switches
Requires: telnet
Requires: fence-agents-common = %version-%release

%description sanbox2
The fence-agents-sanbox2 package contains a fence agent for QLogic SANBox2 switches that are accessed via telnet.

%files sanbox2
%_sbindir/fence_sanbox2
%_man8dir/fence_sanbox2.8*

#%package sbd
#BuildArch: noarch
#Group: System/Base
#Summary: Fence agent for SBD (storage-based death)
#Requires: sbd
#Requires: fence-agents-common = %version-%release

#%description sbd
#The fence-agents-sbd package contains a fence agent for SBD (storage-based death).

#%files sbd
#%_sbindir/fence_sbd
#%_man8dir/fence_sbd.8*

%package scsi
BuildArch: noarch
Group: System/Base
Summary: Fence agent for SCSI persisent reservations
Requires: sg3_utils
Requires: fence-agents-common = %version-%release

%description scsi
The fence-agents-scsi package contains fence agent for SCSI persisent reservations.

%files scsi
%_sbindir/fence_scsi
%_datadir/cluster/fence_scsi_check*
%_man8dir/fence_scsi.8*

%package vbox
BuildArch: noarch
Group: System/Base
Summary: Fence agent for VirtualBox
Requires: openssh-clients
Requires: fence-agents-common = %version-%release

%description vbox
The fence-agents-vbox package contains a fence agent for VirtualBox dom0 accessed via SSH.

%files vbox
%_sbindir/fence_vbox
%_man8dir/fence_vbox.8*

%package virsh
BuildArch: noarch
Group: System/Base
Summary: Fence agent for virtual machines based on libvirt
Requires: openssh-clients libvirt-client
Requires: fence-agents-common = %version-%release

%description virsh
The fence-agents-virsh package contains a fence agent for virtual machines that are accessed via SSH.

%files virsh
%_sbindir/fence_virsh
%_man8dir/fence_virsh.8*

%package vmware
BuildArch: noarch
Group: System/Base
Summary: Fence agent for VMWare with VI Perl Toolkit or vmrun
Requires: fence-agents-common = %version-%release

%description vmware
The fence-agents-vmware package contains a fence agent for VMWare accessed with VI Perl Toolkit or vmrun.

%files vmware
%_sbindir/fence_vmware
%_man8dir/fence_vmware.8*

%package vmware-soap
BuildArch: noarch
Group: System/Base
Summary: Fence agent for VMWare with SOAP API v4.1+
Requires: fence-agents-common = %version-%release

%description vmware-soap
The fence-agents-vmware-soap package contains a fence agent for VMWare with SOAP API v4.1+

%files vmware-soap
%_sbindir/fence_vmware_soap
%_man8dir/fence_vmware_soap.8*

%package wti
BuildArch: noarch
Group: System/Base
Summary: Fence agent for WTI Network power switches
Requires: telnet openssh-clients
Requires: fence-agents-common = %version-%release

%description wti
The fence-agents-wti package contains a fence agent for WTI network power switches that are accessed via telnet or SSH.

%files wti
%_sbindir/fence_wti
%_man8dir/fence_wti.8*

%package xenapi
BuildArch: noarch
Group: System/Base
Summary: Fence agent for Citrix XenServer over XenAPI
Requires: fence-agents-common = %version-%release

%description xenapi
The fence-agents-xenapi package contains a fence agent for Citrix XenServer accessed over XenAPI.

%files xenapi
%_sbindir/fence_xenapi
%_man8dir/fence_xenapi.8*

%package zvm
BuildArch: noarch
Group: System/Base
Summary: Fence agent for IBM z/VM over IP
Requires: fence-agents-common = %version-%release

%description zvm
The fence-agents-zvm package contains a fence agent for IBM z/VM over IP.

%files zvm
%_sbindir/fence_zvmip
%_man8dir/fence_zvmip.8*

%changelog
* Fri Jan 19 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 4.0.24-alt3%ubt
- Fixed localstatedir location.

* Wed Apr 19 2017 Sergey Novikov <sotor@altlinux.org> 4.0.24-alt2%ubt
- fix fence-pve

* Thu Apr 13 2017 Valery Inozemtsev <shrek@altlinux.ru> 4.0.24-alt1
- initial release

