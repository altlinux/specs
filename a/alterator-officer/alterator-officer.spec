Name: alterator-officer
Version: 1.0
Release: alt8

Source:%name-%version.tar


Summary: alterator module for edit system security officer properties
License: GPL
Group: System/Configuration/Other
BuildArch: noarch
Requires: alterator >= 4.6-alt3 alterator-sh-functions >= 0.13-alt2
Requires: shadow-utils passwdqc-utils
Requires: alterator-l10n >= 2.7-alt3
Conflicts: alterator-lookout < 2.2-alt1
Conflicts: alterator-fbi < 5.25-alt4
Conflicts: alterator-users < 8.1

BuildPreReq: alterator >= 4.6-alt3

%description
alterator module for edit system  security officer properties

%prep
%setup -q

%build
%make_build

%install
%makeinstall

%files
%_datadir/alterator/applications/*
%_datadir/alterator/ui/*/
%_alterator_backend3dir/*
%attr(700,root,root) %dir %_libexecdir/alterator/hooks/officer.d

%changelog
* Sat Apr 13 2019 Denis Medvedev <nbr@altlinux.org> 1.0-alt8
- fixes for homedir, also an icon is made the same as for root.

* Tue Oct 09 2018 Denis Medvedev <nbr@altlinux.org> 1.0-alt7
- many fixes due to moving creation of officer user to setup
package

* Fri Oct 05 2018 Denis Medvedev <nbr@altlinux.org> 1.0-alt6
- fixed behavour of UI step skipping and user creation

* Fri Oct 05 2018 Denis Medvedev <nbr@altlinux.org> 1.0-alt5
- fixed prompts and logic of check of selinux present

* Wed Sep 26 2018 Denis Medvedev <nbr@altlinux.org> 1.0-alt4
- When selinux is present, prepare its state for labeling, it is no
way to set up unlabeled system to permissive mode otherwise.

* Wed Sep 26 2018 Denis Medvedev <nbr@altlinux.org> 1.0-alt3
- skip officer operations if selinux is not installed

* Tue Sep 18 2018 Denis Medvedev <nbr@altlinux.org> 1.0-alt2
- Added officer creation

* Tue Sep 18 2018 Denis Medvedev <nbr@altlinux.org> 1.0-alt1
- Initial release, based on alterator-root
