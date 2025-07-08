Name: alterator-module-remote
Version: 0.1.3
Release: alt2

Summary: Module for accessing alterator d-bus interface on a remote machine
License: %gpl2only
Group: System/Configuration/Other
URL: https://altlinux.space/alterator/alterator-module-remote

BuildRequires: cmake gcc rpm-build-licenses
BuildRequires: libgio-devel libpolkit-devel
# libsystemd-devel
BuildRequires: alterator-manager-devel >= 0.1.28

Requires: alterator-manager >= 0.1.28-alt1

Source: %name-%version.tar

%description
Alterator-manager module for accessing alterator d-bus interface on a
remote machine.

%prep
%setup -q

%build
%cmake -DCMAKE_BUILD_TYPE=Release
%cmake_build

%install
%cmakeinstall_std

%files
/usr/libexec/alterator/*

%changelog
* Tue Jul 08 2025 Ivan Savin <svn17@altlinux.org> 0.1.3-alt2
- Change the URL in the spec.

* Fri Apr 11 2025 Ivan Savin <svn17@altlinux.org> 0.1.3-alt1
- Add functionality allowing the manager to track whether the module is busy.
- Remove unnecessary checks. In case of failure on g_new0 and g_thread_new
  the program aborts.

* Wed Feb 26 2025 Ivan Savin <svn17@altlinux.org> 0.1.2-alt2
- Requirements update.

* Fri Nov 08 2024 Ivan Savin <svn17@altlinux.org> 0.1.2-alt1
- Fix return value of Disconnect method. Now it returns true if the kill signal
  was successfully sent to the remote-polkit-agent.
- Remove call to subtrees_info_table_stop_loop from register_subtree. The loop
  is not running at this point yet.
- Fix the description section in spec.

* Wed Oct 30 2024 Ivan Savin <svn17@altlinux.org> 0.1.1-alt1
- First working version.
