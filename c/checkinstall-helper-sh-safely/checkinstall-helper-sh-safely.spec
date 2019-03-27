Name: checkinstall-helper-sh-safely
Version: 0.1
Release: alt1

Summary: Helper for *-checkinstall pkgs to run their scripts safely (kinda isolated)

BuildRequires(pre): rpm-build-licenses
License: %gpl2plus
Group: Development/Tools
Url: http://git.altlinux.org/people/imz/packages/checkinstall-helper-sh-safely.git

Requires: tmpdir.sh

BuildArch: noarch

%{?!_without_check:%{?!_disable_check:BuildRequires: tmpdir.sh fakeroot}}

Source0: sh-safely.sh

%global helper %_sbindir/sh-safely

%description
%helper is an interpreter for *-checkinstall pkgs to run their scripts safely
(without effects on the system):

* as an unpriviledged user ("nobody")
* and in a tmpdir that will be cleaned.

Example (as in %name-checkinstall):

    %%pre checkinstall -p %helper
    touch a

%package checkinstall
Summary: Immediately test %name when installing this package
Group: Other
Requires(pre): %name

%description checkinstall
%summary.

It runs %helper with a simple script (that touches a file).

%files checkinstall

%pre checkinstall -p %helper
touch a

%install
install -m0755 %SOURCE0 -D -T %buildroot%helper

%check
fakeroot -- %buildroot%helper - <<<true
! fakeroot -- %buildroot%helper - <<<false

%files
%helper

%changelog
* Wed Mar 27 2019 Ivan Zakharyaschev <imz@altlinux.org> 0.1-alt1
- initial build for ALT Linux Sisyphus.


