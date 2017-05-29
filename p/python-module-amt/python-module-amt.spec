Name: python-module-amt
Version: 0.7.0
Release: alt1
Summary: Tools for interacting with Intel's Active Management Technology

Group: Development/Python
License: Apache
URL: https://pypi.python.org/pypi/amt/
Source0: %name-%version.tar

BuildArch: noarch
BuildRequires: python-devel
BuildRequires: python-module-setuptools

%description
AMT is a light weight hardware control interface put into some Intel
based laptops and desktops as a tool for corporate fleets to manage
hardware. It provides the basics of power control, as well as remote
console via VNC. It functions by having a dedicated service processor
sniff traffic off the network card on specific ports before it gets to
the operating system. Some versions of Intel NUC boxes have AMT, which
make them ideal candidates for building a reasonable cluster in your
basement.

There was once a tool called ``amttool`` which let you interact with
these systems from Linux. This used the SOAP interface to AMT. That
was removed in v9 of the firmware, which means it no longer works with
modern AMT in the field.

The interface that remains is CIM, a standard from the DMTF that
builds XML models for all the things. There exist very few examples
for how to make this work on the internet, with one exception: the
OpenStack Baremetal (Ironic) service. It has native support for AMT
hardware control.

This project is derivative work from Ironic. The heavy lifting of
understanding all the CIM magic incantations, and oh the magic they
are, comes from that code. Refactored for a more minimal usage.

%prep
%setup

%build
%python_build

%install
%python_install

%files
%_bindir/amtctrl
%python_sitelibdir/*

%changelog
* Tue May 23 2017 Lenar Shakirov <snejok@altlinux.ru> 0.7.0-alt1
- Initial build for ALT


