Name: alterator-roles
Version: 1.3
Release: alt1

Source:%name-%version.tar

BuildArch: noarch

Summary: alterator module for managing roles
License: GPL
Group: System/Configuration/Other

Requires: alterator-l10n >= 2.9.111-alt1 libnss-role >= 0.5.3-alt1
BuildPreReq: alterator >= 4.10-alt1

Provides: alterator-role = %EVR
Obsoletes: alterator-role < 1.1-alt3

%define _unpackaged_files_terminate_build 1

%description
An alterator module for managing roles (it uses libnss-role).

%prep
%setup -q

%build
%make_build

%install
%makeinstall

%files
%_datadir/alterator/applications/*

%dir %_datadir/alterator/ui/roles
%_datadir/alterator/ui/roles/*.scm

%dir %_datadir/alterator/ui/roles/roleadd
%_datadir/alterator/ui/roles/roleadd/*.scm

%dir %_datadir/alterator/ui/roles/roleadd_d
%_datadir/alterator/ui/roles/roleadd_d/*.scm

%dir %_datadir/alterator/ui/roles/roleadd_sys
%_datadir/alterator/ui/roles/roleadd_sys/*.scm

%_alterator_backend3dir/roles
%_datadir/dbus-1/interfaces/*.xml

%changelog
* Wed Apr 06 2022 Ivan Savin <svn17@altlinux.org> 1.3-alt1
- Fix bugs after rename.
- Add ability to enable/disable libnss-role module.

* Fri Oct 29 2021 Ivan Savin <svn17@altlinux.org> 1.2-alt1
- Rename package name to alterator-roles.

* Wed Jul 14 2021 Ivan Savin <svn17@altlinux.org> 1.1-alt3
- Add use of new libnss-role functions for add and delete system roles.

* Wed Jul 14 2021 Ivan Savin <svn17@altlinux.org> 1.1-alt2
- Change the category in the menu from system to users.

* Tue Jul 13 2021 Ivan Savin <svn17@altlinux.org> 1.1-alt1
- Add the ability to manipulate roles and privileges with multi-word names.

* Thu Jul 08 2021 Ivan Savin <svn17@altlinux.org> 1.0-alt2
- Add check of fields for emptiness in dialog boxes.
- Change the titles of the listboxes.
- Change buttons text.
- Add filename substitution by default when adding a privilege to /etc/role.d/.
- Add an introspection file.

* Wed Jun 30 2021 Ivan Savin <svn17@altlinux.org> 1.0-alt1
- Add an expert mode.
- Add a simple mode.

* Thu May 20 2021 Ivan Savin <svn17@altlinux.org> 0.1-alt1
- Initial commit.

