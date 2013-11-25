Name: debug-contracts
Version: 0.1
Release: alt1.r8

Summary: Dummy services for debugging Contractor
Group: Graphical desktop/Other
License: BSD-3-Clause
Url: https://code.launchpad.net/~contractor-dev/contractor/debug-contracts

Source0: %name.tar.xz
Source1: copyright

Requires: contractor zenity

BuildArch: noarch

# Automatically added by buildreq on Mon Nov 25 2013 (-bi)
# optimized out: python-base xz
BuildRequires: zenity

%description
This is a set of dummy services for Contractor, designed to aid debugging its
process spawning. They let you view what exactly it lauches and what parameters
does it pass to the service provider.

%prep
%setup -q -n %name
cp %SOURCE1 .

%build

%install
mkdir -p %buildroot%_bindir/
mkdir -p %buildroot%_datadir/contractor/

install -p -m0755 debug-contract %buildroot%_bindir/
install -p -m0644 *.contract %buildroot%_datadir/contractor/

%files
%doc copyright
%_bindir/*
%_datadir/contractor/*.contract

%changelog
* Mon Nov 25 2013 Igor Zubkov <icesik@altlinux.org> 0.1-alt1.r8
- 0.1-r8

