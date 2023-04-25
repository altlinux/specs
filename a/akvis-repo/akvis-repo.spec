%define akvis_repos http://akvis-alt.sfo2.cdn.digitaloceanspaces.com
%define _unpackaged_files_terminate_build 1

%ifdef _priority_distbranch
%define altbranch %_priority_distbranch
%else
%define altbranch %(rpm --eval %%_priority_distbranch)
%endif
%if "%altbranch" == "%nil"
%define altbranch sisyphus
%endif

Name: akvis-repo
Version: 1.0.1
Release: alt1

Summary: Link to the AKVIS repository
License: GPL-3
Group: System/Configuration/Packaging

BuildArch: noarch

Source: %name-%version.tar
Url: https://alivecolors.com/ru/

Packager: Leonid Krivoshein <klark@altlinux.org>

Requires: apt-conf

%description
This package contains just a link to the AKVIS repository.

%prep
%setup

%build
%if "%altbranch" == "p10"
( echo "rpm %akvis_repos %_arch akvis"
  echo "rpm %akvis_repos noarch akvis"
) > etc/apt/sources.list.d/akvis.list
%endif
mkdir -p -m0755 %buildroot
mv -f etc %buildroot/

%files
%config(noreplace) /etc/apt/sources.list.d/akvis.list

%changelog
* Tue Apr 25 2023 Leonid Krivoshein <klark@altlinux.org> 1.0.1-alt1
- Initial build for Sisyphus.

