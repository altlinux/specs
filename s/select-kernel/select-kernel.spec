Name: select-kernel
Version: 0.99.1
Release: alt1

Summary: Tool to install/upgrade/remove system kernel
License: GPL
Group: System/Kernel and hardware

Packager: Anatoly Kitaykin <cetus@altlinux.ru>
Source: %name-%version.tar
BuildArch: noarch

%description
This package contains a script to conveniently install/update/
upgrade/remove kernel and modules.

It allows to select a kernel from the list of currently available
ones and to choose an action for this kernel from menu, and then
executes your task.

When installing new kernel package it will try to install all kernel
modules as already installed in system. That behavior is cross-flavour.

%prep
%setup

%install
install -pDm755 %name %buildroot%_sbindir/%name

%files
%_sbindir/*

%changelog
* Fri Aug 31 2012 Anatoly Kitaykin <cetus@altlinux.org> 0.99.1-alt1
- Initial build

