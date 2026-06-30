Name: alterator-module-remote
Version: 0.5.0
Release: alt1

Summary: Module for accessing alterator d-bus interface on a remote machine
License: GPLv2
Group: System/Configuration/Other
URL: https://altlinux.space/alterator/alterator-module-remote

BuildRequires: cmake gcc rpm-build-licenses libjson-c-devel
BuildRequires: libgio-devel libpolkit-devel
# libsystemd-devel
BuildRequires: alterator-manager-devel >= 0.1.28

Requires: alterator-manager >= 0.1.28-alt1
Requires: libjson-c5 >= 0.17

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
* Tue Jun 30 2026 Ivan Savin <svn17@altlinux.org> 0.5.0-alt1
- The return value of the "GetConnections" method has been changed.
- Remove unnecessary parameter "remote_address" in function
  "receive_introspections".
- Add missing g_object_unref(stream).

* Fri Jun 19 2026 Ivan Savin <svn17@altlinux.org> 0.4.0-alt1
- Add "repeat_request" parameter to "SelectUser" call on the password agent.
  It is true if this is a retry after an incorrect password was entered.

* Mon Jun 08 2026 Ivan Savin <svn17@altlinux.org> 0.3.0-alt1
- Add "pty" parameter to "ShowResult" call in the password agent.

* Tue Jun 02 2026 Ivan Savin <svn17@altlinux.org> 0.2.0-alt1
- A boolean input parameter, "success", has been added to the "ShowResult"
  method of "Password agent". If authentication is successful, its value is
  set to true; otherwise, it is set to false.
- Methods for manipulating JSON have been replaced with library ones.

* Fri Apr 10 2026 Ivan Savin <svn17@altlinux.org> 0.1.5-alt2
- Update secret scan action to use alterator fork (the-nexi@).

* Fri Feb 27 2026 Ivan Savin <svn17@altlinux.org> 0.1.5-alt1
- Update .clang-format and CODESTYLE.md.
- Bringing the code to the described style.
- Add .forgejo/workflows/clang-format.yml.

* Wed Feb 18 2026 Ivan Savin <svn17@altlinux.org> 0.1.4-alt1
- Add signal retransmission from a remote. Signals from the
  org.altlinux.alterator sender on the remote machine are retransmitted to the
  local d-bus. The signal's object path and signal name fields are replaced. In
  the object path, two more sections are added before the last one. The first
  is the word 'connection'. The second is the connection name. The executor
  module appends a unique bus name to the signal name, replacing periods and
  colons with underscores. When retransmitting, the unique bus name is replaced
  with the connection name, separated by an underscore.

* Fri Jan 23 2026 Ivan Savin <svn17@altlinux.org> 0.1.3-alt3
- Add add secret scanning (alxvmr@).
- Add .clang-format and CODESTYLE.md.

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
