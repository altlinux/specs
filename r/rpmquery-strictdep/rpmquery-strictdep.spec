%global _unpackaged_files_terminate_build 1
Name: rpmquery-strictdep
Version: 1
Release: alt1

Summary: Query an RPM and output the corresponding strict dependency

License: GPLv2+
Group: Development/Other
Url: http://git.altlinux.org/gears/r/rpmquery-strictdep.git

Source0: rpmquery-strictdep

BuildArch: noarch

%{?!_without_check:%{?!_disable_check:BuildRequires: libshell sed}}

%description
%summary.

The output can be used as a Requires in another package.

The most strict dependency is looked for via rpmquery --provides.
Usually, the result would include the disttag.

%%_allow_deps_with_beginning_dot and $allow_deps_with_beginning_dot control
whether the deprecated format (with a dot) is allowed in the output.


%install
%global dest %_bindir/rpmquery-strictdep
install -Dpm0755 %SOURCE0 -T %buildroot%dest

%check
set -o pipefail

# Only one package should be queried.
! %buildroot%dest rpm-build rpm-build
! %buildroot%dest
! %buildroot%dest -a

%buildroot%dest rpm-build | grep -Fe rpm-build
%buildroot%dest -f /usr/bin/rpmbuild | grep -Fe rpm-build


%files
%dest

%changelog
* Thu Apr 25 2019 Ivan Zakharyaschev <imz@altlinux.org> 1-alt1
- initial build for ALT Linux Sisyphus.


