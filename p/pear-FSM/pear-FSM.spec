%define pear_name FSM

Name: pear-FSM
Version: 1.3.0
Release: alt1

Summary: Finite State Machine

License: MIT License
Group: Development/Other
Url: http://pear.php.net/package/FSM

Packager: Vitaly Lipatov <lav@altlinux.ru>

Source: http://pear.php.net/get/FSM-%version.tar.bz2

BuildArchitectures: noarch

Requires: pear-core
BuildRequires: pear-core rpm-build-pear

%description
The FSM package provides a simple class that implements a Finite State
Machine.

In addition to maintaining state, this FSM also maintains a user-defined
payload, therefore effectively making the machine a Pushdown Automaton (a
finite state machine with memory).

%prep
%setup -c

%build
%pear_build

%install
%pear_install_std

%post
%register_pear_module

%preun
%unregister_pear_module

%files
%doc LICENSE CHANGELOG
%pear_testdir/FSM/
%pear_dir/FSM.php
%pear_docdir/%pear_name/
%pear_xmldir/%pear_name.xml

%changelog
* Fri Jun 20 2008 Vitaly Lipatov <lav@altlinux.ru> 1.3.0-alt1
- new version 1.3.0 (with rpmrb script)

* Thu Jan 10 2008 Vitaly Lipatov <lav@altlinux.ru> 1.2.5-alt2
- update according to rpm-build-pear 0.3

* Sat Jan 05 2008 Vitaly Lipatov <lav@altlinux.ru> 1.2.5-alt1
- initial build for ALT Linux Sisyphus

