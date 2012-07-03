Name: iproute2fs
Summary: rtnetlink(7) virtual filesystem
Version: 0.1.1
Release: alt3.1
License: GPLv3
Group: Development/Python
URL: http://projects.radlinux.org/cx/

BuildArch: noarch
BuildPreReq: python-devel rpm-build-python

Requires: python-module-cxnet >= 0.7.2-alt3

Source: %name-%version.tar

%description
Simple VFS implementation that represents rtnetlink(7)
objects as files -- interfaces, routes etc.

%prep
%setup

%install
%{__python} setup.py install --root=%buildroot --install-lib=%{python_sitelibdir}
install -D -m 755 %{name}.service   %buildroot/%_initrddir/%{name}
install -D -m 644 docs/%{name}.1    %buildroot/%_man1dir/%{name}.1
install -D -m 644 docs/README.ALT   %buildroot/%_docdir/%{name}-%{version}/README.ALT

%files

%_initrddir/%{name}
%_bindir/%{name}
%_man1dir/%{name}.*
%_docdir/%{name}-%{version}
%{python_sitelibdir}/%{name}*

%changelog
* Sat Oct 22 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.1.1-alt3.1
- Rebuild with Python-2.7

* Wed Aug 29 2011 Peter V. Saveliev <peet@altlinux.org> 0.1.1-alt3
- experimental routing support (read-only)

* Wed Aug 28 2011 Peter V. Saveliev <peet@altlinux.org> 0.1.1-alt2
- ARP cache tables (for every interface, r/o)
- new lines after mtu and flags content

* Wed Aug 24 2011 Peter V. Saveliev <peet@altlinux.org> 0.1.1-alt1
- initial ALT Linux build
