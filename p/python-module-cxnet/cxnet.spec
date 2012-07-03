%define pprefix python-module

Name: python-module-cxnet
Summary: Python netlink library and more
Version: 0.7.2
Release: alt3.1
License: GPLv3
Group: Development/Python
URL: http://projects.radlinux.org/cx/

BuildArch: noarch
BuildPreReq: python-devel rpm-build-python

Source: %name-%version.tar

%description
Network protocol implementations for Connexion project can be used
by any Python program. This package includes:

* mDNS client/server with DNSSEC extensions

Netlink family protocol implementations:

* Generic netlink
* RT netlink (limited)
* IPQ netlink
* Taskstats

Common definitions of packet structures (in ctypes):

* ARP
* Ethernet
* IPv4
* TCP

%prep
%setup

%install
%makeinstall python=%{__python} root=%buildroot lib=%{python_sitelibdir}

%files

%_bindir/cxkey
%{python_sitelibdir}/cxnet*

%changelog
* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.7.2-alt3.1
- Rebuild with Python-2.7

* Sun Aug 29 2011 Peter V. Saveliev <peet@altlinux.org> 0.7.2-alt3
- new class: cxnet.netlink.rtnl.RtNetlinkEvent (hashable)

* Sun Aug 28 2011 Peter V. Saveliev <peet@altlinux.org> 0.7.2-alt2
- use Condition() to sync internal IpRoute2 commands

* Wed Aug 24 2011 Peter V. Saveliev <peet@altlinux.org> 0.7.2-alt1
- no default RT Netlink thread - one should start it manually
- exception handling
- iproute2 cache removed
- taskstats patches from Sergei Lebedev

* Wed Aug 17 2011 Peter V. Saveliev <peet@altlinux.org> 0.7.1-alt5
- moved cxnet to a separate repository
- IPv6 addresses support for `get` commands
- typo fixed in generic.py
- some API changes in:
    - rtnl.py: instead of 'del' there are 'remove' events from now on
    - genetlink.py: do not call recv() by send_cmd()
    - taskstats.py: use __str__ instead of pprint

* Thu Jul  7 2011 Peter V. Saveliev <peet@altlinux.org> 0.7.1-alt4
- iproute2 can add and delete addresses on interfaces
- more attributes parsed by rtnl
- wireless interfaces detection (ioctl) in rtnl
- get/set attributes in attr_msg class
- new utility function (make_map) that creates two-way mappings of set of attributes

* Wed Jun 17 2011 Peter V. Saveliev <peet@altlinux.org> 0.7.1-alt3
- cxkey utility added
- named parameters for py9p.Dir
- zeroconf.py fixed and tested

* Sun May 29 2011 Peter V. Saveliev <peet@altlinux.org> 0.7.1-alt2
- Sisyphus build fixed.

* Sun May 29 2011 Peter V. Saveliev <peet@altlinux.org> 0.7.1-alt1
- RPM prepared.

* Wed Nov 25 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.4.6-alt7.svn1392.1
- Rebuilt with python 2.6
